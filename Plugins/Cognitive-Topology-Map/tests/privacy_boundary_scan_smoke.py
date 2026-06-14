#!/usr/bin/env python3
"""Regression smoke test for CTMv3's release privacy scanner."""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import privacy_boundary_scan as scanner  # noqa: E402


def write_case(root: Path, name: str, text: str) -> Path:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def assert_finding(findings: list[str], label: str) -> None:
    if not any(label in item for item in findings):
        raise AssertionError(f"expected finding containing {label!r}; got {findings!r}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="ctmv3-privacy-smoke-") as tmp:
        root = Path(tmp)
        (root / ".releaseignore").write_text("ignored/\n", encoding="utf-8")

        allowed = write_case(
            root,
            "allowed.md",
            "Known package root: " + "/" + "home/daeron/Projects/Modern-ML/Plugins/Cognitive-Topology-Map\n"
            "Placeholder root: " + "/" + "home/user/projects\n"
            "Human boundary phrase: semantic archive paths stay private.\n",
        )
        ignored = write_case(
            root,
            "ignored/local.md",
            "Ignored path: " + "/" + "home/daeron/private-lab/source.md\n",
        )
        unapproved = write_case(
            root,
            "unapproved.md",
            "Bad path: " + "/" + "home/daeron/private-lab/source.md\n",
        )
        external = write_case(
            root,
            "external.md",
            "Bad media path: " + "/" + "media/daeron/private-drive/source.md\n",
        )
        compact = write_case(
            root,
            "compact.md",
            "Bad compact token: " + "semantic" + "-archive" + "-index\n",
        )
        codegraph = write_case(
            root,
            "codegraph.md",
            "Bad compact token: " + "mcp" + "-logs" + "-codegraph\n",
        )

        candidates = {path.relative_to(root).as_posix() for path in scanner.iter_candidate_text_files(root)}
        if "ignored/local.md" in candidates:
            raise AssertionError(f"ignored file entered candidate set: {sorted(candidates)!r}")

        allowed_findings = scanner.scan_text(allowed, root, scanner.DEFAULT_ALLOWED_PATH_PREFIXES)
        if allowed_findings:
            raise AssertionError(f"allowed case produced findings: {allowed_findings!r}")

        ignored_findings = scanner.scan_text(ignored, root, scanner.DEFAULT_ALLOWED_PATH_PREFIXES)
        if not ignored_findings:
            raise AssertionError("direct scan should still catch ignored file content")

        assert_finding(
            scanner.scan_text(unapproved, root, scanner.DEFAULT_ALLOWED_PATH_PREFIXES),
            "unapproved_local_path",
        )
        assert_finding(
            scanner.scan_text(external, root, scanner.DEFAULT_ALLOWED_PATH_PREFIXES),
            "external_private_path",
        )
        assert_finding(
            scanner.scan_text(compact, root, scanner.DEFAULT_ALLOWED_PATH_PREFIXES),
            "compact_archive_token",
        )
        assert_finding(
            scanner.scan_text(codegraph, root, scanner.DEFAULT_ALLOWED_PATH_PREFIXES),
            "compact_codegraph_token",
        )

    print("privacy_boundary_scan_smoke: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
