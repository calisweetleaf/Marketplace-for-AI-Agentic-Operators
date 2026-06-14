# OpenCode Adapter — Aeriadne

## Goal

Document how Aeriadne can project skills and subagent prompts into OpenCode-compatible conventions after schema probing.

## Package source

`/home/daeron/Projects/Modern-ML/Plugins/Aeriadne`

## Projection rules

- Keep the canonical skill payload under `skills/`.
- Map role/subagent prompts from `agents/subagents/` only after confirming the current OpenCode prompt/agent layout.
- Mark any unsupported plugin concepts as `schema-probe-needed` rather than pretending parity with Codex or Claude Code.
- Prefer dry-run install docs before copying files into OpenCode paths.

## Current status

Adapter docs exist; no OpenCode install or schema mutation was performed in this pass.
