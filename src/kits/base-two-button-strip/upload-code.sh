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
# Look for a usbmodem serial device — works even if a script is currently
# running on the Pico and holding the REPL.
shopt -s nullglob
serial_devs=( /dev/cu.usbmodem* /dev/tty.usbmodem* )
shopt -u nullglob
if (( ${#serial_devs[@]} == 0 )); then
    echo "Error: No Pico detected (no /dev/cu.usbmodem* device). Plug it in and try again." >&2
    exit 1
fi
echo "Found device: ${serial_devs[0]}"

# Send Ctrl-C to interrupt any running program before copying files.
mpremote connect auto soft-reset >/dev/null 2>&1 || true

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
