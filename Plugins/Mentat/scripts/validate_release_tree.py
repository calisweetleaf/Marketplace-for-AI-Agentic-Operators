#!/usr/bin/env python3
"""Validate Mentat staging tree release/copyover hygiene.

The staging tree may contain local runtime state such as .mentat/, archives,
backup hook libraries, generated filetrees, and task scratch folders. Those are
allowed only when covered by .releaseignore. The candidate release set is every
file not ignored by that file.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


REQUIRED_FILES = [
    "README.md",
    "INSTALL.md",
    "CHANGELOG.md",
    "AGENTS.md",
    "CONTEXT.md",
    "MEMORY.md",
    "PLAN.md",
    "SUBSYSTEM_INVENTORY.md",
    "COPYOVER_MANIFEST.md",
    ".releaseignore",
    ".claude-plugin/plugin.json",
    ".mcp.json",
    "mcp.json",
    "webhooks.json",
    "hooks/hooks.json",
    "state_machine/machine.py",
    "state_machine/q_table.py",
    "state_machine/insights.py",
    "state_machine/session.py",
    "state_machine/drift.py",
    "mcp_server/__main__.py",
    "bin/mentat",
    "bin/mentat-monitors",
    "monitors/monitors.json",
    "scripts/integration_smoke.py",
    "scripts/hook_schema_smoke.py",
    "scripts/command_frontmatter_lint.py",
    "tests/command_frontmatter_lint_smoke.py",
    "scripts/prompt_surface_review.py",
    "tests/prompt_surface_review_smoke.py",
    "scripts/privacy_boundary_scan.py",
    "tests/privacy_boundary_scan_smoke.py",
    "scripts/validate_release_tree.py",
]

JSON_FILES = [
    ".claude-plugin/plugin.json",
    ".mcp.json",
    "mcp.json",
    "webhooks.json",
    "hooks/hooks.json",
    "evals/rubric.json",
    "monitors/monitors.json",
]

FORBIDDEN_PATTERNS = [
    ".git/*",
    ".codegraph/*",
    ".venv/*",
    "venv/*",
    "env/*",
    "ENV/*",
    ".mentat/*",
    ".pytest_cache/*",
    ".mypy_cache/*",
    ".ruff_cache/*",
    "*/__pycache__/*",
    "*.sqlite",
    "*.db",
    "*.db-shm",
    "*.db-wal",
    "*.pid",
    "*.log",
    "*.pyc",
    "*.pyo",
    "*.tmp",
    "*.zip",
    "*.tar.gz",
    "*.tgz",
    "*.tar",
    "*.backup_*",
    "*.metadata.json",
    "filetree-*.md",
    "*filetree*.md",
    "6-11-2026 Task/*",
]


@dataclass(frozen=True)
class IgnoreRule:
    pattern: str
    directory: bool = False

    def matches(self, rel: str) -> bool:
        pattern = self.pattern
        if self.directory:
            prefix = pattern.rstrip("/") + "/"
            return rel == pattern.rstrip("/") or rel.startswith(prefix)
        return fnmatch.fnmatch(rel, pattern) or fnmatch.fnmatch(Path(rel).name, pattern)


def load_releaseignore(root: Path) -> list[IgnoreRule]:
    path = root / ".releaseignore"
    rules: list[IgnoreRule] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        rules.append(IgnoreRule(pattern=line, directory=line.endswith("/")))
    return rules


def ignored(rel: str, rules: list[IgnoreRule]) -> bool:
    return any(rule.matches(rel) for rule in rules)


def forbidden(rel: str) -> bool:
    return any(fnmatch.fnmatch(rel, pat) or fnmatch.fnmatch(Path(rel).name, pat) for pat in FORBIDDEN_PATTERNS)


def validate_json(root: Path, rel: str, errors: list[str]) -> None:
    path = root / rel
    if not path.exists():
        return
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {rel}: {exc}")


def run_validation_command(root: Path, args: list[str], label: str, errors: list[str]) -> None:
    result = subprocess.run(
        args,
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        output = "\n".join(part for part in (result.stdout, result.stderr) if part).strip()
        errors.append(f"{label} failed:\n{output}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Mentat staging root")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    errors: list[str] = []

    if not root.exists() or not root.is_dir():
        print(f"ERROR: root is not a directory: {root}", file=sys.stderr)
        return 2

    releaseignore = root / ".releaseignore"
    if not releaseignore.exists():
        print(f"ERROR: missing .releaseignore at {releaseignore}", file=sys.stderr)
        return 2

    rules = load_releaseignore(root)

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            errors.append(f"missing required release file: {rel}")

    for rel in JSON_FILES:
        validate_json(root, rel, errors)

    candidate_files: list[str] = []
    ignored_forbidden: list[str] = []
    unignored_forbidden: list[str] = []

    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = path.relative_to(root).as_posix()
        is_ignored = ignored(rel, rules)
        is_forbidden = forbidden(rel)
        if is_ignored:
            if is_forbidden:
                ignored_forbidden.append(rel)
            continue
        candidate_files.append(rel)
        if is_forbidden:
            unignored_forbidden.append(rel)

    if unignored_forbidden:
        errors.append("forbidden files would be included in release candidate:")
        errors.extend(f"  {item}" for item in unignored_forbidden)

    run_validation_command(root, [sys.executable, "scripts/privacy_boundary_scan.py", "."], "privacy boundary scan", errors)
    run_validation_command(
        root,
        [sys.executable, "tests/privacy_boundary_scan_smoke.py"],
        "privacy boundary smoke",
        errors,
    )
    run_validation_command(root, [sys.executable, "scripts/command_frontmatter_lint.py", "."], "command frontmatter lint", errors)
    run_validation_command(
        root,
        [sys.executable, "tests/command_frontmatter_lint_smoke.py"],
        "command frontmatter smoke",
        errors,
    )
    run_validation_command(root, [sys.executable, "scripts/prompt_surface_review.py", "."], "prompt surface review", errors)
    run_validation_command(
        root,
        [sys.executable, "tests/prompt_surface_review_smoke.py"],
        "prompt surface smoke",
        errors,
    )

    if errors:
        print("Mentat release tree validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Mentat release tree validation: PASS")
    print(f"root={root}")
    print(f"candidate_files={len(candidate_files)}")
    print(f"ignored_forbidden_files={len(ignored_forbidden)}")
    print("privacy=privacy_boundary_scan.py enforced")
    print("privacy_smoke=tests/privacy_boundary_scan_smoke.py enforced")
    print("commands=command_frontmatter_lint.py enforced")
    print("commands_smoke=tests/command_frontmatter_lint_smoke.py enforced")
    print("prompt_surfaces=prompt_surface_review.py enforced")
    print("prompt_surfaces_smoke=tests/prompt_surface_review_smoke.py enforced")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
