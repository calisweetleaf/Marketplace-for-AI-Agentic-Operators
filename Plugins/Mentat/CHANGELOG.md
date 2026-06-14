# Mentat Plugin — Distribution Changelog

---

## Staging hardening - 2026-06-13 (plugin v0.3.0 source)

### What changed

- Reframed Mentat as an independent cognitive runtime plugin, not a hook pack or skill bundle.
- Added Golden Path runtime doctrine mapping: committed state, validation membrane, compensation/exclusion, divergence, and terminal boundary.
- Added `.releaseignore`, `COPYOVER_MANIFEST.md`, and `scripts/validate_release_tree.py` so public copyover can exclude local archives, `.mentat/` state, backups, caches, filetrees, logs, DBs, and scratch folders without deleting staging evidence.
- Added `scripts/privacy_boundary_scan.py` and `tests/privacy_boundary_scan_smoke.py` so release-candidate text is checked for private source identifiers, unapproved local paths, external media paths, and CodeGraph log/archive path shapes without committing exact private identifiers.
- Added `scripts/hook_schema_smoke.py` to prove the Codex/Claude `additionalContext` hook output includes `hookSpecificOutput.hookEventName` and suppresses unsupported-event stdout.
- Added `scripts/command_frontmatter_lint.py` and `tests/command_frontmatter_lint_smoke.py` so the nine slash command prompts are validated for descriptions, argument hints, scoped shell permissions, and no Bash wildcards.
- Added `scripts/prompt_surface_review.py` and `tests/prompt_surface_review_smoke.py` so the independent agent/helper prompts are validated for role, tool, boundary, and output contracts without treating them as hooks or skills.
- Marked `mentat-a-live-cognitive-substrate-for-claude-code.html` as a preserved local site/prototype artifact: keep expanding it in staging, but exclude it from public copyover until explicitly promoted.
- Updated `adapters/install_universal.sh` so live runtime installs also respect `.releaseignore` instead of copying staging artifacts.
- Added a temp-HOME Codex install check to `adapters/test_universal.sh` and wired that adapter smoke into `scripts/integration_smoke.py`.
- Added `SUBSYSTEM_INVENTORY.md` as the release-facing subsystem map.
- Restored `monitors/monitors.json` and added monitor CLI smoke coverage for status/schedule paths.
- Wired hook-schema, adapter-installer, monitor CLI, and release/copyover hygiene into `scripts/integration_smoke.py`.
- Updated `AGENTS.md`, `CONTEXT.md`, `MEMORY.md`, `PLAN.md`, `README.md`, and `INSTALL.md` to use the current package-root topology rather than stale `plugin/` paths.

### Public repo safety

No public repo edit is implied by this entry. The reviewed copy target remains `/home/daeron/Repositories/Somnus-Intellligence-Stack/Plugins/Mentat`.

### Promotion gate

```bash
python3 scripts/integration_smoke.py
python3 scripts/hook_schema_smoke.py
PYTHONDONTWRITEBYTECODE=1 python3 tests/command_frontmatter_lint_smoke.py
python3 scripts/command_frontmatter_lint.py .
PYTHONDONTWRITEBYTECODE=1 python3 tests/prompt_surface_review_smoke.py
python3 scripts/prompt_surface_review.py .
PYTHONDONTWRITEBYTECODE=1 python3 tests/privacy_boundary_scan_smoke.py
python3 scripts/privacy_boundary_scan.py .
bash adapters/test_universal.sh
python3 scripts/validate_release_tree.py .
```

Hook-schema edits in `hooks/_lib.py` and `adapters/codex/hooks/_lib.py` are now covered by `scripts/hook_schema_smoke.py`.

Latest staging validation: command lint PASS for 9 commands; prompt surface review PASS for 7 prompts plus 1 helper index; release tree validation PASS with 138 candidate files and 250 ignored local-only/forbidden files, with privacy scanner, prompt review, command lint, and their smoke tests enforced.

---

## Release stamp — 2026-05-11 (plugin v0.1.0 tarball)

**Tarball:** `mentat-plugin.tar.gz`
**Size:** 186,843 bytes (182.4 KB)
**sha256:** `9605621f5f08cad279b535c6cfc1d87691fe669e6e97eaf143fd62f63f59f897`
**sha512:** `c8c137c0cb180bff3cd7621de2709cb36d92cd6c1c158babdff287659838d2a3e22ad3cc91dd8c8cc2c1b3b52a9aba980973e6430933dfd410ce216f359409cb`

### What changed in this build (relative to previous tarball)

- `hooks/hooks.json` — patched to CC-required schema: added `"description"` / `"hooks"` wrapper (11 event types, all wired).
- `docs/` directory added inside `plugin/` — `STYLE.v2.md`, `SOTA_CHECKLIST.md`, `PROVENANCE.md`.
- `webhooks.json` — default endpoint updated from `http://localhost:4000` to `https://localhost:8443/events`.
- Historical note: the May tarball shipped a dormant `monitors/monitors.json` against a Claude Code build that did not yet support that schema. This note is superseded by the 2026-06-13 staging hardening above, where the monitor manifest is intentionally restored for Mentat's independent monitor lane and covered by smoke tests.

### Smoke result

49 pass / 0 fail / 0 skip (all 49 checks green)

Subsystems exercised: state_machine compile (6), hooks compile (11), mcp_server compile (1), CLI end-to-end, FSA end-to-end, drift detection end-to-end, webhook_engine smoke + compile (6), evals compile + dry-run (6), debrief smoke + compile (3), monitors smoke + compile (4), adapters compile (9).

### LOC summary (Python only)

| Subsystem                        | LOC  |
|----------------------------------|------|
| state_machine                    |  696 |
| hooks                            |  920 |
| webhook_engine                   |  971 |
| evals                            | 2282 |
| monitors                         |  817 |
| adapters/codex                   |  822 |
| adapters/gemini                  | 1066 |
| skills/mentat-debrief/scripts    | 1567 |
| mcp_server                       |  378 |
| scripts                          |  392 |
| **Total**                        | **9,911** |

### Manifest (plugin.json)

- name: `mentat`
- version: `0.1.0`
- description: present (177 chars)
- license: `MIT`
- author: Daeron Blackfyre / Somnus-Sovereign-Systems

### Note on version

`plugin.json` records `v0.1.0`. `plugin/CHANGELOG.md` describes a v0.2.0 in-progress ship. The manifest was not modified (source files are not touched by the packaging step). The operator should bump `plugin.json` to `v0.2.0` and rebuild before the next public distribution.

### Helpers (outside plugin/)

The `helpers/` directory (`mentat-conductor.md`, `mentat-medic.md`, `mentat-quartermaster.md`, `HELPERS.md`) is intentionally outside `plugin/` and is NOT included in the tarball. These agent definition files install separately to `~/.claude/agents/`, not inside the plugin tree. They are maintained alongside the plugin at `/home/daeron/.claude/plugins/mentat-plugin/helpers/`.

### Install

```bash
tar -xzf mentat-plugin.tar.gz -C ~/.claude/plugins/
mv ~/.claude/plugins/plugin ~/.claude/plugins/mentat
mv ~/.claude/plugins/mentat/mcp.json ~/.claude/plugins/mentat/.mcp.json
claude plugin marketplace add file://$HOME/.claude/plugins/mentat
```

Install helpers separately:

```bash
cp /path/to/helpers/*.md ~/.claude/agents/
```
