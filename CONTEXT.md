# Somnus-Intellligence-Stack Context

_Last updated: 2026-06-05_

## Current operating frame

This repository is the consolidation/staging workspace for Somnus agent-operability assets: skills, plugins, subagents, Muaddib/Sovereign server references, and marketplace/adapter packaging. It is not the full Modern-ML working repository; it is the private-marketplace and distribution-prep layer.

## Active consolidation state

- `skills/grok-build-configurator/` is staged as the canonical Grok Build configurator skill package for this repo.
- `/home/daeron/.local/bin/grok` now sources the skill from this repo and syncs it into `/home/daeron/.grok/runtime-home/skills/grok-build-configurator` on each launch, preserving the one-skill isolated Grok runtime.
- The active Grok runtime remains stripped: no MCP servers, plugins, hooks, agents, subagents, cross-runtime compatibility scans, or Grok memory surfaces.
- The skill manifest was cleaned for staging: Python cache artifacts removed from `generated_files`, public-clean exclusions added, and the internal `/mnt/data/...` source path replaced with uploaded-source provenance.
- The repo skill README now documents Somnus staging status, Grok runtime linkage, install targets, and public-clean constraints.

## Distribution posture

GitHub/private repo should act as the source transport and audit surface. The marketplace/registry layer should act as the install/discovery/version surface, with runtime-specific adapters for Codex, Claude Code, OpenCode, and Grok Build. Open-source payload should include server/package code, manifests, docs, cards, installers, and examples; it should not include Muaddib flywheel data, private BB7 memory/state, sessions, q-tables, auth material, logs, or checkpoints.

## Next sweep targets

1. Add or normalize root-level `Registry/`, `Marketplace/`, `Adapters/`, and `MCP/`/`Servers/` references.
2. Verify the plugin triad package state: Aeriadne, Cognitive-Topology-Map/CTMv3, and Mentat.
3. Decide whether `Codex-Config-Topology` remains archived only or receives an adapter/legacy package entry.
4. Run a public-clean audit before any private repo push: secrets, sessions, data roots, q-tables, `.pyc`, logs, archives, and generated backups.

## 2026-06-05 update — Aeriadne active marketplace package, old plugin markers quarantined

- Working directory for this pass: `/home/daeron/Repositories/Somnus-Intellligence-Stack`.
- Debug finding: `plugins/old/` contained live runtime marker directories (`.codex-plugin/`, `.claude-plugin/`) that could let recursive plugin/marketplace scans expose stale archived packages, including legacy `cpf-plugin-ariadne`, as active installables.
- Fix: moved archived marker directories to `plugins/old/_archived-plugin-descriptors/` and added `plugins/old/ARCHIVE.md` explaining that `plugins/old/` is provenance only.
- Active CPF/private-marketplace package is now clearly `plugins/Aeriadne/` with canonical path `/home/daeron/Repositories/Somnus-Intellligence-Stack/plugins/Aeriadne`.
- Aeriadne manifests, registry card, marketplace card, adapter docs, README, MANIFEST, roadmap, and validation artifacts were realigned away from stale `/home/daeron/Projects/Modern-ML/Plugins/Aeriadne` references.
- Aeriadne validator was hardened to check stale path markers, backup/cache churn, exact manifest mirror equality, canonical path, and old marker leakage.
- Validation passed with `PYTHONDONTWRITEBYTECODE=1`: package validator PASS, JSON/TOML parse PASS, CPF skill validator PASS, stale path scan PASS, old marker scan PASS, transient artifact scan PASS.
