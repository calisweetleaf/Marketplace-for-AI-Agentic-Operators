# Repository Memory: Mentat

This file tracks the history, current state, and milestones of the Mentat codebase.

## Active Status

- **Current Branch**: `main`
- **Last Action**: Staging hardening updated Mentat's ontology to an independent runtime plugin, added release/copyover and installer-copy hygiene, and preserved public repo safety by keeping all work under `/home/daeron/Projects/Modern-ML/Plugins/Mentat`.
- **Current Manifest Version**: `0.3.0` in `.claude-plugin/plugin.json`.
- **Validation Gate**: `python3 scripts/integration_smoke.py`, `python3 scripts/hook_schema_smoke.py`, `PYTHONDONTWRITEBYTECODE=1 python3 tests/command_frontmatter_lint_smoke.py`, `python3 scripts/command_frontmatter_lint.py .`, `PYTHONDONTWRITEBYTECODE=1 python3 tests/prompt_surface_review_smoke.py`, `python3 scripts/prompt_surface_review.py .`, `PYTHONDONTWRITEBYTECODE=1 python3 tests/privacy_boundary_scan_smoke.py`, `python3 scripts/privacy_boundary_scan.py .`, `bash adapters/test_universal.sh`, and `python3 scripts/validate_release_tree.py .` (138 candidate files, 250 local-only/forbidden files excluded after prompt review addition).

## Milestones & History

### 2026-05-23: Initial Git Setup

- Initialized local git repository.
- Created root `.gitignore` to exclude python `__pycache__` and session files.
- Added and committed all project files.
- Created `AGENTS.md`, `MEMORY.md`, and `CONTEXT.md` files at the root.

### 2026-06-13: Runtime Plugin Doctrine + Copyover Hygiene

- Recorded Mentat as an independent cognitive runtime plugin rather than a hook or skill bundle.
- Added `.releaseignore`, `COPYOVER_MANIFEST.md`, and `scripts/validate_release_tree.py`.
- Added `scripts/hook_schema_smoke.py` for Codex/Claude additional-context hook output.
- Added `scripts/command_frontmatter_lint.py` and `tests/command_frontmatter_lint_smoke.py` for slash-command metadata and scoped-tool validation.
- Added `scripts/prompt_surface_review.py` and `tests/prompt_surface_review_smoke.py` for independent agent/helper prompt role, tool, boundary, and output-contract validation.
- Updated `adapters/install_universal.sh` to respect `.releaseignore` during runtime installs.
- Added temp-HOME Codex install hygiene to `adapters/test_universal.sh`.
- Restored `monitors/monitors.json` and added monitor CLI smoke coverage so the monitor lane can run independently.
- Added `SUBSYSTEM_INVENTORY.md` as the release-facing subsystem map.
- Added `scripts/privacy_boundary_scan.py` and `tests/privacy_boundary_scan_smoke.py` so release-candidate text is scanned for private source identifiers, unapproved local paths, external media paths, and CodeGraph log/archive path shapes.
- Wired hook-schema, adapter-installer, monitor CLI, and release/copyover hygiene into `scripts/integration_smoke.py`.
- Updated `AGENTS.md`, `CONTEXT.md`, `PLAN.md`, `README.md`, `INSTALL.md`, and `CHANGELOG.md` to use the current root package layout and public-copyover safety rule.
- Public repo target remains `/home/daeron/Repositories/Somnus-Intellligence-Stack/Plugins/Mentat`; do not edit it directly before review.

## Next Steps

- Treat `hooks/_lib.py` and `adapters/codex/hooks/_lib.py` hook-schema changes as promotable only when `scripts/hook_schema_smoke.py` remains green.
- Treat installer/copyover changes as promotable only when `bash adapters/test_universal.sh` remains green.
- Rebuild any release archive only after integration and release-tree validation pass.
- Copy reviewed files to the public repo only after Daeron approves the exact copy list or diff.
