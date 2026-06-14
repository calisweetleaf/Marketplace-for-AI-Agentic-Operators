"""
CTMv3 Workspace State Constants
================================
Provenance: CTMv3 Engine v1.2.0 — 2026-06-10
Author: Forge (activation engine builder)
Purpose: Canonical state machine constants for CTMv3 workspace lifecycle.
         Provides WorkspaceState string constants, VALID_STATES frozenset,
         and TRANSITIONS dict that formalise valid (from_state, command) -> to_state
         mappings.

Usage:
    from ctmv3.core.states import WorkspaceState, VALID_STATES, TRANSITIONS

Design notes:
  - Plain class with class-level string attributes (no enum dependency) so
    the constants are usable as dict keys, JSON values, and log messages
    without any conversion.
  - TRANSITIONS keys and values always use WorkspaceState.* constants, never
    bare string literals, so a rename inside this file propagates everywhere.
  - orchestration.py imports WorkspaceState to replace bare string literals in
    _CHAIN_TABLE and _MEMORY_TAG_TABLE.
  - sovereign.py uses the string "UNKNOWN" directly (not this import) to
    avoid circular dependency risk; sovereign.py is a low-level module.
"""

from __future__ import annotations

from typing import Dict, Optional, Tuple


# ---------------------------------------------------------------------------
# State constants
# ---------------------------------------------------------------------------


class WorkspaceState:
    """
    String constants representing every valid state in the CTMv3 workspace
    lifecycle state machine.

    All values are lowercase-stable, JSON-serializable strings.  Use these
    constants instead of bare string literals whenever a CTMv3 state name
    appears in logic — comparisons, dict keys, log messages, and JSON output.
    """

    COLD_START: str = "COLD_START"
    WARM_START: str = "WARM_START"
    PARTIAL: str = "PARTIAL"
    ACTIVATING: str = "ACTIVATING"
    SESSION_ACTIVE: str = "SESSION_ACTIVE"
    SESSION_CLOSED: str = "SESSION_CLOSED"
    UNKNOWN: str = "UNKNOWN"


# ---------------------------------------------------------------------------
# Valid state set
# ---------------------------------------------------------------------------

VALID_STATES: frozenset = frozenset(
    {
        WorkspaceState.COLD_START,
        WorkspaceState.WARM_START,
        WorkspaceState.PARTIAL,
        WorkspaceState.ACTIVATING,
        WorkspaceState.SESSION_ACTIVE,
        WorkspaceState.SESSION_CLOSED,
        WorkspaceState.UNKNOWN,
    }
)


# ---------------------------------------------------------------------------
# Transition table
# ---------------------------------------------------------------------------

# Maps (from_state, command) -> to_state.
# Entries use WorkspaceState.* constants exclusively — no bare strings inside
# this dict so a rename inside WorkspaceState propagates to all edges.
#
# The table encodes the *canonical* workflow.  The orchestration layer may
# encounter states not listed here (e.g. a repo stuck in ACTIVATING after a
# crash); those cases are intentionally absent and callers should treat a
# missing entry as "transition undefined — stay in current state".

TRANSITIONS: Dict[Tuple[str, str], Optional[str]] = {
    # Cold start: activate brings a fresh repo into SESSION_ACTIVE
    (WorkspaceState.COLD_START, "activate"): WorkspaceState.SESSION_ACTIVE,

    # Warm start: warm validation confirms the session is resumable
    (WorkspaceState.WARM_START, "warm"): WorkspaceState.SESSION_ACTIVE,

    # Partial state: re-activate to rebuild incomplete artifacts
    (WorkspaceState.PARTIAL, "activate"): WorkspaceState.SESSION_ACTIVE,

    # Session close: active -> closed
    (WorkspaceState.SESSION_ACTIVE, "session-close"): WorkspaceState.SESSION_CLOSED,

    # Boot after close: closed -> warm (repo is already initialised; next
    # entry will be a warm start, not a cold start)
    (WorkspaceState.SESSION_CLOSED, "boot"): WorkspaceState.WARM_START,
}
