# Upload Code Script — Working

## Goal

Create a shell script that uploads every Python sample file from
`src/kits/base-two-button-strip/` onto a connected Raspberry Pi Pico
using `mpremote`, so the kit can be flashed in a single command rather
than copying files one at a time.

## Result

[`src/kits/base-two-button-strip/upload-code.sh`](../src/kits/base-two-button-strip/upload-code.sh)
successfully copied all 48 `.py` files to the Pico in one run.

## What the Script Does

1. Resolves its own directory so it can be invoked from anywhere.
2. Verifies `mpremote` is installed.
3. Detects a connected Pico by scanning for `/dev/cu.usbmodem*` or
   `/dev/tty.usbmodem*` serial devices.
4. Sends a `soft-reset` to free the REPL in case a script is already
   running on the Pico.
5. Globs every `*.py` in the kit directory and copies each one to the
   Pico's root with `mpremote connect auto cp`.
6. Runs `mpremote connect auto ls` so the user can confirm the files
   landed on the device.

## Issue Encountered and Fix

The first version used `mpremote connect auto eval "1+1"` as a liveness
probe. That failed on the user's machine even though the Pico was
clearly present at `/dev/cu.usbmodem1101`. The likely cause: a script
(probably `main.py`) was already running on the Pico and holding the
REPL, so `eval` could not get a response.

The fix swapped the probe for a serial-device file check
(`/dev/cu.usbmodem*`) and added a `soft-reset` before copying. Both
changes make the script robust to a Pico that boots into a running
program.

## Verified Output (Summary)

- 48 files uploaded in a single run.
- `mpremote ls` on the Pico afterward showed all 48 files plus the
  existing `main.py` (655 bytes) that was already on the device.
- Largest files copied: `main-demo-cycle.py` (10,356 bytes),
  `main-old.py` (8,483 bytes), `auto-cycle.py` (8,065 bytes),
  `60-pixel-demo.py` (6,974 bytes), `25-modes.py` (6,878 bytes).

## Notes for Future Cleanup

The kit directory currently contains several `* copy.py` duplicates
(`06-color-wipe copy.py`, `17-ripple copy.py`, `21-larson-scanner copy.py`,
`22-random-bounce copy.py`) and a `main-old.py`. These were uploaded
along with everything else. If they are stale, deleting them from the
source directory before running the script will keep the Pico's
filesystem clean.
