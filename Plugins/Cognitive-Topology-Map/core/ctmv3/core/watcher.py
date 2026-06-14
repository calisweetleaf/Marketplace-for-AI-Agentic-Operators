"""
CTMv3 Project State Watcher
============================
Provenance: CTMv3 Engine v1.3.0 — 2026-06-12
Purpose: Per-project in-memory state cache with mtime-based drift detection.
         Underpins the CTMv3 persistent server — no external dependencies.

Design:
  ProjectState     — snapshot of one CTM-activated project (inventory, session, fingerprint)
  ProjectRegistry  — thread-safe collection of ProjectStates with background polling
  _snapshot_mtimes — records file mtimes for the topology files we care about

The poll loop runs in a daemon thread. It checks mtimes every poll_interval seconds
and calls ProjectState.refresh() when drift is detected. refresh() is the only place
that touches disk; everything else reads from in-memory state.
"""

from __future__ import annotations

import logging
import threading
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from ctmv3.core import boot as boot_module
from ctmv3.core import fingerprint as fp_module
from ctmv3.core import sovereign as sov_module
from ctmv3.core.boot import SignalInventory
from ctmv3.core.orchestration import pre_chain_rules

logger = logging.getLogger(__name__)

_WATCHED_FILES: List[str] = [
    "TOPOLOGY.md",
    "ARCHITECTURE_MAP.md",
    "PROVENANCE.md",
    ".sovereign/session_state.json",
    ".sovereign/topology_fingerprint.txt",
]


def _snapshot_mtimes(root: Path) -> Dict[str, float]:
    mtimes: Dict[str, float] = {}
    for rel in _WATCHED_FILES:
        p = root / rel
        try:
            mtimes[rel] = p.stat().st_mtime
        except OSError:
            mtimes[rel] = 0.0
    return mtimes


@dataclass
class ProjectState:
    """In-memory snapshot of a single CTM-activated project."""

    path: Path
    name: str
    inventory: Optional[SignalInventory] = None
    session_state: dict = field(default_factory=dict)
    fingerprint_matches: bool = False
    current_hash: str = ""
    last_refreshed: Optional[datetime] = None
    _file_mtimes: Dict[str, float] = field(default_factory=dict)

    def refresh(self) -> None:
        """Re-read all project state from disk. Called on init and after drift."""
        try:
            self.inventory = boot_module.discover(self.path)
            self.session_state = sov_module.read_session_state(self.path)
            self.fingerprint_matches, self.current_hash = fp_module.verify(self.path)
            self.last_refreshed = datetime.utcnow()
            self._file_mtimes = _snapshot_mtimes(self.path)
            logger.debug(
                "refresh: %s branch=%s fingerprint_match=%s",
                self.name,
                self.inventory.branch if self.inventory else "?",
                self.fingerprint_matches,
            )
        except Exception as exc:
            logger.warning("refresh failed for %s: %s", self.name, exc)

    def has_drifted(self) -> bool:
        """True if any watched topology file has changed since last refresh."""
        for rel, stored_mtime in self._file_mtimes.items():
            p = self.path / rel
            try:
                current = p.stat().st_mtime
                if current != stored_mtime:
                    return True
            except OSError:
                if stored_mtime != 0.0:
                    return True
        return False

    def to_context(self) -> dict:
        """
        Compact context blob for agent consumption.
        This is what agents query instead of running the full chain themselves.
        """
        inv = self.inventory
        state = self.session_state
        branch = inv.branch if inv else "COLD_START"
        warm_valid = (
            boot_module.is_warm_valid(inv)
            if inv and branch != "COLD_START"
            else False
        )
        suggested = pre_chain_rules("boot", branch) or "activate"

        return {
            "project": self.name,
            "path": str(self.path),
            "branch": branch,
            "warm_valid": warm_valid,
            "suggested_command": suggested,
            "current_state": state.get("current_state", "UNKNOWN"),
            "fingerprint_matches": self.fingerprint_matches,
            "current_hash": self.current_hash,
            "last_agent": state.get("last_agent", ""),
            "last_action": state.get("last_action", ""),
            "open_tasks": state.get("open_tasks", []),
            "tier1_signals": inv.tier1_signals if inv else [],
            "tier2_signals": inv.tier2_signals if inv else [],
            "drift_detected": not self.fingerprint_matches,
            "last_refreshed": self.last_refreshed.isoformat() if self.last_refreshed else None,
        }


class ProjectRegistry:
    """
    Thread-safe registry of watched projects.
    Background daemon thread polls for drift and refreshes stale state.
    """

    def __init__(self, poll_interval: float = 5.0) -> None:
        self._projects: Dict[str, ProjectState] = {}  # keyed by str(resolved path)
        self._lock = threading.RLock()
        self._poll_interval = poll_interval
        self._stop_event = threading.Event()
        self._thread: Optional[threading.Thread] = None

    def register(self, path: Path) -> ProjectState:
        path = path.resolve()
        key = str(path)
        with self._lock:
            if key not in self._projects:
                ps = ProjectState(path=path, name=path.name)
                ps.refresh()
                self._projects[key] = ps
                logger.info("registered: %s (%s)", ps.name, path)
            return self._projects[key]

    def get_by_name(self, name: str) -> Optional[ProjectState]:
        with self._lock:
            for ps in self._projects.values():
                if ps.name == name or str(ps.path).endswith("/" + name):
                    return ps
        return None

    def list_all(self) -> List[ProjectState]:
        with self._lock:
            return list(self._projects.values())

    def start_polling(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(
            target=self._poll_loop,
            daemon=True,
            name="ctmv3-watcher",
        )
        self._thread.start()
        logger.info("watcher started (interval=%.1fs)", self._poll_interval)

    def stop_polling(self) -> None:
        self._stop_event.set()
        if self._thread:
            self._thread.join(timeout=10)
        logger.info("watcher stopped")

    def _poll_loop(self) -> None:
        while not self._stop_event.wait(self._poll_interval):
            with self._lock:
                projects = list(self._projects.values())
            for ps in projects:
                try:
                    if ps.has_drifted():
                        logger.info("drift detected in %s — refreshing", ps.name)
                        ps.refresh()
                except Exception as exc:
                    logger.warning("poll error for %s: %s", ps.name, exc)
