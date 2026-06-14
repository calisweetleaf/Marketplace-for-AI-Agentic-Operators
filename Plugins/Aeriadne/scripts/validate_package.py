#!/usr/bin/env python3
"""Validate the Aeriadne private-v1 plugin package.

This is intentionally stdlib-only. It checks package shape, manifest parseability,
metadata mirror drift, skill frontmatter, declared path existence, and obvious
secret/runtime-state/backup-churn packaging mistakes. It does not install the plugin.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path

REQUIRED_PATHS = [
    "plugin.json",
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    "plugin.toml",
    ".releaseignore",
    "COPYOVER_MANIFEST.md",
    "README.md",
    "MANIFEST.md",
    "MARKETPLACE_ROADMAP.md",
    "CHANGELOG.md",
    "LICENSE.md",
    "registry/aeriadne.plugin.json",
    "registry/cognitive-topology-map.plugin.json",
    "registry/mentat.plugin.json",
    "registry/codex-config-topology.plugin.json",
    "registry/plugins.yaml",
    "registry/skills.yaml",
    "registry/agents.yaml",
    "registry/mcp_servers.yaml",
    "registry/site_prototypes.json",
    "scripts/privacy_boundary_scan.py",
    "tests/privacy_boundary_scan_smoke.py",
    "scripts/site_prototype_audit.py",
    "tests/site_prototype_audit_smoke.py",
    "skills/constitutional-prompt-framework/SKILL.md",
    "skills/aeriadne-marketplace-operator/SKILL.md",
    "agents/README.md",
    "agents/subagents/prompt-architect.md",
    "agents/subagents/package-cartographer.md",
    "agents/subagents/compatibility-auditor.md",
    "agents/subagents/registry-scribe.md",
    "agents/subagents/release-sentinel.md",
    "adapters/codex/README.md",
    "adapters/claude-code/README.md",
    "adapters/opencode/README.md",
    "mcp/README.md",
    "mcp/servers/sovereign-bb7.md",
    "mcp/contracts/tool-capabilities.yaml",
    "mcp/contracts/client-bindings.yaml",
    "marketplace/cards/aeriadne.plugin.md",
    "marketplace/cards/cognitive-topology-map.plugin.md",
    "marketplace/cards/mentat.plugin.md",
    "marketplace/cards/codex-config-topology.plugin.md",
    "marketplace/cards/constitutional-prompt-framework.skill.md",
    "marketplace/cards/aeriadne-marketplace-operator.skill.md",
    "marketplace/cards/sovereign-bb7.mcp.md",
    "marketplace/site-prototypes.md",
]

FORBIDDEN_NAME_PATTERNS = [
    re.compile(r"(^|/)auth\.json$"),
    re.compile(r"(^|/)installation_id$"),
    re.compile(r"(^|/)\.codegraph(/|$)"),
    re.compile(r"\.(sqlite|sqlite3|db|db-shm|db-wal)$"),
    re.compile(r"(^|/)(sessions|logs|tmp|cache)(/|$)"),
    re.compile(r"(^|/)\.env($|\.)"),
    re.compile(r"backup_\d{8}_\d{6}"),
    re.compile(r"~$"),
]

REQUIRED_RELEASEIGNORE_ENTRIES = {
    ".git/",
    ".codegraph/",
    ".venv/",
    "__pycache__/",
    "*.pyc",
    "*.sqlite",
    "*.sqlite3",
    "*.db",
    "*.db-shm",
    "*.db-wal",
    ".env",
    ".env.*",
    "sessions/",
    "logs/",
    "tmp/",
    "cache/",
    "*.log",
    "backup_*",
    "*~",
    ".sovereign/session_state.json",
    "filetree.md",
    "*filetree*.md",
}

FRONTMATTER_RE = re.compile(r"^---\n(?P<body>.*?)\n---\n", re.DOTALL)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - validator reports all parse failures.
        fail(errors, f"JSON parse failed: {path}: {exc}")
        return None


def check_skill_frontmatter(root: Path, rel: str, expected_name: str, errors: list[str]) -> None:
    path = root / rel
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        fail(errors, f"missing YAML frontmatter: {rel}")
        return
    body = match.group("body")
    if f"name: {expected_name}" not in body:
        fail(errors, f"frontmatter name mismatch in {rel}; expected {expected_name}")
    if "description:" not in body:
        fail(errors, f"missing description in {rel}")


def check_forbidden_files(root: Path, errors: list[str]) -> None:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        for pattern in FORBIDDEN_NAME_PATTERNS:
            if pattern.search(rel):
                fail(errors, f"forbidden package file detected: {rel}")


def check_releaseignore(root: Path, errors: list[str]) -> None:
    path = root / ".releaseignore"
    if not path.exists():
        return
    entries = {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }
    missing = sorted(REQUIRED_RELEASEIGNORE_ENTRIES - entries)
    for entry in missing:
        fail(errors, f".releaseignore missing required release exclusion: {entry}")


def check_privacy_boundary(root: Path, errors: list[str]) -> None:
    script = root / "scripts/privacy_boundary_scan.py"
    if not script.exists():
        return
    result = subprocess.run(
        [sys.executable, str(script), str(root)],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        output = "\n".join(part for part in (result.stdout, result.stderr) if part).strip()
        fail(errors, f"privacy boundary scan failed:\n{output}")


def check_privacy_smoke(root: Path, errors: list[str]) -> None:
    script = root / "tests/privacy_boundary_scan_smoke.py"
    if not script.exists():
        return
    result = subprocess.run(
        [sys.executable, str(script)],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        output = "\n".join(part for part in (result.stdout, result.stderr) if part).strip()
        fail(errors, f"privacy boundary smoke test failed:\n{output}")


def check_site_prototypes(root: Path, errors: list[str]) -> None:
    script = root / "scripts/site_prototype_audit.py"
    if not script.exists():
        return
    result = subprocess.run(
        [sys.executable, str(script), str(root)],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        output = "\n".join(part for part in (result.stdout, result.stderr) if part).strip()
        fail(errors, f"site prototype audit failed:\n{output}")


def check_site_prototype_smoke(root: Path, errors: list[str]) -> None:
    script = root / "tests/site_prototype_audit_smoke.py"
    if not script.exists():
        return
    result = subprocess.run(
        [sys.executable, str(script)],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        output = "\n".join(part for part in (result.stdout, result.stderr) if part).strip()
        fail(errors, f"site prototype smoke test failed:\n{output}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Aeriadne plugin root")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    errors: list[str] = []

    if not root.exists():
        print(f"ERROR: root does not exist: {root}", file=sys.stderr)
        return 2

    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            fail(errors, f"missing required path: {rel}")

    root_manifest = load_json(root / "plugin.json", errors) if (root / "plugin.json").exists() else None
    codex_manifest = load_json(root / ".codex-plugin/plugin.json", errors) if (root / ".codex-plugin/plugin.json").exists() else None
    claude_manifest = load_json(root / ".claude-plugin/plugin.json", errors) if (root / ".claude-plugin/plugin.json").exists() else None
    registry_card = load_json(root / "registry/aeriadne.plugin.json", errors) if (root / "registry/aeriadne.plugin.json").exists() else None
    ctmv3_card = load_json(root / "registry/cognitive-topology-map.plugin.json", errors) if (root / "registry/cognitive-topology-map.plugin.json").exists() else None
    mentat_card = load_json(root / "registry/mentat.plugin.json", errors) if (root / "registry/mentat.plugin.json").exists() else None
    codex_config_card = load_json(root / "registry/codex-config-topology.plugin.json", errors) if (root / "registry/codex-config-topology.plugin.json").exists() else None

    if isinstance(root_manifest, dict):
        if root_manifest.get("name") != "aeriadne":
            fail(errors, "plugin.json name must be aeriadne")
        if root_manifest.get("skills") != "./skills/":
            fail(errors, "plugin.json skills must be ./skills/")

    if root_manifest is not None and codex_manifest is not None and root_manifest != codex_manifest:
        fail(errors, "plugin.json and .codex-plugin/plugin.json drifted")
    if root_manifest is not None and claude_manifest is not None and root_manifest != claude_manifest:
        fail(errors, "plugin.json and .claude-plugin/plugin.json drifted")

    if registry_card and isinstance(registry_card, dict):
        includes = registry_card.get("includes", {})
        skills = set(includes.get("skills", [])) if isinstance(includes, dict) else set()
        for expected in {"constitutional-prompt-framework", "aeriadne-marketplace-operator"}:
            if expected not in skills:
                fail(errors, f"registry card missing skill include: {expected}")

    native_cards = {
        "registry/cognitive-topology-map.plugin.json": (ctmv3_card, "cognitive-topology-map"),
        "registry/mentat.plugin.json": (mentat_card, "mentat"),
        "registry/codex-config-topology.plugin.json": (codex_config_card, "codex-config-topology"),
    }
    for rel, (card, expected_id) in native_cards.items():
        if not isinstance(card, dict):
            continue
        status = card.get("status")
        if card.get("id") != expected_id:
            fail(errors, f"{rel} id must be {expected_id}")
        if not card.get("canonical_path"):
            fail(errors, f"{rel} missing canonical_path")
        if not card.get("public_copy_target"):
            fail(errors, f"{rel} missing public_copy_target")
        installed = card.get("installed")
        if not isinstance(installed, bool):
            fail(errors, f"{rel} installed must be a boolean")
        if installed:
            install_evidence = card.get("install_evidence")
            if not isinstance(install_evidence, dict):
                fail(errors, f"{rel} installed=true requires install_evidence")
            else:
                for field in ("codex_plugin_id", "status", "version", "cache_path"):
                    if not str(install_evidence.get(field, "")).strip():
                        fail(errors, f"{rel} install_evidence missing {field}")
                if install_evidence.get("status") != "installed, enabled":
                    fail(errors, f"{rel} install_evidence.status must be installed, enabled")
                for field in ("marketplace_path", "cache_path"):
                    path_value = str(install_evidence.get(field, "")).strip()
                    if path_value and not Path(path_value).exists():
                        fail(errors, f"{rel} install_evidence.{field} does not exist: {path_value}")
        validation = card.get("validation", {})
        copyover = card.get("copyover", {})
        if not isinstance(copyover, dict) or not copyover.get("requires_operator_review"):
            fail(errors, f"{rel} copyover.requires_operator_review must be true")
        if status in {"staged-green", "staged-local"}:
            if not isinstance(validation, dict) or validation.get("last_status") != "PASS":
                fail(errors, f"{rel} validation.last_status must be PASS")
            latest_summary = validation.get("latest_summary", {}) if isinstance(validation, dict) else {}
            if status == "staged-green":
                commands = validation.get("commands", []) if isinstance(validation, dict) else []
                if not isinstance(latest_summary, dict) or not latest_summary.get("privacy_boundary"):
                    fail(errors, f"{rel} staged-green card must record privacy_boundary evidence")
                if not any("privacy_boundary_scan.py" in str(command) for command in commands):
                    fail(errors, f"{rel} staged-green validation commands must include privacy_boundary_scan.py")
            if status == "staged-local" and card.get("release_ready") is not False:
                fail(errors, f"{rel} release_ready must remain false while staged-local")
        else:
            if card.get("release_ready") is not False:
                fail(errors, f"{rel} release_ready must be false for non-green package cards")
            if not card.get("expected_staging_path"):
                fail(errors, f"{rel} missing expected_staging_path for non-green package card")
            if not card.get("known_gaps"):
                fail(errors, f"{rel} must list known_gaps while not staged-green")
            if not isinstance(validation, dict) or validation.get("last_status") not in {"FAIL", "PENDING", "NEEDS_RESTAGE"}:
                fail(errors, f"{rel} validation.last_status must record FAIL, PENDING, or NEEDS_RESTAGE while not staged-green")

    try:
        data = tomllib.loads((root / "plugin.toml").read_text(encoding="utf-8"))
        if data.get("id") != "aeriadne":
            fail(errors, "plugin.toml id must be aeriadne")
        for skill in data.get("skills", []):
            path = skill.get("path")
            if path and not (root / path).exists():
                fail(errors, f"plugin.toml references missing skill path: {path}")
        for server in data.get("mcp_servers", []):
            path = server.get("path")
            if path and not (root / path).exists():
                fail(errors, f"plugin.toml references missing MCP path: {path}")
    except Exception as exc:  # noqa: BLE001
        fail(errors, f"TOML parse failed: plugin.toml: {exc}")

    if (root / "skills/constitutional-prompt-framework/SKILL.md").exists():
        check_skill_frontmatter(
            root,
            "skills/constitutional-prompt-framework/SKILL.md",
            "constitutional-prompt-framework",
            errors,
        )
    if (root / "skills/aeriadne-marketplace-operator/SKILL.md").exists():
        check_skill_frontmatter(
            root,
            "skills/aeriadne-marketplace-operator/SKILL.md",
            "aeriadne-marketplace-operator",
            errors,
        )

    check_releaseignore(root, errors)
    check_forbidden_files(root, errors)
    check_privacy_boundary(root, errors)
    check_privacy_smoke(root, errors)
    check_site_prototypes(root, errors)
    check_site_prototype_smoke(root, errors)

    if errors:
        print("Aeriadne package validation: FAIL")
        for item in errors:
            print(f"- {item}")
        return 1

    print("Aeriadne package validation: PASS")
    print(f"root={root}")
    print("skills=aeriadne-marketplace-operator, constitutional-prompt-framework")
    print("mcp=sovereign-bb7 canonical-reference")
    print("copyover=COPYOVER_MANIFEST.md reviewed-gate, .releaseignore enforced")
    print("privacy=privacy_boundary_scan.py enforced")
    print("privacy_smoke=tests/privacy_boundary_scan_smoke.py enforced")
    print("site_prototypes=site_prototype_audit.py enforced")
    print("site_prototypes_smoke=tests/site_prototype_audit_smoke.py enforced")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
