# PROVENANCE.md - Aeriadne

Root: `/home/daeron/Projects/Modern-ML/Plugins/Aeriadne`
Workspace role: outside staging/package workspace for review and copy/paste
Canonical review repo: `/home/daeron/Repositories/Somnus-Intellligence-Stack/`
Purpose: decision lineage, rejected alternatives, integration history, and session log for Aeriadne.

## Snapshot Lineage

### 2026-06-05 - Private v1 staging

Aeriadne was staged as a private-v1 skill-activated plugin package. The package copied `constitutional-prompt-framework` from `/home/daeron/.codex/skills/custom/constitutional-prompt-framework`, added `aeriadne-marketplace-operator`, registry skeletons, cards, adapters, agent prompts, MCP/server catalog reference, validator, tests, and validation report.

Status: originally validated locally and not installed; current local install evidence is recorded in `registry/aeriadne.plugin.json`.

### 2026-06-10 - File tree inventory

`filetree.md` was generated for Aeriadne. It recorded the staged package layout before CTMv3 activation artifacts existed.

### 2026-06-13 - CTMv3 activation

CTMv3 boot reported COLD_START: no Tier 1 or Tier 2 CTM signals, no provenance, no CTMv3-recognized manifest, 112 files. Package validation still passed. This activation adds the CTMv3 warm-start layer around the existing staged package workspace without replacing its docs or registry. The canonical repo is not edited by this activation.

### 2026-06-13 - Staging sequence correction

Daeron clarified the intended path: work on `/home/daeron/Projects/Modern-ML/Plugins/Cognitive-Topology-Map` and `/home/daeron/Projects/Modern-ML/Plugins/Mentat` until they are done, then set up proper Aeriadne, then copy reviewed artifacts into `/home/daeron/Repositories/Somnus-Intellligence-Stack/`. The public repo already has clone pressure, so the next push must not destabilize that codebase.

### 2026-06-13 - Native plugin doctrine correction

Daeron clarified that plugins are not tools, hooks, or skills. They are independent environment-intelligence packages that run between the operator and agent runtime. The private Golden Path source packet is the internal anchor for treating plugins as committed-state loops with validation membranes, compensation/exclusion ledgers, divergence monitoring, and terminal boundaries. Exact private source paths must stay out of marketplace-facing cards and copyover docs.

### 2026-06-13 - CTMv3 and Mentat native registry entries

After CTMv3 and Mentat staging hardening, Aeriadne added package-level registry and marketplace cards for both substrates. The cards describe committed state, validation gates, copyover boundaries, and client surfaces while keeping runtime ownership in the source packages.

### 2026-06-13 - CTMv3 privacy boundary evidence synced

CTMv3 now has its own release-candidate privacy scanner and synthetic smoke test. Aeriadne's CTMv3 registry/card evidence now records the privacy boundary gate, `140` release candidate files, and `1045` ignored local-only/forbidden files after command backfill and cache cleanup while preserving CTMv3 as the workspace activation owner.

### 2026-06-13 - Golden Path runtime contract surfaced

Aeriadne package-facing docs now normalize the internal Golden Path runtime roles: committed state ledger, validation membrane, compensation ledger, divergence process, and terminal boundary. Marketplace cards keep that contract without copying private source paths.

### 2026-06-13 - Codex ingestion manifest aligned

The root, Codex, and Claude plugin metadata mirrors now include the Codex-facing `interface` object. The `.codex-plugin/plugin.json` manifest passes the plugin-creator ingestion validator.

### 2026-06-13 - Non-owned local tool boundary and Codex Config card

Aeriadne removed CodeGraph from the attached marketplace/MCP card surface after Daeron clarified it is non-owned, Codex-only, and being phased out. Codex Config Topology was first added as a restage-required control-plane plugin card because live evidence showed it was available but not installed and its current manifest failed the plugin ingestion validator.

### 2026-06-13 - Codex Config Topology staging restored

Codex Config Topology was restored from `Plugins/old` into the current `Plugins/Codex-Config-Topology` staging root. Its plugin manifests now include the Codex-facing `interface` block, plugin ingestion validation passes, the bundled skill quick-validates, and a copyover manifest/release ignore/provenance file exist. Install state remains `not installed`; the local marketplace source has not been refreshed.

### 2026-06-13 - Aeriadne copyover gate added

