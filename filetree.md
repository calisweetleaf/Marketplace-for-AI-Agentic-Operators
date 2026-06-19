# File Tree: Somnus-Intellligence-Stack

**Generated:** 6/19/2026, 1:12:50 PM
**Root Path:** `/home/daeron/Repositories/Somnus-Intellligence-Stack`

```
├── Adapters
├── Agents
│   ├── claude-code
│   │   ├── defense-grade-doc-engine.md
│   │   ├── golden-path-architect.md
│   │   └── prod-finalizer.md
│   └── codex
│       ├── defense-grade-doc-engine.toml
│       ├── golden-path-architect.toml
│       └── prod-finalizer.toml
├── Core
│   └── Kernel
│       ├── CONTEXT.md
│       ├── MEMORY.md
│       ├── README_DEPLOYMENT.md
│       ├── STAGING_ANALYSIS.md
│       ├── config.toml
│       ├── hooks.json
│       ├── research.config.toml
│       ├── sovereign.config.toml
│       ├── validation_manifest.json
│       └── workflows.md
├── Docs
│   ├── detailed-webpages
│   │   └── mentat-a-live-cognitive-substrate-plugin.html
│   ├── AGENTS.md
│   ├── ARCHITECTURE_MAP.md
│   ├── CONTEXT.md
│   ├── ECOSYSTEM_ADOPTION_MAP.md
│   ├── MEMORY.md
│   ├── PLAN.md
│   ├── REPO_ENTRY_MATRIX.md
│   └── TECHNICAL_REFERENCE.md
├── Marketplace
├── Plugins
│   ├── Aeriadne
│   │   ├── .claude
│   │   │   ├── CLAUDE.md
│   │   │   └── settings.json
│   │   ├── .claude-plugin
│   │   │   └── plugin.json
│   │   ├── .codex
│   │   │   ├── skills
│   │   │   │   └── README.md
│   │   │   └── README.md
│   │   ├── .codex-plugin
│   │   │   └── plugin.json
│   │   ├── .github
│   │   │   ├── instructions
│   │   │   │   └── aeriadne-package.instructions.md
│   │   │   ├── workflows
│   │   │   │   └── aeriadne-validation.yml
│   │   │   └── copilot-instructions.md
│   │   ├── .sovereign
│   │   │   ├── golden_paths.json
│   │   │   └── topology_fingerprint.txt
│   │   ├── adapters
│   │   │   ├── claude-code
│   │   │   │   └── README.md
│   │   │   ├── codex
│   │   │   │   └── README.md
│   │   │   ├── opencode
│   │   │   │   └── README.md
│   │   │   └── README.md
│   │   ├── agents
│   │   │   ├── claude-code
│   │   │   │   └── README.md
│   │   │   ├── codex
│   │   │   │   └── README.md
│   │   │   ├── opencode
│   │   │   │   └── README.md
│   │   │   ├── subagents
│   │   │   │   ├── compatibility-auditor.md
│   │   │   │   ├── package-cartographer.md
│   │   │   │   ├── prompt-architect.md
│   │   │   │   ├── registry-scribe.md
│   │   │   │   └── release-sentinel.md
│   │   │   └── README.md
│   │   ├── marketplace
│   │   │   ├── cards
│   │   │   │   ├── aeriadne-marketplace-operator.skill.md
│   │   │   │   ├── aeriadne.plugin.md
│   │   │   │   ├── codex-config-topology.plugin.md
│   │   │   │   ├── cognitive-topology-map.plugin.md
│   │   │   │   ├── constitutional-prompt-framework.skill.md
│   │   │   │   ├── mentat.plugin.md
│   │   │   │   └── sovereign-bb7.mcp.md
│   │   │   ├── indexes
│   │   │   │   ├── agent-index.yaml
│   │   │   │   ├── mcp-index.yaml
│   │   │   │   ├── plugin-index.yaml
│   │   │   │   └── skill-index.yaml
│   │   │   ├── README.md
│   │   │   └── site-prototypes.md
│   │   ├── mcp
│   │   │   ├── contracts
│   │   │   │   ├── client-bindings.yaml
│   │   │   │   └── tool-capabilities.yaml
│   │   │   ├── servers
│   │   │   │   └── sovereign-bb7.md
│   │   │   └── README.md
│   │   ├── registry
│   │   │   ├── README.md
│   │   │   ├── aeriadne.plugin.json
│   │   │   ├── agents.yaml
│   │   │   ├── codex-config-topology.plugin.json
│   │   │   ├── cognitive-topology-map.plugin.json
│   │   │   ├── mcp_servers.yaml
│   │   │   ├── mentat.plugin.json
│   │   │   ├── plugins.yaml
│   │   │   ├── site_prototypes.json
│   │   │   └── skills.yaml
│   │   ├── scripts
│   │   │   ├── privacy_boundary_scan.py
│   │   │   ├── site_prototype_audit.py
│   │   │   └── validate_package.py
│   │   ├── skills
│   │   │   ├── aeriadne-marketplace-operator
│   │   │   │   ├── references
│   │   │   │   │   └── marketplace-schema.md
│   │   │   │   ├── templates
│   │   │   │   │   ├── plugin-card.md
│   │   │   │   │   └── registry-entry.yaml
│   │   │   │   ├── tests
│   │   │   │   │   └── smoke_cases.yaml
│   │   │   │   └── SKILL.md
│   │   │   └── constitutional-prompt-framework
│   │   │       ├── agents
│   │   │       │   └── openai.yaml
│   │   │       ├── assets
│   │   │       │   ├── templates
│   │   │       │   │   ├── agent-constitution-full.md
│   │   │       │   │   ├── audit-report-template.md
│   │   │       │   │   ├── capability-dispatch-table.md
│   │   │       │   │   ├── constitution-spec.example.json
│   │   │       │   │   ├── intake-form.md
│   │   │       │   │   ├── memory-policy-template.md
│   │   │       │   │   ├── platform-binding-template.md
│   │   │       │   │   ├── red-team-report-template.md
│   │   │       │   │   ├── release-checklist.md
│   │   │       │   │   └── rewrite-plan-template.md
│   │   │       │   └── single-file-agent-constitution-skeleton.md
│   │   │       ├── examples
│   │   │       │   ├── example-agent-constitution.md
│   │   │       │   ├── example-audit-report.md
│   │   │       │   ├── example-rewrite-plan.md
│   │   │       │   └── rendered-from-spec.md
│   │   │       ├── references
│   │   │       │   ├── 00-doc-chain.md
│   │   │       │   ├── 01-constitutional-prompt-theory.md
│   │   │       │   ├── 02-derivation-guide.md
│   │   │       │   ├── 03-layer-contracts.md
│   │   │       │   ├── 04-authority-and-governance.md
│   │   │       │   ├── 05-rules-of-engagement-patterns.md
│   │   │       │   ├── 06-operating-doctrine-library.md
│   │   │       │   ├── 07-persona-architecture.md
│   │   │       │   ├── 08-capability-dispatch.md
│   │   │       │   ├── 09-memory-continuity.md
│   │   │       │   ├── 10-platform-binding-matrix.md
│   │   │       │   ├── 11-security-privacy-safety.md
│   │   │       │   ├── 12-long-context-and-compaction.md
│   │   │       │   ├── 13-domain-ingestion-and-knowledge-modeling.md
│   │   │       │   ├── 14-output-contracts.md
│   │   │       │   ├── 15-audit-checklist.md
│   │   │       │   ├── 16-evaluation-rubric.md
│   │   │       │   ├── 17-red-team-suite.md
│   │   │       │   ├── 18-anti-patterns.md
│   │   │       │   ├── 19-rewrite-playbook.md
│   │   │       │   ├── 20-deployment-and-maintenance.md
│   │   │       │   ├── 21-interoperability-notes.md
│   │   │       │   ├── 22-glossary.md
│   │   │       │   ├── 23-schema-driven-authoring.md
│   │   │       │   └── 24-failure-mode-atlas.md
│   │   │       ├── schemas
│   │   │       │   ├── audit-report.schema.json
│   │   │       │   ├── constitution-spec.schema.json
│   │   │       │   └── skill-package.schema.json
│   │   │       ├── scripts
│   │   │       │   ├── _cpf_common.py
│   │   │       │   ├── constitution_linter.py
│   │   │       │   ├── render_constitution_from_spec.py
│   │   │       │   ├── run_static_evals.py
│   │   │       │   ├── score_constitution.py
│   │   │       │   └── validate_skill_package.py
│   │   │       ├── tests
│   │   │       │   ├── fixtures
│   │   │       │   │   └── minimal_constitution_spec.json
│   │   │       │   ├── README.md
│   │   │       │   └── eval_cases.yaml
│   │   │       ├── CHANGELOG.md
│   │   │       ├── MANIFEST.md
│   │   │       ├── README.md
│   │   │       ├── RELEASE_NOTES.md
│   │   │       ├── SKILL.md
│   │   │       └── package-manifest.json
│   │   ├── tests
│   │   │   ├── compatibility_matrix.yaml
│   │   │   ├── privacy_boundary_scan_smoke.py
│   │   │   ├── site_prototype_audit_smoke.py
│   │   │   └── smoke_cases.yaml
│   │   ├── validation
│   │   │   ├── validation_manifest.json
│   │   │   └── validation_report.md
│   │   ├── .releaseignore
│   │   ├── AGENTS.md
│   │   ├── ARCHITECTURE_MAP.md
│   │   ├── CHANGELOG.md
│   │   ├── CLAUDE.md
│   │   ├── COPYOVER_MANIFEST.md
│   │   ├── FAILURE_GRAMMAR.md
│   │   ├── LICENSE.md
│   │   ├── MANIFEST.md
│   │   ├── MARKETPLACE_ROADMAP.md
│   │   ├── PROVENANCE.md
│   │   ├── README.md
│   │   ├── TOPOLOGY.md
│   │   ├── plugin.json
│   │   └── plugin.toml
│   ├── Cognitive-Topology-Map
│   │   ├── .github
│   │   │   └── workflows
│   │   │       ├── release.yml
│   │   │       ├── schema-check.yml
│   │   │       ├── topology-enforce.yml
│   │   │       └── validate.yml
│   │   ├── claude-code
│   │   │   ├── .claude-plugin
│   │   │   │   └── plugin.json
│   │   │   ├── agents
│   │   │   │   └── ctmv3-architect.md
│   │   │   ├── commands
│   │   │   │   ├── ctmv3-activate.md
│   │   │   │   ├── ctmv3-architecture-map.md
│   │   │   │   ├── ctmv3-boot.md
│   │   │   │   ├── ctmv3-dot-init.md
│   │   │   │   ├── ctmv3-session-close.md
│   │   │   │   ├── ctmv3-sovereign-init.md
│   │   │   │   ├── ctmv3-status.md
│   │   │   │   └── ctmv3-warm.md
│   │   │   ├── hooks
│   │   │   │   ├── hooks.json
│   │   │   │   ├── session_start_codex.py
│   │   │   │   └── stop_codex.py
│   │   │   ├── skills
│   │   │   │   └── ctmv3
│   │   │   │       └── SKILL.md
│   │   │   ├── README.md
│   │   │   └── settings.json
│   │   ├── codex
│   │   │   ├── config-fragments
│   │   │   │   ├── config.toml.fragment
│   │   │   │   └── hooks.json.fragment
│   │   │   ├── skills
│   │   │   │   └── ctmv3
│   │   │   │       ├── agents
│   │   │   │       │   └── openai.yaml
│   │   │   │       ├── scripts
│   │   │   │       │   ├── ctmv3-boot.sh
│   │   │   │       │   └── ctmv3-status.sh
│   │   │   │       ├── REFERENCES.md
│   │   │   │       └── SKILL.md
│   │   │   ├── README.md
│   │   │   └── install.sh
│   │   ├── core
│   │   │   ├── ctmv3
│   │   │   │   ├── core
│   │   │   │   │   ├── templates
│   │   │   │   │   │   ├── extras
│   │   │   │   │   │   │   ├── claude-settings.json.template
│   │   │   │   │   │   │   ├── golden_paths.json.template
│   │   │   │   │   │   │   ├── pre-commit-config.yaml.template
│   │   │   │   │   │   │   └── session_state.json.template
│   │   │   │   │   │   ├── AGENTS.md.template
│   │   │   │   │   │   ├── ARCHITECTURE_MAP.md.template
│   │   │   │   │   │   ├── CLAUDE.md.template
│   │   │   │   │   │   ├── FAILURE_GRAMMAR.md.template
│   │   │   │   │   │   ├── PROVENANCE.md.template
│   │   │   │   │   │   ├── TOPOLOGY.md.template
│   │   │   │   │   │   ├── copilot-instructions.md.template
│   │   │   │   │   │   └── topology-enforce.yml.template
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── activate.py
│   │   │   │   │   ├── architecture_map.py
│   │   │   │   │   ├── boot.py
│   │   │   │   │   ├── cli.py
│   │   │   │   │   ├── dot_init.py
│   │   │   │   │   ├── fingerprint.py
│   │   │   │   │   ├── orchestration.py
│   │   │   │   │   ├── server.py
│   │   │   │   │   ├── sovereign.py
│   │   │   │   │   ├── states.py
│   │   │   │   │   ├── templates.py
│   │   │   │   │   └── watcher.py
│   │   │   │   ├── tests
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── test_engine.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── __main__.py
│   │   │   ├── README.md
│   │   │   └── pyproject.toml
│   │   ├── cursor
│   │   │   ├── scripts
│   │   │   │   ├── ctmv3-activate.sh
│   │   │   │   ├── ctmv3-architecture-map.sh
│   │   │   │   ├── ctmv3-boot.sh
│   │   │   │   ├── ctmv3-chain.sh
│   │   │   │   ├── ctmv3-dot-init.sh
│   │   │   │   ├── ctmv3-fingerprint.sh
│   │   │   │   ├── ctmv3-session-close.sh
│   │   │   │   ├── ctmv3-sovereign-init.sh
│   │   │   │   ├── ctmv3-status.sh
│   │   │   │   └── ctmv3-warm.sh
│   │   │   ├── README.md
│   │   │   └── install.sh
│   │   ├── docs
│   │   │   ├── examples
│   │   │   │   └── case_codebase_entry.md
│   │   │   ├── interfaces
│   │   │   │   ├── orchestration.md
│   │   │   │   └── python.md
│   │   │   ├── AGENTS_ADDENDUM.md
│   │   │   ├── ARCHITECTURE_MAP_TEMPLATE.md
│   │   │   ├── BOOT_PROTOCOL.md
│   │   │   ├── CONSTITUTION.md
│   │   │   ├── DOT_TOPOLOGY.md
│   │   │   ├── EXPLANATION.md
│   │   │   ├── FAILURE_GRAMMAR.md
│   │   │   ├── GOLDEN_PATH.md
│   │   │   ├── PROVENANCE.md
│   │   │   ├── SCHEMA_AUDIT.md
│   │   │   ├── SKILL.md
│   │   │   └── TOPOLOGY.md
│   │   ├── examples
│   │   │   └── cold-start-trace.md
│   │   ├── extras
│   │   │   ├── templates
│   │   │   │   ├── AGENTS.example.md
│   │   │   │   ├── CLAUDE.example.md
│   │   │   │   ├── golden_paths.example.json
│   │   │   │   └── topology-enforce.example.yml
│   │   │   └── README.md
│   │   ├── gemini-cli
│   │   │   ├── ctmv3
│   │   │   │   ├── commands
│   │   │   │   │   └── ctmv3
│   │   │   │   │       ├── boot.toml
│   │   │   │   │       └── status.toml
│   │   │   │   ├── scripts
│   │   │   │   │   ├── ctmv3-session-start.sh
│   │   │   │   │   └── ctmv3-wrap.sh
│   │   │   │   ├── skills
│   │   │   │   │   └── ctmv3
│   │   │   │   │       └── SKILL.md
│   │   │   │   ├── GEMINI.md
│   │   │   │   └── gemini-extension.json
│   │   │   ├── README.md
│   │   │   └── install.sh
│   │   ├── opencode
│   │   │   ├── agent
│   │   │   │   └── ctmv3-architect.md
│   │   │   ├── command
│   │   │   │   └── ctmv3-status.md
│   │   │   ├── plugin
│   │   │   │   └── ctmv3.ts
│   │   │   ├── README.md
│   │   │   ├── install.sh
│   │   │   └── opencode.json.fragment
│   │   ├── research
│   │   │   └── RUNTIME_FORMATS.md
│   │   ├── scripts
│   │   │   ├── privacy_boundary_scan.py
│   │   │   └── validate_release_tree.py
│   │   ├── tests
│   │   │   ├── privacy_boundary_scan_smoke.py
│   │   │   ├── run-all.sh
│   │   │   ├── smoke.sh
│   │   │   └── verify-install.sh
│   │   ├── .releaseignore
│   │   ├── CHANGELOG.md
│   │   ├── CODEBASE_INTELLIGENCE.md
│   │   ├── CONTRIBUTING.md
│   │   ├── COPYOVER_MANIFEST.md
│   │   ├── INSTALL.md
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── STRUCTURE.md
│   │   ├── __init__.py
│   │   └── ctm-plugin-filetree-5-24.md
│   └── Mentat
│       ├── .claude-plugin
│       │   └── plugin.json
│       ├── adapters
│       │   ├── codex
│       │   │   ├── hooks
│       │   │   │   ├── _lib.py
│       │   │   │   ├── _lib.py.backup_hook_schema_20260603_1530
│       │   │   │   ├── permission_request.py
│       │   │   │   ├── post_tool_use.py
│       │   │   │   ├── pre_tool_use.py
│       │   │   │   ├── session_start.py
│       │   │   │   ├── stop.py
│       │   │   │   └── user_prompt_submit.py
│       │   │   ├── AGENTS.snippet.md
│       │   │   ├── README.md
│       │   │   ├── config.toml.snippet
│       │   │   └── hooks.json
│       │   ├── gemini
│       │   │   ├── hooks
│       │   │   │   ├── _lib.py
│       │   │   │   ├── after_agent.py
│       │   │   │   ├── after_model.py
│       │   │   │   ├── after_tool.py
│       │   │   │   ├── before_agent.py
│       │   │   │   ├── before_model.py
│       │   │   │   ├── before_tool.py
│       │   │   │   ├── before_tool_selection.py
│       │   │   │   ├── hooks.json
│       │   │   │   ├── notification.py
│       │   │   │   ├── pre_compress.py
│       │   │   │   ├── session_end.py
│       │   │   │   └── session_start.py
│       │   │   ├── GEMINI.snippet.md
│       │   │   ├── README.md
│       │   │   └── gemini-extension.json
│       │   ├── install_universal.sh
│       │   └── test_universal.sh
│       ├── agents
│       │   ├── mentat-cartographer.md
│       │   ├── mentat-crucible.md
│       │   ├── mentat-scribe.md
│       │   └── mentat-sentinel.md
│       ├── commands
│       │   ├── README.md
│       │   ├── debrief.md
│       │   ├── dispatch.md
│       │   ├── drift-check.md
│       │   ├── plan.md
│       │   ├── qtable.md
│       │   ├── reflect.md
│       │   ├── scope.md
│       │   ├── status.md
│       │   └── tail.md
│       ├── docs
│       │   ├── PROVENANCE.md
│       │   ├── SOTA_CHECKLIST.md
│       │   └── STYLE.v2.md
│       ├── evals
│       │   ├── agents
│       │   │   ├── comparator.md
│       │   │   └── grader.md
│       │   ├── references
│       │   │   └── schemas.md
│       │   ├── scenarios
│       │   │   ├── __init__.py
│       │   │   ├── _types.py
│       │   │   ├── persistence_recovery.py
│       │   │   ├── predictive_routing.py
│       │   │   └── state_transitions.py
│       │   ├── scripts
│       │   │   ├── __init__.py
│       │   │   ├── aggregate_benchmark.py
│       │   │   ├── generate_report.py
│       │   │   └── run_eval.py
│       │   ├── README.md
│       │   ├── SKILL.md
│       │   ├── __init__.py
│       │   ├── harness.py
│       │   └── rubric.json
│       ├── helpers
│       │   ├── HELPERS.md
│       │   ├── mentat-conductor.md
│       │   ├── mentat-medic.md
│       │   └── mentat-quartermaster.md
│       ├── hooks
│       │   ├── _lib.py
│       │   ├── _lib.py.backup_hook_schema_20260603_1530
│       │   ├── hooks.json
│       │   ├── post_compact.py
│       │   ├── post_tool_use.py
│       │   ├── pre_compact.py
│       │   ├── pre_tool_use.py
│       │   ├── session_start.py
│       │   ├── stop.py
│       │   ├── stop_failure.py
│       │   ├── subagent_start.py
│       │   ├── subagent_stop.py
│       │   └── user_prompt_submit.py
│       ├── mcp_server
│       │   ├── __init__.py
│       │   └── __main__.py
│       ├── monitors
│       │   ├── README.md
│       │   ├── archivist.py
│       │   ├── drift_watcher.py
│       │   ├── entropy_watcher.py
│       │   ├── monitors.json
│       │   └── test_smoke.py
│       ├── schemas
│       ├── scripts
│       │   ├── command_frontmatter_lint.py
│       │   ├── hook_schema_smoke.py
│       │   ├── integration_smoke.py
│       │   ├── privacy_boundary_scan.py
│       │   ├── prompt_surface_review.py
│       │   └── validate_release_tree.py
│       ├── skills
│       │   ├── mentat-debrief
│       │   │   ├── scripts
│       │   │   │   ├── __init__.py
│       │   │   │   ├── aggregate.py
│       │   │   │   ├── render.py
│       │   │   │   ├── template.html
│       │   │   │   └── test_smoke.py
│       │   │   └── SKILL.md
│       │   ├── mentat-dispatch
│       │   │   └── SKILL.md
│       │   ├── mentat-plan
│       │   │   └── SKILL.md
│       │   └── mentat-reflect
│       │       └── SKILL.md
│       ├── state_machine
│       │   ├── __init__.py
│       │   ├── drift.py
│       │   ├── insights.py
│       │   ├── machine.py
│       │   ├── q_table.py
│       │   └── session.py
│       ├── style
│       │   ├── PROVENANCE.md
│       │   ├── SOTA_CHECKLIST.md
│       │   └── STYLE.v2.md
│       ├── tests
│       │   ├── command_frontmatter_lint_smoke.py
│       │   ├── privacy_boundary_scan_smoke.py
│       │   └── prompt_surface_review_smoke.py
│       ├── webhook_engine
│       │   ├── __init__.py
│       │   ├── config.py
│       │   ├── dlq.py
│       │   ├── emitter.py
│       │   ├── envelope.py
│       │   └── test_smoke.py
│       ├── .mcp.json
│       ├── .releaseignore
│       ├── 5-24-filetree-mentatv2-plugin.md
│       ├── AGENTS.md
│       ├── CHANGELOG.md
│       ├── CONTEXT.md
│       ├── COPYOVER_MANIFEST.md
│       ├── INSTALL.md
│       ├── MEMORY.md
│       ├── PLAN.md
│       ├── README.md
│       ├── SUBSYSTEM_INVENTORY.md
│       ├── mcp.json
│       └── webhooks.json
├── Registry
│   └── plugins.yaml
├── Scripts
├── Servers
│   └── Muaddib
│       ├── databus
│       │   ├── __init__.py
│       │   ├── openrouter.yaml
│       │   ├── openrouter_wrapper.py
│       │   └── sovereign_openrouter.py
│       ├── docs
│       │   ├── expose_mcp_to_internet.md
│       │   └── https_wrapper_endpoints.md
│       ├── infrustructure
│       │   ├── __init__.py
│       │   ├── ai_integration_core.py
│       │   ├── ai_system_integration.py
│       │   └── meta_intelligence_engine.py
│       ├── muadib
│       │   ├── 5-7-26-muadib.md
│       │   ├── README.md
│       │   ├── __init__.py
│       │   ├── advanced_bridge.py
│       │   ├── aeron_neural_memory.py
│       │   ├── code_and_structured_modality.py
│       │   ├── continual_learning_module.py
│       │   ├── infrustructure-filetree-6-9.md
│       │   ├── knowledge_graph_attention.py
│       │   ├── memory_attention_classes.py
│       │   ├── muaddib.py
│       │   ├── muadib-filetree-6-9.md
│       │   ├── neural_config.py
│       │   ├── neural_memory_network.py
│       │   ├── structured_data_modalities.py
│       │   ├── tool_modality.py
│       │   └── unified_modality.py
│       ├── runtime-tools
│       │   ├── README.backup_20260606_173807.md
│       │   ├── README.md
│       │   ├── ai-system-integration.md
│       │   ├── auto-tool-module.md
│       │   ├── code-analysis-tool.md
│       │   ├── enhanced-code-analysis-tool.md
│       │   ├── enhanced-web-tool.md
│       │   ├── exo-and-lisan.md
│       │   ├── file-tool.md
│       │   ├── memory-and-mem-interconnect.md
│       │   ├── meta-intelligence-engine.md
│       │   ├── muaddib-network.md
│       │   ├── openrouter-agent-tool.md
│       │   ├── openrouter-planner-tool.md
│       │   ├── project-context-tool.md
│       │   ├── session-manager-enterprise.md
│       │   ├── session-tool.md
│       │   ├── shell-tool.md
│       │   ├── thought_journal_tool.md
│       │   ├── visual-tool.md
│       │   └── vscode-terminal-tool.md
│       ├── tools
│       │   ├── __init__.py
│       │   ├── auto_tool_module.py
│       │   ├── code_analysis_tool.py
│       │   ├── enhanced_code_analysis_tool.py
│       │   ├── enhanced_web_tool.py
│       │   ├── exoskeleton_tool.py
│       │   ├── file_tool.py
│       │   ├── lisan_al_gaib.py
│       │   ├── memory_interconnect.py
│       │   ├── memory_tool.py
│       │   ├── meta_intelligence_engine.py
│       │   ├── openrouter_agent_tool.py
│       │   ├── openrouter_planner_tool.py
│       │   ├── project_context_tool.py
│       │   ├── session_manager_tool.py
│       │   ├── shell_tool.py
│       │   ├── thought_journal_tool.py
│       │   ├── visual_tool.py
│       │   ├── vscode_terminal_tool.py
│       │   └── web_tool.py
│       ├── AGENTS.md
│       ├── ARCHITECTURE.md
│       ├── ARCHITECTURE_MAP.md
│       ├── CONTEXT.md
│       ├── HOOK_BRIDGE.md
│       ├── MCP_SPEC.md
│       ├── MEMORY.md
│       ├── PROVENANCE.md
│       ├── README.md
│       ├── all_tools.json
│       ├── claude_desktop_config.json
│       ├── config_manager.py
│       ├── golden_paths.json
│       ├── golden_paths_meta.json
│       ├── hook_executor.py
│       ├── hooks_manifest.json
│       ├── https_wrapper.py
│       ├── intelligent_output_hook.py
│       ├── manifest.json
│       ├── mcp.json
│       ├── mcp_api.py
│       ├── mcp_server.py
│       ├── openapi_builder.py
│       ├── sovereign_context_hook.py
│       ├── sse_broadcaster.py
│       ├── test_https_wrapper.py
│       ├── tool_manifest.json
│       ├── webhook_engine.py
│       └── workflows-new.md
├── Skills
│   ├── academic-whitepaper-engine
│   │   ├── assets
│   │   │   └── whitepaper-template.tex
│   │   ├── references
│   │   │   ├── citation-styles.md
│   │   │   ├── code-validation.md
│   │   │   ├── latex-preamble.tex
│   │   │   └── visual-examples.md
│   │   ├── scripts
│   │   │   ├── attachments
│   │   │   │   ├── md2tex (1).py
│   │   │   │   └── sart (1).py
│   │   │   ├── generate_metadata.py
│   │   │   ├── md2tex.py
│   │   │   └── sart.py
│   │   └── SKILL.md
│   ├── codex-config-topology
│   │   ├── agents
│   │   │   └── openai.yaml
│   │   ├── references
│   │   │   ├── source
│   │   │   │   ├── AGENTS.md
│   │   │   │   ├── AGENTS.override.md
│   │   │   │   ├── MCP_SPEC.md
│   │   │   │   ├── OPSEC.md
│   │   │   │   ├── STYLE.md
│   │   │   │   ├── default.rules
│   │   │   │   └── tool_manifest.json
│   │   │   ├── bb7-exo-loop.md
│   │   │   ├── current-codex-surfaces-2026-06-04.md
│   │   │   ├── doctrine-stack.md
│   │   │   ├── examples.md
│   │   │   ├── failure-grammar.md
│   │   │   ├── host-surface.md
│   │   │   ├── json-tool-output-hygiene.md
│   │   │   ├── operator-control-plane.md
│   │   │   ├── provenance.md
│   │   │   ├── topology.md
│   │   │   └── windows-host-surface.md
│   │   ├── SKILL.backup_20260604_031221.md
│   │   └── SKILL.md
│   ├── constitutional-prompt-framework
│   │   ├── agents
│   │   │   └── openai.yaml
│   │   ├── assets
│   │   │   ├── templates
│   │   │   │   ├── agent-constitution-full.md
│   │   │   │   ├── audit-report-template.md
│   │   │   │   ├── capability-dispatch-table.md
│   │   │   │   ├── constitution-spec.example.json
│   │   │   │   ├── intake-form.md
│   │   │   │   ├── memory-policy-template.md
│   │   │   │   ├── platform-binding-template.md
│   │   │   │   ├── red-team-report-template.md
│   │   │   │   ├── release-checklist.md
│   │   │   │   └── rewrite-plan-template.md
│   │   │   └── single-file-agent-constitution-skeleton.md
│   │   ├── examples
│   │   │   ├── example-agent-constitution.md
│   │   │   ├── example-audit-report.md
│   │   │   ├── example-rewrite-plan.md
│   │   │   └── rendered-from-spec.md
│   │   ├── references
│   │   │   ├── 00-doc-chain.md
│   │   │   ├── 01-constitutional-prompt-theory.md
│   │   │   ├── 02-derivation-guide.md
│   │   │   ├── 03-layer-contracts.md
│   │   │   ├── 04-authority-and-governance.md
│   │   │   ├── 05-rules-of-engagement-patterns.md
│   │   │   ├── 06-operating-doctrine-library.md
│   │   │   ├── 07-persona-architecture.md
│   │   │   ├── 08-capability-dispatch.md
│   │   │   ├── 09-memory-continuity.md
│   │   │   ├── 10-platform-binding-matrix.md
│   │   │   ├── 11-security-privacy-safety.md
│   │   │   ├── 12-long-context-and-compaction.md
│   │   │   ├── 13-domain-ingestion-and-knowledge-modeling.md
│   │   │   ├── 14-output-contracts.md
│   │   │   ├── 15-audit-checklist.md
│   │   │   ├── 16-evaluation-rubric.md
│   │   │   ├── 17-red-team-suite.md
│   │   │   ├── 18-anti-patterns.md
│   │   │   ├── 19-rewrite-playbook.md
│   │   │   ├── 20-deployment-and-maintenance.md
│   │   │   ├── 21-interoperability-notes.md
│   │   │   ├── 22-glossary.md
│   │   │   ├── 23-schema-driven-authoring.md
│   │   │   └── 24-failure-mode-atlas.md
│   │   ├── schemas
│   │   │   ├── audit-report.schema.json
│   │   │   ├── constitution-spec.schema.json
│   │   │   └── skill-package.schema.json
│   │   ├── scripts
│   │   │   ├── _cpf_common.py
│   │   │   ├── constitution_linter.py
│   │   │   ├── render_constitution_from_spec.py
│   │   │   ├── run_static_evals.py
│   │   │   ├── score_constitution.py
│   │   │   └── validate_skill_package.py
│   │   ├── tests
│   │   │   ├── fixtures
│   │   │   │   └── minimal_constitution_spec.json
│   │   │   ├── README.md
│   │   │   └── eval_cases.yaml
│   │   ├── CHANGELOG.md
│   │   ├── MANIFEST.md
│   │   ├── README.md
│   │   ├── RELEASE_NOTES.md
│   │   ├── SKILL.md
│   │   └── package-manifest.json
│   ├── document-omniscient
│   │   ├── agents
│   │   │   └── openai.yaml
│   │   ├── references
│   │   │   ├── CLAUDE_PROJECT_SETUP.md
│   │   │   ├── FAILURE_GRAMMAR.md
│   │   │   ├── OUTPUT_CONTRACTS.md
│   │   │   ├── TOOLING_PLAYBOOK.md
│   │   │   ├── TOPOLOGY.md
│   │   │   ├── claude_tool_pack.md
│   │   │   └── codebase_omniscient_source.md
│   │   └── SKILL.md
│   ├── grok-build-configurator
│   │   ├── agents
│   │   │   ├── AGENTS.md
│   │   │   └── openai.yaml
│   │   ├── assets
│   │   │   └── templates
│   │   │       ├── hooks
│   │   │       │   └── git-gh-only
│   │   │       │       ├── git-gh-only.json
│   │   │       │       └── git-gh-only.sh
│   │   │       ├── AGENTS.grok-project.md
│   │   │       ├── config.ci-safe.toml
│   │   │       ├── config.daily.toml
│   │   │       ├── config.enterprise-oidc.toml
│   │   │       ├── headless-ci-review.sh
│   │   │       ├── pager.tui.toml
│   │   │       ├── project.grok.config.mcp.toml
│   │   │       └── sandbox.toml
│   │   ├── references
│   │   │   ├── xai-docs
│   │   │   │   ├── 01-getting-started.md
│   │   │   │   ├── 02-authentication.md
│   │   │   │   ├── 03-keyboard-shortcuts.md
│   │   │   │   ├── 04-slash-commands.md
│   │   │   │   ├── 05-configuration.md
│   │   │   │   ├── 06-theming.md
│   │   │   │   ├── 07-mcp-servers.md
│   │   │   │   ├── 08-skills.md
│   │   │   │   ├── 09-plugins.md
│   │   │   │   ├── 10-hooks.md
│   │   │   │   ├── 11-custom-models.md
│   │   │   │   ├── 12-project-rules.md
│   │   │   │   ├── 13-memory.md
│   │   │   │   ├── 14-headless-mode.md
│   │   │   │   ├── 15-agent-mode.md
│   │   │   │   ├── 16-subagents.md
│   │   │   │   ├── 17-sessions.md
│   │   │   │   ├── 18-sandbox.md
│   │   │   │   ├── 19-plan-mode.md
│   │   │   │   ├── 20-background-tasks.md
│   │   │   │   ├── 21-terminal-support.md
│   │   │   │   └── 22-permissions-and-safety.md
│   │   │   ├── grok-build-command-cheatsheet.md
│   │   │   └── grok-build-configuration-field-guide.md
│   │   ├── scripts
│   │   │   ├── grok_build_doctor.py
│   │   │   ├── install_codex_skill.sh
│   │   │   └── render_grok_config.py
│   │   ├── README.md
│   │   ├── SKILL.md
│   │   └── manifest.json
│   ├── somnus-intelligent-workspace
│   │   ├── assets
│   │   │   └── ssds_sic_template.md
│   │   ├── casefiles
│   │   │   ├── .gitkeep
│   │   │   └── Intelligence-Casefile-Template.md
│   │   ├── references
│   │   │   ├── sovereign_doctrine.md
│   │   │   └── varys_strategic_substrate.md
│   │   ├── scripts
│   │   │   └── init_casefile.sh
│   │   ├── {assets,casefiles,references,scripts}
│   │   ├── AGENTS.md
│   │   ├── README.md
│   │   └── SKILL.md
│   └── sovereign-skill-architect
│       ├── examples
│       │   └── case_codebase_entry.md
│       ├── interfaces
│       │   └── python.md
│       ├── AGENTS_ADDENDUM.md
│       ├── ARCHITECTURE_MAP_TEMPLATE.md
│       ├── BOOT_PROTOCOL.md
│       ├── CONSTITUTION.md
│       ├── DOT_TOPOLOGY.md
│       ├── FAILURE_GRAMMAR.md
│       ├── PROVENANCE.md
│       ├── SKILL.md
│       ├── TOPOLOGY.md
│       ├── case_codebase_entry.md
│       └── python.md
├── templates
│   └── logo.png
├── README.md
└── install.sh
```

---
*Generated by FileTree Pro Extension*
