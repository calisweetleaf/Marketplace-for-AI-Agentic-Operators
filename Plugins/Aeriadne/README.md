# Aeriadne - CPF + Private Marketplace Plugin

`Aeriadne` is a **skill-activated plugin** for Daeron's local/private agent marketplace stack.

It packages the existing `constitutional-prompt-framework` skill, adds a second `aeriadne-marketplace-operator` skill, and provides the first concrete scaffold for a private marketplace spanning Codex, Claude Code, OpenCode, plugin packages, skills, agent/subagent prompts, and MCP/server-plane reference cards.

Sequencing note: Aeriadne is downstream of `../Cognitive-Topology-Map/` and `../Mentat/`. Those two staging packages now have release/copyover gates and Aeriadne is beginning to rebuild around their current package truth before any reviewed copy into `/home/daeron/Repositories/Somnus-Intellligence-Stack/`.

Native plugin doctrine: plugins are independent environment-intelligence packages between the operator and the active agent runtime. A plugin may expose hooks, skills, commands, MCP tools, monitors, adapters, registries, or cards, but those are projections of the package, not the package itself. See `../PLUGIN_RUNTIME_DOCTRINE.md`.

Golden Path contract: Aeriadne registry entries should preserve the five runtime roles from the internal Golden Path doctrine without copying private source paths into public-facing package cards:

- committed state ledger: what durable state the plugin actually owns;
- validation membrane: what accepts or rejects candidate transitions;
- compensation ledger: what copyover, rollback, uninstall, or release-exclude paths exist;
- divergence process: what drift, stale state, or topology mismatch means;
- terminal boundary: what irreversible pivot requires Daeron review.

This is why native plugin cards lead with committed state, validation, copyover, known gaps, and notes before listing hooks, commands, skills, or MCP surfaces.

## Current status

- Status: `private-v1` / validated-local, installed locally as `aeriadne@local`
- CTMv3 state: activated locally on `2026-06-13`; read `TOPOLOGY.md`, `ARCHITECTURE_MAP.md`, `FAILURE_GRAMMAR.md`, and `PROVENANCE.md` for warm-start context
- Date staged: `2026-06-05`
- Source CPF skill copied from: `/home/daeron/.codex/skills/custom/constitutional-prompt-framework`
- Modern-ML plugin path: `/home/daeron/Projects/Modern-ML/Plugins/Aeriadne`
- Workspace role: outside staging/package workspace for review and copy/paste
- Canonical review repo: `/home/daeron/Repositories/Somnus-Intellligence-Stack/`
- Repo edit rule: do not edit the canonical repo unless Daeron explicitly requests it
- Primary plugin id: `aeriadne`
- Display name: `Aeriadne`
- Legacy/search aliases: `Ariadne`, `cpf-plugin-ariadne`, `CPF-Plugin-Ariadne`
- Deprecated provenance path: `Plugins/old/Parallax-Narthex/CPF-Plugin-Ariadne/`
- Install action: local marketplace refresh performed; `aeriadne@local`, `mentat@local`, and `ctmv3-workspace-activator@local` are installed/enabled in Codex
- Git action: none; do not push during the Modern-ML restructure pass
- Public copyover: performed into this teaser/review repo on `2026-06-13`; `COPYOVER_MANIFEST.md` and `.releaseignore` remain the boundary ledger

## What it contains

Aeriadne v1 contains **two first-class skills**:

1. `constitutional-prompt-framework`
   - copied from the direct Codex custom skill source
   - derives, hardens, audits, ports, scores, and packages constitutions/prompts/skill instructions
2. `aeriadne-marketplace-operator`
   - new plugin-local skill
   - packages plugins, skills, agent prompts, MCP/server cards, registries, adapters, marketplace cards, and release gates

Aeriadne also includes:

