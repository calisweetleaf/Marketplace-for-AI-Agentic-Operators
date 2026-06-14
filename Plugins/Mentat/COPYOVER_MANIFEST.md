# COPYOVER_MANIFEST.md - Mentat Staging To Public Repo

Snapshot date: 2026-06-13
Staging root: `/home/daeron/Projects/Modern-ML/Plugins/Mentat`
Public repo target: `/home/daeron/Repositories/Somnus-Intellligence-Stack/Plugins/Mentat`

## Release Rule

Treat this staging tree as the working source. Treat the public repo as the reviewed release surface. Do not copy generated runtime state, local archives, analysis caches, task scratch, or backup files into the public repo.

Mentat is an independent runtime plugin, not a hook bundle. Its release boundary must preserve the state machine, Q-table, insight bus, drift monitor, MCP server, CLI, adapters, monitors, evals, commands, skills, agents, and package metadata as one coherent substrate.

## Include

Copy these surfaces after validation passes:

- `README.md`
- `INSTALL.md`
- `CHANGELOG.md`
- `AGENTS.md`
- `CONTEXT.md`
- `MEMORY.md`
- `PLAN.md`
- `SUBSYSTEM_INVENTORY.md`
- `.claude-plugin/`
- `.mcp.json`
- `mcp.json`
- `webhooks.json`
- `hooks/`
- `state_machine/`
- `mcp_server/`
- `bin/`
- `commands/`
- `skills/`
- `agents/`
- `helpers/`
- `adapters/`
- `webhook_engine/`
- `evals/`
- `monitors/`
- `docs/`
- `style/`
- `scripts/`
- `.gitignore`
- `.releaseignore`
- `COPYOVER_MANIFEST.md`

## Exclude

Never copy these into the public repo:

- `.git/`
- `.codegraph/`
- `.venv/`, `venv/`, `env/`, `ENV/`
- `.mentat/`
- `__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`
- generated archives such as `mentat-plugin.tar.gz`, `mentat-v2.zip`, `*.zip`, `*.tar.gz`
- local DB/log/process files such as `*.sqlite`, `*.db`, `*.db-wal`, `*.db-shm`, `*.pid`, `*.log`
- generated filetree snapshots unless Daeron explicitly promotes one as a documentation artifact
- scratch/task folders such as `6-11-2026 Task/`
- backup hook libraries such as `*.backup_*`
- generated local HTML/report artifacts such as `mentat-a-live-cognitive-substrate-for-claude-code.html`
  unless Daeron explicitly promotes the linked-doc/site layer

## Validation Gate

Run from the staging root before copyover:

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
python3 -m json.tool .claude-plugin/plugin.json >/dev/null
python3 -m json.tool mcp.json >/dev/null
python3 -m json.tool webhooks.json >/dev/null
python3 -m json.tool monitors/monitors.json >/dev/null
```

The release tree validator does not require local-only artifacts to be deleted. It verifies that they are covered by `.releaseignore` and therefore excluded from the candidate copy set.

`mentat-a-live-cognitive-substrate-for-claude-code.html` is a preserved local
site/prototype artifact. Do not delete it during cleanup. Keep it in staging and
expand it as the future linked-doc/site page evolves; it remains excluded from
public copyover until Daeron explicitly promotes that layer.

`scripts/validate_release_tree.py` now invokes `scripts/privacy_boundary_scan.py`
and `tests/privacy_boundary_scan_smoke.py`. The scanner respects `.releaseignore`
and checks only release-candidate text files, so staging evidence can remain
local while private semantic archive/source identifiers, unapproved local paths,
external media paths, and CodeGraph log/archive path shapes stay out of public
copyover.

The same release validator invokes `scripts/prompt_surface_review.py` and
`tests/prompt_surface_review_smoke.py` so `agents/*.md`, `helpers/*.md`, and the
helper index declare role, tool posture, write/scope boundaries, and output
contracts before copyover. These prompt surfaces stay independent of hooks and
skills.

`adapters/install_universal.sh` also respects `.releaseignore` when copying a live plugin tree into a runtime install path. `adapters/test_universal.sh` proves that behavior by installing into a temporary Codex HOME and asserting that staging artifacts such as `.mentat/`, archive files, generated filetrees, scratch folders, and hook backups are not copied.

## Candidate Copy Command

Use this only after review:

```bash
rsync -av --delete \
  --exclude-from=.releaseignore \
  /home/daeron/Projects/Modern-ML/Plugins/Mentat/ \
  /home/daeron/Repositories/Somnus-Intellligence-Stack/Plugins/Mentat/
```

Then inspect the public repo diff before committing.

## Current Hardening Notes

- Manifest version is `0.3.0` in `.claude-plugin/plugin.json`.
- `scripts/integration_smoke.py` currently exercises the runtime substrate end to end and includes the universal adapter installer smoke.
- `scripts/hook_schema_smoke.py` directly verifies schema-safe `additionalContext` output for `hooks/_lib.py` and `adapters/codex/hooks/_lib.py`.
- `scripts/command_frontmatter_lint.py` validates all nine slash command prompt files for required descriptions, argument hints, scoped shell permissions, and no Bash wildcards.
- `scripts/prompt_surface_review.py` validates all seven agent/helper prompt files plus `helpers/HELPERS.md` for role, tool, boundary, and output contracts.
- `mentat-a-live-cognitive-substrate-for-claude-code.html` is intentionally preserved as a local site/prototype artifact while excluded from release copyover.
- Existing local archives and filetree snapshots are staging artifacts and should stay outside release copyover unless explicitly promoted.
- The generated local HTML report is staging evidence and remains excluded from release copyover unless explicitly promoted.
