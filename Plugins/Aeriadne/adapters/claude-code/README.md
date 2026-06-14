# Claude Code Adapter — Aeriadne

## Goal

Document the Claude Code projection of Aeriadne without making Claude-specific files canonical.

## Package source

`/home/daeron/Projects/Modern-ML/Plugins/Aeriadne`

## Projection rules

- Preserve `skills/constitutional-prompt-framework/SKILL.md` frontmatter and references.
- Project `agents/subagents/*.md` into Claude agent/subagent prompt slots only after review.
- Keep Claude settings/commands out of the canonical skill unless they are placed under a Claude-specific adapter/generated folder.
- Treat `.claude-plugin/plugin.json` as a metadata mirror, not the only source of truth.

## Current status

Adapter docs exist; no Claude plugin install was performed in this pass.
