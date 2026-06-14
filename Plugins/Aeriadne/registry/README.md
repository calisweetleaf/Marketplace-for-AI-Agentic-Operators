# Aeriadne Registry

This directory is the v1 local marketplace registry for Aeriadne.

It is intentionally small and private-first. The goal is to make package contents queryable and installable later without turning the plugin into a public marketplace prematurely.

## Files

- `aeriadne.plugin.json` — JSON package card for clients/scripts that expect JSON.
- `cognitive-topology-map.plugin.json` — native workspace activation plugin card.
- `mentat.plugin.json` — native runtime plugin card.
- `codex-config-topology.plugin.json` — Codex control-plane plugin card; currently staged-local and not installed.
- `plugins.yaml` — plugin inventory.
- `skills.yaml` — bundled skill inventory.
- `agents.yaml` — agent/subagent prompt pack inventory.
- `mcp_servers.yaml` — canonical MCP/server reference inventory.
- `site_prototypes.json` — staging-local site/page prototype ledger.

## Rules

- Registry status must match evidence.
- Installed status requires install verification.
- Native plugins must be represented by committed state, validation gates, copyover boundaries, and exposed surfaces.
- MCP servers should be cataloged by canonical reference unless intentionally vendored.
- Site prototypes are preserved local artifacts until explicitly promoted; keep
  them excluded by the owning package's `.releaseignore`.
- Do not include secrets, tokens, auth files, runtime databases, sessions, or caches.
- Do not include private semantic archive paths or private indexed workspace paths.