Aeriadne now has its own `COPYOVER_MANIFEST.md` and `.releaseignore` before any public repo copy. The gate names the staging root, public review target, candidate copy surfaces, release exclusions, validation commands, privacy scan requirement, and promotion rules. `.sovereign/session_state.json`, private semantic archive paths, private indexed workspace paths, stale local tool index state, runtime DBs, caches, generated filetrees, and secrets are excluded from copyover.

### 2026-06-13 - Privacy boundary scanner added

`scripts/privacy_boundary_scan.py` was added and wired into `scripts/validate_package.py`. The scanner uses generic leak shapes and an explicit allowlist of known package/review/control-plane roots, so exact private archive identifiers do not need to be committed into package-facing files just to enforce the boundary.

### 2026-06-13 - Privacy boundary regression smoke added

`tests/privacy_boundary_scan_smoke.py` was added with synthetic fixtures. It proves the scanner accepts known package roots and human-facing boundary prose while rejecting unapproved local paths, external media paths, compact private source identifiers, and stale local tool log-token shapes. The test constructs sensitive-shaped tokens at runtime so package-facing files still avoid exact private archive identifiers.

### 2026-06-13 - Mentat privacy boundary evidence synced

Mentat now has its own release-candidate privacy scanner and synthetic smoke test. Aeriadne's Mentat registry/card evidence now records `139` candidate files, `299` ignored local-only/forbidden files, and the privacy boundary gate while preserving Mentat as the runtime owner.

### 2026-06-13 - Mentat command-frontmatter evidence synced

Mentat gained command-frontmatter lint and a synthetic smoke test covering all nine slash command prompts. At that checkpoint Aeriadne's Mentat registry/card evidence recorded the command lint gate before the later prompt-surface review update superseded the counts.

### 2026-06-13 - Mentat prompt-surface evidence synced

Mentat now has prompt-surface review and a synthetic smoke test covering the seven agent/helper prompt files plus `helpers/HELPERS.md`. Aeriadne's Mentat registry/card evidence now records `58 pass / 0 fail / 0 skip`, the prompt-surface gate, and `139` release candidate files after cache cleanup.

### 2026-06-13 - Mentat local site prototype preserved

Daeron clarified that the root Mentat HTML artifact should not be deleted. It is preserved as a staging-local linked-doc/site prototype while remaining excluded from public copyover until explicitly promoted.

### 2026-06-13 - Site prototype ledger added

Aeriadne added `registry/site_prototypes.json`, `marketplace/site-prototypes.md`, and `scripts/site_prototype_audit.py` so local HTML/site pages are first-class preserved staging artifacts. The audit currently proves the Mentat HTML exists, remains local-only, and is excluded by Mentat's `.releaseignore`.

Daeron then clarified that the Mentat HTML is meaningful specification, not just a page mockup. Aeriadne's site audit now validates declared semantic requirements for the preserved Mentat page: live state-machine substrate, Q-table learning loop, insight bus, scope drift and hooks, plus MCP/runtime projection markers.

## Architectural Decisions

### Aeriadne remains the package/compiler layer

Aeriadne is the marketplace operator/proof package. It may catalog Mentat, CTMv3, Codex Config Topology, and Somnus-MCP / BB7, but it does not absorb or vendor those systems. Non-owned local development tools stay outside the attached marketplace surface.

### Plugins are independent runtime packages

Hooks, skills, commands, MCP tools, adapters, cards, and registries are exposed surfaces. The plugin is the package-level loop that owns committed state, validation, drift handling, and promotion boundaries. Aeriadne must represent that loop instead of reducing plugins to surface inventories.

### Somnus-MCP / BB7 remains a canonical-reference server plane

BB7 is represented by `mcp/servers/sovereign-bb7.md` and registry/card references. Its canonical root remains `/home/daeron/Somnus-MCP`; data remains under `/home/daeron/Somnus-MCP/data`.

### CPF direct authoring source remains intact

The plugin copy under Aeriadne is for packaging/distribution. The direct source under `/home/daeron/.codex/skills/custom/constitutional-prompt-framework` remains available until Daeron explicitly retires it.

### Client adapters remain subordinate

Codex, Claude Code, and OpenCode adapter docs describe projection routes. They do not own canonical package identity, status, or validation truth.

### Installed status requires command evidence

Aeriadne is locally validated and installed only when command evidence exists. Current evidence records `aeriadne@local`, `mentat@local`, and `ctmv3-workspace-activator@local` as installed/enabled; public copyover remains unperformed.

## Rejected Alternatives

