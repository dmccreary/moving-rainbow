# Rotary Spinner Box — Lab Progression

A single-box NeoPixel project for teaching computational thinking. Every lab
runs standalone in Thonny and imports `config.py` for the hardware pins.

## Hardware (see `config.py`)

| Part | GPIO Pin | Notes |
|------|----------|-------|
| NeoPixel ring (12 pixels) | 0 | `NEOPIXEL_PIN`, `NUMBER_PIXELS` |
| Rotary encoder A / B | 12 / 13 | the knob you spin |
| Push button 1 | 14 | `PUSH_BUTTON_PIN_1` |
| Push button 2 | 15 | `PUSH_BUTTON_PIN_2` |

## The Labs

### Diagnostics — does the hardware work?

| Lab | File | What it teaches |
|-----|------|-----------------|
| 01 | `01-blink.py` | First light: blink one pixel |
| 02 | `02-button-test.py` | Read both buttons with interrupts + debounce; print presses |
| 03 | `03-rotary-test.py` | Read the knob; print clockwise / counterclockwise turns |
| 04 | `04-strip-test.py` | Light all 12 pixels through red/green/blue/white |

### Patterns — making the ring move

| Lab | File | What it teaches |
|-----|------|-----------------|
| 05 | `05-spinner.py` | One dot travels around the ring (loops + wraparound) |
| 06 | `06-comet.py` | A fading tail; compute a color for every pixel each step |
| 07 | `07-rainbow.py` | The color wheel; map a rainbow around 12 pixels |
| 08 | `08-moving-rainbow.py` | Animate the rainbow with a growing offset |

### Parameters — inputs that change a value

| Lab | File | What it teaches |
|-----|------|-----------------|
| 09 | `09-rotary-brightness.py` | Knob controls a **brightness** parameter |
| 10 | `10-rotary-color.py` | Knob controls a **color** parameter (hue) |
| 11 | `11-button-speed.py` | Buttons control a **speed** parameter while the spinner runs |

### Capstone — modes + parameters together

| Lab | File | What it teaches |
|-----|------|-----------------|
| 20 | `20-mode-machine.py` | Buttons pick the **mode**; the knob adjusts that mode's **parameter**. Uses interrupts + a `ticks_ms` timer so the knob stays responsive while the pattern animates. |

## Teaching Arc

1. **Diagnostics (01–04):** confirm each input/output works before building on it.
2. **Patterns (05–08):** loops, arrays, wraparound, and the color wheel.
3. **Parameters (09–11):** an input device changes a variable that changes the output — the core "parameter" idea.
4. **Capstone (20):** a state machine where one input chooses *what* runs and another input tunes *how* it runs.
