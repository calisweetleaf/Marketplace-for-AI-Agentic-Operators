# SUBSYSTEM_INVENTORY.md - Mentat Runtime Plugin

Snapshot date: 2026-06-13
Staging root: `/home/daeron/Projects/Modern-ML/Plugins/Mentat`
Scope: release-candidate subsystem inventory, excluding files ignored by `.releaseignore`

## Inventory Rule

Mentat is an independent runtime plugin. The subsystems below are surfaces over
the same committed substrate: state machine, Q-table, insight bus, session
records, drift detection, handoff state, and runtime adapters. Do not promote a
single surface as "the plugin" by itself.

Counts below use the release/copyover membrane: generated eval output,
`__pycache__/`, hook backups, archives, filetree snapshots, and local runtime
state are not counted.

## Status Legend

- **green**: implementation is present and covered by the current smoke gate.
- **partial**: implementation exists, but the current gate does not prove the
  whole user-facing surface.
- **docs-only**: prompt/document surface with no direct execution semantics.

## Release-Candidate Summary

| Subsystem | Files | Lines | Primary surface | Status | Gate |
| --- | ---: | ---: | --- | --- | --- |
| Adapters | 29 | 3,127 | Codex + Gemini hook projections, universal installer | green | `bash adapters/test_universal.sh` |
| Evals | 18 | 2,848 | deterministic/stochastic rubric harness | green | `python3 evals/scripts/run_eval.py --rubric all` via integration smoke |
| Webhook engine | 6 | 971 | optional signed event emitter + DLQ | green | `python3 webhook_engine/test_smoke.py` |
| Monitors | 6 | 966 | entropy/drift/archivist background monitor lane | green | `python3 monitors/test_smoke.py` plus monitor CLI status/schedule smoke |
| Slash commands | 12 | 503 | 9 Claude Code command prompts + README + lint gate | green | `python3 scripts/command_frontmatter_lint.py .` plus smoke |
| Plugin agents | 4 | 208 | cartographer, crucible, scribe, sentinel | green | prompt-surface review |
| Helper agents | 4 | 380 | conductor, medic, quartermaster + index | green | prompt-surface review |
| Debrief skill scripts | 5 | 2,418 | deterministic HTML debrief renderer | green | `python3 skills/mentat-debrief/scripts/test_smoke.py` |
| Privacy/release boundary | 2 | 282 | release-candidate private path/source leak scanner | green | `python3 scripts/privacy_boundary_scan.py .` plus smoke |
| Prompt-surface review | 2 | 331 | agent/helper prompt contract validator | green | `python3 scripts/prompt_surface_review.py .` plus smoke |
| Docs | 3 | 1,431 | style, provenance, SOTA checklist | docs-only | markdown present |

## Subsystem Notes

### Adapters

Codex wires six events: `SessionStart`, `UserPromptSubmit`, `PreToolUse`,
`PermissionRequest`, `PostToolUse`, and `Stop`. Gemini wires eleven events:
`SessionStart`, `SessionEnd`, `BeforeAgent`, `AfterAgent`, `BeforeModel`,
`AfterModel`, `BeforeToolSelection`, `BeforeTool`, `AfterTool`, `PreCompress`,
and `Notification`.

Both adapters reconstruct a `HookContext` from disk on every hook invocation,
step the shared FSA, update session state, emit state-transition insights, and
write reward signals through the same Q-table. The adapter layer is therefore a
runtime projection, not a fork of Mentat's substrate.

`adapters/install_universal.sh` now respects `.releaseignore` when copying the
live plugin tree into runtime install paths. `adapters/test_universal.sh` proves
that with a temporary Codex HOME and asserts that `.mentat/`, generated
archives, filetrees, task scratch, and hook backups are not copied.

### Evals

The eval rig is a stdlib Python harness with three rubric criteria:
`state_transition_correctness`, `predictive_routing_accuracy`, and
`persistence_recovery_integrity`. Scenarios run in temporary directories and do
not touch the operator's real `~/.mentat/` data.

Generated files under `evals/output/` are local evidence artifacts and are
excluded from release copyover by `.releaseignore`.

### Webhook Engine

The webhook engine is optional and disabled by default in `webhooks.json`.
When enabled, it builds signed envelopes, enforces a payload-size cap, retries
within a hook-safe budget, and sends final failures into the DLQ. Hook callers
can ignore its return value; it is designed not to crash the hook path.

### Monitors

The monitor lane contains three independently runnable monitors:

- `entropy-watcher`: flags stale `EXECUTING` sessions with long tool chains.
- `drift-watcher`: flags sessions left in `DRIFTING`.
- `archivist`: rotates stale insight/handoff/session artifacts and vacuums
  low-confidence Q-table rows.

`monitors/monitors.json` is now present and is required by the release-tree
validator. `bin/mentat-monitors status` and `bin/mentat-monitors schedule` are
smoked under a temporary `MENTAT_HOME` inside `scripts/integration_smoke.py`.

### Slash Commands

The command surface contains `/status`, `/reflect`, `/plan`, `/dispatch`,
`/debrief`, `/scope`, `/qtable`, `/tail`, and `/drift-check`, plus the command
README. These are prompt bindings over Mentat skills, sub-agents, and CLI
inspectors. `scripts/command_frontmatter_lint.py` now checks every command for
required descriptions, `$ARGUMENTS` / `argument-hint` consistency, scoped
`allowed-tools` on live shell injections, and forbidden Bash wildcards.

### Agents And Helpers

Plugin-scoped agents:

- `mentat-cartographer`
- `mentat-crucible`
- `mentat-scribe`
- `mentat-sentinel`

User/helper agents:

- `mentat-conductor`
- `mentat-medic`
- `mentat-quartermaster`

These prompt surfaces are independent operator prompts. They are not hooks,
skills, or slash commands. `scripts/prompt_surface_review.py` now checks the
four plugin-scoped agents, three user/helper agents, and `helpers/HELPERS.md`
for role declaration, non-empty tool posture, write/scope boundaries, and
output/report contracts before public copyover.

### Debrief Skill

The debrief skill uses deterministic Python scripts to aggregate session state,
Q-table rows, insight logs, drift events, contradiction rows, entropy spikes,
sub-agent provenance, source grounding, tool ledgers, and forward moves into a
self-contained HTML report. The renderer is canonical; agents should not hand
author replacement HTML.

## Current Gate

Run from the Mentat staging root:

```bash
python3 scripts/integration_smoke.py
python3 scripts/hook_schema_smoke.py
PYTHONDONTWRITEBYTECODE=1 python3 tests/command_frontmatter_lint_smoke.py
python3 scripts/command_frontmatter_lint.py .
PYTHONDONTWRITEBYTECODE=1 python3 tests/prompt_surface_review_smoke.py
python3 scripts/prompt_surface_review.py .
PYTHONDONTWRITEBYTECODE=1 python3 tests/privacy_boundary_scan_smoke.py
python3 scripts/privacy_boundary_scan.py .
bash adapters/test_universal.sh
python3 scripts/validate_release_tree.py .
```

The full integration smoke currently covers the hook schema, adapter installer,
eval harness, webhook engine, monitor scripts and monitor CLI, debrief renderer,
core FSA/Q-table/session/drift paths, command-frontmatter lint, prompt-surface
review, privacy boundary scanner, and release-tree validator.

Latest validation: `58 pass / 0 fail / 0 skip`; release-tree validator reports
`138` candidate files and `250` ignored local-only/forbidden files.

## Known Gaps

- Rebuild release archives only after Daeron reviews the exact candidate copy
  list and the public repo diff target.
