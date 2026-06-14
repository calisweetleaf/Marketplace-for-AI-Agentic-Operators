#!/usr/bin/env python3
"""Lint Mentat slash-command prompt frontmatter.

Claude Code command files are lightweight markdown prompts with YAML-ish
frontmatter. This linter intentionally stays stdlib-only and validates the
metadata conventions Mentat relies on for safe command execution.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\n(?P<body>.*?)\n---\n(?P<prompt>.*)\Z", re.DOTALL)
LIVE_SHELL_RE = re.compile(r"!\s*`(?P<command>[^`]+)`")
SAFE_COMMAND_NAME_RE = re.compile(r"^[a-z][a-z0-9-]*$")
FIELD_RE = re.compile(r"^(?P<key>[a-z][a-z0-9-]*):\s*(?P<value>.*)$")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str, list[str]]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text, [f"{path.name}: missing frontmatter block"]

    fields: dict[str, str] = {}
    errors: list[str] = []
    for line_no, line in enumerate(match.group("body").splitlines(), 2):
        if not line.strip():
            continue
        field_match = FIELD_RE.match(line)
        if not field_match:
            errors.append(f"{path.name}:{line_no}: invalid frontmatter line: {line}")
            continue
        key = field_match.group("key")
        value = field_match.group("value").strip()
        if key in fields:
            errors.append(f"{path.name}:{line_no}: duplicate frontmatter key: {key}")
        fields[key] = value
    return fields, match.group("prompt"), errors


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def lint_allowed_tools(path: Path, value: str, live_commands: list[str]) -> list[str]:
    errors: list[str] = []
    raw = strip_quotes(value)
    if not raw.strip():
        errors.append(f"{path.name}: allowed-tools must not be empty")
        return errors
    if "Bash(*)" in raw or "Bash(*" in raw:
        errors.append(f"{path.name}: allowed-tools must not wildcard Bash")
    if live_commands and "Bash(" not in raw:
        errors.append(f"{path.name}: live shell injection requires scoped Bash(...) allowed-tools")
    for item in re.findall(r"Bash\(([^)]*)\)", raw):
        if not item.strip():
            errors.append(f"{path.name}: empty Bash(...) allowed-tools entry")
        if item.strip() == "*":
            errors.append(f"{path.name}: Bash(*) is forbidden")
    return errors


def lint_command(path: Path) -> list[str]:
    fields, prompt, errors = parse_frontmatter(path)
    name = path.stem
    if not SAFE_COMMAND_NAME_RE.match(name):
        errors.append(f"{path.name}: command filename must be kebab-case")

    description = strip_quotes(fields.get("description", "")).strip()
    if not description:
        errors.append(f"{path.name}: missing non-empty description")

    uses_arguments = "$ARGUMENTS" in prompt
    has_argument_hint = bool(strip_quotes(fields.get("argument-hint", "")).strip())
    if uses_arguments and not has_argument_hint:
        errors.append(f"{path.name}: uses $ARGUMENTS but lacks argument-hint")
    if has_argument_hint and not uses_arguments:
        errors.append(f"{path.name}: declares argument-hint but does not reference $ARGUMENTS")

    live_commands = [match.group("command").strip() for match in LIVE_SHELL_RE.finditer(prompt)]
    if live_commands and "allowed-tools" not in fields:
        errors.append(f"{path.name}: live shell injection requires allowed-tools")
    if "allowed-tools" in fields:
        errors.extend(lint_allowed_tools(path, fields["allowed-tools"], live_commands))

    unknown_fields = set(fields) - {"description", "argument-hint", "allowed-tools"}
    for key in sorted(unknown_fields):
        errors.append(f"{path.name}: unknown frontmatter key: {key}")

    return errors


def command_files(root: Path) -> list[Path]:
    commands = root / "commands"
    return sorted(path for path in commands.glob("*.md") if path.name != "README.md")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Mentat plugin root")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not (root / "commands").is_dir():
        print(f"ERROR: commands directory not found under {root}", file=sys.stderr)
        return 2

    errors: list[str] = []
    files = command_files(root)
    if not files:
        errors.append("no command files found")
    for path in files:
        errors.extend(lint_command(path))

    if errors:
        print("Mentat command frontmatter lint: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Mentat command frontmatter lint: PASS")
    print(f"commands={len(files)}")
    print("policy=description-required, scoped-shell-tools, argument-hints-checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
