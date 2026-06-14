#!/usr/bin/env python3
"""Regression smoke test for Mentat command frontmatter lint."""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import command_frontmatter_lint as lint  # noqa: E402


def write_command(root: Path, name: str, text: str) -> Path:
    commands = root / "commands"
    commands.mkdir(parents=True, exist_ok=True)
    path = commands / name
    path.write_text(text, encoding="utf-8")
    return path


def assert_error(path: Path, needle: str) -> None:
    errors = lint.lint_command(path)
    if not any(needle in error for error in errors):
        raise AssertionError(f"expected {needle!r} in {errors!r}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="mentat-command-lint-") as tmp:
        root = Path(tmp)
        valid = write_command(
            root,
            "status.md",
            "---\n"
            "description: Show status\n"
            "allowed-tools: \"Bash(python3 ${CLAUDE_PLUGIN_ROOT}/bin/mentat*)\"\n"
            "---\n\n"
            "!`python3 \"${CLAUDE_PLUGIN_ROOT}/bin/mentat\" status`\n",
        )
        valid_errors = lint.lint_command(valid)
        if valid_errors:
            raise AssertionError(f"valid command failed lint: {valid_errors!r}")

        assert_error(
            write_command(root, "missing-description.md", "---\nargument-hint: \"[x]\"\n---\n\n$ARGUMENTS\n"),
            "missing non-empty description",
        )
        assert_error(
            write_command(root, "missing-hint.md", "---\ndescription: Needs args\n---\n\n$ARGUMENTS\n"),
            "lacks argument-hint",
        )
        assert_error(
            write_command(root, "missing-tools.md", "---\ndescription: Shell\n---\n\n!`echo hi`\n"),
            "requires allowed-tools",
        )
        assert_error(
            write_command(
                root,
                "wildcard.md",
                "---\ndescription: Shell\nallowed-tools: \"Bash(*)\"\n---\n\n!`echo hi`\n",
            ),
            "wildcard Bash",
        )

    print("command_frontmatter_lint_smoke: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
