# Cognitive Topology Map / CTMv3

Type: Workspace activation plugin
Status: Staged green, installed locally, not copied to public repo
Version: 1.3.0
Clients: Claude Code, Codex, opencode, Gemini CLI, Cursor
Canonical path: `/home/daeron/Projects/Modern-ML/Plugins/Cognitive-Topology-Map`
Public copy target: `/home/daeron/Repositories/Somnus-Intellligence-Stack/Plugins/Cognitive-Topology-Map`

## What it does

CTMv3 is the cross-runtime workspace activation system. It enters a codebase,
classifies cold/warm/partial state, creates topology and provenance artifacts,
initializes `.sovereign/` and client context directories, fingerprints topology,
and exposes a persistent context server lane.

CTMv3 is not a skill maker. A skill can be an output of an activation pass, but
the activated workspace is the committed state.

## Committed State

- `TOPOLOGY.md`
- `FAILURE_GRAMMAR.md`
- `PROVENANCE.md`
- `ARCHITECTURE_MAP.md`
- `AGENTS.md`
- `.sovereign/` warm-start state
- topology fingerprint
- golden-path signal records

## Surfaces

- Stdlib Python engine under `core/`.
- CLI commands including `boot`, `activate`, `warm`, `fingerprint`, `state`,
  `serve`, `context`, and `ping`.
- Claude Code, Codex, opencode, Gemini CLI, and Cursor adapters.
- Protocol docs, schema audit, examples, and CI workflows.

## Validation

Latest staging gate:

```bash
bash tests/run-all.sh
PYTHONDONTWRITEBYTECODE=1 python3 tests/privacy_boundary_scan_smoke.py
python3 scripts/privacy_boundary_scan.py .
python3 scripts/validate_release_tree.py .
```

Current evidence: engine version `1.3.0`; `tests/run-all.sh` `PASS` with 155
unit tests plus smoke, JSON, bash syntax, TOML command, inventory, and release
hygiene checks; privacy boundary `PASS`; release tree `PASS` with `140`
candidate files and `1045` ignored local-only/forbidden files after command
backfill and cache cleanup. `ctmv3-workspace-activator@local` is
installed/enabled in Codex; its plugin manifest and staged engine are both
`1.3.0`.

## Boundary

Aeriadne catalogs CTMv3 but does not own CTMv3's activation state. Public
copyover requires Daeron review of `COPYOVER_MANIFEST.md` and the exact public
repo diff, with stable public paths preserved unless a migration note is
approved.
CTMv3's validator now checks release-candidate text for private source
identifiers, unapproved local paths, external media paths, and stale local tool
log/archive token shapes while respecting `.releaseignore`.
