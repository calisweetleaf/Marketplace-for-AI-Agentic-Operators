"""
CTMv3 Core Engine — Workspace Activation System
================================================
Provenance: CTMv3 Engine v1.3.0 — 2026-06-12
Author: Forge (activation engine builder)
Purpose: Python activation engine for CTMv3 plugin. Entry point for all host
         adapter integrations (Claude Code, Codex, opencode, Gemini CLI).

This package implements the BOOT_PROTOCOL.md state machine, artifact scaffolding,
fingerprint management, session close protocol, and the persistent server described
in the CTMv3 source docs.

Public API surface:
    boot.discover()          -- run discovery sequence, return SignalInventory
    boot.classify_branch()   -- classify as COLD_START / WARM_START / PARTIAL
    activate.run()           -- full cold-start Phase 0-5 build
    fingerprint.compute()    -- SHA-256 of TOPOLOGY.md + ARCHITECTURE_MAP.md
    fingerprint.verify()     -- check stored fingerprint against current
    sovereign.init()         -- scaffold .sovereign/ directory
    sovereign.write_session_state()  -- update session_state.json
    sovereign.update_session_log()   -- append to PROVENANCE.md Session Log
    server.CTMv3Server       -- persistent HTTP server (serve, context, ping commands)
    watcher.ProjectRegistry  -- in-memory project state cache with background polling

Changes in v1.3.0:
    - Added persistent server: `ctmv3 serve` starts CTMv3Server on port 7430.
    - Added `ctmv3 context`: queries server if up, else runs inline discovery.
    - Added `ctmv3 ping`: checks if server is reachable.
    - Added watcher.py: ProjectState + ProjectRegistry with mtime-based drift detection.
    - Added server.py: CTMv3Server with HTTP endpoints for agent context consumption.
"""

__version__ = "1.3.0"
__ctmv3_protocol__ = "3.0"

from pathlib import Path

# Re-export the most commonly used public symbols so adapter code can do:
#   from ctmv3.core import discover, classify_branch
from ctmv3.core.boot import discover, classify_branch, is_warm_valid, SignalInventory
from ctmv3.core.fingerprint import compute as compute_fingerprint
from ctmv3.core.fingerprint import verify as verify_fingerprint
from ctmv3.core.sovereign import init as sovereign_init
from ctmv3.core.sovereign import write_session_state, update_session_log
from ctmv3.core.activate import run as activate_run

__all__ = [
    "__version__",
    "__ctmv3_protocol__",
    "SignalInventory",
    "discover",
    "classify_branch",
    "is_warm_valid",
    "compute_fingerprint",
    "verify_fingerprint",
    "sovereign_init",
    "write_session_state",
    "update_session_log",
    "activate_run",
]
