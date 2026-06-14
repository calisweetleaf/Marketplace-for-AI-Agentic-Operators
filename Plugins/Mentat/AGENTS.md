# Agent Directory: Mentat

Welcome, agent. This is the entry point for the **Mentat** repository.

## Map of the Substrate
- **[Memory & Milestones](file:///home/daeron/Projects/Modern-ML/Plugins/Mentat/MEMORY.md)**: Current status, log of changes, and active tasks.
- **[Context & Architecture](file:///home/daeron/Projects/Modern-ML/Plugins/Mentat/CONTEXT.md)**: Technical architecture, directory layouts, and execution rules.

## Core Purpose
Mentat is an independent cognitive runtime plugin. Its committed state is a session-scoped finite-state machine, persistent session record, Q-table, insight bus, drift detector, and compaction handoff layer.

Hooks, MCP tools, commands, monitors, adapters, skills, and agent prompts are boundary surfaces. They are how Mentat senses and influences the host runtime; they are not the whole plugin.

Golden Path invariant: Mentat should commit only validated session/runtime state, purge rejected or drifted branches from future conditioning when possible, preserve reversible state through handoff/rollback surfaces, and stop before public copyover or install pivots unless validation evidence is present.

## Project Guidelines
1. **Loud Failures**: Never fail silently. All exceptions and error codes must be logged clearly.
2. **Virtual Environment**: Run all tasks within the designated python environment and ensure dependencies are installed.
3. **No Drift**: Pay close attention to `.mentat/scope.md`. Avoid out-of-scope discussion topics to prevent triggering FSA drift blocks.
4. **Plugin Boundary**: Do not flatten Mentat into hooks or skills. Preserve the runtime substrate and document any new surface as a projection of that substrate.
5. **Copyover Gate**: Before promotion, run `python3 scripts/integration_smoke.py` and `python3 scripts/validate_release_tree.py .`.
