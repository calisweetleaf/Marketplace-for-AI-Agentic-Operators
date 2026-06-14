# Aeriadne

Type: Plugin
Status: Private v1 / staged, installed locally
Version: 1.0.0
Clients: Codex, Claude Code, OpenCode
Canonical path: `/home/daeron/Projects/Modern-ML/Plugins/Aeriadne`

## What it does

Aeriadne packages the Constitutional Prompt Framework as a skill-activated plugin and adds a private marketplace scaffold for plugin manifests, skills, agent prompts, adapters, and MCP/server cards.

## Includes

- `constitutional-prompt-framework` skill
- `aeriadne-marketplace-operator` skill
- Aeriadne subagent prompt pack
- `sovereign-bb7` MCP/server reference card
- Registry and marketplace card skeleton
- Codex, Claude Code, and OpenCode adapter docs

## Codex exposure

```text
aeriadne:constitutional-prompt-framework
aeriadne:aeriadne-marketplace-operator
```

## Boundary

Installed locally as `aeriadne@local` after marketplace refresh. BB7/SovereignMCP is referenced as canonical server plane, not vendored. Public copyover remains blocked on Daeron review.
