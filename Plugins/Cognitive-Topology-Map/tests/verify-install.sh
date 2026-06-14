#!/usr/bin/env bash
set -euo pipefail

PASS=0
FAIL=0

check() {
    local label="$1"; shift
    if "$@" >/dev/null 2>&1; then
        echo "OK:   $label"
        ((PASS++)) || true
    else
        echo "FAIL: $label"
        ((FAIL++)) || true
    fi
}

echo "=== CTMv3 Install Verification ==="

check "ctmv3 engine importable" python3 -m ctmv3 version
check "ctmv3 boot command present" python3 -m ctmv3 boot --help
check "ctmv3 activate command present" python3 -m ctmv3 activate --help
check "ctmv3 state command present" python3 -m ctmv3 state --help
check "claude CLI present" which claude

echo ""
echo "Results: $PASS passed, $FAIL failed"
[[ $FAIL -eq 0 ]]
