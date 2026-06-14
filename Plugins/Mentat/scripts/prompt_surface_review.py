#!/usr/bin/env python3
"""Review Mentat agent/helper prompt surfaces for release readiness.

Mentat's agents and helpers are independent prompt surfaces, not slash-command
hooks and not Codex skills. This review keeps that boundary explicit: it checks
that each shipped prompt declares a role, tool posture, execution boundaries,
and output contract without trying to execute the prompt.
"""
from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\n(?P<body>.*?)\n---\n(?P<prompt>.*)\Z", re.DOTALL)
FIELD_RE = re.compile(r"^(?P<key>[A-Za-z][A-Za-z0-9_-]*):\s*(?P<value>.*)$")
SAFE_PROMPT_NAME_RE = re.compile(r"^mentat-[a-z][a-z0-9-]*$")
BOUNDARY_TERMS = (
    "do not",
    "don't",
    "never",
    "may not",
    "read-only",
    "read access only",
    "do not write",
    "do not edit",
    "do not modify",
    "not modify",
    "refuse",
)
OUTPUT_TERMS = (
    "output",
    "return",
    "report",
    "produce",
    "writes",
    "write documents",
    "artifact",
    "recommendation",
)
PROCEDURE_TERMS = (
    "procedure",
    "\n1.",
    "\n2.",
    "for every",
)


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str, list[str]]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text, [f"{path.relative_to(path.parent.parent)}: missing frontmatter block"]

    fields: dict[str, list[str]] = {}
    current_key: str | None = None
    errors: list[str] = []
    for line_no, line in enumerate(match.group("body").splitlines(), 2):
        field_match = FIELD_RE.match(line)
        if field_match:
            current_key = field_match.group("key")
            value = field_match.group("value").strip()
            if current_key in fields:
                errors.append(f"{path.name}:{line_no}: duplicate frontmatter key: {current_key}")
            fields[current_key] = [] if value in {"|", ">"} else [value]
            continue
        if current_key and (line.startswith(" ") or line.startswith("\t") or not line.strip()):
            if line.strip():
                fields[current_key].append(line.strip())
            continue
        errors.append(f"{path.name}:{line_no}: invalid frontmatter line: {line}")

    flattened = {key: "\n".join(value).strip() for key, value in fields.items()}
    return flattened, match.group("prompt"), errors


def parse_tools(raw: str) -> list[str]:
    raw = raw.strip()
    if not raw:
        return []
    try:
        value = ast.literal_eval(raw)
    except (SyntaxError, ValueError):
        value = [part.strip().strip("'\"") for part in raw.strip("[]").split(",")]
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def contains_any(text: str, needles: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(needle in lowered for needle in needles)


def expected_role(path: Path) -> str:
    return path.stem.removeprefix("mentat-").replace("-", " ")


def lint_prompt(path: Path, family: str) -> list[str]:
    fields, prompt, errors = parse_frontmatter(path)
    rel = path.relative_to(path.parent.parent).as_posix()
    body = prompt.strip()
    lowered_body = body.lower()
    role = expected_role(path)

    if not SAFE_PROMPT_NAME_RE.match(path.stem):
        errors.append(f"{rel}: prompt filename must be mentat-* kebab-case")
    if fields.get("name", "").strip() != path.stem:
        errors.append(f"{rel}: frontmatter name must match filename stem")
    if not fields.get("description", "").strip():
        errors.append(f"{rel}: missing non-empty description")
    if not parse_tools(fields.get("tools", "")):
        errors.append(f"{rel}: tools list must be present and non-empty")
    if not fields.get("model", "").strip():
        errors.append(f"{rel}: missing model field")
    if not fields.get("maxTurns", "").strip().isdigit():
        errors.append(f"{rel}: maxTurns must be an integer")
    if family == "helper" and not fields.get("when_to_use", "").strip():
        errors.append(f"{rel}: helper prompt must declare when_to_use retrieval signals")

    if "you are" not in lowered_body or role not in lowered_body:
        errors.append(f"{rel}: body must explicitly declare the operator role")
    if not contains_any(body, PROCEDURE_TERMS):
        errors.append(f"{rel}: body must include an operational procedure")
    if not contains_any(body, BOUNDARY_TERMS):
        errors.append(f"{rel}: body must declare write/tool/scope boundaries")
    if not contains_any(body, OUTPUT_TERMS):
        errors.append(f"{rel}: body must declare an output or report contract")

    tools = set(parse_tools(fields.get("tools", "")))
    can_write = {"Write", "Edit"} & tools
    if can_write and not any(term in lowered_body for term in ("doc", "release", "notes", "artifact")):
        errors.append(f"{rel}: Write/Edit prompts must constrain their writable artifact lane")
    if "Bash" in tools and not any(term in lowered_body for term in ("run", "command", "smoke", "do not", "never")):
        errors.append(f"{rel}: Bash-enabled prompts must explain command posture")

    return errors


def lint_helper_index(path: Path) -> list[str]:
    rel = path.relative_to(path.parent.parent).as_posix()
    text = path.read_text(encoding="utf-8")
    lowered = text.lower()
    errors: list[str] = []
    if not text.startswith("# "):
        errors.append(f"{rel}: helper index must start with a markdown title")
    for helper in ("mentat-medic", "mentat-quartermaster", "mentat-conductor"):
        if helper not in lowered:
            errors.append(f"{rel}: helper index must list {helper}")
    if "user scope" not in lowered or "plugin scope" not in lowered:
        errors.append(f"{rel}: helper index must preserve user-scope/plugin-scope distinction")
    if "operator-grade" not in lowered or "user-facing" not in lowered:
        errors.append(f"{rel}: helper index must distinguish helper and shipped operator surfaces")
    return errors


def prompt_files(root: Path) -> tuple[list[Path], list[Path], list[Path]]:
    agent_files = sorted((root / "agents").glob("mentat-*.md"))
    helper_files = sorted((root / "helpers").glob("mentat-*.md"))
    index_files = [root / "helpers" / "HELPERS.md"]
    return agent_files, helper_files, [path for path in index_files if path.exists()]


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Mentat plugin root")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not (root / "agents").is_dir() or not (root / "helpers").is_dir():
        print(f"ERROR: agents/helpers directories not found under {root}", file=sys.stderr)
        return 2

    agent_files, helper_files, index_files = prompt_files(root)
    errors: list[str] = []
    if not agent_files:
        errors.append("no agent prompt files found")
    if not helper_files:
        errors.append("no helper prompt files found")
    if not index_files:
        errors.append("missing helpers/HELPERS.md")

    for path in agent_files:
        errors.extend(lint_prompt(path, "agent"))
    for path in helper_files:
        errors.extend(lint_prompt(path, "helper"))
    for path in index_files:
        errors.extend(lint_helper_index(path))

    if errors:
        print("Mentat prompt surface review: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Mentat prompt surface review: PASS")
    print(f"prompts={len(agent_files) + len(helper_files)}")
    print(f"indexes={len(index_files)}")
    print("policy=frontmatter-role-boundary-output-checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
