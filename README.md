# Modern-ML — Sovereign Agent Marketplace / Onboarding Workspace

**Owner:** Daeron (Somnus Sovereign Systems)  
**Purpose:** Local-first organization layer for plugins, skills, agents, MCP/server visibility, and marketplace-ready agent-operability artifacts.

`Modern-ML` is not the full ML empire. It is the onboarding/control-plane workspace that makes Daeron's broader stack legible to Codex, Claude Code, OpenCode, and future coding agents.

---

## Current high-level shape

```text
Modern-ML/
├── Agents/                         # role/subagent prompt surfaces; mostly mirrored from canonical agent roots
├── Plugins/
│   ├── Aeriadne/                   # CPF + private marketplace scaffold; staged v1, not installed
│   ├── Codex-Config-Topology/      # Codex control-plane topology plugin; installed as codex-config-topology@local
│   ├── Cognitive-Topology-Map/     # CTMv3 workspace activation / topology package
│   ├── Mentat/                     # live cognitive/runtime substrate plugin
│   └── old/                        # graveyard/provenance for superseded staging attempts
├── Skills/                         # mixed local and symlinked skill/topology packages
├── Servers/                        # visible server-plane mirrors; active server root is /home/daeron/Somnus-MCP
├── AGENTS.md
├── CONTEXT.md
├── MEMORY.md
├── ARCHITECTURE_MAP.md
├── ECOSYSTEM_ADOPTION_MAP.md
├── REPO_ENTRY_MATRIX.md
└── 5-22-2026-modernMlTools-filetree.md
```

---

## Plugin map

### `Plugins/Aeriadne/`

Aeriadne is the newest staged v1 plugin package. It is a **skill-activated plugin** and private marketplace scaffold.

It contains two first-class skills:

- `constitutional-prompt-framework` — copied from `/home/daeron/.codex/skills/custom/constitutional-prompt-framework`; builds, audits, hardens, ports, scores, and packages constitutions/prompts/skill instructions.
- `aeriadne-marketplace-operator` — new packaging/registry/adapter/marketplace/MCP-card/release-gate skill.

It also contains:

- plugin manifests: `plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, `plugin.toml`
- registry skeleton: `registry/`
- marketplace cards and indexes: `marketplace/`
- client adapters: `adapters/codex/`, `adapters/claude-code/`, `adapters/opencode/`
- no-hierarchy subagent prompt pack: `agents/subagents/`
- MCP/server corner: `mcp/`, with `sovereign-bb7` as canonical reference

Expected Codex exposure after a future install:

```text
aeriadne:constitutional-prompt-framework
aeriadne:aeriadne-marketplace-operator
```

Aeriadne is currently staged and validated locally; it has **not** been installed/enabled in Codex in this pass.

### `Plugins/Codex-Config-Topology/`

Installable Codex plugin for doctrine-aware Codex control-plane work: AGENTS/override files, config, hooks, MCP wiring, plugins, skills, memory files, permissions, and operator topology.

Current installed exposure:

```text
codex-config-topology:codex-config-topology
```

### `Plugins/Cognitive-Topology-Map/`

CTMv3 workspace activation / topology package. Treat it as a portable codebase-entry package, not merely a skill maker.

### `Plugins/Mentat/`

Live cognitive/runtime substrate: state-machine instrumentation, Q-table route hints, drift detection, hook surfaces, debrief/reflect/dispatch/plan skills, and local introspection surfaces.

### `Plugins/old/`

Provenance/graveyard for superseded staging packages. The older `CPF-Plugin-Ariadne` / `cpf-plugin-ariadne` spelling should be treated as a legacy alias, not the canonical current package.

---

## Operator-stack relationship

```text
Codex Config Topology     # inspect/configure Codex control plane
Aeriadne / CPF            # constitution + prompt + private marketplace compiler
CTMv3 / Cognitive Map     # workspace activation and codebase topology
Mentat                    # session/runtime instrumentation substrate
Somnus-MCP / BB7          # canonical MCP/tool/server plane and data root
operator execution        # normal task work
```

Key distinction: Codex is the active state machine. Plugins are cognitive/environment support surfaces. BB7/SovereignMCP remains the canonical MCP/tool/server plane.

---

## Active server / MCP plane

The active server plane for current Codex work is external to this repo:

```text
/home/daeron/Somnus-MCP
/home/daeron/Somnus-MCP/data
```

`Servers/Muaddib` remains a visible legacy mirror/symlink artifact. Do not cite it as the active Codex server root unless specifically working on that mirror.

Aeriadne's `mcp/` folder is a **catalog/reference corner**, not a vendored server bundle.

---

## Local vs linked reality

Do not assume everything in this workspace is local.

- `Plugins/Aeriadne/`, `Plugins/Codex-Config-Topology/`, `Plugins/Cognitive-Topology-Map/`, and `Plugins/Mentat/` are local payload/package surfaces.
- Many entries under `Agents/` are mirrored/symlinked from canonical Claude agent roots.
- Many entries under `Skills/` are mirrored/symlinked from canonical OpenCode/custom skill roots.
- The active BB7/Sovereign server plane lives outside this repo at `/home/daeron/Somnus-MCP`.

---

## Cold-entry read order

For a cold-entry coding agent, the correct read order is:

1. `AGENTS.md`
2. `CONTEXT.md`
3. `MEMORY.md`
4. `README.md`
5. `ARCHITECTURE_MAP.md`
6. `ECOSYSTEM_ADOPTION_MAP.md`
7. `REPO_ENTRY_MATRIX.md`
8. `TECHNICAL_REFERENCE.md` — master technical spec; architecture, plane specs, flows, installation, glossary
9. `5-22-2026-modernMlTools-filetree.md` plus newer addenda/context before trusting old inventory wording

Branch by need:

- Codex control-plane/plugin/config topology → `Plugins/Codex-Config-Topology/`
- Constitution/prompt/marketplace packaging → `Plugins/Aeriadne/`
- Workspace activation/codebase topology → `Plugins/Cognitive-Topology-Map/`
- Live session instrumentation → `Plugins/Mentat/`
- Active MCP/tool/server plane → `/home/daeron/Somnus-MCP`

---

## Aeriadne validation evidence

From `Plugins/Aeriadne/`, the v1 staging pass validated:

- package validator: `PASS`
- JSON manifests: `PASS`
- TOML manifest: `PASS`
- plugin metadata mirrors identical: `PASS`
- CPF package validation: `PASS`
- CPF constitution linter: `PASS`
- CPF score: `87/100`, production candidate
- CPF static evals: `PASS`
- CPF render fixture: wrote `/tmp/aeriadne-cpf-rendered-check.md` (`3165` bytes)

Install was intentionally deferred.

---

## Next steps

1. Decide whether to install `aeriadne@local` now or keep it staged until the broader marketplace registry is moved to a root-level `Registry/` / `Marketplace/` structure.
2. If installing, mirror the proven local marketplace/cache/config pattern used by `codex-config-topology@local`.
3. Avoid installing the legacy `cpf-plugin-ariadne@local` unless duplicate CPF exposure is intentional.
4. Restructure Modern-ML into a private marketplace repo only after Aeriadne proves the package pattern.
5. Add explicit MCP cards for CodeGraph, Mentat, and CTMv3 if the marketplace server corner becomes the next workstream.

---

*Last updated: 2026-06-05*
