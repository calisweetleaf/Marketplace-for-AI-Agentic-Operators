#!/usr/bin/env python3
"""Scan Aeriadne package text for private boundary leaks.

The scanner intentionally avoids embedding private archive names. It enforces a
small allowlist of package/review/control-plane roots and catches generic leak
shapes: unapproved local absolute paths, external media paths, and name-like
tokens that combine sensitive concepts into a private source identifier.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEFAULT_ALLOWED_PATH_PREFIXES = (
    "/home/daeron/Projects/Modern-ML/Plugins",
    "/home/daeron/Projects/Modern-ML/Plugins/Aeriadne",
    "/home/daeron/Projects/Modern-ML/Plugins/Cognitive-Topology-Map",
    "/home/daeron/Projects/Modern-ML/Plugins/Mentat",
    "/home/daeron/Projects/Modern-ML/Plugins/Codex-Config-Topology",
    "/home/daeron/Projects/Modern-ML/Plugins/old/Codex-Config-Topology",
    "/home/daeron/Repositories/Somnus-Intellligence-Stack",
    "/home/daeron/Somnus-MCP",
    "/home/daeron/.codex/skills/custom/constitutional-prompt-framework",
    "/home/daeron/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py",
    "/home/daeron/.codex/skills/.system/skill-creator/scripts/quick_validate.py",
    "/home/daeron/.claude/plugins/marketplaces/local/plugins",
    "/home/daeron/.codex/plugins/cache/local",
)

SKIP_DIRS = {
    ".git",
    ".codegraph",
    ".venv",
    "venv",
    "env",
    "ENV",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}

SKIP_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".db",
    ".sqlite",
    ".sqlite3",
    ".db-shm",
    ".db-wal",
    ".zip",
    ".tar",
    ".tgz",
    ".gz",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".pdf",
}

ABSOLUTE_LOCAL_PATH_RE = re.compile(r"/(?:home|media|mnt|run/media)/[^\s`\"')\]}>]+")

FORBIDDEN_TOKEN_PATTERNS = {
    "compact_private_archive_token": re.compile(r"\b[\w.-]*semantic[\w.-]*archive[\w.-]*\b", re.IGNORECASE),
    "compact_private_mail_token": re.compile(r"\b[\w.-]*mail[\w.-]*room[\w.-]*\b", re.IGNORECASE),
    "compact_private_source_token": re.compile(r"\b[\w.-]*golden[\w.-]*path[\w.-]*loop[\w.-]*\b", re.IGNORECASE),
    "compact_private_codegraph_token": re.compile(r"\b[\w.-]*mcp[\w.-]*logs[\w.-]*codegraph[\w.-]*\b", re.IGNORECASE),
}

SENSITIVE_PATH_COMPONENT_RE = re.compile(
    r"(semantic[^/]*archive|archive[^/]*semantic|whitepapers?|mail[-_. ]?room|"
    r"mcp[-_. ]?logs|codegraph[^/]*(?:log|archive|db))",
    re.IGNORECASE,
)


def normalize_path_token(token: str) -> str:
    return token.rstrip(".,:;")


def is_allowed_path(path: str, allowed_prefixes: tuple[str, ...]) -> bool:
    for prefix in allowed_prefixes:
        if path == prefix or path.startswith(prefix.rstrip("/") + "/"):
            return True
    return False


def iter_text_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if path.suffix in SKIP_SUFFIXES:
            continue
        files.append(path)
    return files


def scan_text(path: Path, root: Path, allowed_prefixes: tuple[str, ...]) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []

    rel = path.relative_to(root).as_posix()
    findings: list[str] = []
    for line_no, line in enumerate(text.splitlines(), 1):
        for match in ABSOLUTE_LOCAL_PATH_RE.finditer(line):
            token = normalize_path_token(match.group(0))
            if is_allowed_path(token, allowed_prefixes):
                continue
            if token.startswith(("/media/", "/mnt/", "/run/media/")):
                findings.append(f"{rel}:{line_no}: external_private_path: {token}")
                continue
            if SENSITIVE_PATH_COMPONENT_RE.search(token):
                findings.append(f"{rel}:{line_no}: sensitive_private_path: {token}")
                continue
            findings.append(f"{rel}:{line_no}: unapproved_local_path: {token}")

        for label, pattern in FORBIDDEN_TOKEN_PATTERNS.items():
            for match in pattern.finditer(line):
                token = match.group(0)
                # Human-facing boundary prose such as "semantic archive paths" is
                # allowed; compact identifier-like tokens are not.
                if " " in token:
                    continue
                findings.append(f"{rel}:{line_no}: {label}: {token}")
    return findings


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Aeriadne plugin root")
    parser.add_argument(
        "--allow-prefix",
        action="append",
        default=[],
        help="Additional absolute local path prefix allowed in package-facing docs",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"ERROR: root does not exist: {root}", file=sys.stderr)
        return 2

    allowed_prefixes = tuple(DEFAULT_ALLOWED_PATH_PREFIXES + tuple(args.allow_prefix))
    findings: list[str] = []
    for path in iter_text_files(root):
        findings.extend(scan_text(path, root, allowed_prefixes))

    if findings:
        print("Aeriadne privacy boundary scan: FAIL")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Aeriadne privacy boundary scan: PASS")
    print(f"root={root}")
    print("policy=allowlisted-local-roots, no private archive/source identifiers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