- plugin manifests (`plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`)
- canonical local/private manifest (`plugin.toml`)
- copyover gate and release exclusions (`COPYOVER_MANIFEST.md`, `.releaseignore`)
- registry files (`registry/*.yaml`, `registry/*.plugin.json`)
- marketplace cards and indexes (`marketplace/`)
- site prototype ledger and audit (`registry/site_prototypes.json`,
  `marketplace/site-prototypes.md`, `scripts/site_prototype_audit.py`)
- Codex, Claude Code, and OpenCode adapter docs (`adapters/`)
- subagent prompt pack (`agents/subagents/`)
- MCP/server catalog corner (`mcp/`), with BB7/SovereignMCP as the canonical non-vendored server-plane reference
- validation script and smoke case docs (`scripts/`, `tests/`)
- CTMv3 warm-start artifacts (`TOPOLOGY.md`, `FAILURE_GRAMMAR.md`, `ARCHITECTURE_MAP.md`, `PROVENANCE.md`, `.sovereign/`)

## Native substrate registry

Aeriadne now catalogs native substrate packages by evidence status:

- `cognitive-topology-map` / CTMv3: workspace activation plugin, version `1.3.0`, staged at `/home/daeron/Projects/Modern-ML/Plugins/Cognitive-Topology-Map`.
- `mentat`: live cognitive runtime plugin, version `0.3.0`, staged at `/home/daeron/Projects/Modern-ML/Plugins/Mentat`.
- `codex-config-topology`: Codex control-plane plugin, version `1.0.0`, currently `staged-local` at `/home/daeron/Projects/Modern-ML/Plugins/Codex-Config-Topology`; it validates locally but is not installed or marketplace-refreshed.

These are represented by machine-readable registry cards under `registry/` and human-facing marketplace cards under `marketplace/cards/`. Aeriadne catalogs their committed state, validation gates, copyover boundaries, and exposed client surfaces. It does not own their runtime state.

CodeGraph is not part of the owned marketplace surface. It remains a non-owned local development aid used outside this package, and Aeriadne does not ship a card, registry row, or client attachment for it.

Site prototypes are cataloged separately from plugin packages. The current
prototype ledger preserves the Mentat root HTML page as a staging-local
linked-doc/site seed while keeping `public_copyover=false` until Daeron promotes
that surface. The site audit also checks semantic markers from the page's
Mentat spec: state-machine substrate, Q-table learning loop, insight bus,
drift/hooks, and MCP/runtime projection.

## Layer classification

Aeriadne does **not** replace BB7, Mentat, Codex Config Topology, or CTMv3.

```text
Codex Config Topology     # Codex control-plane topology and plugin/config/hook doctrine
Aeriadne / CPF            # constitution, prompt, plugin-packaging, registry, marketplace compiler
CTMv3 / Cognitive Map     # workspace activation and codebase topology
Mentat                    # live session/runtime substrate
Somnus-MCP / BB7          # canonical MCP/tool/server plane and data root
```

Codex remains the active agent runtime in a Codex session, but native plugins are not passive accessories. They are independent local runtime packages that improve state transitions, packaging, context routing, validation, observation, and operator ergonomics through their exposed surfaces.

## Directory shape

```text
Aeriadne/
├── plugin.json
├── plugin.toml
├── .codex-plugin/plugin.json
├── .claude-plugin/plugin.json
├── .releaseignore
├── COPYOVER_MANIFEST.md
├── README.md
├── MANIFEST.md
├── MARKETPLACE_ROADMAP.md
├── CHANGELOG.md
├── LICENSE.md
├── registry/
├── marketplace/
├── adapters/
├── agents/
├── mcp/
├── scripts/
├── tests/
└── skills/
    ├── constitutional-prompt-framework/
    └── aeriadne-marketplace-operator/
```

## Codex Exposure

Installed `aeriadne@local` exposes:

```text
aeriadne:constitutional-prompt-framework
aeriadne:aeriadne-marketplace-operator
```

