# CTMv3 opencode Adapter

The CTMv3 opencode adapter wires the CTMv3 workspace activation engine into opencode
as a subagent, one read-only status command, and a session-start plugin.

CTMv3 is a codebase activation and workspace onboarding system. It is not a skill maker.
Its purpose is to enter a repo, install the full agent-operability structure, and make the
codebase living for ongoing agent work. The adapter provides an opencode-native interface
to the Python engine in `../core/`.

---

## Requirements

- opencode (recent version — see schema assumptions below)
- Python 3.9+ with the ctmv3 engine installed: `python3 -m ctmv3 version`

---

## Install

### Project scope (installs to `.opencode/` in the current directory)

```bash
cd /path/to/your/repo
bash /path/to/ctmv3-plugin/opencode/install.sh
```

### Global scope (installs to `~/.config/opencode/`)

```bash
bash /path/to/ctmv3-plugin/opencode/install.sh global
```

The installer copies:
- `agent/ctmv3-architect.md` to `<target>/agents/`
- `command/ctmv3-status.md` to `<target>/commands/`
- `plugin/ctmv3.ts` to `<target>/plugins/`

---

## Command Surface

All OpenCode slash commands are invoked from the TUI with a leading `/`.

### `/ctmv3-status`

Show activation status: which artifacts exist, session state, health warnings, and
recommended next command. Read-only.

```
/ctmv3-status
```

The session plugin performs boot discovery automatically on session creation when the
engine is installed. All other CTMv3 operations stay on the canonical engine CLI:

```bash
python3 -m ctmv3 <command> --project-root "$PWD"
```

Supported engine commands include `boot`, `activate`, `warm`, `architecture-map`,
`dot-init`, `sovereign-init`, `session-close`, `state`, `context`, `ping`, and `serve`.

---

## Subagent

The `ctmv3-architect` subagent can be invoked directly with `@ctmv3-architect` for
bespoke CTMv3 work not covered by the commands above.

```
@ctmv3-architect The repo has TOPOLOGY.md but FAILURE_GRAMMAR.md is missing. Build it.
```

---

## Plugin

`plugin/ctmv3.ts` registers a `session.created` hook that automatically runs
`python3 -m ctmv3 boot --json` when a new opencode session starts. This populates the
session context with the signal inventory (boot state, Tier 1/2/3 signals, last session
summary) before any agent messages are processed.

The hook is silent on failure: if ctmv3 is not installed, the session starts normally.

---

## What this plugin assumes about opencode

The following schema fields and behaviors depend on opencode being on a version that
supports them. The canonical source is https://opencode.ai/docs/ (verified 2026-05-23).

### Agent front-matter (`.opencode/agents/*.md`)

- `mode: subagent` — declares a subagent invokable via `@name` and by the Task tool.
- `permission:` — object controlling tool access. Each key maps to `allow`, `ask`, or
  `deny`. For `bash`, accepts an object of glob-pattern -> action for fine-grained control.
- `temperature:` — float, 0.0 to 1.0.
- `model:` — provider/model-id string.
- `description:` — required; shown in @ autocomplete.

The `tools:` key is deprecated in favor of `permission:`. This adapter uses `permission:`.

### Command front-matter (`.opencode/commands/*.md`)

- `agent:` — name of the agent to delegate to; if a subagent, triggers subtask mode.
- `subtask: true` — forces subagent invocation so the command does not pollute primary
  context. This adapter sets it for all CTMv3 commands.
- `description:` — required; shown in `/` autocomplete.
- `$ARGUMENTS` — placeholder in the command body replaced with arguments passed after the
  command name in the TUI.

### Plugin (`.opencode/plugins/*.ts`)

- Plugins are TypeScript or JavaScript modules that export a named async function.
- The function receives `{ project, client, $, directory, worktree }`.
- It returns a hooks object. Hooks include `event: async ({ event }) => {...}`.
- The `$` parameter is Bun's shell API.
- The `session.created` event fires when a new session is created.
- The `@opencode-ai/plugin` package provides TypeScript types; it is optional at runtime.

### Highest-risk assumption

The `session.created` event key in the plugin is the highest-risk assumption: if the
opencode team renames this event or changes the event dispatch shape, the auto-boot hook
will silently do nothing. The commands still work without the plugin.

---

## Troubleshooting

**"ctmv3-architect is not available"** - Verify the `.opencode/agents/` directory exists
and `ctmv3-architect.md` is in it. Check that opencode was restarted after installation.

**Commands not appearing in `/` autocomplete** - Verify `.opencode/commands/` contains
`ctmv3-status.md`. opencode loads commands at startup; restart after installing.

**`python3 -m ctmv3` not found** - Install the Python engine from the sibling `core/`
directory in this plugin checkout. The adapter shells out to the engine
for all discovery and artifact generation.

**Plugin not running on session start** - Verify `ctmv3.ts` is in `.opencode/plugins/`.
Check that your opencode version loads TypeScript plugins from the plugins directory. If
Bun is not available, the plugin may need to be transpiled to JavaScript first.
