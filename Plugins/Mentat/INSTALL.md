# Mentat — Installation Notes

Quick handoff to Codex on Kubuntu.

## Steps

```bash
# 1. Clone the plugin into your Claude Code plugin tree
mkdir -p ~/.claude/plugins
cd ~/.claude/plugins
# either copy from this workspace tarball, or git clone if you've pushed it
tar -xzf /path/to/mentat-plugin.tar.gz
cd mentat

# 2. Make hook scripts executable (if not already)
chmod +x hooks/*.py bin/mentat mcp_server/__main__.py

# 3. Confirm Python 3 is on PATH (no third-party deps — stdlib only)
python3 --version

# 4. Tell Claude Code about the plugin
claude plugin marketplace add file://$HOME/.claude/plugins/mentat
# or for dev:
claude --plugin-dir $HOME/.claude/plugins/mentat
```

Mentat installs as a runtime plugin package. The hooks, MCP server, CLI,
skills, monitors, evals, and adapters are surfaces over the same committed
state substrate; do not install only one surface and call it the whole plugin.

## First-run smoke test

```bash
# 1. Open a session in any project
cd ~/Projects/ADA-Step-Entropy
claude

# 2. In another terminal, watch the insight bus
$HOME/.claude/plugins/mentat/bin/mentat tail --n 5
# (should show SESSION_START + USER_PROMPT after first message)

# 3. Author a scope file
mkdir -p .mentat
cat > .mentat/scope.md <<'EOF'
# Scope — current task

## In
- whatever you're doing

## Out (deferred — DO NOT re-inject)
- inference
- model loading
EOF

# 4. Send a message in the session that mentions "inference"
# Mentat should emit SCOPE_DRIFT and the next Edit/Bash should be denied with
# a clear reason.
```

## Hooking the bb7 server alongside

Mentat does not duplicate bb7 — it's session-scoped where bb7 is global. If
you want both, list both in `.claude.json`:

```json
{
  "mcpServers": {
    "bb7": {
      "type": "stdio",
      "command": "python3",
      "args": ["/home/daeron/Somnus-MCP/server.py"]
    },
    "mentat": {
      "type": "stdio",
      "command": "python3",
      "args": ["/home/daeron/.claude/plugins/mentat/mcp_server/__main__.py"]
    }
  }
}
```

The Mentat MCP server is read-mostly (introspection of its own state); bb7 is
write-heavy (real tool execution). They don't compete.

## Staging copyover check

Before rebuilding archives or copying into
`/home/daeron/Repositories/Somnus-Intellligence-Stack/Plugins/Mentat`, run:

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

The validator allows local-only artifacts to remain in staging only when
covered by `.releaseignore`. The universal installer uses the same
`.releaseignore` membrane when copying the live plugin tree into runtime
install paths. The privacy scanner uses that membrane too, so ignored staging
evidence can remain local while release-candidate text is checked for private
source identifiers and unapproved local paths.
The command-frontmatter lint checks all slash command prompt files for
descriptions, argument hints, scoped `allowed-tools`, and forbidden Bash
wildcards.
The prompt-surface review checks `agents/*.md` and `helpers/*.md` for role,
tool, boundary, and output contracts while preserving their independent
operator-prompt role.

Review `SUBSYSTEM_INVENTORY.md` before copyover for the current status of
adapters, evals, webhooks, monitors, commands, agents, helpers, and debrief.

## Codex parallel

Codex CLI uses `[mcp_servers.mentat]` in `~/.codex/config.toml` instead of
`.mcp.json`. The same `python3 -m mcp_server` command works:

```toml
[mcp_servers.mentat]
command = "python3"
args = ["/home/daeron/.claude/plugins/mentat/mcp_server/__main__.py"]
startup_timeout_sec = 5
tool_timeout_sec = 10
```

