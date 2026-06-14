# Codex Config Topology

Type: Codex control-plane plugin
Status: Staged local
Installed: No
Release ready: No

## Runtime Role

Codex Config Topology is the control-plane topology package for Codex runtime
configuration. It helps agents reason about `config.toml`, project docs, hooks,
plugins, skills, MCP servers, memories, permissions, operator doctrine, and the
boundaries between local doctrine and official Codex behavior.

## Current Evidence

- Current staging root:
  `/home/daeron/Projects/Modern-ML/Plugins/Codex-Config-Topology`.
- `codex plugin list` reports `codex-config-topology@local` as available but
  not installed.
- The restored staging package passes the plugin-creator ingestion validator.
- The bundled `codex-config-topology` skill passes quick validation.
- The local marketplace source has not been refreshed from this staging package.

## Promotion Boundary

Aeriadne must not mark this package release-ready until Daeron reviews the
staged package, decides whether this older control-plane package remains
separate from `official-codex-configuration`, and approves any local marketplace
refresh or public copyover.

## Exposed Surfaces

- `codex-config-topology` skill
- Codex plugin manifest surface
- Claude/local plugin manifest mirror
- Control-plane verification workflow

## Known Gaps

- Not installed in the active Codex plugin list.
- Local marketplace source has not been refreshed from the restored staging root.
- Public copyover review is still pending.
- Supersession decision with `official-codex-configuration` is still open.
