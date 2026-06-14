#!/usr/bin/env python3
"""Scan Mentat release-candidate text for private boundary leaks.

The scanner respects `.releaseignore`, so local staging evidence can remain in
the working tree without entering the public copy candidate. It avoids embedding
private archive names and instead checks generic leak shapes.
"""
from __future__ import annotations

import argparse
import fnmatch
import re
import sys
from dataclasses import dataclass
from pathlib import Path

DEFAULT_ALLOWED_PATH_PREFIXES = (
    "/home/daeron/Projects/Modern-ML/Plugins/Mentat",
    "/home/daeron/Projects/Modern-ML/Plugins/Cognitive-Topology-Map",
    "/home/daeron/Repositories/Somnus-Intellligence-Stack/Plugins/Mentat",
    "/home/daeron/Somnus-MCP",
    "/home/daeron/.claude/plugins/mentat",
    "/home/daeron/.claude/plugins/mentat-plugin",
    "/home/daeron/.codex/plugins/mentat",
)

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
    "compact_archive_token": re.compile(r"\b[\w.-]*semantic[\w.-]*archive[\w.-]*\b", re.IGNORECASE),
    "compact_mail_token": re.compile(r"\b[\w.-]*mail[\w.-]*room[\w.-]*\b", re.IGNORECASE),
    "compact_source_token": re.compile(r"\b[\w.-]*golden[\w.-]*path[\w.-]*loop[\w.-]*\b", re.IGNORECASE),
    "compact_codegraph_token": re.compile(r"\b[\w.-]*mcp[\w.-]*logs[\w.-]*codegraph[\w.-]*\b", re.IGNORECASE),
}

SENSITIVE_PATH_COMPONENT_RE = re.compile(
    r"(semantic[^/]*archive|archive[^/]*semantic|whitepapers?|mail[-_. ]?room|"
    r"mcp[-_. ]?logs|codegraph[^/]*(?:log|archive|db))",
    re.IGNORECASE,
)


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
    if not path.exists():
        return []
    rules: list[IgnoreRule] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        rules.append(IgnoreRule(pattern=line, directory=line.endswith("/")))
    return rules


def ignored(rel: str, rules: list[IgnoreRule]) -> bool:
    return any(rule.matches(rel) for rule in rules)


def normalize_path_token(token: str) -> str:
    return token.rstrip(".,:;")


def is_allowed_path(path: str, allowed_prefixes: tuple[str, ...]) -> bool:
    for prefix in allowed_prefixes:
        if path == prefix or path.startswith(prefix.rstrip("/") + "/"):
            return True
    return False


def iter_candidate_text_files(root: Path) -> list[Path]:
    rules = load_releaseignore(root)
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if ignored(rel, rules):
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
                if " " in token:
                    continue
                findings.append(f"{rel}:{line_no}: {label}: {token}")
    return findings


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Mentat staging root")
    parser.add_argument(
        "--allow-prefix",
        action="append",
        default=[],
        help="Additional absolute local path prefix allowed in release-candidate docs",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"ERROR: root does not exist: {root}", file=sys.stderr)
        return 2

    allowed_prefixes = tuple(DEFAULT_ALLOWED_PATH_PREFIXES + tuple(args.allow_prefix))
    findings: list[str] = []
    for path in iter_candidate_text_files(root):
        findings.extend(scan_text(path, root, allowed_prefixes))

    if findings:
        print("Mentat privacy boundary scan: FAIL")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Mentat privacy boundary scan: PASS")
    print(f"root={root}")
    print("policy=release-candidate-files-only, allowlisted-local-roots")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
