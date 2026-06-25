#!/usr/bin/env bash
# Upload all sample code from this directory to a connected Raspberry Pi Pico
# using mpremote. Run from within this directory or from anywhere — the script
# resolves its own location.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if ! command -v mpremote >/dev/null 2>&1; then
    echo "Error: mpremote is not installed. Install with: pip install mpremote" >&2
    exit 1
fi

echo "Checking for connected Pico..."
if ! mpremote connect auto eval "1+1" >/dev/null 2>&1; then
    echo "Error: No Pico detected. Plug it in and try again." >&2
    exit 1
fi

shopt -s nullglob
files=( *.py )
shopt -u nullglob

if (( ${#files[@]} == 0 )); then
    echo "No .py files found in $SCRIPT_DIR" >&2
    exit 1
fi

echo "Uploading ${#files[@]} file(s) to Pico..."
for f in "${files[@]}"; do
    echo "  -> $f"
    mpremote connect auto cp "$f" ":$f"
done

echo "Done. Files on Pico:"
mpremote connect auto ls
