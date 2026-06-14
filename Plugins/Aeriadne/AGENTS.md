# AGENTS.md - Aeriadne

## Scope

This file governs `/home/daeron/Projects/Modern-ML/Plugins/Aeriadne`.

This path is an outside staging/package workspace for review and copy/paste. The canonical review repo is `/home/daeron/Repositories/Somnus-Intellligence-Stack/`. Do not edit that repo from Aeriadne work unless Daeron explicitly asks.

Aeriadne is a private-v1, skill-activated plugin package and marketplace proof pattern. It packages the Constitutional Prompt Framework, adds the Aeriadne Marketplace Operator skill, and defines the local/private registry, card, adapter, agent prompt, and MCP/server reference pattern for Daeron's native plugin environment.

## Precedence

Apply instructions in this order:

1. Global `.codex` runtime and safety law.
2. Modern-ML root `AGENTS.md`.
3. This Aeriadne `AGENTS.md`.
4. `TOPOLOGY.md`, `FAILURE_GRAMMAR.md`, `ARCHITECTURE_MAP.md`, and `PROVENANCE.md`.
5. Package docs: `README.md`, `MANIFEST.md`, `MARKETPLACE_ROADMAP.md`, registry files, and validation docs.

## Three Non-Negotiables

1. Keep artifact ontology intact: plugin, skill, agent prompt, MCP/server card, adapter, registry, and marketplace card are different things.
2. Do not vendor Somnus-MCP / BB7, Mentat runtime state, CTMv3 engine state, secrets, caches, logs, DBs, or auth files into Aeriadne.
3. Do not claim installed or exposed plugin status without command evidence.

## Entry Protocol

For any substantive Aeriadne work:

1. Read `TOPOLOGY.md` for the current cognitive map.
2. Read `FAILURE_GRAMMAR.md` if a task involves expansion, install status, registry changes, MCP/server references, or client adapters.
3. Use `ARCHITECTURE_MAP.md` to pick the first file path.
4. Check `PROVENANCE.md` before revisiting an already-decided boundary.
5. Run validation before finalizing package changes.

## Package Ontology

- Root manifests: `plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, `plugin.toml`.
- Skills: `skills/constitutional-prompt-framework/` and `skills/aeriadne-marketplace-operator/`.
- Registry: `registry/`.
- Marketplace cards and indexes: `marketplace/`.
- Client adapters: `adapters/`.
- Agent prompts: `agents/`.
- MCP/server references: `mcp/`.
- Validation: `scripts/`, `tests/`, `validation/`.
- CTMv3 warm-start layer: `TOPOLOGY.md`, `FAILURE_GRAMMAR.md`, `ARCHITECTURE_MAP.md`, `PROVENANCE.md`, `.sovereign/`.

## Editing Rules

- Preserve local/private status unless install or promotion evidence exists.
- Update registry and marketplace cards together when status, paths, package contents, or validation state changes.
- Keep client-specific mechanics inside `adapters/`.
- Keep server-plane reality inside MCP/server cards and contracts.
- Preserve CPF provenance to the direct authoring source.
- Keep validation evidence current when changing manifests, registries, skills, adapters, or package boundaries.
- Treat this as staging outside the canonical repo: avoid destructive edits, leave clear provenance, and assume Daeron reviews/copies changes into `/home/daeron/Repositories/Somnus-Intellligence-Stack/`.

## Validation Commands

Run from this directory:

```bash
python3 scripts/validate_package.py .
python3 -m json.tool plugin.json
python3 -m json.tool .codex-plugin/plugin.json
python3 -m json.tool .claude-plugin/plugin.json
python3 -m json.tool registry/aeriadne.plugin.json
python3 skills/constitutional-prompt-framework/scripts/validate_skill_package.py skills/constitutional-prompt-framework
python3 -m ctmv3 status --json --project-root /home/daeron/Projects/Modern-ML/Plugins/Aeriadne
```

Use the heavier CPF lint/score/static eval/render commands from `README.md` when editing CPF content itself.

## Native Plugin Expansion Doctrine

Aeriadne can help the environment become a smarter native plugin marketplace by adding registry/card/adapter surfaces for sibling systems:

- Somnus-MCP / BB7: MCP/server card and capability contract.
- Mentat: plugin/runtime substrate package or card.
- CTMv3: workspace activation package/card.
- Codex Config Topology: Codex control-plane plugin/card.
- Non-owned local development tools: no marketplace attachment; keep only release-hygiene exclusions for stale local state when needed.

For each expansion, first classify the artifact and identify canonical root. Do not copy implementation trees unless the artifact is truly a vendored skill/plugin payload and the package boundary says so.

## Current State

Status: `private-v1`, validated-local, installed locally as `aeriadne@local`.
CTMv3 state after this activation: warm-start artifacts present.
Codex exposure: `aeriadne:constitutional-prompt-framework`, `aeriadne:aeriadne-marketplace-operator`.
