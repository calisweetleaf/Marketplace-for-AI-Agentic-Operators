<div align="center">

<img src="templates/logo.png" alt="Aeriadne — Autonomous Intelligence Marketplace" width="440"/>

<br/>

# AERIADNE

**The first-of-its-kind private marketplace for agentic operability.**<br/>
*Plugins · Skills · Agents · MCP Servers — delivered to any coding agent.*

<br/>

[![Plugins](https://img.shields.io/badge/Plugins-3%20Active-667eea?style=flat-square&labelColor=0d1117)](Plugins/)
[![Skills](https://img.shields.io/badge/Skills-6%2B-764ba2?style=flat-square&labelColor=0d1117)](Skills/)
[![Runtimes](https://img.shields.io/badge/Runtimes-5-06b6d4?style=flat-square&labelColor=0d1117)](Adapters/)
[![Status](https://img.shields.io/badge/Status-Private%20v1-28c840?style=flat-square&labelColor=0d1117)](#)
[![License](https://img.shields.io/badge/License-SSS%20Internal-484f58?style=flat-square&labelColor=0d1117)](#license)

</div>

---

## What Is Aeriadne

Aeriadne is an **agent-operability marketplace** — not an ML framework, not a prompt collection, not a vibe-coded toolkit. It packages installable intelligence surfaces that make coding agents smarter, more disciplined, and operationally capable across five runtimes: Codex, Claude Code, OpenCode, Gemini CLI, and Grok Build.

The stack is built around a hard ontological separation: **plugins** handle session-state and runtime coupling; **skills** carry the cognitive payloads; **agents** are deployable role packs; **servers** define the MCP/tool plane; **the registry** makes everything discoverable. Nothing bleeds into anything else.

The design philosophy is operator-grade. The documentation reads like a running system because it is one.

---

## The Plugin Triad

Three first-class plugins form the operational core. Each is independently installable.

```
 ┌──────────────────────────────────────────────────────────────────────────┐
 │  PLUGIN TRIAD  ·  Aeriadne Intelligence Stack  ·  Private v1             │
 ├──────────────────┬───────────────────────────────────────┬───────────────┤
 │  PLUGIN          │  ROLE                                 │  STATUS       │
 ├──────────────────┼───────────────────────────────────────┼───────────────┤
 │  Mentat          │  Live session FSA + Q-table substrate │  Active       │
 │  CTMv3           │  Workspace activation engine          │  Active       │
 │  Aeriadne        │  CPF + private marketplace operator   │  Staged       │
 └──────────────────┴───────────────────────────────────────┴───────────────┘
```

<br/>

### Mentat — Live Cognitive Substrate

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Supported-3b82f6?style=flat-square&labelColor=0d1117)](Plugins/Mentat/)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Supported-8b5cf6?style=flat-square&labelColor=0d1117)](Plugins/Mentat/)
[![Codex](https://img.shields.io/badge/Codex-Adapter-06b6d4?style=flat-square&labelColor=0d1117)](Plugins/Mentat/)

A session-scoped state machine and reinforcement-learning Q-table that runs alongside the agent loop. Mentat observes every tool call, classifies state transitions, guards against scope drift, and snapshots session intelligence across compaction events.

```
  STATES: planning → exploring → executing → verifying → reflecting
          └→ blocked | drifting | compacting

  LEARNING: TD(0) Q-table · α=0.2, γ=0.8 · shared across Claude/Codex runtimes
  DRIFT GUARD: .mentat/scope.md → write-tool denial when deferred topics re-inject
  PERSISTENCE: handoff snapshots survive context compaction
```

**[Full Documentation](Docs/detailed-webpages/mentat-a-live-cognitive-substrate-plugin.html)** — complete Somnus design system page, full architecture and session lifecycle.<br/>
*View in browser after cloning · or open directly in the GitHub file viewer above.*

**→ [Plugins/Mentat/](Plugins/Mentat/)**

<br/>

### CTMv3 — Workspace Activation Engine

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Supported-3b82f6?style=flat-square&labelColor=0d1117)](Plugins/Cognitive-Topology-Map/)
[![Codex](https://img.shields.io/badge/Codex-Supported-8b5cf6?style=flat-square&labelColor=0d1117)](Plugins/Cognitive-Topology-Map/)
[![OpenCode](https://img.shields.io/badge/OpenCode-Supported-06b6d4?style=flat-square&labelColor=0d1117)](Plugins/Cognitive-Topology-Map/)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Supported-10b981?style=flat-square&labelColor=0d1117)](Plugins/Cognitive-Topology-Map/)
[![Cursor](https://img.shields.io/badge/Cursor-Supported-f59e0b?style=flat-square&labelColor=0d1117)](Plugins/Cognitive-Topology-Map/)

CTMv3 is **not a skill maker.** It is a codebase activation system — enter a repo and make it living for agents. Sets up topology, installs the agent-facing structure, wires in hooks and workflow surfaces, establishes memory/context/doctrine, and leaves the codebase in a state where an agent can actually work inside it instead of guessing.

```
  BOOT PROTOCOL:
  ─────────────────────────────────────────────────────────────────────────
  1. COLD_START detection  →  reads repo, classifies activation state
  2. BUILD artifacts       →  TOPOLOGY.md, FAILURE_GRAMMAR.md, PROVENANCE.md,
                              ARCHITECTURE_MAP.md, AGENTS.md, CLAUDE.md
  3. SCAFFOLD .xyz dirs    →  .sovereign/, .claude/, .codex/, .github/
  4. SEED golden paths     →  .sovereign/golden_paths.json
  5. FINGERPRINT           →  SHA-256 drift detection for topology docs
  6. LOG                   →  every action in PROVENANCE.md Session Log
  ─────────────────────────────────────────────────────────────────────────
  A skill may be one byproduct. The activated repo is the real output.
```

**→ [Plugins/Cognitive-Topology-Map/](Plugins/Cognitive-Topology-Map/)**

<br/>

### Aeriadne Plugin — CPF + Private Marketplace Operator

[![Codex](https://img.shields.io/badge/Codex-Staged-f59e0b?style=flat-square&labelColor=0d1117)](Plugins/Aeriadne/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Staged-f59e0b?style=flat-square&labelColor=0d1117)](Plugins/Aeriadne/)
[![OpenCode](https://img.shields.io/badge/OpenCode-Staged-f59e0b?style=flat-square&labelColor=0d1117)](Plugins/Aeriadne/)

Two skills, one plugin shell. `constitutional-prompt-framework` derives, hardens, audits, and packages agent constitutions across runtimes. `aeriadne-marketplace-operator` is the packaging engine — it writes plugin cards, registry entries, adapter docs, and release gates.

```
  aeriadne (plugin shell)
  ├── constitutional-prompt-framework    (CPF skill)
  │   └── derives · hardens · audits · ports · scores constitutions
  └── aeriadne-marketplace-operator      (marketplace skill)
      └── packages · registers · adapts · releases across 4 runtimes
```

**→ [Plugins/Aeriadne/](Plugins/Aeriadne/)**

---

## Quick Install

```bash
# Prerequisites: git, python3

# Clone the marketplace staging workspace
git clone https://github.com/calisweetleaf/Aeriadne.git
cd Aeriadne

# Bootstrap installer — sets up registry and local paths
bash install.sh
```

Individual plugin install instructions: each plugin's `README.md` and `INSTALL.md`.

---

## The Marketplace Planes

| Plane | Path | Purpose |
|---|---|---|
| **Plugins** | [`Plugins/`](Plugins/) | Installable runtime/cognitive package shells |
| **Skills** | [`Skills/`](Skills/) | Reusable cognitive workflows and domain-entry artifacts |
| **Agents** | [`Agents/`](Agents/) | Specialized subagent prompt packs for parallel workstreams |
| **Servers** | [`Servers/`](Servers/) | MCP/tool-plane reference cards and canonical server docs |
| **Registry** | [`Registry/`](Registry/) | Machine-readable inventory — `plugins.yaml`, `skills.yaml` |
| **Marketplace** | [`Marketplace/`](Marketplace/) | Human-facing package cards and browsable indexes |
| **Core** | [`Core/`](Core/) | Kernel, constitution, and runtime configuration surfaces |

---

## Design System

Documentation across this repo follows the **[Somnus Documentation Design System v3](desk/Somnus_Documentation_Design_System_v3.md)** — a terminal-first, operator-grade documentation aesthetic. Dark backgrounds. Monospace typography. Architecture diagrams in terminal frames. No collapsibles. No emoji in chrome.

Full-fidelity HTML documentation (complete Somnus glassmorphism design system — open in browser or via GitHub file viewer):

| Page | Description |
|---|---|
| [Mentat — Live Cognitive Substrate](Docs/detailed-webpages/mentat-a-live-cognitive-substrate-plugin.html) | Full architecture, FSA state machine, session lifecycle, and install guide |

---

## Repository Provenance

```
  Aeriadne / Somnus Intelligence Stack
  ─────────────────────────────────────────────────────────────────────────
  Operator:     Daeron  ·  Somnus Sovereign Systems
  Runtime axis: Codex · Claude Code · OpenCode · Gemini CLI · Cursor
  Server plane: Sovereign BB7 MCP
  Plugin triad: Mentat · CTMv3 · Aeriadne
  ─────────────────────────────────────────────────────────────────────────
  This repo is the agent-operability, onboarding, and private-marketplace
  staging workspace. It is not the full sovereign stack — it is the support
  layer that makes that stack accessible to agents and operators.
```

---

## License

Internal / Private Release v1 — UNLICENSED<br/>
© 2026 Somnus Sovereign Systems

---

<div align="center">

*Aeriadne · Autonomous Intelligence · Unlimited*

</div>
