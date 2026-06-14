---
description: Full CTMv3 workspace activation — runs the complete Phase 0-5 cold start on the current repo
allowed-tools:
  - Bash(python3 -m ctmv3 *)
  - Read
  - Write
  - Edit
argument-hint: "[--force] [--project-root PATH]"
---
# /ctmv3:activate

Full workspace activation. Runs the complete CTMv3 Phase 0-5 cold start sequence on the
project root, producing the full artifact set: TOPOLOGY.md, FAILURE_GRAMMAR.md,
ARCHITECTURE_MAP.md, PROVENANCE.md, AGENTS.md, CLAUDE.md, and the .xyz directories
(.sovereign/, .claude/, .codex/, .github/).

This is the entry command for a repo that has never been CTM-encoded. For repos that
have already been activated, use /ctmv3:warm instead.

## Invocation

```bash
python3 -m ctmv3 activate --json $ARGUMENTS
```

Parse the JSON output. The engine will report the boot state it detected (COLD, WARM, or
PARTIAL) and the artifact list it intends to produce.

## Safety check

Before writing anything, check whether any Tier 1 CTM artifacts already exist:
- .sovereign/ directory
- ARCHITECTURE_MAP.md
- AGENTS.md

If any Tier 1 artifact exists and --force is NOT in $ARGUMENTS, pause and report to the
operator:

> CTMv3 artifacts detected. This repo may already be activated. Pass --force to
> overwrite existing artifacts, or run /ctmv3:warm to continue from the current state.

Do not proceed past this check without explicit confirmation or --force.

## Execution sequence

If boot state is COLD or --force is passed:

1. Run discovery sequence (read-only): scan root-level config spine, .xyz directories,
   AGENTS.md / CLAUDE.md if present.
2. Invoke Phase 0 domain archaeology — read config spine files (pyproject.toml, go.mod,
   Cargo.toml, package.json, manifest.json) to extract dependency map and entry points.
3. Run the engine for each phase in order:
   ```
   python3 -m ctmv3 topology --json $ARGUMENTS
   python3 -m ctmv3 failure-grammar --json $ARGUMENTS
   python3 -m ctmv3 architecture-map --json $ARGUMENTS
   python3 -m ctmv3 sovereign-init --json $ARGUMENTS
   python3 -m ctmv3 dot-init --json $ARGUMENTS
   ```
4. After each phase, verify the expected output file was created. If a file is missing,
   report the failure immediately — do not continue to the next phase.

## Expected artifacts

After successful activation, the following must exist:
- TOPOLOGY.md (load-bearing concepts, interface map, complexity distribution)
- FAILURE_GRAMMAR.md (pre-failure signatures, adversarial patterns if applicable)
- ARCHITECTURE_MAP.md (traversal map, not a summary)
- PROVENANCE.md (snapshot lineage + first session log entry)
- AGENTS.md (operational posture for all agents)
- CLAUDE.md (Claude Code-specific context)
- .sovereign/session_state.json
- .sovereign/topology_fingerprint.txt
- .claude/settings.json

## Report back

Summarize: which artifacts were created, what the detected project type is (Python/Go/etc.),
what the 3 load-bearing concepts are from TOPOLOGY.md, and the warm start state written to
.sovereign/session_state.json. Flag anything that could not be produced.
