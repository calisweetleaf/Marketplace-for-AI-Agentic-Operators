# Plan - Mentat Runtime Plugin Staging + Packaging

## Phase 0 - Runtime Plugin Doctrine

- [x] Treat Mentat as an independent runtime plugin, not a hook pack or skill pack.
- [x] Map Mentat to the Golden Path roles: committed state, validation membrane, compensation/exclusion, divergence, terminal boundary.
- [x] Add copyover hygiene so local session state, archives, backups, filetrees, and task scratch do not cross into public release.

## Phase 1 - Inventory (mentat-cartographer)

- [x] Read adapters/codex/ and adapters/gemini/ - captured hook names, config shapes, install flow
- [x] Read evals/ - harness interface, scenario list, script outputs, rubric scoring
- [x] Read webhook_engine/ - emitter API, DLQ contract, envelope schema
- [x] Read monitors/ - watcher behavior, manifest, CLI scheduling path
- [x] Read commands/*.md - each slash command's invocation and behavior
- [x] Read agents/*.md and helpers/*.md - all 7 agent definitions (4 plugin-scoped + 3 user-scope)
- [x] Read skills/mentat-debrief/scripts/ - actual implementation depth of the debrief pipeline
- [x] Produce `SUBSYSTEM_INVENTORY.md`: per-subsystem name, file count, LOC, key API surface, status

## Phase 2 - Integration Check (mentat-medic)

- [x] Run `python3 scripts/integration_smoke.py` - 58 pass / 0 fail / 0 skip on 2026-06-13 after prompt-surface review wiring
- [x] Run `python3 scripts/hook_schema_smoke.py` - additionalContext output schema-safe on 2026-06-13
- [x] Run `bash adapters/test_universal.sh` - temp Codex install excludes staging artifacts on 2026-06-13
- [x] Run `python3 scripts/validate_release_tree.py .` - 138 candidate files, 250 local-only/forbidden files excluded on 2026-06-13 after prompt review addition and cache cleanup
- [x] Run `PYTHONDONTWRITEBYTECODE=1 python3 tests/privacy_boundary_scan_smoke.py` and `python3 scripts/privacy_boundary_scan.py .` - private-boundary gate enforced on release-candidate text
- [x] Run `PYTHONDONTWRITEBYTECODE=1 python3 tests/command_frontmatter_lint_smoke.py` and `python3 scripts/command_frontmatter_lint.py .` - nine slash commands lint clean
- [x] Run `PYTHONDONTWRITEBYTECODE=1 python3 tests/prompt_surface_review_smoke.py` and `python3 scripts/prompt_surface_review.py .` - seven agent/helper prompts plus helper index review clean
- [x] Check `.claude-plugin/plugin.json` - version field and JSON syntax verified
- [x] Check `mcp.json`, `webhooks.json`, `hooks/hooks.json`, and `evals/rubric.json` for JSON syntax
- [x] Verify `adapters/install_universal.sh` is executable, syntax-safe, and `.releaseignore`-aware
- [x] Promote hook-schema lane for `hooks/_lib.py` and `adapters/codex/hooks/_lib.py` with focused smoke coverage
- [x] Restore `monitors/monitors.json` and smoke `bin/mentat-monitors` status/schedule paths
- [x] Report: which subsystems are smoke-test green vs. partial vs. docs-only in `SUBSYSTEM_INVENTORY.md`

## Phase 3 - HTML Additions (mentat-conductor -> mentat-scribe)

- [ ] Insert Somnus DS v3 global styles block into HTML head (if not already present)
- [ ] Add SVG v2 identity banner section near top of doc
- [ ] Add section: Multi-Runtime Adapter System (codex + gemini, with terminal frames showing install flow)
- [ ] Add section: Evals Rig (harness architecture, scenario table, rubric scoring, benchmark output)
- [ ] Add section: Webhook Engine (envelope schema, emitter flow, DLQ, smoke test)
- [ ] Add section: Monitors (archivist, drift_watcher, entropy_watcher — terminal monitor view)
- [ ] Add section: Slash Commands (9 commands table + terminal demo)
- [ ] Add section: Agent Roster (4 plugin-scoped + 3 user-scope — intelligence panel format)
- [ ] Update stat-row stats in hero to v2 actuals (subsystem count, file count, LOC, agent count)
- [ ] Update TOC nav links to include all new sections

## Phase 4 - Repo Cleanup

- [ ] Remove or archive stale root-level files: mentat-file-tree.md (superseded by 5-22-2026 version), Archive.zip if confirmed stale, mentat-plugin.tar.gz if outdated
- [ ] Rebuild mentat-plugin.tar.gz from the current package root only after validation passes
- [ ] Confirm plugin.json version field matches v2 reality
- [ ] Do not copy `.mentat/`, generated archives, backup hook files, task scratch, filetree snapshots, caches, DBs, or logs into public release

## Phase 5 - Final Review

- [ ] Verify HTML renders correctly (no broken terminal frames, no overflow issues)
- [ ] Cross-check every new section against scope.md — no deferred topics injected
- [ ] Emit mentat insight: documentation v2 complete
- [ ] Daeron reviews exact staged copy list before any public repo copyover
