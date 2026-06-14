# Aeriadne v1 Validation Report

Date: 2026-06-13
Workspace: `/home/daeron/Projects/Modern-ML/Plugins/Aeriadne`
Status: PASS
Install performed: Yes, local Codex marketplace refresh only
Git push performed: No

## Commands and Results

### Package validator

```text
Aeriadne package validation: PASS
root=/home/daeron/Projects/Modern-ML/Plugins/Aeriadne
skills=aeriadne-marketplace-operator, constitutional-prompt-framework
mcp=sovereign-bb7 canonical-reference
copyover=COPYOVER_MANIFEST.md reviewed-gate, .releaseignore enforced
privacy=privacy_boundary_scan.py enforced
privacy_smoke=tests/privacy_boundary_scan_smoke.py enforced
site_prototypes=site_prototype_audit.py enforced
site_prototypes_smoke=tests/site_prototype_audit_smoke.py enforced
```

### Codex plugin ingestion validator

```text
Plugin validation passed: /home/daeron/Projects/Modern-ML/Plugins/Aeriadne
```

The `.codex-plugin/plugin.json` manifest now includes the Codex-facing
`interface` object required by the plugin ingestion validator. Root and Claude
metadata mirrors carry the same interface block so package metadata stays
coherent across projection surfaces.

### JSON manifests

```text
json manifests parse: PASS
```

Checked:

- `plugin.json`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `registry/aeriadne.plugin.json`
- `registry/cognitive-topology-map.plugin.json`
- `registry/mentat.plugin.json`
- `registry/codex-config-topology.plugin.json`

### TOML manifest

```text
toml parse: PASS
id= aeriadne
skills= constitutional-prompt-framework, aeriadne-marketplace-operator
```

### Plugin metadata mirrors

```text
plugin metadata mirrors match: PASS
```

### Native plugin registry cards

```text
registry/cognitive-topology-map.plugin.json: PASS
registry/mentat.plugin.json: PASS
registry/codex-config-topology.plugin.json: PASS (explicit staged-local state)
```

The package validator now checks staged-green and staged-local native plugin
cards for id, canonical path, public copy target, installed boolean, install
evidence when installed, PASS validation status, and copyover operator review
gate. Staged-local cards must also keep `release_ready=false` and list known
gaps.
Staged-green native plugin cards must also record upstream `privacy_boundary`
evidence and include a `privacy_boundary_scan.py` validation command.

The CTMv3 card currently records engine version `1.3.0`, `tests/run-all.sh`
PASS with 155 unit tests plus smoke, JSON, bash syntax, TOML command, inventory,
and release hygiene checks, privacy-boundary enforcement, and release-tree
validation with `140` candidate files and `1045` ignored local-only/forbidden
files after command backfill and cache cleanup. `ctmv3-workspace-activator@local`
is installed/enabled; its plugin manifest and staged engine are both `1.3.0`.

The Mentat card currently records `58 pass / 0 fail / 0 skip`, command
frontmatter lint for nine slash commands, prompt-surface review for seven
agent/helper prompts plus the helper index, privacy-boundary enforcement, and
release-tree validation with `139` candidate files and `299` ignored
local-only/forbidden files after cache cleanup. The count includes the
install-facing `.mcp.json` projection; `mentat@local` is installed/enabled and
its plugin-provided MCP server hydrates again from `.mcp.json`.

### Copyover release membrane

```text
COPYOVER_MANIFEST.md: PASS
.releaseignore: PASS
```

The package validator now requires Aeriadne's own copyover manifest and release
ignore. `.releaseignore` must cover local VCS/index state, runtime/session
state, caches, secrets, DBs, logs, generated filetrees, and
`.sovereign/session_state.json` before package validation can pass.

### Releaseignore dry-run

```text
rsync -avn --exclude-from=.releaseignore ./ /tmp/aeriadne-copy-dryrun/
.releaseignore
COPYOVER_MANIFEST.md
.sovereign/golden_paths.json
.sovereign/topology_fingerprint.txt
```

The filtered dry-run confirms the copy set includes the release gate and the
deliberate CTMv3 warm-start artifacts, while excluding
`.sovereign/session_state.json`, generated filetree snapshots, local indexes,
secrets, and runtime DB patterns.

