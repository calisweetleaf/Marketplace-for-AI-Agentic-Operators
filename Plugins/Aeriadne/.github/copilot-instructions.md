# Aeriadne Instructions

This path is a private Aeriadne plugin and marketplace package staging workspace. The canonical review repo is `/home/daeron/Repositories/Somnus-Intellligence-Stack/`; do not edit it unless Daeron explicitly asks.

Before changing files, read:

- `AGENTS.md`
- `TOPOLOGY.md`
- `ARCHITECTURE_MAP.md`
- `FAILURE_GRAMMAR.md`
- `PROVENANCE.md`

Rules:

- Keep plugin, skill, agent prompt, MCP/server card, adapter, registry, and marketplace card boundaries distinct.
- Do not vendor Somnus-MCP / BB7, Mentat runtime state, CTMv3 engine state, secrets, caches, logs, databases, or auth files.
- Do not claim installed status without command evidence.
- Update registry and marketplace cards together when status or package contents change.
- Run `python3 scripts/validate_package.py .` before treating package edits as complete.
