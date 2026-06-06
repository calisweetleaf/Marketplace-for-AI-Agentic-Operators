# CPF Plugin Ariadne

`CPF-Plugin-Ariadne` packages the existing `constitutional-prompt-framework` skill as an installable Codex plugin.

## Classification

Ariadne is **both plugin-level and skill-level**, but those words refer to different layers:

- **Skill-level payload:** `skills/constitutional-prompt-framework/` is the actual cognitive workflow. It derives, hardens, audits, ports, and packages agent constitutions and prompt frameworks.
- **Plugin-level distribution:** this directory is the installable wrapper that lets Codex expose the CPF skill as a plugin skill such as `cpf-plugin-ariadne:constitutional-prompt-framework` after local plugin installation.

This is the same pattern used by `Plugins/Codex-Config-Topology/`: the plugin is the install/distribution shell; the skill remains the executable cognitive unit.

## Source and provenance

- Authoring source copied from: `/home/daeron/.codex/skills/custom/constitutional-prompt-framework`
- Modern-ML package path: `/home/daeron/Projects/Modern-ML/Plugins/CPF-Plugin-Ariadne`
- Bundled skill path: `skills/constitutional-prompt-framework`
- Package created: 2026-06-05

Do **not** delete the direct custom skill merely because this plugin package exists. The direct skill remains useful as the local authoring/source surface until Daeron explicitly decides to remove or disable the duplicate direct exposure.

## Layer position

```text
Parallax / Narthex     # meta-observer of the operator identity and prompt stack
  ↓
CPF / Ariadne          # constitution and prompt architecture compiler
  ↓
CTM / repo skills      # workspace activation and task-entry topology
  ↓
operator execution     # ordinary task work
```

Ariadne is not the Parallax/Narthex layer. Ariadne answers: **what constitution or prompt architecture should this operator obey?** Parallax/Narthex answers: **what is this operator identity-shell, why is it shaped this way, and should it be preserved, patched, forked, replaced, suspended, or rebound?**

## Validation

From this plugin root:

```bash
python skills/constitutional-prompt-framework/scripts/validate_skill_package.py skills/constitutional-prompt-framework
python skills/constitutional-prompt-framework/scripts/constitution_linter.py skills/constitutional-prompt-framework/examples/example-agent-constitution.md
python skills/constitutional-prompt-framework/scripts/score_constitution.py skills/constitutional-prompt-framework/examples/example-agent-constitution.md
python skills/constitutional-prompt-framework/scripts/run_static_evals.py skills/constitutional-prompt-framework/tests/eval_cases.yaml
python skills/constitutional-prompt-framework/scripts/render_constitution_from_spec.py skills/constitutional-prompt-framework/tests/fixtures/minimal_constitution_spec.json -o /tmp/ariadne-cpf-rendered-check.md
```

## Install note

This package is staged in Modern-ML. Installing/enabling it in Codex should be a separate explicit install step, mirroring the `codex-config-topology@local` pattern.
