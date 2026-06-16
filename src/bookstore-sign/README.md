# Bookstore Sign - Pattern Mode Test

A MicroPython program for the Raspberry Pi Pico that lights up a 134-pixel
**BOOKSTORE** sign with six colorful patterns. Two push buttons switch between
the patterns, and a built-in auto-cycle mode rotates through all of them on its
own.

The main program is [`pattern-mode-test.py`](pattern-mode-test.py).

## Hardware

The sign spells **BOOKSTORE** with one addressable LED strip (WS2812B /
NeoPixel). All hardware settings live in [`config.py`](config.py):

| Setting | Value | Meaning |
|---------|-------|---------|
| `NEOPIXEL_PIN` | `0` | Data pin to the LED strip |
| `NUMBER_PIXELS` | `134` | Total LEDs across all nine letters |
| `BUTTON_PIN_1` | `15` | "Next mode" button |
| `BUTTON_PIN_2` | `14` | "Previous mode" button |
| `BUILT_IN_LED_PIN` | `25` | On-board LED (blinks on mode change) |

Each letter occupies a fixed range of pixels (see `LETTERS` in `config.py`).
Because the word contains the letter **O** three times, the layout is stored as
an ordered *list* of `(letter, start, end)` tuples rather than a dictionary.

## The modes

There are seven modes (0-6). Mode 0 cycles automatically; modes 1-6 each lock
the sign on a single pattern.

| Mode | Name | What you see | Borrowed from |
|------|------|--------------|---------------|
| **0** | **Auto-Cycle** | Steps through patterns 1-6, spending 60 seconds on each | — |
| **1** | **Color Letters** | Each letter of BOOKSTORE glows its own rainbow color (static) | `06-color-letter-test.py` |
| **2** | **Rainbow Flow** | The full rainbow spectrum scrolls smoothly across the sign | `tiki-bar-sign/06-rainbow-wipe.py` |
| **3** | **Rainbow Solid** | The whole sign glows one color, slowly cycling the rainbow | `jason-sign/main.py` (mode 2) |
| **4** | **Color Sparkle** | Every pixel drifts independently through random colors | `jason-sign/main.py` (mode 3) |
| **5** | **Color Wipe** | The whole sign holds one bright color, then wipes to the next | `tiki-bar-sign/04-named-colors.py` |
| **6** | **Comet** | A bright dot races across the sign leaving a fading tail | `tiki-bar-sign/01-move-red.py` |

## Using the buttons

- **BUTTON_1 (pin 15)** — advance to the **next** mode.
- **BUTTON_2 (pin 14)** — go back to the **previous** mode.

Modes wrap around: pressing "next" past mode 6 returns to mode 0, and pressing
"previous" from mode 0 jumps to mode 6. The on-board LED toggles each time the
mode changes, and the new mode name prints to the Thonny console.

A 200-millisecond debounce keeps a single press from registering as several.

## Running it

1. Copy `config.py` and `pattern-mode-test.py` to the Raspberry Pi Pico
   (for example with Thonny's *Save as... → Raspberry Pi Pico*).
2. Open `pattern-mode-test.py` in Thonny and press **Run** (green arrow).
3. The sign starts in **Mode 0 (Auto-Cycle)**. Press the buttons to jump to a
   specific pattern.

To make the program run automatically every time the Pico powers on, save it to
the Pico as `main.py`.

## Files in this kit

| File | Purpose |
|------|---------|
| [`pattern-mode-test.py`](pattern-mode-test.py) | The multi-pattern sign program described here |
| [`config.py`](config.py) | Hardware settings and letter-to-pixel layout |
| [`01-test-buttons.py`](01-test-buttons.py) | Minimal button + mode counter example |
| [`04-blink-single-pixel.py`](04-blink-single-pixel.py) | Blink one pixel |
| [`05-all-pixels-same-color.py`](05-all-pixels-same-color.py) | Light every pixel one color |
| [`06-color-letter-test.py`](06-color-letter-test.py) | Each letter a different color (the basis for Mode 1) |

## Learn more

See [`user-guide.md`](user-guide.md) for a beginner-friendly explanation of
*how* each pattern works and how to create your own.
