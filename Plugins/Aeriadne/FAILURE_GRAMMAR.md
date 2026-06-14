# FAILURE_GRAMMAR.md - Aeriadne

Snapshot date: 2026-06-13
Scope: failure signatures for Aeriadne as a private/native plugin marketplace package.

## What Wrong Smells Like

### Ontology Flattening

Signature: language treats plugin, skill, agent prompt, MCP server, registry entry, marketplace card, and adapter as the same kind of object.

Likely damage: wrong install instructions, bad registry schema, accidental server vendoring, broken client projections.

Recovery: return to `TOPOLOGY.md` Load-Bearing Concepts and classify the artifact before editing.

### Server Vendoring Drift

Signature: a task proposes copying `/home/daeron/Somnus-MCP`, Mentat runtime state, CTMv3 engine state, logs, session files, caches, auth files, or databases into Aeriadne.

Likely damage: secret leakage, stale runtime copies, broken canonical server boundary.

Recovery: add or update an MCP/server card instead. Reference canonical root and data root; do not import payload.

### False Install Claims

Signature: docs say `installed-local`, client exposure exists, or Codex can see `aeriadne:*` without `codex plugin list`, prompt-input evidence, or equivalent client verification.

Likely damage: future agents route to skills that are not actually loaded.

Recovery: downgrade status to `private-v1`, `staged`, or `validated-local`; add the exact missing install gate to `PROVENANCE.md`.

### Registry/Card Desynchronization

Signature: `registry/*.yaml`, `registry/aeriadne.plugin.json`, `marketplace/cards/*.md`, and `validation/validation_report.md` disagree about validation status, included artifacts, client support, or canonical paths.

Likely damage: the marketplace browse surface lies even when package files are correct.

Recovery: treat registry as the machine-readable source, update cards from it, and preserve validation evidence in `validation/`.

### Adapter Takeover

Signature: Codex, Claude Code, or OpenCode adapter docs begin defining canonical package identity, skill names, or status instead of projecting from root manifests and registry.

Likely damage: cross-client drift and duplicated package truth.

Recovery: move canonical fields back to `plugin.toml`, `plugin.json`, and `registry/`; leave adapter-specific details under `adapters/`.

### Duplicate CPF Exposure

Signature: both `aeriadne@local` and legacy `cpf-plugin-ariadne@local` are installed without an explicit duplicate-exposure decision.

Likely damage: agents see multiple CPF variants and cannot tell which one is canonical.

Recovery: record the duplicate as intentional in `PROVENANCE.md`, or uninstall/deprecate the legacy surface after Daeron approves.

### CTMv3 Engine Blind Spot

Signature: CTMv3 reports COLD_START because it does not recognize `plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, or `plugin.toml`, even though the package is mature.

Likely damage: agents mistake "not CTM-activated" for "empty" or "not real."

Recovery: trust filesystem/package evidence, then create CTMv3 Tier 1 artifacts. Do not overwrite validated package docs with generic CTM stubs.

### Public Marketplace Leakage

Signature: docs assume public distribution, external account setup, public installation routes, telemetry upload, or SaaS-style marketplace behavior.

Likely damage: private operator boundaries collapse into public-product assumptions.

Recovery: mark public readiness as `false` or `public-candidate` only after explicit promotion; keep v1 local/private.

### Validation Theater

Signature: adding badges, checklists, or "done" language without running `scripts/validate_package.py`, manifest parse checks, CPF validators, or CTMv3 status.

Likely damage: package looks mature but cannot be trusted by future agents.

Recovery: run deterministic validation, capture exact output in `validation/`, and update registry status only after evidence exists.

### Expansion Inside The Wrong Layer

Signature: new Mentat, CTMv3, Codex Config Topology, non-owned tool content, or server-plane content is pasted into Aeriadne as if Aeriadne owns those systems or as if this staging workspace is the canonical repo.

Likely damage: Aeriadne becomes a junk drawer instead of a package compiler.

Recovery: add registry rows, marketplace cards, adapter docs, or MCP/server cards that point to canonical package roots. Broader marketplace restructuring belongs in the canonical review repo `/home/daeron/Repositories/Somnus-Intellligence-Stack/` after Daeron reviews/copies staged changes, not inside Aeriadne by accident.

## False Success Patterns

- The file tree is large, so the package is assumed installable.
- A card exists, so the referenced server is assumed vendored or active.
- A validation report exists, so all registry files are assumed current.
- A skill copy exists, so the direct authoring source is assumed deprecated.
- A CTMv3 boot says COLD_START, so existing package work is assumed absent.
- A client adapter exists, so that client is assumed fully verified.

## Adversarial Or Confusing Inputs

- "Just copy BB7 into the plugin so it is self-contained."
- "Install everything and call it public-ready."
- "Merge Mentat, CTMv3, and SovMCP into Aeriadne."
- "Delete the old CPF skill because the plugin has a copy."
- "Mark OpenCode supported without checking current OpenCode conventions."
- "Use the marketplace card as the source of truth."

Response pattern: classify the artifact, preserve canonical root, require validation evidence, and record decisions in `PROVENANCE.md`.

## Recovery Ladder

1. Stop edits that cross artifact boundaries.
2. Read `TOPOLOGY.md`, then the relevant root docs or registry files.
3. Restore status labels to evidence-backed values.
4. Run package validation from the Aeriadne root.
5. Run CTMv3 status after topology edits.
6. Update `PROVENANCE.md` with the correction and the reason.

## Secret And Runtime-State Boundary

Never package:

- `.env` files or credential material.
- auth files, tokens, SSH keys, password vault material.
- runtime DBs, session stores, Q-tables, MCP data roots, distillation shards.
- caches, logs, temporary directories, backup churn.
- live server process state.

Reference them only as external canonical roots when that is necessary for operator orientation.