- Treating Aeriadne as the whole canonical marketplace repo instead of an outside staging/package workspace.
- Vendoring Somnus-MCP / BB7 into the plugin package.
- Treating MCP/server cards as plugins.
- Removing the direct CPF authoring skill because a plugin copy exists.
- Installing both `aeriadne@local` and legacy `cpf-plugin-ariadne@local` without an explicit duplicate-exposure decision.
- Making public marketplace readiness part of v1.
- Running generic CTMv3 activation stubs over validated package-specific docs.

## Open Questions

- Should `aeriadne@local` be installed before or after broader Modern-ML registry restructuring?
- Should Somnus-MCP / BB7 remain MCP-only, or should Aeriadne add a broader environment-plane card alongside the existing `sovereign-bb7` MCP card?
- Should staged Codex Config Topology be refreshed/installed, or should `official-codex-configuration` supersede it before public copyover?
- After Daeron reviews `COPYOVER_MANIFEST.md`, should any optional generated inventory such as `filetree.md` be explicitly promoted?
- Should CTMv3 engine config-spine detection be extended to recognize plugin manifests (`plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, `plugin.toml`)?
- What is the current OpenCode plugin/skill projection contract?
- Should validation output be regenerated under `validation/` after every structural package edit, or only at release gates?

## Integration History

| Date | Change | Evidence |
| --- | --- | --- |
| 2026-06-05 | Aeriadne private-v1 package staged | `README.md`, `MANIFEST.md`, `CHANGELOG.md`, `validation/validation_report.md` |
| 2026-06-10 | File tree generated | `filetree.md` |
| 2026-06-13 | CTMv3 activation artifacts added | `TOPOLOGY.md`, `FAILURE_GRAMMAR.md`, `ARCHITECTURE_MAP.md`, `.sovereign/` |
| 2026-06-13 | Staging sequence corrected to CTMv3/Mentat first, Aeriadne later | `../STAGING_RELEASE_PLAN.md`, `MARKETPLACE_ROADMAP.md` |
| 2026-06-13 | Native plugin doctrine added from Golden Path loop | `../PLUGIN_RUNTIME_DOCTRINE.md`, `TOPOLOGY.md`, `README.md` |
| 2026-06-13 | CTMv3 and Mentat native plugin cards added | `registry/cognitive-topology-map.plugin.json`, `registry/mentat.plugin.json`, `marketplace/cards/` |
| 2026-06-13 | CTMv3 privacy boundary evidence synced | `registry/cognitive-topology-map.plugin.json`, `marketplace/cards/cognitive-topology-map.plugin.md`, `registry/plugins.yaml` |
| 2026-06-13 | Golden Path runtime contract surfaced in package docs | `README.md`, `validation/validation_report.md` |
| 2026-06-13 | Codex ingestion manifest aligned | `.codex-plugin/plugin.json`, `plugin.json`, `.claude-plugin/plugin.json`, `validation/validation_report.md` |
| 2026-06-13 | Non-owned local tool attachment removed and Codex Config card retained with privacy-safe boundaries | `mcp/servers/`, `marketplace/cards/`, `registry/codex-config-topology.plugin.json` |
| 2026-06-13 | Codex Config Topology staging restored and schema-aligned | `../Codex-Config-Topology/README.md`, `../Codex-Config-Topology/COPYOVER_MANIFEST.md`, `registry/codex-config-topology.plugin.json` |
| 2026-06-13 | Aeriadne copyover gate added | `COPYOVER_MANIFEST.md`, `.releaseignore`, `scripts/validate_package.py` |
| 2026-06-13 | Aeriadne privacy boundary scanner added | `scripts/privacy_boundary_scan.py`, `scripts/validate_package.py`, `validation/validation_report.md` |
| 2026-06-13 | Aeriadne privacy boundary smoke added | `tests/privacy_boundary_scan_smoke.py`, `scripts/validate_package.py`, `validation/validation_report.md` |
| 2026-06-13 | Mentat privacy boundary evidence synced | `registry/mentat.plugin.json`, `marketplace/cards/mentat.plugin.md`, `registry/plugins.yaml` |
| 2026-06-13 | Mentat command-frontmatter evidence synced | `registry/mentat.plugin.json`, `marketplace/cards/mentat.plugin.md`, `registry/plugins.yaml` |
| 2026-06-13 | Mentat prompt-surface evidence synced | `registry/mentat.plugin.json`, `marketplace/cards/mentat.plugin.md`, `registry/plugins.yaml` |
| 2026-06-13 | Site prototype ledger added | `registry/site_prototypes.json`, `marketplace/site-prototypes.md`, `scripts/site_prototype_audit.py` |
| 2026-06-13 | Mentat HTML semantic gate added | `registry/site_prototypes.json`, `scripts/site_prototype_audit.py`, `tests/site_prototype_audit_smoke.py` |

## Session Log

| Date | Agent | Action | Topology Drift? | Next Recommended Action |
|------|-------|--------|----------------|------------------------|
| 2026-06-13 | Codex | CTMv3 activation staged outside canonical repo | no | Review/copy accepted changes into Somnus-Intellligence-Stack or add native plugin cards |
| 2026-06-13 | Codex | Corrected staging sequence to CTMv3 and Mentat first | no | Stabilize Cognitive-Topology-Map and Mentat before final Aeriadne copyover |
| 2026-06-13 | Codex | Added native plugin doctrine: plugins are independent runtime loops, not hook/skill/tool bundles | no | Use doctrine while hardening Mentat and rebuilding Aeriadne cards |
| 2026-06-13 | Codex | Added CTMv3 and Mentat as native plugin registry/card entries in Aeriadne | no | Add remaining MCP/control-plane cards, then add Aeriadne copyover manifest |
| 2026-06-13 | Codex | Added CTMv3 release-candidate privacy boundary scanner and synced Aeriadne CTMv3 evidence | no | Continue holding public copyover until exact candidate diff review |
| 2026-06-13 | Codex | Surfaced Golden Path contract in package docs without putting private source paths into marketplace cards | no | Keep validating package cards against the committed-state/membrane/copyover model |
| 2026-06-13 | Codex | Added Codex-facing interface metadata and passed plugin-creator validation | no | Keep official Codex ingestion validation in the Aeriadne gate |
| 2026-06-13 | Codex | Removed non-owned local development tool attachment and restored staged-local Codex Config Topology card | no | Decide whether to refresh/install Codex Config Topology or supersede it |
| 2026-06-13 | Codex | Added Aeriadne copyover manifest and release ignore before any public repo copy | no | Run validation, privacy scan, and public repo clean check |
| 2026-06-13 | Codex | Added generic privacy boundary scanner without committing exact private archive identifiers | no | Keep the scanner in the package gate and expand allowlist only with evidence |
| 2026-06-13 | Codex | Added synthetic privacy boundary smoke test and wired it into package validation | no | Keep test fixtures synthetic and avoid raw private source identifiers |
| 2026-06-13 | Codex | Added Mentat release-candidate privacy boundary scanner and synced Aeriadne Mentat evidence | no | Continue with command-frontmatter and prompt-surface gates |
| 2026-06-13 | Codex | Added Mentat command-frontmatter lint and synced Aeriadne Mentat evidence | no | Prompt-surface evidence synced in following entry |
| 2026-06-13 | Codex | Added Mentat prompt-surface review and synced Aeriadne Mentat evidence | no | Keep Mentat staged-green until Daeron reviews the candidate copy list and archive rebuild |
| 2026-06-13 | Codex | Added Aeriadne site prototype ledger and audit for the preserved Mentat HTML | no | Expand linked-doc/site layer in staging without public copyover until promoted |

### 2026-06-13 - Codex CTMv3 activation

Prompt: Daeron asked whether it was too late to CTMv3-activate Aeriadne because it is technically the marketplace for SovMCP, Mentat, and CTMv3 plugin surfaces, and asked for CTMv3 activator plus exo brief/bootstrap/route/reflect.

Findings:

- It is not too late. CTMv3 activation is appropriate because the package is mature but CTMv3-cold.
- The package is locally validated before activation.
- This path is not the canonical repo. The canonical review/copy target is `/home/daeron/Repositories/Somnus-Intellligence-Stack/`, and it was not edited.
- CTMv3 engine does not recognize Aeriadne's plugin manifests as config-spine signals.

Actions:

- Added CTMv3 topology, failure grammar, architecture map, provenance, local agent docs, session state, and enforcement scaffolds.
- Aligned registry JSON validation state with validation evidence.
- Marked native plugin expansion direction explicitly without turning Aeriadne into BB7, Mentat, or CTMv3.

Next:

- Work `../Cognitive-Topology-Map/` until the CTMv3 package is stable.
- Work `../Mentat/` until the runtime/session plugin is stable.
- Then rebuild proper Aeriadne package registry/cards/adapters from those stable truths.
- Consider a small CTMv3 engine improvement for plugin manifest detection.
