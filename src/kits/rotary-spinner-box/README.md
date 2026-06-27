# Rotary Spinner Box — Lab Progression

A single-box NeoPixel project for teaching computational thinking. Every lab
runs standalone in Thonny and imports `config.py` for the hardware pins.

## Using the Box as a "Demo of Capability"

This box is a crowd magnet at **science fairs, STEM nights, and teacher
training**. We set out a table of boxes; participants — kids, parents,
teachers — walk up, pick one up, and start playing. You typically get about
**60 seconds** to explain the box and get them hooked.

The hook is simple and physical: **"Pick it up and spin the knob."** Something
visibly changes on the strip *every* time — a dot slides, a bar grows, colors
shift. That instant cause-and-effect is what sells it. From there the pitch
writes itself: lights, color, and motion that anyone can control, built on a
**~$15 kit** that teaches real computational thinking (variables, loops,
parameters, state machines).

The demo program for this is **`21-demo.py`** (see the table below). It cycles
through nine patterns, and in every one the knob changes something you can
see at a glance — perfect for a fast, hands-on table demo. After testing, it
is intended to become the box's default `main.py`.

> **60-second script:** *"Pick it up — spin the knob. See it move? You're
> controlling those lights with code. Press a button — new pattern, spin
> again. Same idea, different effect. It's a $15 kit and it's how we teach
> kids to think like programmers."*

## Hardware (see `config.py`)

| Part | GPIO Pin | Notes |
|------|----------|-------|
| NeoPixel strip (12 pixels) | 0 | `NEOPIXEL_PIN`, `NUMBER_PIXELS` |
| Rotary encoder A / B | 12 / 13 | the knob you spin |
| Push button 1 | 14 | `PUSH_BUTTON_PIN_1` |
| Push button 2 | 15 | `PUSH_BUTTON_PIN_2` |

## Uploading the Code

Use the `upload-code.sh` script to copy every lab onto the Pico:

```bash
./upload-code.sh
```

> **⚠️ Quit or disconnect Thonny first.** Only one program can use the Pico's
> serial port at a time. If Thonny is still connected, the upload fails with
> *"failed to access ... (it may be in use by another program)"*. In Thonny,
> click **Stop/Restart** then **Run → Disconnect**, or just quit Thonny, then
> run the script again.

## Auto-Run on Power-Up

`main.py` is a copy of `20-mode-machine.py`. The Pico automatically runs
`main.py` whenever it powers up, so once the code is uploaded the box starts in
the mode machine on its own — no computer required. Edit
`20-mode-machine.py` and re-upload to change what runs on boot.

## The Labs

### Diagnostics — does the hardware work?

| Lab | File | What it teaches |
|-----|------|-----------------|
| 01 | `01-blink.py` | First light: blink one pixel |
| 02 | `02-button-test.py` | Read both buttons with interrupts + debounce; print presses |
| 03 | `03-rotary-test.py` | Read the knob; print clockwise / counterclockwise turns |
| 04 | `04-strip-test.py` | Light all 12 pixels through red/green/blue/white |

### Patterns — making the strip move

| Lab | File | What it teaches |
|-----|------|-----------------|
| 05 | `05-spinner.py` | One dot bounces back and forth along the strip (loops + direction) |
| 06 | `06-comet.py` | A fading tail that follows the head; compute a color for every pixel each step |
| 07 | `07-rainbow.py` | The color wheel; map a rainbow across 12 pixels |
| 08 | `08-moving-rainbow.py` | Scroll the rainbow along the strip with a growing offset |

### Parameters — inputs that change a value

| Lab | File | What it teaches |
|-----|------|-----------------|
| 09 | `09-rotary-brightness.py` | Knob controls a **brightness** parameter |
| 10 | `10-rotary-color.py` | Knob controls a **color** parameter (hue) |
| 11 | `11-button-speed.py` | Buttons control a **speed** parameter while the scanner runs |

### Capstone — modes + parameters together

| Lab | File | What it teaches |
|-----|------|-----------------|
| 20 | `20-mode-machine.py` | Buttons pick the **mode**; the knob adjusts that mode's **parameter**. Uses interrupts + a `ticks_ms` timer so the knob stays responsive while the pattern animates. |
| 21 | `21-demo.py` | **Capability demo** for events (see above). Nine patterns — Knob Dot, Bar/Level, Solid Color, Larson Scanner, Comet, Theater Chase, Sparkle, Candle Flicker, Rainbow — where the knob always produces a visible change. Slated to become the default `main.py`. |

**The nine demo patterns and what the knob does in each:**

| Pattern | Knob controls | Spin to see |
|---------|---------------|-------------|
| Knob Dot | pixel position | a dot slide along the strip |
| Bar / Level | how many pixels are lit | a bar grow/shrink like a volume knob |
| Solid Color | hue | the whole strip change color |
| Larson Scanner | eye color | the sweeping eye change color |
| Comet | tail length | the glowing tail grow/shrink |
| Theater Chase | bulb spacing | the marquee gaps widen/narrow |
| Sparkle | density | more/fewer vivid random sparkles |
| Candle Flicker | brightness | the flame brighten/dim |
| Rainbow | offset | the whole rainbow rotate |

Random sparkle colors are picked as a random **hue** through the color wheel
(not random RGB), so every sparkle is vivid and easy to tell apart.

## Teaching Arc

1. **Diagnostics (01–04):** confirm each input/output works before building on it.
2. **Patterns (05–08):** loops, arrays, bouncing motion (the dot reverses at
   each end because the strip is linear, not a ring), and the color wheel.
3. **Parameters (09–11):** an input device changes a variable that changes the output — the core "parameter" idea.
4. **Capstone (20):** a state machine where one input chooses *what* runs and another input tunes *how* it runs.
5. **Demo (21):** the same state-machine idea scaled up to nine showcase
   patterns — the "demo of capability" used at events to hook newcomers.
