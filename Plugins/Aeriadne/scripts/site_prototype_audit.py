#!/usr/bin/env python3
"""Audit staging-local site prototypes listed by Aeriadne.

The audit makes the preservation rule executable: local HTML/site prototypes
must exist, remain marked local-only until promotion, be excluded by their
owning package's `.releaseignore`, and keep any declared semantic/spec-bearing
content markers intact.
"""
from __future__ import annotations

import argparse
import fnmatch
import html
import json
import re
import sys
from pathlib import Path


REQUIRED_FIELDS = {
    "id",
    "title",
    "owner_package",
    "source_path",
    "releaseignore_path",
    "promotion_status",
    "local_only",
    "public_copyover",
    "preserve",
    "future_surface",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def releaseignore_entries(path: Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def ignored_by_releaseignore(source_path: Path, releaseignore_path: Path) -> bool:
    root = releaseignore_path.parent
    try:
        rel = source_path.relative_to(root).as_posix()
    except ValueError:
        rel = source_path.name
    for entry in releaseignore_entries(releaseignore_path):
        if entry.endswith("/"):
            prefix = entry.rstrip("/") + "/"
            if rel == entry.rstrip("/") or rel.startswith(prefix):
                return True
            continue
        if fnmatch.fnmatch(rel, entry) or fnmatch.fnmatch(source_path.name, entry):
            return True
    return False


def normalized_html_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.lower()


def normalized_marker(marker: str) -> str:
    return re.sub(r"\s+", " ", marker.strip().lower())


def audit_semantic_requirements(item_id: str, item: dict, source_path: Path) -> list[str]:
    errors: list[str] = []
    requirements = item.get("semantic_requirements", [])
    if requirements in (None, []):
        return errors
    if not isinstance(requirements, list):
        return [f"{item_id}: semantic_requirements must be a list"]
    if not source_path.exists():
        return errors

    content = normalized_html_text(source_path)
    for index, requirement in enumerate(requirements):
        prefix = f"{item_id}: semantic_requirements[{index}]"
        if not isinstance(requirement, dict):
            errors.append(f"{prefix}: must be an object")
            continue
        requirement_id = str(requirement.get("id", "")).strip()
        if not requirement_id:
            errors.append(f"{prefix}: id must be non-empty")
        mode = str(requirement.get("mode", "all")).strip().lower()
        if mode not in {"all", "any"}:
            errors.append(f"{prefix}: mode must be all or any")
            continue
        terms = requirement.get("terms")
        if not isinstance(terms, list) or not terms:
            errors.append(f"{prefix}: terms must be a non-empty list")
            continue
        markers = [normalized_marker(str(term)) for term in terms if str(term).strip()]
        if len(markers) != len(terms):
            errors.append(f"{prefix}: terms must all be non-empty strings")
            continue
        missing = [marker for marker in markers if marker not in content]
        if mode == "all" and missing:
            errors.append(
                f"{prefix}: missing required content markers: {', '.join(missing)}"
            )
        elif mode == "any" and len(missing) == len(markers):
            errors.append(
                f"{prefix}: none of the required content markers were found: "
                f"{', '.join(markers)}"
            )
    return errors


def audit_prototype(item: dict, index: int) -> list[str]:
    errors: list[str] = []
    prefix = f"prototypes[{index}]"
    missing = sorted(REQUIRED_FIELDS - set(item))
    for field in missing:
        errors.append(f"{prefix}: missing required field: {field}")
    if missing:
        return errors

    item_id = str(item["id"])
    source_path = Path(str(item["source_path"]))
    releaseignore_path = Path(str(item["releaseignore_path"]))

    if not item_id or any(ch.isspace() for ch in item_id):
        errors.append(f"{item_id or prefix}: id must be non-empty and whitespace-free")
    if item.get("preserve") is not True:
        errors.append(f"{item_id}: preserve must be true")
    if item.get("local_only") is not True:
        errors.append(f"{item_id}: local_only must be true until promoted")
    if item.get("public_copyover") is not False:
        errors.append(f"{item_id}: public_copyover must be false until promoted")
    if item.get("promotion_status") != "staging-local":
        errors.append(f"{item_id}: promotion_status must be staging-local")
    if not str(item.get("future_surface", "")).strip():
        errors.append(f"{item_id}: future_surface must be non-empty")
    if not source_path.exists():
        errors.append(f"{item_id}: source_path does not exist: {source_path}")
    if source_path.suffix.lower() not in {".html", ".htm"}:
        errors.append(f"{item_id}: source_path must be an HTML artifact")
    if not releaseignore_path.exists():
        errors.append(f"{item_id}: releaseignore_path does not exist: {releaseignore_path}")
    elif source_path.exists() and not ignored_by_releaseignore(source_path, releaseignore_path):
        errors.append(f"{item_id}: source_path is not excluded by {releaseignore_path}")
    notes = item.get("notes", [])
    note_text = " ".join(str(note).lower() for note in notes if isinstance(note, str))
    if "do not delete" not in note_text:
        errors.append(f"{item_id}: notes must include a do-not-delete preservation rule")
    if "copyover" not in note_text:
        errors.append(f"{item_id}: notes must describe copyover boundary")
    errors.extend(audit_semantic_requirements(item_id, item, source_path))
    return errors


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Aeriadne plugin root")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    registry_path = root / "registry" / "site_prototypes.json"
    errors: list[str] = []

    if not registry_path.exists():
        print(f"ERROR: missing {registry_path}", file=sys.stderr)
        return 2
    try:
        registry = load_json(registry_path)
    except Exception as exc:  # noqa: BLE001 - audit reports parse failure.
        print(f"ERROR: failed to parse {registry_path}: {exc}", file=sys.stderr)
        return 2

    prototypes = registry.get("prototypes")
    if not isinstance(prototypes, list) or not prototypes:
        errors.append("registry/site_prototypes.json must contain at least one prototype")
    else:
        for index, item in enumerate(prototypes):
            if not isinstance(item, dict):
                errors.append(f"prototypes[{index}]: must be an object")
                continue
            errors.extend(audit_prototype(item, index))

    if errors:
        print("Aeriadne site prototype audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Aeriadne site prototype audit: PASS")
    print(f"prototypes={len(prototypes)}")
    semantic_count = sum(
        len(item.get("semantic_requirements", []))
        for item in prototypes
        if isinstance(item, dict) and isinstance(item.get("semantic_requirements", []), list)
    )
    print(f"semantic_requirements={semantic_count}")
    print(
        "policy=preserve-local-spec-site-artifacts, "
        "semantic-content-enforced, "
        "releaseignore-excluded-until-promoted"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
