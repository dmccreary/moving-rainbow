# Coding Guidelines

This guide should be used when generating sample code within the documentation
or when generating code for the project kits.

## Key Configuration Pattern

Each kit uses a `config.py` for hardware abstraction that is imported by all lesson files:
```python
# src/led-strip-two-buttons/config.py
NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30
BUTTON_PIN_1 = 15
BUTTON_PIN_2 = 14
```

When creating new MicroPython examples, always `import config` and copy each setting the
program uses into a variable of the same name in one block at the top. Never hard-code a
pin number or the pixel count. Programs in `src/kits/moving-rainbow-base/` all follow this shape:
```python
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BUTTON_PIN_1 = config.BUTTON_PIN_1      # only the settings the program uses
BUTTON_PIN_2 = config.BUTTON_PIN_2
```
Pins that are not in `config.py` (the Pico's built-in LED is pin 25) get a named constant
in the same block, for example `BUILT_IN_LED_PIN = 25`.

The very first lab (`01-blink-onboard-led.py`) is the one exception: it must run before
`config.py` is on the Pico, so it does not import it.

## Lab File Header and Numbering

Labs in `src/kits/moving-rainbow-base/` are numbered sequentially with two digits
(`01-`, `02-`, ... `44-`), with no gaps and no repeats. When a lab is added, removed or
renumbered, also update the file tables in `docs/kits/moving-rainbow-base/index.md`.

Every program starts with this header. The `Filename` line must match the real file name,
and the version starts at `1.0.0`:
```python
# Lab 05: Move a Pixel
# Filename: 05-move.py
# Version: 1.0.0
#
# A single red pixel moves along the strip, one pixel at a time.
```
Programs that are not numbered labs (`main-demo-cycle.py` and similar demos) use
`# Demo Program: <title> (not a numbered lab)` as the first line. `config.py` uses the same
Filename and Version lines.

## Platform-Specific Notes

### MicroPython (Raspberry Pi Pico)
- Uses `neopixel` and `machine` libraries (built into MicroPython)
- Standard pattern: `strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)` (after the config block above)
- Files run directly on Pico via Thonny IDE
- Call `strip.write()` once per animation step, then `sleep()`. Never write, erase, and write
  again with no delay between them: on the Pico the quiet gap between two back-to-back writes
  is only about 150 microseconds, and many WS2812B strips need about 280 to latch a frame, so
  the strip can swallow the second frame. Erase a pixel in memory (`strip[i] = (0,0,0)`) and
  let the next step's `write()` show it. (Labs 05 and 06 showed only the first pixel because
  of this.)

### Pi 500+ Keyboard RGB
- Uses `rpi-keyboard-config` command-line tool and `RPiKeyboardConfig` Python library
- 45 built-in effects (IDs 0-44), 7 preset slots (0-6)
- Key commands: `rpi-keyboard-config effect <id>`, `rpi-keyboard-config preset set <slot> <effect>`
- Keystroke-triggered effects: 29, 31-42 (react to key presses)
- See `src/pi-500-keyboard/cycle-effects.sh` for effect names

### MicroSims Generation
- Use the /microsim-generator skill
- Follow the guidelines in that skill for all MicroSims
- Place browser-based simulations in `docs/sims/`
- Each MicroSim has: `index.md` (documentation), `main.html` (entry point), `sketch.js` (p5.js code)
- Each MicroSim must be listed in the main mkdocs.yml and the /docs/sims/index.md using the mkdocs-material grid-card format

## Lesson File Numbering Convention

Files in `src/led-strip-two-buttons/` follow a progression:
- 01-10: Basics (blink, colors, dimmer, movement)
- 11-20: Patterns (bands, comets, rainbow, candle, theater chase)
- 20-30: Advanced (clock, larson scanner, random bounce)
- 30-40: Button integration
- 50+: Complete demos