Do not install both `aeriadne@local` and the legacy `cpf-plugin-ariadne@local` unless duplicate CPF exposure is intentional.

Do not delete `/home/daeron/.codex/skills/custom/constitutional-prompt-framework` just because this package exists. Direct authoring and plugin distribution can coexist.

## Validation

From this plugin root:

```bash
python3 scripts/validate_package.py .
python3 scripts/privacy_boundary_scan.py .
PYTHONDONTWRITEBYTECODE=1 python3 tests/privacy_boundary_scan_smoke.py
python3 /home/daeron/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
python3 -m json.tool plugin.json >/dev/null
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 -m json.tool .claude-plugin/plugin.json >/dev/null
python3 -m json.tool registry/aeriadne.plugin.json >/dev/null
python3 -m json.tool registry/cognitive-topology-map.plugin.json >/dev/null
python3 -m json.tool registry/mentat.plugin.json >/dev/null
python3 -m json.tool registry/codex-config-topology.plugin.json >/dev/null
python3 skills/constitutional-prompt-framework/scripts/validate_skill_package.py skills/constitutional-prompt-framework
python3 skills/constitutional-prompt-framework/scripts/constitution_linter.py skills/constitutional-prompt-framework/examples/example-agent-constitution.md
python3 skills/constitutional-prompt-framework/scripts/score_constitution.py skills/constitutional-prompt-framework/examples/example-agent-constitution.md
python3 skills/constitutional-prompt-framework/scripts/run_static_evals.py skills/constitutional-prompt-framework/tests/eval_cases.yaml
python3 skills/constitutional-prompt-framework/scripts/render_constitution_from_spec.py skills/constitutional-prompt-framework/tests/fixtures/minimal_constitution_spec.json -o /tmp/aeriadne-cpf-rendered-check.md
```

Local install evidence is recorded in the status block above and in `registry/aeriadne.plugin.json`.

## Copyover gate

This public tree is the clean review mirror, not the active private workspace and not the semantic archive. Before the next refresh into `/home/daeron/Repositories/Somnus-Intellligence-Stack/Plugins/Aeriadne`, review `COPYOVER_MANIFEST.md`, run the validation commands above, and use `.releaseignore` as the release exclusion ledger. The package validator invokes `scripts/privacy_boundary_scan.py`, which allows only known package/review/control-plane roots and rejects unapproved local paths or compact private source identifiers. The copyover gate excludes private semantic archive paths, private indexed workspace paths, stale local tool index state, runtime DBs, secrets, `.sovereign/session_state.json`, and generated filetree snapshots unless Daeron explicitly promotes one.

## Marketplace role

Aeriadne is the current proof pattern for a private marketplace structure:

- `Plugins/` for installable package shells.
- `Skills/` for reusable cognitive payloads.
- `Agents/` for role/subagent prompt packs.
- `MCP/` or `Servers/` for canonical server/tool-plane cards.
- `Registry/` for machine-readable inventory.
- `Marketplace/` for human-facing package cards and indexes.
- `Adapters/` for Codex, Claude Code, and OpenCode projections.

The full staged plan is in `MARKETPLACE_ROADMAP.md`.

## CTMv3 activation

Aeriadne is now CTMv3-activated as a package workspace, not merely documented as a plugin folder.

Use:

- `TOPOLOGY.md` for load-bearing concepts and boundaries.
- `FAILURE_GRAMMAR.md` for pre-failure signatures.
- `ARCHITECTURE_MAP.md` for traversal by question.
- `PROVENANCE.md` for decisions, rejected alternatives, open questions, and session log.
- `.sovereign/session_state.json` for warm-start state.

This activation answers the main expansion question: it is not too late to activate Aeriadne. The package was already the right proof pattern; CTMv3 gives it a durable warm-start layer before expanding the native plugin marketplace around the owned plugin triad, Codex Config Topology as a staged control-plane candidate, and Somnus-MCP / BB7 as the core server plane.
