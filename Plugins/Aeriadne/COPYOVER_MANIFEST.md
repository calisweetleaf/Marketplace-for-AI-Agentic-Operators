# COPYOVER_MANIFEST.md - Aeriadne Staging To Public Repo

Snapshot date: 2026-06-13
Staging root: `/home/daeron/Projects/Modern-ML/Plugins/Aeriadne`
Public review target: `/home/daeron/Repositories/Somnus-Intellligence-Stack/Plugins/Aeriadne`

## Status

Status: private-v1 / validated-local, installed locally as `aeriadne@local`.
Operator review required: yes.
Public copyover performed: yes, into the teaser/review repo on 2026-06-13.

Aeriadne is the marketplace/compiler package for private plugin, skill, agent,
adapter, and MCP/server cataloging. It can describe CTMv3, Mentat, Codex Config
Topology, and BB7/SovereignMCP, but it does not own their runtime
state or vendor their private indexes.

## Release Rule

Treat this staging tree as the working source. Treat the public repo as the
reviewed release surface. Do not copy generated runtime state, local analysis
caches, private semantic archive paths, plugin caches, local marketplace caches,
or secret-bearing files into the public repo.

The public repo already has external clone pressure. A copyover must preserve
existing user paths and installer expectations unless a migration/deprecation
note is included and reviewed first.

## Candidate Copy List

Copy these surfaces only after validation passes and Daeron reviews the exact
diff:

- `plugin.json`
- `plugin.toml`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `README.md`
- `MANIFEST.md`
- `MARKETPLACE_ROADMAP.md`
- `CHANGELOG.md`
- `LICENSE.md`
- `AGENTS.md`
- `CLAUDE.md`
- `TOPOLOGY.md`
- `ARCHITECTURE_MAP.md`
- `FAILURE_GRAMMAR.md`
- `PROVENANCE.md`
- `.releaseignore`
- `COPYOVER_MANIFEST.md`
- `.claude/`
- `.codex/`
- `.github/`
- `.sovereign/golden_paths.json`
- `.sovereign/topology_fingerprint.txt`
- `registry/`
- `marketplace/`
- `adapters/`
- `agents/`
- `mcp/`
- `scripts/`
- `tests/`
- `validation/`
- `skills/constitutional-prompt-framework/`
- `skills/aeriadne-marketplace-operator/`

## Exclusions

Never copy these into the public repo:

- `.git/`
- `.codegraph/`
- `.venv/`, `venv/`, `env/`, `ENV/`
- `__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`
- `.sovereign/session_state.json`
- local DB/log/process files such as `*.sqlite`, `*.sqlite3`, `*.db`,
  `*.db-wal`, `*.db-shm`, `*.pid`, and `*.log`
- secret/auth files such as `.env`, `.env.*`, `auth.json`, and
  `installation_id`
- scratch or runtime folders such as `sessions/`, `logs/`, `tmp/`, and
  `cache/`
- generated archives such as `*.zip`, `*.tar.gz`, `*.tgz`, and `*.tar`
- generated filetree snapshots unless Daeron explicitly promotes one as a
  documentation artifact
- local marketplace cache artifacts, plugin cache payloads, and runtime DBs
- staging-local site prototypes that are marked `public_copyover=false` in
  `registry/site_prototypes.json`
- backup files and editor scratch files

Do not include private semantic archive paths, private indexed workspace paths,
or raw private Golden Path source paths in public release notes, marketplace
cards, validation reports, or copyover docs.

## Validation Gate

Run from the staging root before copyover:

```bash
python3 scripts/validate_package.py .
python3 scripts/privacy_boundary_scan.py .
PYTHONDONTWRITEBYTECODE=1 python3 tests/privacy_boundary_scan_smoke.py
python3 scripts/site_prototype_audit.py .
PYTHONDONTWRITEBYTECODE=1 python3 tests/site_prototype_audit_smoke.py
python3 /home/daeron/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
python3 -m json.tool plugin.json >/dev/null
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 -m json.tool .claude-plugin/plugin.json >/dev/null
python3 -m json.tool registry/aeriadne.plugin.json >/dev/null
python3 -m json.tool registry/cognitive-topology-map.plugin.json >/dev/null
python3 -m json.tool registry/mentat.plugin.json >/dev/null
python3 -m json.tool registry/codex-config-topology.plugin.json >/dev/null
cmp -s plugin.json .codex-plugin/plugin.json
cmp -s plugin.json .claude-plugin/plugin.json
python3 skills/constitutional-prompt-framework/scripts/validate_skill_package.py skills/constitutional-prompt-framework
python3 skills/constitutional-prompt-framework/scripts/constitution_linter.py skills/constitutional-prompt-framework/examples/example-agent-constitution.md
python3 skills/constitutional-prompt-framework/scripts/score_constitution.py skills/constitutional-prompt-framework/examples/example-agent-constitution.md
python3 skills/constitutional-prompt-framework/scripts/run_static_evals.py skills/constitutional-prompt-framework/tests/eval_cases.yaml
python3 skills/constitutional-prompt-framework/scripts/render_constitution_from_spec.py skills/constitutional-prompt-framework/tests/fixtures/minimal_constitution_spec.json -o /tmp/aeriadne-cpf-rendered-check.md
```

`scripts/validate_package.py` invokes `scripts/privacy_boundary_scan.py`, and
the scanner may also be run directly. It intentionally avoids embedding private
archive names while failing on unapproved local absolute paths, external media
paths, private source identifiers, and stale local tool log/archive path shapes.

`scripts/validate_package.py` also invokes `scripts/site_prototype_audit.py`.
The audit preserves staging-local site/page prototypes such as the Mentat HTML
artifact while proving they stay excluded from public copyover until Daeron
promotes the linked-doc/site layer.

## Candidate Copy Command

Use this only after review:

```bash
rsync -av --delete \
  --exclude-from=.releaseignore \
  /home/daeron/Projects/Modern-ML/Plugins/Aeriadne/ \
  /home/daeron/Repositories/Somnus-Intellligence-Stack/Plugins/Aeriadne/
```

Then inspect the public repo diff before committing. If any existing public
path is moved or removed, add migration/deprecation notes before push.

## Promotion Rules

- Do not install `aeriadne@local` without explicit operator approval.
- Do not claim installed status without `codex plugin list` and prompt-input
  evidence.
- Do not refresh local marketplace cache payloads from this tree until Daeron
  reviews the staged package.
- Do not copy into the public repo until this manifest and the exact diff are
  reviewed.
- Keep direct CPF authoring sources intact unless Daeron explicitly retires
  them.
- Keep CTMv3, Mentat, Codex Config Topology, and BB7/SovereignMCP as
  independently owned packages or capability planes; Aeriadne catalogs them.
- Keep non-owned local development tools out of the attached marketplace surface.
