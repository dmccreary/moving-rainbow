---
name: circuit-diagram-generator
description: >-
  Generate clear, beginner-friendly circuit and wiring diagrams for
  microcontroller projects (Raspberry Pi Pico + NeoPixels, push buttons, rotary
  encoders, sensors, switches, batteries) using the schemdraw Python library,
  in the Moving Rainbow house style — red power rail across the top, black
  ground rail across the bottom, amber signal wires, light component blocks,
  white background, and PNG + SVG output. Use this skill whenever the user
  wants to create, draw, generate, redraw, or update a circuit diagram, wiring
  diagram, schematic, hookup figure, "how the parts connect" illustration, or
  breadboard wiring picture for a kit or microcontroller project — even if they
  don't mention schemdraw by name. Also use it when adding a wiring figure to a
  kit's documentation page.
---

# Circuit Diagram Generator

Generate consistent, classroom-friendly wiring diagrams as code so they are
reproducible, version-controlled, and easy to tweak. Every diagram is a small
Python program that uses [schemdraw](https://schemdraw.readthedocs.io) to emit
a PNG and an SVG.

The goal is a picture a beginner can *follow with their finger*: power comes in
at the top, ground sits at the bottom, and each wire is color-coded by what it
carries. Prioritize readability over schematic formality.

## When to use this

Use it for any request like "draw the circuit for the X kit", "make a wiring
diagram", "show how the parts connect", "update the schematic", or "add a
hookup figure to the kit page". It targets microcontroller + peripheral
projects (Pico, NeoPixel strips/rings, buttons, encoders, potentiometers,
sensors, battery packs), but the house style works for any small DC circuit.

## Prerequisites

`schemdraw` must be importable. Check it, and stop to ask the user to install
it if missing (don't silently pip-install):

```bash
python3 -c "import schemdraw; print(schemdraw.__version__)"   # expect 0.20+
```

## Workflow

### 1. Get the pin map and the electrical details — don't guess

The diagram must match the code that will actually run. Read the kit's
`config.py` and the lab/example source under `src/kits/<kit>/` to learn:

- **Which GPIO pin each part uses** (e.g. `NEOPIXEL_PIN = 0`,
  `ROTARY_ENCODER_PIN_A = 12`). The shared `config.py` is the source of truth —
  prefer it over comments.
- **How switches are wired electrically.** If the code calls
  `machine.Pin(..., Pin.PULL_UP)`, the button/encoder uses the Pico's
  *internal* pull-up, so its other leg goes straight to **GND** — no external
  resistor and no VCC pin. This is the common case in these kits. Only show a
  `+`/VCC pin and pull-up resistor if the code/hardware actually needs one
  (e.g. a KY-040 module with onboard resistors).
- **Where power comes from.** Power an addressable LED strip from **VSYS** so
  it runs on battery (~4.5 V from 3×AA) *and* on USB (~5 V). A battery pack
  feeds VSYS through the power switch.

If the pin map is genuinely unavailable, ask the user rather than inventing
pins — a wrong pin number in a "helpful" diagram is worse than none.

### 2. Hold the house-style layout in mind

This layout is what makes the diagrams feel calm and legible. Follow it unless
the user asks otherwise.

- **White background.**
- **Red power rail across the TOP**, **black ground rail across the BOTTOM** —
  this mirrors a breadboard's `+`/`–` rails and physical intuition (power up
  high, ground down low). It is the signature of the house style.
- **Microcontroller** as a light-blue block, center-left. Put **signal/GPIO
  pins on its right** (facing the peripherals) and **power pins (VSYS, GND) on
  its left**.
- **Peripherals** (LED strip, encoder, sensor, potentiometer) as light-fill
  blocks to the **right**, pins on their left facing the MCU. **Align each
  peripheral's signal pin to its MCU GPIO pin** (use the same `pinspacing`) so
  the wires are straight horizontal runs — slanted or jogging signal wires are
  the number-one thing that makes these diagrams look messy.
- **Watch for the adjacent-pin overlap trap.** If two *multi-pin* peripherals
  (say two potentiometers, or an encoder + a sensor) attach to GPIO pins that
  sit next to each other, aligning each block to its single pin forces the
  blocks to overlap vertically. The fix: give the MCU **extra empty GPIO slots
  as spacers** (e.g. lay out 7 slots and leave gaps) so consecutive
  peripherals land on rows far enough apart for their full height. Decide the
  vertical budget before placing blocks.
- **Power input** (battery pack + power switch) as a vertical column on the
  **far left**: it taps the top rail, runs down through the switch and battery,
  and its negative terminal drops into the bottom ground rail.
- **Common ground:** every ground returns to the single bottom rail. Place one
  `Ground` symbol on it.
- **Color = meaning.** Red = power, amber/orange = data & signal (including
  button lines), black = ground. Put a small **wire-color legend in the
  top-left**, above the power rail, and a **title** at the very top.
- **Light pastel fills with dark text** so pin names stay readable; give each
  component class its own hue.
- **Dots mark real connections.** Wires that merely cross with no dot read as
  not connected — lean on this instead of forcing every wire to avoid every
  other.

### 3. Write the generator script

Copy [`scripts/circuit_diagram_template.py`](scripts/circuit_diagram_template.py)
to live next to the kit's source — the repo convention is
`src/kits/<kit>/circuit-diagram.py` — and adapt the three marked sections:
the component blocks, the signal wiring, and the power/ground wiring. The
template already encodes the house style (rails, colors, legend, battery
column, PNG+SVG export) and runs as-is so you have a working starting point.

Set `OUT_DIR` to the kit's docs image folder
(`docs/kits/<kit>/img/`) so the figure lands where the page can reference it.

Keep each diagram a **standalone script** (no shared import) so it stays
independently editable and copy-pasteable — matching how code is stored
per-kit in this repo.

For the schemdraw API specifics you'll need while editing — the `Ic`/`IcPin`
parameters, orthogonal `Wire` routing, the `.linewidth()` vs `.lw()` gotcha,
labeling vertical elements, and white-background export — read
[`references/schemdraw-cookbook.md`](references/schemdraw-cookbook.md).

### 4. Render, then LOOK at the result and iterate

Run the script, then **Read the generated PNG** and inspect it like a student
would. This visual check is not optional — schemdraw places things exactly
where you tell it, so the first render almost always has an overlap or a
slanted wire to fix.

```bash
cd src/kits/<kit> && python3 circuit-diagram.py
```

Check for: blocks overlapping each other, pin labels colliding with the block
title, signal wires that aren't perfectly horizontal, labels clipped at the
canvas edge, and wires crossing *through* a block. Nudge coordinates, widen a
block (`edgepadW`), or reroute, then re-render. Repeat until it's clean.

### 5. Embed it in the kit page

Reference the PNG from the kit's markdown with descriptive alt text, restate
the color key in words, and list the connections. Pattern:

```markdown
![Wiring diagram for the <kit> showing the Pico connected to ...](img/circuit-diagram.png)

Follow the colors: **red** wires carry *power*, **amber** wires carry *data
and button signals*, and **black** wires are *ground*.

- The strip's **DIN** (data-in) goes to **GP0**.
- ...
```

For student-facing pages, add a short "how to read it" note (a dot = connected;
crossing wires without a dot are not) and follow `CONTENT-GENERATION-GUIDE.md`
(reading level, and the Pixel mascot voice for tips). Teacher-facing pages use
the professional register with no mascot.

## Checklist before you call it done

- [ ] Pin numbers match `config.py` / the lab code exactly.
- [ ] Power rail is red and on top; ground rail is black and on the bottom.
- [ ] Signal wires are straight and amber; power is red; ground is black.
- [ ] Background is white (`d.save(..., transparent=False)`).
- [ ] Both `circuit-diagram.png` and `circuit-diagram.svg` were written.
- [ ] You actually opened the PNG and confirmed nothing overlaps or clips.
- [ ] The figure is embedded with alt text and a color key on the kit page.
