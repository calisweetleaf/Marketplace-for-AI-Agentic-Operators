# Aeriadne Marketplace Surface

This folder is the human-facing rendered side of the private/local marketplace scaffold.

Registry files under `../registry/` are the machine-readable source. Marketplace cards here are readable summaries generated or maintained from registry facts.

## Contents

- `cards/aeriadne.plugin.md`
- `cards/cognitive-topology-map.plugin.md`
- `cards/mentat.plugin.md`
- `cards/codex-config-topology.plugin.md`
- `cards/constitutional-prompt-framework.skill.md`
- `cards/aeriadne-marketplace-operator.skill.md`
- `cards/sovereign-bb7.mcp.md`
- `indexes/plugin-index.yaml`
- `indexes/skill-index.yaml`
- `indexes/agent-index.yaml`
- `indexes/mcp-index.yaml`
- `site-prototypes.md`

## Rule

Cards must not claim installed status without install evidence. Use `private-v1`, `staged`, `validated-local`, or `installed-local` precisely.

Plugin cards must describe the package-level state loop first. Hooks, commands,
skills, MCP surfaces, monitors, and adapters are projections of the package, not
the package identity.

MCP cards must describe owned or canonical server planes, not private indexed
workspaces, semantic archives, runtime logs, local databases, or non-owned
development tools.

Local site prototypes are tracked separately from plugin cards. They are
preserved staging artifacts for future linked-doc/site pages, not public
copyover payloads until Daeron promotes them.
