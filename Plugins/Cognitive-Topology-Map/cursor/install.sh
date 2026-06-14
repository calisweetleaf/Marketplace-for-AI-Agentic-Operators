#!/usr/bin/env bash
# CTMv3 Cursor adapter installer
#
# Usage:
#   bash install.sh            # project scope: installs to .cursor/ in $PWD
#   bash install.sh global     # global scope: installs to ~/.cursor/
#
# The adapter installs:
#   .cursor/rules/ctmv3.mdc       -- Cursor Rules: CTMv3 cognitive doctrine
#   .cursor/commands/ctmv3-*.md   -- Cursor Commands: one per CTMv3 subcommand
#   .cursor/scripts/ctmv3/        -- Bash wrappers that shell out to python3 -m ctmv3
#
# Idempotent: running the installer twice overwrites existing files but does not
# corrupt any non-CTMv3 .cursor/ content.
#
# After installing, restart Cursor for rules and commands to take effect.

set -euo pipefail

# -----------------------------------------------------------------------
# Helper: verify source exists, then copy; exit clearly on any failure
# -----------------------------------------------------------------------
safe_cp() {
    local src="$1"
    local dest="$2"
    if [ ! -e "$src" ]; then
        echo "ERROR: source file not found: $src" >&2
        exit 1
    fi
    cp "$src" "$dest" || { echo "ERROR: failed to copy $src to $dest" >&2; exit 1; }
}

SCOPE="${1:-project}"

if [ "$SCOPE" = "global" ]; then
    TARGET="$HOME/.cursor"
else
    TARGET="$PWD/.cursor"
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CURSOR_SRC="${SCRIPT_DIR}/.cursor"

# -----------------------------------------------------------------------
# Global-scope confirmation prompt
# -----------------------------------------------------------------------
if [ "$SCOPE" = "global" ]; then
    echo "Installing to ~/.cursor/ — continue? [y/N]"
    read -r _confirm
    case "$_confirm" in
        [yY]|[yY][eE][sS]) ;;
        *)
            echo "Aborted."
            exit 0
            ;;
    esac
fi

echo "Installing CTMv3 Cursor adapter to: $TARGET (scope: $SCOPE)"

# -----------------------------------------------------------------------
# Create target directories
# -----------------------------------------------------------------------
mkdir -p "$TARGET/rules" \
    || { echo "ERROR: failed to create $TARGET/rules" >&2; exit 1; }
mkdir -p "$TARGET/commands" \
    || { echo "ERROR: failed to create $TARGET/commands" >&2; exit 1; }
mkdir -p "$TARGET/scripts/ctmv3" \
    || { echo "ERROR: failed to create $TARGET/scripts/ctmv3" >&2; exit 1; }

# -----------------------------------------------------------------------
# Install Cursor Rule
# -----------------------------------------------------------------------
echo "  -> rules/ctmv3.mdc"
safe_cp "$CURSOR_SRC/rules/ctmv3.mdc" "$TARGET/rules/"

# -----------------------------------------------------------------------
# Install Cursor Commands
# -----------------------------------------------------------------------
echo "  -> commands/ctmv3-*.md"
_found_commands=0
for cmd_file in "$CURSOR_SRC/commands"/ctmv3-*.md; do
    # Guard against a literal glob string when no files match
    [ -e "$cmd_file" ] || { echo "ERROR: no ctmv3-*.md command files found in $CURSOR_SRC/commands/" >&2; exit 1; }
    filename="$(basename "$cmd_file")"
    echo "     $filename"
    safe_cp "$cmd_file" "$TARGET/commands/"
    _found_commands=$(( _found_commands + 1 ))
done
if [ "$_found_commands" -eq 0 ]; then
    echo "ERROR: no ctmv3-*.md command files found in $CURSOR_SRC/commands/" >&2
    exit 1
fi

# -----------------------------------------------------------------------
# Install bash wrappers
# -----------------------------------------------------------------------
echo "  -> scripts/ctmv3/"
_found_scripts=0
for script_file in "$SCRIPT_DIR/scripts"/ctmv3-*.sh; do
    [ -e "$script_file" ] || { echo "ERROR: no ctmv3-*.sh script files found in $SCRIPT_DIR/scripts/" >&2; exit 1; }
    filename="$(basename "$script_file")"
    echo "     $filename"
    safe_cp "$script_file" "$TARGET/scripts/ctmv3/"
    chmod +x "$TARGET/scripts/ctmv3/$filename" \
        || { echo "ERROR: failed to chmod +x $TARGET/scripts/ctmv3/$filename" >&2; exit 1; }
    _found_scripts=$(( _found_scripts + 1 ))
done
if [ "$_found_scripts" -eq 0 ]; then
    echo "ERROR: no ctmv3-*.sh script files found in $SCRIPT_DIR/scripts/" >&2
    exit 1
fi

echo ""
echo "Installation complete."
echo ""
echo "Restart Cursor for rules and commands to take effect."
echo ""
echo "Verify Python engine is installed:"
if python3 -m ctmv3 version 2>/dev/null; then
    echo "  ctmv3 engine: OK"
else
    echo "  ctmv3 engine: NOT FOUND"
    echo "  Install the engine before using CTMv3 commands."
    echo "  pip install -e /path/to/ctmv3-plugin/core/"
fi
echo ""
echo "Test with:"
echo "  bash $TARGET/scripts/ctmv3/ctmv3-status.sh"
