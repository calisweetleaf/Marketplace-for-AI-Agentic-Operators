# Manifest - Aeriadne

Package: `aeriadne`  
Version: `1.0.0`  
Date: `2026-06-05`  
Status: `private-v1` / validated-local, installed locally as `aeriadne@local`
Purpose: Skill-activated plugin wrapper for CPF plus local/private marketplace scaffold.

## Root contents

- `plugin.json` — root plugin metadata, including the shared Codex-facing `interface` block.
- `.codex-plugin/plugin.json` — Codex plugin metadata mirror validated by the plugin-creator ingestion checker.
- `.claude-plugin/plugin.json` — Claude/local plugin metadata mirror.
- `plugin.toml` — canonical local/private marketplace manifest.
- `.releaseignore` — release/copyover exclusion ledger.
- `COPYOVER_MANIFEST.md` — review gate from staging tree to public repo target.
- `README.md` — package ontology, provenance, validation, install/exposure notes.
- `MANIFEST.md` — this file.
- `MARKETPLACE_ROADMAP.md` — staged Codex/Claude Code/OpenCode/private marketplace plan.
- `CHANGELOG.md` — package change log.
- `LICENSE.md` — private/internal notice.
- `registry/` — machine-readable marketplace inventory.
- `marketplace/` — human-facing cards and indexes.
- `adapters/` — Codex, Claude Code, and OpenCode projection docs.
- `agents/` — subagent prompt pack and client projection placeholders.
- `mcp/` — MCP/server catalog corner.
- `scripts/validate_package.py` — stdlib package validator.
- `scripts/privacy_boundary_scan.py` — generic private-boundary scanner for local path and compact source-identifier leaks.
- `tests/` — package smoke/compatibility cases, including `tests/privacy_boundary_scan_smoke.py`.
- `skills/` — bundled cognitive payloads.
- `TOPOLOGY.md` — CTMv3 load-bearing concept map.
- `FAILURE_GRAMMAR.md` — CTMv3 pre-failure and false-success map.
- `ARCHITECTURE_MAP.md` — CTMv3 traversal map.
- `PROVENANCE.md` — CTMv3 lineage, decisions, and session log.
- `.sovereign/` — CTMv3 warm-start artifacts; release copyover includes golden paths and topology fingerprint, but excludes runtime session state unless explicitly promoted.
- `.claude/`, `.codex/`, `.github/` — local client/context/enforcement scaffolds.

## Bundled skills

### `constitutional-prompt-framework`

Copied from `/home/daeron/.codex/skills/custom/constitutional-prompt-framework`.

Contains:

- `SKILL.md`
- `README.md`
- `MANIFEST.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `package-manifest.json`
- `agents/openai.yaml`
- `assets/`
- `examples/`
- `references/`
- `schemas/`
- `scripts/`
- `tests/`

### `aeriadne-marketplace-operator`

New plugin-local skill for registry, packaging, adapters, marketplace cards, agent prompt packs, MCP/server cards, and release validation.

Contains:

- `SKILL.md`
- `references/marketplace-schema.md`
- `templates/plugin-card.md`
- `templates/registry-entry.yaml`
- `tests/smoke_cases.yaml`

## Agent prompt pack

- `agents/subagents/prompt-architect.md`
- `agents/subagents/package-cartographer.md`
- `agents/subagents/compatibility-auditor.md`
- `agents/subagents/registry-scribe.md`
- `agents/subagents/release-sentinel.md`

These are parallel workstream prompts, not rank hierarchy.

## MCP/server card

- `mcp/servers/sovereign-bb7.md`

BB7/SovereignMCP is represented as an MCP/server capability-plane reference,
not vendored code or copied runtime state. Non-owned local development tools are
not attached as marketplace cards.

## Native plugin registry cards

- `registry/cognitive-topology-map.plugin.json`
- `registry/mentat.plugin.json`
- `registry/codex-config-topology.plugin.json`
- `marketplace/cards/cognitive-topology-map.plugin.md`
- `marketplace/cards/mentat.plugin.md`
- `marketplace/cards/codex-config-topology.plugin.md`

These represent CTMv3, Mentat, and Codex Config Topology as independent native
plugin packages with their own committed state, validation membranes, exposed
surfaces, and copyover boundaries. Codex Config Topology is explicitly marked
`staged-local`; it validates locally but is not installed, marketplace-refreshed,
or release-ready.

Non-owned local development tools are not represented under the MCP/server
catalog. Their private indexes, logs, and state roots remain outside the package
boundary and are excluded by release hygiene rules when stale local artifacts are
present.

## Copyover gate

- `.releaseignore`
- `COPYOVER_MANIFEST.md`

The copyover gate marks the public repo copy target, candidate copy surfaces,
required validation commands, privacy scan requirement, and release exclusions.
No public copyover or plugin install has been performed.

## Expected Codex exposure after install

```text
aeriadne:constitutional-prompt-framework
aeriadne:aeriadne-marketplace-operator
```

## Provenance

CPF copied from `/home/daeron/.codex/skills/custom/constitutional-prompt-framework` into `/home/daeron/Projects/Modern-ML/Plugins/Aeriadne/skills/constitutional-prompt-framework` on `2026-06-05`.

The source path remains intact for direct authoring. The plugin path is the distribution and marketplace staging surface.

## Boundary

Aeriadne does not replace:

- `Codex-Config-Topology` for Codex control-plane/config/plugin/hook topology.
- `Cognitive-Topology-Map` / CTMv3 for workspace activation.
- `Mentat` for live runtime state-machine instrumentation.
- `Somnus-MCP` / BB7 for the canonical MCP/tool/server plane.

## Validation status

Package validation passes with the copyover manifest, release ignore, and
privacy boundary scanner present. Commands are listed in `README.md` and
`COPYOVER_MANIFEST.md`. Installation and public copyover have not been
performed.

The site prototype audit also passes. It currently preserves Mentat's root HTML
artifact as a staging-local linked-doc/site seed, verifies the file exists, and
keeps it excluded by the owning package's `.releaseignore` until explicitly
promoted.