### Privacy scan

```text
privacy_boundary_scan_smoke: PASS
Aeriadne privacy boundary scan: PASS
root=/home/daeron/Projects/Modern-ML/Plugins/Aeriadne
policy=allowlisted-local-roots, no private archive/source identifiers
external_privacy_spot_check: PASS
```

The package validator now invokes `scripts/privacy_boundary_scan.py`. The
scanner uses an allowlist of known package/review/control-plane roots and
generic leak shapes for unapproved local absolute paths, external media paths,
compact private source identifiers, and stale local tool log/archive path shapes. It
does not commit exact private archive identifiers into the package.
`tests/privacy_boundary_scan_smoke.py` proves the allow and reject cases with
synthetic fixtures while disabling bytecode writes. The external spot-check also
did not find private semantic archive names, raw Golden Path source paths, local
media paths, or stale local tool log/archive paths in the checked staging docs.

### Site prototype audit

```text
site_prototype_audit_smoke: PASS
Aeriadne site prototype audit: PASS
prototypes=1
semantic_requirements=4
policy=preserve-local-spec-site-artifacts, semantic-content-enforced, releaseignore-excluded-until-promoted
```

The site prototype audit preserves staging-local HTML/site pages without moving
them into public copyover. It currently proves the Mentat root HTML artifact
exists, is marked local-only and `public_copyover=false`, carries a do-not-delete
note, is excluded by Mentat's `.releaseignore`, and still contains the declared
state-machine substrate, Q-table loop, insight-bus, drift/hook, and MCP/runtime
projection markers until Daeron promotes the linked-doc/site surface.

### Public repo clean check

```text
/home/daeron/Repositories/Somnus-Intellligence-Stack: clean
```

The public repo was not edited during this pass.

### Codex Config Topology staging validation

```text
Plugin validation passed: /home/daeron/Projects/Modern-ML/Plugins/Codex-Config-Topology
Skill is valid!
json manifests parse: PASS
plugin metadata mirrors match: PASS
```

Installed status remains false. `codex plugin list` still reports
`codex-config-topology@local` as not installed, and the local marketplace source
has not been refreshed from staging.

### MCP server cards

```text
mcp/servers/sovereign-bb7.md: PASS
marketplace/cards/sovereign-bb7.mcp.md: PASS
```

Non-owned local development tools are not attached as marketplace MCP cards.
Private indexed workspaces, semantic archives, logs, and stale local tool state
are not package identity and must not be listed in public or copyover-facing
cards.

Codex Config Topology validates from the restored current staging root but is
still not installed or refreshed into the local marketplace source.

### CPF package validation

```text
Constitutional Prompt Framework package validation
INFO: Skill name: constitutional-prompt-framework
INFO: Description length: 450
RESULT: PASS
```

### CPF linter

```text
Lint report: skills/constitutional-prompt-framework/examples/example-agent-constitution.md
Structural checks:
  PASS mission_identity
  PASS authority_governance
  PASS rules_of_engagement
  PASS operating_doctrine
  PASS persona
  PASS capability
  PASS memory
  PASS output_contracts
  PASS evaluation
  PASS living_status
RESULT: PASS
```

### CPF score

```text
Overall: 87/100
Readiness: production candidate
```

Category scores:

- Mission and identity: 8/10
- Authority and governance: 9/10
- Rules of engagement: 10/10
- Operating doctrine: 10/10
- Persona architecture: 8/10
- Capability dispatch: 9/10
- Memory and continuity: 8/10
- Output contracts: 8/10
- Evaluation and maintenance: 9/10
- Living status: 8/10

### CPF static evals

```text
Static eval report: skills/constitutional-prompt-framework/tests/eval_cases.yaml
Cases: 6
RESULT: PASS
```

Layer coverage:

- approval
- authority
- automation
- capability
- domain_modeling
- evidence
- integrity
- memory
- portability
- privacy
- prompt_injection
- roe
- safety
- scope
- security
- truthfulness

### CPF render fixture

```text
3165 /tmp/aeriadne-cpf-rendered-check.md
```

