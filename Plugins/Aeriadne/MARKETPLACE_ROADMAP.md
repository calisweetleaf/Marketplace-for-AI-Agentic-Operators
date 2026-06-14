# Aeriadne Marketplace Roadmap

This is the staged path from a copied CPF skill package to a private multi-client agent marketplace for Codex, Claude Code, OpenCode, plugins, skills, agents/subagent prompts, and the canonical MCP/server plane.

Important sequencing correction: Aeriadne is downstream of CTMv3 and Mentat hardening. Work should stabilize `../Cognitive-Topology-Map/` and `../Mentat/` first, then use Aeriadne to package, index, card, validate, and adapt that native plugin environment.

Native plugin correction: plugins are independent environment-intelligence packages, not tool lists, hook folders, or skill bundles. Aeriadne should catalog the package state loop and validation gates first, then list exposed hooks/skills/tools as surfaces. See `../PLUGIN_RUNTIME_DOCTRINE.md`.

## Operating constraint

No git push in this pass. Aeriadne is an outside staging/package workspace; Daeron reviews/copies changes into the canonical repo at `/home/daeron/Repositories/Somnus-Intellligence-Stack/` when ready. Package work should remain local, auditable, and easy to move.

Public repo risk: `Somnus-Intellligence-Stack` already has external clone pressure. The next public push cannot destabilize current paths or installers. Reorganize and validate here first, then copy reviewed artifacts.

## Core model

Aeriadne starts as a **skill-activated plugin**, not a full platform rewrite. This describes Aeriadne's current payload shape; it does not define all plugins as skill bundles.

It has two first-class skills:

1. `constitutional-prompt-framework` — prompt/constitution architecture, audits, hardening, platform binding, prompt-to-skill conversion.
2. `aeriadne-marketplace-operator` — packaging, registry, adapters, marketplace cards, agent prompt packs, MCP/server cataloging, release gates.

Aeriadne references canonical MCP/server planes. It does not vendor BB7/SovereignMCP.

## Phase 0 — Current v1 staging

Goal: make Aeriadne a clean plugin-wrapped skill package inside `Modern-ML/Plugins/Aeriadne/`.

Deliverables:

- [x] Copy `/home/daeron/.codex/skills/custom/constitutional-prompt-framework` into `skills/constitutional-prompt-framework/`.
- [x] Add second skill shell: `skills/aeriadne-marketplace-operator/`.
- [x] Add root `plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`.
- [x] Add `plugin.toml` as canonical local/private manifest.
- [x] Add README, manifest, changelog, license notice, and marketplace roadmap.
- [x] Add registry skeleton: `registry/*.yaml`, `registry/aeriadne.plugin.json`.
- [x] Add marketplace cards and indexes.
- [x] Add Codex, Claude Code, and OpenCode adapter docs.
- [x] Add agents/subagents prompt pack.
- [x] Add MCP/server corner with `sovereign-bb7` canonical reference.
- [x] Add stdlib package validator.
- [x] Run deterministic validation.
- [ ] Install only after explicit operator review.

## Phase 0.5 — CTMv3 activation and native plugin map

Goal: make Aeriadne agent-operable as the proof package for a smarter native plugin environment before broadening the marketplace.

Deliverables:

- [x] Add `TOPOLOGY.md`.
- [x] Add `FAILURE_GRAMMAR.md`.
- [x] Add `ARCHITECTURE_MAP.md`.
- [x] Add `PROVENANCE.md`.
- [x] Add `.sovereign/` warm-start state.
- [x] Add local `.claude/`, `.codex/`, and `.github/` context/enforcement scaffolds.
- [ ] Decide whether to install `aeriadne@local`.
- [x] Add distinct marketplace cards/registry entries for Mentat and CTMv3 from their stabilized staging truth.
- [x] Add status-aware registry/card entry for Codex Config Topology and keep non-owned local development tools out of marketplace attachment.
- [ ] Decide whether Somnus-MCP / BB7 remains MCP-only or also needs a broader environment-plane card beyond `sovereign-bb7.mcp.md`.

Expansion rule: Aeriadne can compile and catalog native plugins, skills, agent packs, and MCP/server cards. It must not become the runtime owner of Mentat, CTMv3, or Somnus-MCP, and it must not flatten their independent loops into exposed-surface inventories.

## Phase 0.6 — CTMv3 and Mentat stabilization before final Aeriadne

Goal: finish the substrate plugins before promoting Aeriadne from scaffold to proper marketplace compiler.

Priority lanes:

- [x] Add workspace-level native plugin doctrine in `../PLUGIN_RUNTIME_DOCTRINE.md`.
- [x] Harden `../Cognitive-Topology-Map/` package shape, install flow, CTMv3 engine, client projections, committed state, and validation gates.
- [x] Harden `../Mentat/` package shape, runtime state loop, hooks, MCP/server components, state machine, monitors, evals, and validation gates.
- [x] Define CTMv3 and Mentat copyover manifests from staging tree to `/home/daeron/Repositories/Somnus-Intellligence-Stack/`.
- [x] Rebuild the initial Aeriadne registry/cards around current CTMv3 and Mentat package truth.
- [x] Preserve the internal Golden Path runtime roles in Aeriadne package-facing docs without leaking raw private source paths into marketplace cards.
- [x] Remove non-owned local development tool attachment and keep staged-local Codex Config Topology card.
- [x] Add Mentat command-frontmatter lint and prompt-surface review gates.
- [ ] Decide whether to refresh/install staged Codex Config Topology or supersede it with `official-codex-configuration`.
- [x] Add Aeriadne's own copyover manifest before any public repo copy.
- [ ] Keep existing public repo consumers stable; add migration/deprecation notes before moving or removing public paths.

