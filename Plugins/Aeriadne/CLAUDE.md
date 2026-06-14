# CLAUDE.md - Aeriadne

This directory is the Aeriadne private marketplace plugin package.

## Read First

1. `AGENTS.md`
2. `TOPOLOGY.md`
3. `ARCHITECTURE_MAP.md`
4. `FAILURE_GRAMMAR.md` when touching registry, adapters, MCP/server cards, install state, or native plugin expansion.
5. `PROVENANCE.md` before changing boundaries or revisiting old decisions.

## Current Operating State

- Package id: `aeriadne`
- Status: `private-v1`, validated-local, installed locally as `aeriadne@local`.
- Contains two skills:
  - `constitutional-prompt-framework`
  - `aeriadne-marketplace-operator`
- Codex exposure after local install:
  - `aeriadne:constitutional-prompt-framework`
  - `aeriadne:aeriadne-marketplace-operator`

## Do Not Blur

- Aeriadne is not BB7/Somnus-MCP.
- Aeriadne is not Mentat.
- Aeriadne is not CTMv3.
- Aeriadne is not a public marketplace.
- MCP/server cards are references, not vendored runtime code.
- Adapters are projections, not canonical package truth.

## Validation

Run from this directory:

```bash
python3 scripts/validate_package.py .
python3 skills/constitutional-prompt-framework/scripts/validate_skill_package.py skills/constitutional-prompt-framework
python3 -m ctmv3 status --json --project-root /home/daeron/Projects/Modern-ML/Plugins/Aeriadne
```

Use the longer validation list in `README.md` when changing CPF internals.
