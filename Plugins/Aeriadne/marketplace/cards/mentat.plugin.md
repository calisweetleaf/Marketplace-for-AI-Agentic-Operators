# Mentat

Type: Native runtime plugin
Status: Staged green, installed locally, not copied to public repo
Version: 0.3.0
Clients: Claude Code, Codex, Gemini
Canonical path: `/home/daeron/Projects/Modern-ML/Plugins/Mentat`
Public copy target: `/home/daeron/Repositories/Somnus-Intellligence-Stack/Plugins/Mentat`

## What it does

Mentat is the live cognitive runtime substrate for agent sessions. It commits
session state, state-machine position, Q-table learning, insight bus events,
drift state, handoff snapshots, and monitor state. Hooks, commands, MCP,
monitors, evals, skills, and agent prompts are surfaces over that substrate.

## Committed State

- Session records under the Mentat home root.
- FSA state and transition counts.
- Q-table values and reward signals.
- Insight bus JSONL.
- Drift and handoff events.
- Monitor last-run state.

## Surfaces

- Claude/Codex/Gemini adapter hooks.
- Claude Code slash commands.
- Mentat MCP introspection server.
- Entropy, drift, and archivist monitors.
- Eval harness and debrief renderer.
- Plugin-scoped and helper agent prompts.

## Validation

Latest staging gate:

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

Current evidence: `58 pass / 0 fail / 0 skip`; command-frontmatter lint `PASS`
for 9 commands; prompt-surface review `PASS` for 7 agent/helper prompts plus
the helper index; privacy boundary `PASS`; release tree `PASS` with `139`
candidate files and `299` ignored local-only/forbidden files after cache
cleanup. `mentat@local` is installed/enabled in Codex, and the installed cache
preserves `.mcp.json` so the plugin-provided Mentat MCP server hydrates.

## Boundary

Aeriadne catalogs Mentat but does not own Mentat's runtime state. Public copyover
requires Daeron review of `COPYOVER_MANIFEST.md` and the exact public repo diff.
Mentat's validator now checks release-candidate text for private source
identifiers, unapproved local paths, external media paths, and stale local tool
log/archive path shapes while respecting `.releaseignore`.
It also checks slash command prompt frontmatter for required descriptions,
argument hints, scoped shell permissions, and forbidden Bash wildcards.
Agent and helper prompt files are separately checked for role declarations,
tool posture, write/scope boundaries, and output contracts. They remain
independent operator-prompt surfaces, not hooks or skills.
The local root HTML artifact is preserved as a future linked-doc/site prototype
but remains outside public copyover until Daeron promotes that site surface.
Aeriadne's site audit now also verifies the page keeps its state-machine,
Q-table, insight-bus, drift, hook, and MCP projection language intact.
