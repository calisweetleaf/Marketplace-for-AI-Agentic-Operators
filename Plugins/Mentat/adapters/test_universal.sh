#!/usr/bin/env bash
# Mentat — adapter smoke test.
#
# Validates:
#   1. Every adapter Python file compiles clean (py_compile).
#   2. install_universal.sh --dry-run runs without error for each runtime.
#   3. The Codex hooks.json and Gemini hooks/hooks.json are valid JSON.
#   4. The Gemini gemini-extension.json is valid JSON.
#
# No third-party deps. Exits non-zero on the first failure.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ADAPTERS="$PLUGIN_ROOT/adapters"

pass() { printf "  ok    %s\n" "$*"; }
fail() { printf "  FAIL  %s\n" "$*" >&2; exit 1; }
heading() { printf "\n== %s ==\n" "$*"; }

# ---- Python compile -------------------------------------------------------
heading "compile: codex hooks"
CODEX_HOOKS=(
    "$ADAPTERS/codex/hooks/_lib.py"
    "$ADAPTERS/codex/hooks/session_start.py"
    "$ADAPTERS/codex/hooks/user_prompt_submit.py"
    "$ADAPTERS/codex/hooks/pre_tool_use.py"
    "$ADAPTERS/codex/hooks/post_tool_use.py"
    "$ADAPTERS/codex/hooks/permission_request.py"
    "$ADAPTERS/codex/hooks/stop.py"
)
for f in "${CODEX_HOOKS[@]}"; do
    [[ -f "$f" ]] || fail "missing: $f"
    python3 -c "import py_compile, sys; py_compile.compile(r'$f', doraise=True)" \
        || fail "compile failed: $f"
    pass "$(basename "$f")"
done

heading "compile: gemini hooks"
GEMINI_HOOKS=(
    "$ADAPTERS/gemini/hooks/_lib.py"
    "$ADAPTERS/gemini/hooks/session_start.py"
    "$ADAPTERS/gemini/hooks/session_end.py"
    "$ADAPTERS/gemini/hooks/before_agent.py"
    "$ADAPTERS/gemini/hooks/after_agent.py"
    "$ADAPTERS/gemini/hooks/before_model.py"
    "$ADAPTERS/gemini/hooks/after_model.py"
    "$ADAPTERS/gemini/hooks/before_tool_selection.py"
    "$ADAPTERS/gemini/hooks/before_tool.py"
    "$ADAPTERS/gemini/hooks/after_tool.py"
    "$ADAPTERS/gemini/hooks/pre_compress.py"
    "$ADAPTERS/gemini/hooks/notification.py"
)
for f in "${GEMINI_HOOKS[@]}"; do
    [[ -f "$f" ]] || fail "missing: $f"
    python3 -c "import py_compile, sys; py_compile.compile(r'$f', doraise=True)" \
        || fail "compile failed: $f"
    pass "$(basename "$f")"
done

# ---- JSON validity --------------------------------------------------------
heading "json: hook / manifest files"
JSON_FILES=(
    "$ADAPTERS/codex/hooks.json"
    "$ADAPTERS/gemini/hooks/hooks.json"
    "$ADAPTERS/gemini/gemini-extension.json"
)
for f in "${JSON_FILES[@]}"; do
    [[ -f "$f" ]] || fail "missing: $f"
    python3 -c "import json,sys; json.load(open(r'$f'))" \
        || fail "json invalid: $f"
    pass "$(basename "$f")"
done

# ---- Installer dry-run ----------------------------------------------------
heading "installer: dry-run scenarios"
"$ADAPTERS/install_universal.sh" --dry-run --all >/dev/null \
    || fail "install_universal.sh --dry-run --all"
pass "install_universal.sh --dry-run --all"

"$ADAPTERS/install_universal.sh" --dry-run --codex >/dev/null \
    || fail "install_universal.sh --dry-run --codex"
pass "install_universal.sh --dry-run --codex"

"$ADAPTERS/install_universal.sh" --dry-run --gemini >/dev/null \
    || fail "install_universal.sh --dry-run --gemini"
pass "install_universal.sh --dry-run --gemini"

"$ADAPTERS/install_universal.sh" --dry-run --claude >/dev/null \
    || fail "install_universal.sh --dry-run --claude"
pass "install_universal.sh --dry-run --claude"

# ---- Installer copy hygiene -----------------------------------------------
heading "installer: temp codex copy hygiene"
TMP_HOME="$(mktemp -d)"
cleanup_tmp_home() { rm -rf "$TMP_HOME"; }
trap cleanup_tmp_home EXIT

HOME="$TMP_HOME" "$ADAPTERS/install_universal.sh" \
    --plugin-root "$PLUGIN_ROOT" --codex >/dev/null \
    || fail "install_universal.sh --plugin-root <root> --codex in temp HOME"

INSTALLED="$TMP_HOME/.codex/plugins/mentat"
[[ -d "$INSTALLED" ]] || fail "missing installed plugin root: $INSTALLED"

REQUIRED_INSTALLED=(
    ".releaseignore"
    ".claude-plugin/plugin.json"
    ".mcp.json"
    "adapters/install_universal.sh"
    "scripts/hook_schema_smoke.py"
    "state_machine/machine.py"
)
for rel in "${REQUIRED_INSTALLED[@]}"; do
    [[ -e "$INSTALLED/$rel" ]] || fail "installed copy missing: $rel"
    pass "installed: $rel"
done

FORBIDDEN_INSTALLED=(
    ".mentat"
    "mentat-plugin.tar.gz"
    "mentat-v2.zip"
    "filetree-6-13.md"
    "6-11-2026 Task"
    "hooks/_lib.py.backup_hook_schema_20260603_1530"
    "adapters/codex/hooks/_lib.py.backup_hook_schema_20260603_1530"
)
for rel in "${FORBIDDEN_INSTALLED[@]}"; do
    [[ ! -e "$INSTALLED/$rel" ]] || fail "staging artifact copied: $rel"
    pass "not copied: $rel"
done

[[ -f "$TMP_HOME/.codex/hooks.json" ]] || fail "missing rendered Codex hooks.json"
python3 -c "import json; json.load(open(r'$TMP_HOME/.codex/hooks.json'))" \
    || fail "rendered Codex hooks.json invalid"
pass "rendered Codex hooks.json"

# ---- Snippet line caps ----------------------------------------------------
heading "snippet: line caps (≤ 80)"
for snip in \
    "$ADAPTERS/codex/AGENTS.snippet.md" \
    "$ADAPTERS/gemini/GEMINI.snippet.md"
do
    [[ -f "$snip" ]] || fail "missing: $snip"
    n=$(wc -l < "$snip")
    if [[ $n -gt 80 ]]; then
        fail "$(basename "$snip") is $n lines (> 80)"
    fi
    pass "$(basename "$snip") ($n lines)"
done

printf "\nall adapter smoke tests passed.\n"
