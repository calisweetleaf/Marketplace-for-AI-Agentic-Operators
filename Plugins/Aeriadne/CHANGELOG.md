# Changelog — Aeriadne

## Unreleased — 2026-06-13

CTMv3 activation and native plugin expansion framing.

- Added `TOPOLOGY.md`, `FAILURE_GRAMMAR.md`, `ARCHITECTURE_MAP.md`, and `PROVENANCE.md`.
- Added `.sovereign/` warm-start state and golden paths.
- Added local `.claude/`, `.codex/`, and `.github/` context/enforcement scaffolds.
- Clarified that Aeriadne is the package/compiler layer for native plugin marketplace expansion, not the runtime owner of Somnus-MCP / BB7, Mentat, or CTMv3.
- Added the native plugin doctrine correction: plugins are independent runtime packages between operator and agent runtime, not just hooks, skills, commands, or tools.
- Added native plugin registry/card entries for CTMv3 and Mentat based on their current staging package truth.
- Updated the CTMv3 registry/card evidence after adding CTMv3's release-candidate privacy boundary scanner and synthetic smoke test.
- Restored Codex Config Topology into the current staging root and added a staged-local registry/card entry based on validation evidence.
- Removed non-owned local development tool attachment from the MCP/server card surface while keeping stale local-state leak guards.
- Added Aeriadne's own `COPYOVER_MANIFEST.md` and `.releaseignore` release membrane before any public repo copy.
- Added `scripts/privacy_boundary_scan.py` so private semantic archive/source leakage is checked without committing exact private archive identifiers.
- Added `tests/privacy_boundary_scan_smoke.py` as a synthetic regression test for allowed roots, unapproved local paths, external media paths, compact private source identifiers, and stale local tool log-token shapes.
- Updated the Mentat registry/card evidence after adding Mentat's release-candidate privacy boundary scanner and synthetic smoke test.
- Updated the Mentat registry/card evidence after adding Mentat's command-frontmatter lint for all nine slash commands.
- Updated the Mentat registry/card evidence after adding Mentat's prompt-surface review for agent/helper prompts and helper index.
- Extended `scripts/validate_package.py` so CTMv3 and Mentat package cards are part of Aeriadne's validation membrane.
- Extended `scripts/validate_package.py` so non-green package cards must explicitly record known gaps and release-ready=false.
- Extended `scripts/validate_package.py` so Aeriadne requires the copyover manifest and release exclusions before validation can pass.
- Extended `scripts/validate_package.py` so the privacy boundary scanner is enforced in the package gate.
- Extended `scripts/validate_package.py` so the privacy boundary smoke test is enforced in the package gate.
- Extended `scripts/validate_package.py` so staged-green native plugin cards must record upstream privacy-boundary evidence and validation commands.
- Added `registry/site_prototypes.json`, `marketplace/site-prototypes.md`, `scripts/site_prototype_audit.py`, and `tests/site_prototype_audit_smoke.py` so local HTML/site prototypes are preserved, audited, and excluded from public copyover until promoted.
- Extended the site prototype audit so the preserved Mentat HTML must retain its state-machine, Q-table, insight-bus, drift/hook, and MCP projection specification markers.
- Added Codex-facing `interface` metadata to plugin manifests and validated `.codex-plugin/plugin.json` with the plugin-creator ingestion validator.
- Aligned registry validation state with existing package validation evidence.
- Corrected staging sequence: harden Cognitive-Topology-Map and Mentat first, then finalize proper Aeriadne and copy reviewed artifacts into the public Somnus-Intellligence-Stack repo.

## 1.0.0 — 2026-06-05

Initial private v1 staging.

- Copied `constitutional-prompt-framework` from `/home/daeron/.codex/skills/custom/constitutional-prompt-framework` into `skills/constitutional-prompt-framework/`.
- Added plugin metadata for root, Codex, and Claude/local plugin surfaces.
- Added `plugin.toml` as canonical v1 registry-oriented manifest.
- Added second skill shell: `aeriadne-marketplace-operator`.
- Added private marketplace registry skeleton.
- Added Codex, Claude Code, and OpenCode adapter docs.
- Added agent/subagent prompt pack skeleton.
- Added MCP/server catalog corner with `sovereign-bb7` as canonical reference, not vendored code.
- Added marketplace cards and roadmap.

## Notes

- No plugin install was performed in this staging pass.
- No git push was performed.
- The direct CPF authoring skill remains intact.