## Phase 1 — Local Codex plugin install

Goal: expose CPF and Aeriadne packaging through the Codex plugin namespace while preserving the direct authoring skill.

Pattern to mirror:

```text
Modern-ML source package -> local marketplace package -> Codex cache -> config.toml plugin entry -> prompt-input evidence
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

## Phase 2 — Private marketplace canonical repository shape

Goal: stage the private marketplace index shape here, then let Daeron review/copy the accepted shape into `/home/daeron/Repositories/Somnus-Intellligence-Stack/`.

Candidate shape:

```text
Modern-ML/
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
├── Plugins/
│   ├── Aeriadne/
│   ├── Mentat/
│   ├── Cognitive-Topology-Map/
│   └── Codex-Config-Topology/
├── Skills/
│   ├── custom/
│   └── archived/
├── Agents/
│   ├── subagents/
│   ├── codex/
│   ├── claude-code/
│   └── opencode/
├── MCP/
│   ├── servers/
│   ├── contracts/
│   └── adapters/
├── Adapters/
│   ├── codex/
│   ├── claude-code/
│   └── opencode/
├── Docs/
└── Scripts/
```

Restructure principle:

- `Plugins/` contains complete packages with their own runtime/state doctrine, not just exposed hooks, skills, commands, or tools.
- `Skills/` contains standalone/shared skills.
- `Agents/` contains reusable subagent prompts.
- `MCP/` catalogs canonical servers and contracts.
- `Registry/` is machine-readable inventory.
- `Marketplace/` is rendered human-facing inventory.
- `Adapters/` projects canonical packages into client-specific shapes.

Do this as a restructuring pass, not as incidental cleanup inside a plugin edit.

## Phase 3 — Cross-client adapter contracts

Goal: one package card can tell Codex, Claude Code, and OpenCode how to consume the same cognitive payload.

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

Adapter rule: canonical package lives in `Plugins/Aeriadne/`. Client adapters generate or document client-specific projections. Do not make any client projection the source of truth.

## Phase 4 — MCP corner / server-plane cards

Goal: make the private marketplace show server/tool-plane reality without pretending MCP servers are plugins.

Initial MCP cards:

- `sovereign-bb7` — active canonical server plane at `/home/daeron/Somnus-MCP`, data root `/home/daeron/Somnus-MCP/data`.
- Non-owned local development tools stay outside the marketplace attachment surface.
- `mentat` — Mentat local introspection server inside the Mentat plugin/runtime substrate; future card.
- `ctmv3` — workspace activation package/server capability notes; future card if needed.

Rules:

- MCP cards document connection, capabilities, data roots, and safety boundaries.
- MCP cards do not claim to be skill/plugin payloads.
- The active BB7 data root remains `/home/daeron/Somnus-MCP/data`.

## Phase 5 — Agent/subagent prompt market

Goal: pull useful agent prompts from Claude Code, Codex, OpenCode, and local experiments into a normalized marketplace plane.

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
- Install exposure is verified in at least one client.
- Docs state local vs symlink vs external canonical roots.

## Non-negotiables

- Do not make public marketplace assumptions in v1.
- Do not vendor BB7/SovereignMCP into Aeriadne.
- Do not let client adapters become canonical source.
- Do not flatten skills, agents, MCP servers, and plugins into one undifferentiated folder.
- Do not copy secrets, cache files, runtime DBs, auth files, or session state.
- Do not overbuild UI before the registry exists.
- Do not restructure all of Modern-ML before Aeriadne proves the package pattern.

## Definition of v1 done

Aeriadne v1 is done when:

- It exists as a complete local plugin package.
- It contains exactly two first-class skills:
  - `constitutional-prompt-framework`
  - `aeriadne-marketplace-operator`
- It has an agents/subagents prompt folder.
- It has an MCP/server catalog with BB7/SovereignMCP as the canon server reference.
- It has registry/inventory docs.
- It has marketplace cards.
- It has Codex, Claude Code, and OpenCode adapter docs.
- It has validation gates.
- It has a copyover manifest and release exclusion ledger.
- It can be installed or dry-run installed locally without needing the broader Modern-ML restructure.
- The broader private repo restructure has a clear staged path but is not blocking v1.

## Current next move after v1 staging

1. Review `COPYOVER_MANIFEST.md` and the exact public repo diff before any copy.
2. Decide whether to install `aeriadne@local` or keep it staged until the broader marketplace registry is created.
3. Decide whether staged Codex Config Topology should be refreshed into the local marketplace, installed, or superseded by `official-codex-configuration`.
4. Update Modern-ML root docs so they reference `Plugins/Aeriadne/` as canonical and move older `CPF-Plugin-Ariadne` wording to legacy/provenance.
5. Only then stage the broader marketplace/private repo shape for Daeron to review and copy into `/home/daeron/Repositories/Somnus-Intellligence-Stack/`.
