#!/usr/bin/env python3
"""Regression smoke test for Aeriadne site prototype audit."""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import site_prototype_audit as audit  # noqa: E402


def write_registry(root: Path, item: dict) -> None:
    registry = root / "registry" / "site_prototypes.json"
    registry.parent.mkdir(parents=True, exist_ok=True)
    registry.write_text(
        json.dumps({"schema_version": 1, "prototypes": [item]}, indent=2),
        encoding="utf-8",
    )


def assert_error(errors: list[str], needle: str) -> None:
    if not any(needle in error for error in errors):
        raise AssertionError(f"expected {needle!r} in {errors!r}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="aeriadne-site-audit-") as tmp:
        root = Path(tmp)
        source = root / "owner" / "page.html"
        releaseignore = root / "owner" / ".releaseignore"
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text(
            "<!doctype html><title>Prototype</title>"
            "<main>Eight-state FSA with Q-table, insight bus, drift detector, "
            "hook lifecycle, and MCP projection.</main>",
            encoding="utf-8",
        )
        releaseignore.write_text("page.html\n", encoding="utf-8")
        valid = {
            "id": "owner-page",
            "title": "Owner Page",
            "owner_package": "owner",
            "source_path": str(source),
            "releaseignore_path": str(releaseignore),
            "promotion_status": "staging-local",
            "local_only": True,
            "public_copyover": False,
            "preserve": True,
            "future_surface": "linked-doc/site-page",
            "semantic_requirements": [
                {
                    "id": "state-machine-spec",
                    "description": "Prototype must preserve the state-machine spec markers.",
                    "mode": "all",
                    "terms": [
                        "Eight-state FSA",
                        "Q-table",
                        "insight bus",
                        "drift detector",
                        "hook lifecycle",
                        "MCP projection",
                    ],
                }
            ],
            "notes": [
                "Do not delete during cleanup.",
                "Exclude from public copyover until promoted.",
            ],
        }
        write_registry(root, valid)
        errors = audit.audit_prototype(valid, 0)
        if errors:
            raise AssertionError(f"valid prototype failed audit: {errors!r}")

        missing_file = dict(valid, source_path=str(root / "missing.html"))
        assert_error(audit.audit_prototype(missing_file, 0), "source_path does not exist")

        promoted_too_soon = dict(valid, public_copyover=True)
        assert_error(audit.audit_prototype(promoted_too_soon, 0), "public_copyover must be false")

        missing_marker = dict(valid)
        missing_marker["semantic_requirements"] = [
            {
                "id": "missing-marker",
                "description": "Synthetic failure path.",
                "mode": "all",
                "terms": ["not present in the HTML"],
            }
        ]
        assert_error(audit.audit_prototype(missing_marker, 0), "missing required content markers")

        releaseignore.write_text("other.html\n", encoding="utf-8")
        assert_error(audit.audit_prototype(valid, 0), "not excluded")

    print("site_prototype_audit_smoke: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
