# Codex Config Topology Plugin

This plugin packages the `codex-config-topology` skill as an installable Codex plugin.

It is a cognitive/environment support surface for Codex, not a replacement for BB7/Sovereign tools. Codex remains the active state machine; this plugin helps it reason about the surrounding control plane: config layers, plugin/skill packaging, hooks, MCP servers, memories, permissions, project docs, and operator doctrine.

## Live ontology

- Active server plane: `/home/daeron/Somnus-MCP`
- Sovereign data root: `/home/daeron/Somnus-MCP/data`
- Skill source used for this package: `/home/daeron/.codex/skills/custom/codex-config-topology`
- Modern-ML package source: `Plugins/Codex-Config-Topology`
- Local marketplace install source: `~/.claude/plugins/marketplaces/local/plugins/codex-config-topology`

## Verification

```bash
codex plugin list | grep codex-config-topology
codex debug prompt-input 'probe $codex-config-topology plugin visibility'
```

The expected prompt-input evidence is a plugin skill entry similar to:

```text
codex-config-topology:codex-config-topology
```

There may also be a direct user-skill entry from `~/.codex/skills/custom/codex-config-topology`; that is intentionally left in place for local authoring while the plugin provides installable distribution.
