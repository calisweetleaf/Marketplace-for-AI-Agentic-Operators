#!/usr/bin/env python3
"""Regression smoke test for Mentat prompt-surface review."""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import prompt_surface_review as review  # noqa: E402


VALID_FRONTMATTER = """---
name: mentat-cartographer
description: |
  Maps a repository and returns a structural inventory.
tools: ["Read", "Grep", "Glob", "LS"]
model: inherit
maxTurns: 10
---

You are Cartographer. Your job is mapping, not editing.

Procedure:

1. Read the project entry files.
2. Produce a markdown report with source-grounded findings.

Do not write code, edit files, or run commands. Output is a report.
"""


VALID_HELPER = """---
name: mentat-medic
description: |
  Diagnoses Mentat plugin failures and returns a triage report.
when_to_use: |
  Use for Mentat errors, hook logs, or smoke failures.
tools: ["Read", "Grep", "Glob", "LS", "Bash"]
model: inherit
maxTurns: 15
---

You are Medic. Your job is diagnosis.

Procedure:

1. Run the smoke command.
2. Return a triage report.

Read access only. Do not modify files. Never patch from this helper.
"""


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def assert_error(errors: list[str], needle: str) -> None:
    if not any(needle in error for error in errors):
        raise AssertionError(f"expected {needle!r} in {errors!r}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="mentat-prompt-review-") as tmp:
        root = Path(tmp)
        agent = write(root / "agents" / "mentat-cartographer.md", VALID_FRONTMATTER)
        helper = write(root / "helpers" / "mentat-medic.md", VALID_HELPER)
        index = write(
            root / "helpers" / "HELPERS.md",
            "# Mentat Helpers\n\n"
            "These user scope helpers are separate from plugin scope operators.\n"
            "- mentat-medic\n- mentat-quartermaster\n- mentat-conductor\n\n"
            "They are operator-grade helpers, not the user-facing plugin agents.\n",
        )

        valid_errors = []
        valid_errors.extend(review.lint_prompt(agent, "agent"))
        valid_errors.extend(review.lint_prompt(helper, "helper"))
        valid_errors.extend(review.lint_helper_index(index))
        if valid_errors:
            raise AssertionError(f"valid prompt surfaces failed: {valid_errors!r}")

        missing_boundary = write(
            root / "agents" / "mentat-scribe.md",
            VALID_FRONTMATTER.replace("mentat-cartographer", "mentat-scribe")
            .replace("Cartographer", "Scribe")
            .replace("Do not write code, edit files, or run commands. Output is a report.", "Output is a report."),
        )
        assert_error(review.lint_prompt(missing_boundary, "agent"), "boundaries")

        missing_output = write(
            root / "agents" / "mentat-sentinel.md",
            VALID_FRONTMATTER.replace("mentat-cartographer", "mentat-sentinel")
            .replace("Cartographer", "Sentinel")
            .replace("2. Produce a markdown report with source-grounded findings.", "2. Read the requested files.")
            .replace("Output is a report.", "Do not modify files."),
        )
        assert_error(review.lint_prompt(missing_output, "agent"), "output")

        helper_without_trigger = write(
            root / "helpers" / "mentat-quartermaster.md",
            VALID_HELPER.replace("mentat-medic", "mentat-quartermaster").replace(
                "when_to_use: |\n  Use for Mentat errors, hook logs, or smoke failures.\n",
                "",
            ),
        )
        assert_error(review.lint_prompt(helper_without_trigger, "helper"), "when_to_use")

        bad_index = write(root / "helpers" / "HELPERS.md", "# Mentat Helpers\n\n- mentat-medic\n")
        assert_error(review.lint_helper_index(bad_index), "mentat-quartermaster")

    print("prompt_surface_review_smoke: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