### Backup churn scan

```text
backup churn scan: PASS
```

### Git status

```text
not a git repository; no git status available and no push performed
```

## Outcome

Aeriadne v1 is locally staged, validated, and installed into Codex as `aeriadne@local`. It has not been copied into the public repo. The next gate is operator approval for copyover review or broader Modern-ML marketplace restructuring first.

## 2026-06-13 CTMv3 activation rerun

During CTMv3 activation, the package validator and CPF package validator were rerun from `/home/daeron/Projects/Modern-ML/Plugins/Aeriadne`.

```text
python3 scripts/validate_package.py .
Aeriadne package validation: PASS
root=/home/daeron/Projects/Modern-ML/Plugins/Aeriadne
skills=aeriadne-marketplace-operator, constitutional-prompt-framework
mcp=sovereign-bb7 canonical-reference
```

```text
python3 skills/constitutional-prompt-framework/scripts/validate_skill_package.py skills/constitutional-prompt-framework
Constitutional Prompt Framework package validation
INFO: Skill name: constitutional-prompt-framework
INFO: Description length: 450
RESULT: PASS
```

CTMv3 boot before activation reported `COLD_START` with 112 files and no Tier 1/Tier 2 CTM signals. Activation artifacts now exist locally; install status remains unchanged.

Boundary correction from Daeron: `/home/daeron/Projects/Modern-ML/Plugins/Aeriadne` is the outside staging/package workspace. The canonical review repo is `/home/daeron/Repositories/Somnus-Intellligence-Stack/`, and it was not edited in this activation pass.

## 2026-06-13 native substrate registry expansion

Aeriadne now catalogs CTMv3 and Mentat as native plugin packages rather than
surface bundles.

The package-facing docs now carry the Golden Path runtime contract in normalized
form: committed state ledger, validation membrane, compensation ledger,
divergence process, and terminal boundary. Raw internal source paths stay out of
marketplace cards and copyover-facing docs.

Added machine-readable cards:

- `registry/cognitive-topology-map.plugin.json`
- `registry/mentat.plugin.json`
- `registry/codex-config-topology.plugin.json`

Added marketplace cards:

- `marketplace/cards/cognitive-topology-map.plugin.md`
- `marketplace/cards/mentat.plugin.md`
- `marketplace/cards/codex-config-topology.plugin.md`

Updated indexes:

- `registry/plugins.yaml`
- `registry/mcp_servers.yaml`
- `marketplace/indexes/plugin-index.yaml`
- `marketplace/indexes/mcp-index.yaml`

Validation rerun:

```text
python3 scripts/validate_package.py .
Aeriadne package validation: PASS
root=/home/daeron/Projects/Modern-ML/Plugins/Aeriadne
skills=aeriadne-marketplace-operator, constitutional-prompt-framework
mcp=sovereign-bb7 canonical-reference
copyover=COPYOVER_MANIFEST.md reviewed-gate, .releaseignore enforced
privacy=privacy_boundary_scan.py enforced
privacy_smoke=tests/privacy_boundary_scan_smoke.py enforced
site_prototypes=site_prototype_audit.py enforced
site_prototypes_smoke=tests/site_prototype_audit_smoke.py enforced
```

```text
json manifests parse: PASS
```

Checked:

- `plugin.json`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `registry/aeriadne.plugin.json`
- `registry/cognitive-topology-map.plugin.json`
- `registry/mentat.plugin.json`

CPF validation rerun:

```text
Constitutional Prompt Framework package validation
INFO: Skill name: constitutional-prompt-framework
INFO: Description length: 450
RESULT: PASS
```

```text
Lint report: skills/constitutional-prompt-framework/examples/example-agent-constitution.md
RESULT: PASS
```

```text
Overall: 87/100
Readiness: production candidate
```

```text
Static eval report: skills/constitutional-prompt-framework/tests/eval_cases.yaml
Cases: 6
RESULT: PASS
```

```text
3165 /tmp/aeriadne-cpf-rendered-check.md
```

Public repo status after this pass:

```text
/home/daeron/Repositories/Somnus-Intellligence-Stack: clean
```
