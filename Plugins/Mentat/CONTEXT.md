# Repository Context: Mentat

This document tracks the codebase topology, components, and development standards.

## Codebase Topology
- **Runtime core**:
  - **`state_machine/`**: Committed session state, deterministic transition table, Q-table routing, insight bus, disk session record, and drift detector.
  - **`mcp_server/`**: Stdio MCP introspection/control surface for the active Mentat state.
  - **`bin/`**: CLI inspectors and operational commands.
- **Host membranes and exposed surfaces**:
  - **`hooks/`**: Claude Code hook membrane.
  - **`adapters/`**: Codex and Gemini projection layers over the same runtime substrate.
  - **`commands/`**: Operator slash-command docs.
  - **`skills/`**: Reflect/plan/dispatch/debrief cognitive workflows that call into the substrate.
  - **`agents/`** and **`helpers/`**: Role prompts and operational playbooks.
- **Observation and validation**:
  - **`monitors/`**: Session watchers for drift, entropy, and telemetry.
  - **`webhook_engine/`**: Webhook emission and dead-letter queueing.
  - **`evals/`**: Scenario harnesses and rubric scoring.
  - **`scripts/`**: Integration and release/copyover validation.
  - **`docs/`** and **`style/`**: Provenance, SOTA checklist, and style references.

There is no current `plugin/` wrapper directory in this staging tree. The repository root is the plugin package root.

## Runtime Doctrine

Mentat is not a hook pack or skill pack. It is a native runtime plugin that lives between the operator and the agent runtime.

The Golden Path mapping is:

- committed state ledger: `state_machine/session.py`, `q_table.py`, `insights.py`, `.mentat/` runtime state outside release;
- validation membrane: hook schemas, JSON manifests, `scripts/integration_smoke.py`, `scripts/validate_release_tree.py`;
- compensation/exclusion ledger: `COPYOVER_MANIFEST.md` and `.releaseignore`;
- divergence process: `state_machine/drift.py`, monitors, scope checks, dirty-public-repo checks;
- terminal boundary: no public copyover or install pivot without local validation and operator review.

## Active Rules & Environment
- **Virtual Environment**: Run commands in the `.venv` or corresponding python environment.
- **Failure Etiquette**: Ensure all errors fail loud and write logs/telemetry to stdout/stderr.
- **Verification**: Run verify steps (e.g. scripts/smoke tests) after modifying plugin components.
- **Scope Discipline**: Respect `.mentat/scope.md` to prevent drifting.
- **Release Hygiene**: Generated archives, caches, runtime state, task scratch, backup files, DBs, logs, and filetree snapshots must be excluded by `.releaseignore` before copyover.