Codex hooks are a different shape (6 events vs Claude Code's 25), but the
state-machine reconstruction logic in `state_machine/` is runtime-agnostic.
The current Codex projection lives under `adapters/codex/` and reads the same
SQLite + JSONL state model instead of forking the substrate.

## Uninstall

```bash
claude plugin uninstall mentat
rm -rf ~/.mentat                          # global state + Q-table
rm -rf ~/Projects/*/.mentat               # per-project scope + active-session pointer
```

## File-system permissions

Hooks write to `~/.mentat/` and `${CLAUDE_PROJECT_DIR}/.mentat/`. Both
directories are created on first run. Hooks never write outside those paths
or `~/.claude/plugins/mentat/` itself (no production code edits, no system
files). The MCP server is also strictly scoped to those paths.

## Known edge cases

- **No CLAUDE_PROJECT_DIR**: Mentat falls back to `~/.mentat/` for scope
  detection. Drift detection becomes a no-op. State machine still works.
- **No CLAUDE_SESSION_ID**: Mentat treats the session as `default`. Q-table
  updates still accumulate but you lose per-session insight separation.
- **Hook script crash**: Logged to stderr (visible in Claude Code's debug
  output). The session continues — hook failures do not block the turn.
- **Concurrent sessions in the same project**: SQLite handles concurrent
  writes safely (WAL mode); the JSONL files are append-only so concurrent
  appends interleave but don't corrupt.

## Cross-runtime install (Codex / Gemini)

Mentat v0.2 ships adapters for Codex CLI and Gemini CLI. The `state_machine/`,
`mcp_server/`, and `bin/mentat` packages are runtime-agnostic and reused as-is;
only the thin hook entry scripts differ. The same `~/.mentat/q_table.sqlite`
accumulates rewards across Claude Code, Codex, and Gemini.

### One-shot universal installer

```bash
# Auto-detect: installs into every runtime whose home dir exists.
./adapters/install_universal.sh

# Or explicit:
./adapters/install_universal.sh --claude --codex --gemini
./adapters/install_universal.sh --all
./adapters/install_universal.sh --dry-run --all     # preview without writing
```

The installer renders the runtime-specific hooks files with absolute paths
substituted in, and appends the substrate vocabulary snippets to your
`AGENTS.md` (Codex) / `GEMINI.md` (Gemini) — idempotent via marker comments.

### Codex CLI quickstart

```bash
./adapters/install_universal.sh --codex
# manually verify [features] codex_hooks = true is in ~/.codex/config.toml
codex      # launch — Mentat fires SessionStart hook on first prompt
$HOME/.codex/plugins/mentat/bin/mentat tail --n 5    # inspect insight bus
```

Codex wires six events: `SessionStart`, `UserPromptSubmit`, `PreToolUse`,
`PermissionRequest`, `PostToolUse`, `Stop`. The `Stop` hook doubles as the
handoff write (Codex has no separate PreCompact). Full notes in
`adapters/codex/README.md`.

### Gemini CLI quickstart

```bash
./adapters/install_universal.sh --gemini
gemini     # launch — extension discovered from ~/.gemini/extensions/mentat
# run /hooks panel inside Gemini to confirm Mentat is wired
```

Gemini wires eleven events: `SessionStart`, `SessionEnd`, `BeforeAgent`,
`AfterAgent`, `BeforeModel`, `AfterModel`, `BeforeToolSelection`,
`BeforeTool`, `AfterTool`, `PreCompress`, `Notification`. The `PreCompress`
hook is the canonical handoff-write point (Gemini's PreCompact equivalent),
and the primary verify trigger is `AfterTool` on a `run_shell_command` whose
command matches a known verify prefix (pytest / ruff / mypy / cargo test / …).
Full notes in `adapters/gemini/README.md`.

### Smoke-testing the adapters

```bash
./adapters/test_universal.sh
# Compiles every hook script, validates every JSON file, runs dry-runs for
# each runtime, then installs into a temporary Codex HOME to prove staging
# artifacts are not copied.
```
