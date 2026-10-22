#!/usr/bin/env bash
# Build the printable Demo Mode Guide for the Tilt-a-Rainbow Mini kit:
# draws each of the 18 modes from the real code, refreshes the pictures and
# QR code in docs/kits/8x8-matrix-accel/demo-mode-guide.html, writes the
# mode grid for the Lab 19 page, and renders demo-mode-guide.pdf (US Letter)
# with the installed Google Chrome.
#
# Requires: pip install segno playwright
# Usage:    scripts/demo-mode-guide/build.sh
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

python3 build-guide.py

echo "Open: $(cd ../../docs/kits/8x8-matrix-accel && pwd)/demo-mode-guide.pdf"
