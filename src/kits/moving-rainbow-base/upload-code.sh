#!/usr/bin/env bash
# Upload all sample code from this directory to a connected Raspberry Pi Pico
# using mpremote. Run from within this directory or from anywhere — the script
# resolves its own location.
#
# Usage:
#   ./upload-code.sh            Upload all .py files, leaving anything else
#                                already on the Pico untouched.
#   ./upload-code.sh --clean    Erase EVERYTHING on the Pico first (all
#                                files and folders, including anything not
#                                part of this kit), then upload fresh.

set -euo pipefail

CLEAN=0
for arg in "$@"; do
    case "$arg" in
        --clean)
            CLEAN=1
            ;;
        *)
            echo "Error: unknown option '$arg'" >&2
            echo "Usage: $0 [--clean]" >&2
            exit 1
            ;;
    esac
done

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

if (( CLEAN )); then
    echo ""
    echo "WARNING: --clean will permanently delete ALL files and folders"
    echo "currently on the Pico, including anything not part of this kit"
    echo "(like a student's own saved projects)."
    read -r -p "Type 'yes' to erase the Pico and continue: " confirm
    if [[ "$confirm" != "yes" ]]; then
        echo "Aborted. Nothing was deleted or uploaded." >&2
        exit 1
    fi

    echo "Erasing everything on the Pico..."
    mpremote connect auto exec "
import os

def remove(path):
    try:
        if os.stat(path)[0] & 0x4000:  # bit set means this is a directory
            for child in os.listdir(path):
                remove(path + '/' + child)
            os.rmdir(path)
        else:
            os.remove(path)
    except OSError:
        pass

for name in os.listdir('/'):
    remove('/' + name)
"
    echo "Pico is now empty."
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
