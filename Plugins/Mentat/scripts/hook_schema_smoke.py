#!/usr/bin/env python3
"""Smoke-test Mentat hook JSON output contracts.

This covers the Codex/Claude compatibility edge where additionalContext output
must include hookSpecificOutput.hookEventName, while unsupported events must
emit nothing instead of invalid JSON.
"""

from __future__ import annotations

import importlib.util
import io
import json
import sys
from pathlib import Path
from types import ModuleType


PLUGIN_ROOT = Path(__file__).resolve().parent.parent


def load_module(name: str, path: Path) -> ModuleType:
    if str(PLUGIN_ROOT) not in sys.path:
        sys.path.insert(0, str(PLUGIN_ROOT))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"could not load module spec for {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def capture_stdout(fn, *args) -> str:
    previous = sys.stdout
    buffer = io.StringIO()
    try:
        sys.stdout = buffer
        fn(*args)
        return buffer.getvalue()
    finally:
        sys.stdout = previous


def feed_stdin(fn, raw: str) -> dict:
    previous = sys.stdin
    try:
        sys.stdin = io.StringIO(raw)
        return fn()
    finally:
        sys.stdin = previous


def parse_context_output(raw: str, expected_event: str, expected_text: str | None = None) -> dict:
    if not raw.strip():
        raise AssertionError(f"expected JSON output for {expected_event}, got empty stdout")
    data = json.loads(raw)
    hook_output = data.get("hookSpecificOutput")
    if not isinstance(hook_output, dict):
        raise AssertionError(f"missing hookSpecificOutput for {expected_event}: {data}")
    if hook_output.get("hookEventName") != expected_event:
        raise AssertionError(f"wrong hookEventName: {hook_output}")
    if "additionalContext" not in hook_output:
        raise AssertionError(f"missing additionalContext for {expected_event}: {hook_output}")
    if expected_text is not None and hook_output["additionalContext"] != expected_text:
        raise AssertionError(f"wrong additionalContext text: {hook_output}")
    return hook_output


def check_writer(module: ModuleType, writer_name: str) -> None:
    writer = getattr(module, writer_name)

    explicit = capture_stdout(writer, "session boot", "SessionStart")
    parse_context_output(explicit, "SessionStart", "session boot")

    payload = feed_stdin(module.read_payload, '{"hook_event_name":"UserPromptSubmit"}')
    if payload.get("hook_event_name") != "UserPromptSubmit":
        raise AssertionError(f"snake-case payload did not round-trip: {payload}")
    inferred = capture_stdout(writer, "prompt hint")
    parse_context_output(inferred, "UserPromptSubmit", "prompt hint")

    payload = feed_stdin(module.read_payload, '{"hookEventName":"PostToolUse"}')
    if payload.get("hookEventName") != "PostToolUse":
        raise AssertionError(f"camel-case payload did not round-trip: {payload}")
    inferred_camel = capture_stdout(writer, "post tool hint")
    parse_context_output(inferred_camel, "PostToolUse", "post tool hint")

    unsupported = capture_stdout(writer, "must not leak", "Stop")
    if unsupported != "":
        raise AssertionError(f"unsupported Stop event emitted stdout: {unsupported!r}")

    feed_stdin(module.read_payload, '["not", "a", "dict"]')
    cleared = capture_stdout(writer, "must not infer")
    if cleared != "":
        raise AssertionError(f"non-dict payload did not clear inferred event: {cleared!r}")

    long_text = "x" * (module.CONTEXT_INJECTION_BYTE_CAP + 100)
    long_raw = capture_stdout(writer, long_text, "SessionStart")
    hook_output = parse_context_output(long_raw, "SessionStart")
    if len(hook_output["additionalContext"]) > module.CONTEXT_INJECTION_BYTE_CAP:
        raise AssertionError("truncated additionalContext still exceeds cap")


def main() -> int:
    root_hooks = load_module("mentat_root_hooks_lib_schema_smoke", PLUGIN_ROOT / "hooks" / "_lib.py")
    codex_hooks = load_module(
        "mentat_codex_hooks_lib_schema_smoke",
        PLUGIN_ROOT / "adapters" / "codex" / "hooks" / "_lib.py",
    )

    check_writer(root_hooks, "write_user_message")
    check_writer(codex_hooks, "write_additional_context")
    print("PASSED - hook schema output smoke green")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
