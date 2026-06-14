# Local Site Prototypes

This page tracks staging-local HTML/site artifacts that should be preserved as
future linked-doc or site-page surfaces. These artifacts are not public copyover
payloads until Daeron explicitly promotes them.

## Current Prototypes

| ID | Owner | Source | Status | Public copyover | Semantic gate |
| --- | --- | --- | --- | --- | --- |
| `mentat-live-cognitive-substrate` | Mentat | `/home/daeron/Projects/Modern-ML/Plugins/Mentat/mentat-a-live-cognitive-substrate-for-claude-code.html` | staging-local, preserve | no | state-machine substrate, Q-table loop, insight/drift/hooks, MCP/runtime projection |

## Rules

- Do not delete listed prototypes during cleanup.
- Keep local site prototypes covered by the owning package's `.releaseignore`
  while they are staging-local.
- Do not copy local-only prototypes into the public repo unless Daeron promotes
  the linked-doc/site layer.
- Aeriadne catalogs these site artifacts but does not own the runtime packages
  they describe.
- Site prototypes that carry package specifications should declare semantic
  requirements in `registry/site_prototypes.json`. The audit then proves the
  page still contains the load-bearing terms, not just that an HTML file exists.
