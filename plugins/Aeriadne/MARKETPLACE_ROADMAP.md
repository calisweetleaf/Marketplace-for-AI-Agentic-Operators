# Aeriadne Marketplace Roadmap

This is the staged path from a copied CPF skill package to a private multi-client agent marketplace for Codex, Claude Code, OpenCode, Grok Build, plugins, skills, agents/subagent prompts, and the canonical MCP/server plane.

## Operating constraint

No git push in this pass. `Somnus-Intellligence-Stack` is being restructured; package work should remain local, auditable, and easy to move.

## Core model

Aeriadne starts as a **skill-activated plugin**, not a full platform rewrite.

It has two first-class skills:

1. `constitutional-prompt-framework` — prompt/constitution architecture, audits, hardening, platform binding, prompt-to-skill conversion.
2. `aeriadne-marketplace-operator` — packaging, registry, adapters, marketplace cards, agent prompt packs, MCP/server cataloging, release gates.

Aeriadne references canonical MCP/server planes. It does not vendor BB7/SovereignMCP.

Canonical source path for this consolidation repo:

```text
/home/daeron/Repositories/Somnus-Intellligence-Stack/plugins/Aeriadne
```

## Phase 0 — Current v1 staging

Goal: make Aeriadne a clean plugin-wrapped skill package inside `plugins/Aeriadne/`.

Deliverables:

- [x] Copy `/home/daeron/.codex/skills/custom/constitutional-prompt-framework` into `skills/constitutional-prompt-framework/`.
- [x] Add second skill shell: `skills/aeriadne-marketplace-operator/`.
- [x] Add root `plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`.
- [x] Add `plugin.toml` as canonical local/private manifest.
- [x] Add README, manifest, changelog, license notice, and marketplace roadmap.
- [x] Add registry skeleton: `registry/*.yaml`, `registry/aeriadne.plugin.json`.
- [x] Add marketplace cards and indexes.
- [x] Add Codex, Claude Code, OpenCode, and Grok Build adapter docs.
- [x] Add agents/subagents prompt pack.
- [x] Add MCP/server corner with `sovereign-bb7` canonical reference.
- [x] Add stdlib package validator.
- [x] Quarantine legacy runtime plugin marker directories from `plugins/old/` into `plugins/old/_archived-plugin-descriptors/`.
- [ ] Run deterministic validation after archive/path realignment.
- [ ] Install only after explicit operator review.

## Phase 1 — Local Codex plugin install

Goal: expose CPF and Aeriadne packaging through the Codex plugin namespace while preserving the direct authoring skill.

Pattern to mirror:

```text
Somnus-Intellligence-Stack source package -> local marketplace package -> Codex cache -> config.toml plugin entry -> prompt-input evidence
```

Expected exposure if installed as `aeriadne@local`:

```text
aeriadne:constitutional-prompt-framework
aeriadne:aeriadne-marketplace-operator
```

Validation:

```bash
codex plugin list | grep aeriadne
codex debug prompt-input 'probe $aeriadne plugin visibility'
```

Do not remove `/home/daeron/.codex/skills/custom/constitutional-prompt-framework` until Daeron explicitly decides direct authoring should stop.

Do not install legacy `cpf-plugin-ariadne@local` beside `aeriadne@local` unless duplicate CPF exposure is intentional.

## Phase 2 — Private marketplace repository shape

Goal: restructure `Somnus-Intellligence-Stack` into a marketplace index instead of a loose artifact shelf.

Candidate shape:

```text
Somnus-Intellligence-Stack/
├── Registry/
│   ├── plugins.yaml
│   ├── skills.yaml
│   ├── agents.yaml
│   ├── mcp_servers.yaml
│   └── compatibility.yaml
├── Marketplace/
│   ├── cards/
│   ├── indexes/
│   └── rendered/
├── plugins/
│   ├── Aeriadne/
│   ├── Mentat/
│   ├── Cognitive-Topology-Map/
│   └── old/
├── skills/
│   ├── grok-build-configurator/
│   ├── custom/
│   └── archived/
├── agents/
│   ├── subagents/
│   ├── codex/
│   ├── claude-code/
│   └── opencode/
├── MCP/ or Servers/
│   ├── servers/
│   ├── contracts/
│   └── adapters/
├── Adapters/
│   ├── codex/
│   ├── claude-code/
│   ├── opencode/
│   └── grok-build/
├── Docs/
└── Scripts/
```

Restructure principle:

- `plugins/` contains complete packages.
- `skills/` contains standalone/shared skills.
- `agents/` contains reusable subagent prompts.
- `MCP/` or `Servers/` catalogs canonical servers and contracts.
- `Registry/` is machine-readable inventory.
- `Marketplace/` is rendered human-facing inventory.
- `Adapters/` projects canonical packages into client-specific shapes.
- `plugins/old/` is archive/provenance only, not an installable root.

Do this as a restructuring pass, not as incidental cleanup inside a plugin edit.

## Phase 3 — Cross-client adapter contracts

Goal: one package card can tell Codex, Claude Code, OpenCode, and Grok Build how to consume the same cognitive payload.

Minimum adapter contract per package:

- Package name and aliases.
- Payload type: plugin, skill, agent-pack, MCP card, mixed bundle.
- Canonical source path.
- Local marketplace path.
- Client support matrix.
- Install command or manual install route per client.
- Expected exposure string per client.
- Validation command per client.
- Known conflicts/duplicates.
- Security/privacy notes.

Adapter rule: canonical package lives in `plugins/Aeriadne/`. Client adapters generate or document client-specific projections. Do not make any client projection the source of truth.

## Phase 4 — MCP corner / server-plane cards

Goal: make the private marketplace show server/tool-plane reality without pretending MCP servers are plugins.

Initial MCP cards:

- `sovereign-bb7` — active canonical server plane at `/home/daeron/Somnus-MCP`, data root `/home/daeron/Somnus-MCP/data`.
- `codegraph` — structural code intelligence; future card.
- `mentat` — Mentat local introspection server inside the Mentat plugin/runtime substrate; future card.
- `ctmv3` — workspace activation package/server capability notes; future card if needed.

Rules:

- MCP cards document connection, capabilities, data roots, and safety boundaries.
- MCP cards do not claim to be skill/plugin payloads.
- The active BB7 data root remains `/home/daeron/Somnus-MCP/data`.

## Phase 5 — Agent/subagent prompt market

Goal: pull useful agent prompts from Claude Code, Codex, OpenCode, Grok Build, and local experiments into a normalized marketplace plane.

Initial Aeriadne subagents:

- `prompt-architect`
- `package-cartographer`
- `compatibility-auditor`
- `registry-scribe`
- `release-sentinel`

Each agent card should include:

- Intended client(s).
- Required tools/capabilities.
- Write permissions and forbidden scopes.
- Expected final report shape.
- How it composes with skills/plugins.

Subagent rule: these are parallel workstreams, not rank hierarchy. Each produces an artifact and returns evidence. The main operator integrates.

## Phase 6 — Marketplace artifact build

Goal: generate installable archives and a searchable index from the source tree.

Artifacts:

- `registry.json` or YAML registry set.
- per-package manifest.
- per-package marketplace card.
- install instructions.
- validation report.
- optional zip/tarball.

Gate before publishing even privately:

- JSON/TOML/YAML validates.
- Skill frontmatter validates.
- Package paths exist.
- No secret-bearing files are packaged.
- No archived plugin marker directories are treated as active installables.
- Install exposure is verified in at least one client.
- Docs state local vs symlink vs external canonical roots.

## Non-negotiables

- Do not make public marketplace assumptions in v1.
- Do not vendor BB7/SovereignMCP into Aeriadne.
- Do not let client adapters become canonical source.
- Do not flatten skills, agents, MCP servers, and plugins into one undifferentiated folder.
- Do not copy secrets, cache files, runtime DBs, auth files, or session state.
- Do not overbuild UI before the registry exists.
- Do not let `plugins/old/` leak legacy packages as active installable plugin roots.

## Definition of v1 done

Aeriadne v1 is done when:

- It exists as a complete local plugin package.
- It contains exactly two first-class skills:
  - `constitutional-prompt-framework`
  - `aeriadne-marketplace-operator`
- It has an agents/subagents prompt folder.
- It has an MCP/server catalog with BB7/SovereignMCP as the canonical server reference.
- It has registry/inventory docs.
- It has marketplace cards.
- It has Codex, Claude Code, OpenCode, and Grok Build adapter docs.
- It has validation gates.
- It can be installed or dry-run installed locally without needing the broader repo restructure.
- The broader private repo restructure has a clear staged path but is not blocking v1.

## Current next move after v1 staging

1. Validate `plugins/Aeriadne/`.
2. Update repo root docs so they reference `plugins/Aeriadne/` as canonical and move older `CPF-Plugin-Ariadne` wording to legacy/provenance.
3. Decide whether to install `aeriadne@local` or keep it staged until the broader marketplace registry is created.
4. Only then restructure `Somnus-Intellligence-Stack` into the marketplace/private repo shape.
