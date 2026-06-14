# COPYOVER_MANIFEST.md - CTMv3 Staging To Public Repo

Snapshot date: 2026-06-13
Staging root: `/home/daeron/Projects/Modern-ML/Plugins/Cognitive-Topology-Map`
Public repo target: `/home/daeron/Repositories/Somnus-Intellligence-Stack/Plugins/Cognitive-Topology-Map`

## Release Rule

Treat this staging tree as the working source. Treat the public repo as the reviewed release surface. Do not copy generated runtime state or local analysis artifacts into the public repo.

The public repo already has clone pressure. A copyover must preserve existing user paths and installer expectations unless a migration note is included.

## Include

Copy these surfaces after validation passes:

- `README.md`
- `INSTALL.md`
- `CHANGELOG.md`
- `STRUCTURE.md`
- `CONTRIBUTING.md`
- `LICENSE`
- `CODEBASE_INTELLIGENCE.md`
- `core/`
- `docs/`
- `claude-code/`
- `codex/`
- `opencode/`
- `gemini-cli/`
- `cursor/`
- `research/`
- `extras/`
- `examples/`
- `tests/`
- `.github/workflows/`
- `.releaseignore`
- `COPYOVER_MANIFEST.md`
- `scripts/validate_release_tree.py`
- `scripts/privacy_boundary_scan.py`
- `tests/privacy_boundary_scan_smoke.py`

## Exclude

Never copy these into the public repo:

- `.git/`
- `.venv/`
- `.codegraph/`
- `.mentat/`
- `.pytest_cache/`
- `__pycache__/`
- `core/ctmv3.egg-info/`
- `data/`
- generated archives such as `Archive.zip`, `ctmv3-plugin-*.zip`, `*.zip`, `*.tar.gz`
- local DB/log/process files such as `*.db`, `*.db-wal`, `*.db-shm`, `*.pid`, `*.log`
- generated filetree snapshots unless Daeron explicitly wants one as a documentation artifact

## Validation Gate

Run from the staging root before copyover:

```bash
bash tests/run-all.sh
PYTHONDONTWRITEBYTECODE=1 python3 tests/privacy_boundary_scan_smoke.py
python3 scripts/privacy_boundary_scan.py .
python3 scripts/validate_release_tree.py .
```

The release tree validator does not require local-only artifacts to be deleted. It verifies that they are covered by `.releaseignore` and therefore excluded from the candidate copy set.
It also invokes the privacy boundary scanner and synthetic smoke test, so
release-candidate text is checked for private source identifiers, unapproved
local paths, external media paths, and stale local tool log/archive token shapes before
copyover.

## Candidate Copy Command

Use this only after review:

```bash
rsync -av --delete \
  --exclude-from=.releaseignore \
  /home/daeron/Projects/Modern-ML/Plugins/Cognitive-Topology-Map/ \
  /home/daeron/Repositories/Somnus-Intellligence-Stack/Plugins/Cognitive-Topology-Map/
```

Then inspect the public repo diff before committing.

## Current Hardening Notes

- Engine version is `1.3.0`.
- `ctmv3 state`, `ctmv3 serve`, `ctmv3 context`, and `ctmv3 ping` are part of the current CLI surface.
- `scripts/privacy_boundary_scan.py` enforces the private-source boundary over the release candidate text set.
- Latest release-tree validator result: `140` candidate files and `1045` ignored local-only/forbidden files after command backfill and cache cleanup.
- The local staging tree contains generated analysis/runtime artifacts; those are intentional local state and must remain excluded from release/copyover.
