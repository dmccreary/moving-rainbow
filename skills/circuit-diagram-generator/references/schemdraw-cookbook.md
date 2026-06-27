# schemdraw cookbook (for wiring diagrams)

Practical recipes and gotchas for drawing microcontroller wiring diagrams with
schemdraw 0.20–0.22. Read this when editing a generator script. Everything here
was learned building real diagrams — the gotchas are the parts that waste time
if you don't know them.

## Contents

- [Imports and drawing setup](#imports-and-drawing-setup)
- [Components as IC blocks](#components-as-ic-blocks)
- [Placing blocks and reading pin coordinates](#placing-blocks-and-reading-pin-coordinates)
- [Wires and orthogonal routing](#wires-and-orthogonal-routing)
- [Rails, dots, and grounds](#rails-dots-and-grounds)
- [Battery and switch column](#battery-and-switch-column)
- [Potentiometers and other analog / 3-terminal parts](#potentiometers-and-other-analog--3-terminal-parts)
- [Labels (and the vertical-element gotcha)](#labels-and-the-vertical-element-gotcha)
- [Colors / house style](#colors--house-style)
- [Exporting with a white background](#exporting-with-a-white-background)
- [Gotchas, ranked](#gotchas-ranked)

## Imports and drawing setup

```python
import schemdraw
import schemdraw.elements as elm
from schemdraw.elements import intcircuits as ic

d = schemdraw.Drawing()
d.config(fontsize=12, lw=2)   # drawing-level line width is `lw`; per-element it is .linewidth()
```

## Components as IC blocks

A microcontroller or peripheral is best drawn as a labeled rectangle with named
pins, using `ic.Ic`. Pins are `ic.IcPin` objects:

```python
pico = ic.Ic(
    pins=[
        ic.IcPin(name="GP0",  side="right", slot="5/5"),   # slot = "position/total"
        ic.IcPin(name="GP12", side="right", slot="4/5"),
        ic.IcPin(name="GP13", side="right", slot="3/5"),
        ic.IcPin(name="GP14", side="right", slot="2/5"),
        ic.IcPin(name="GP15", side="right", slot="1/5"),   # slot 1 is the BOTTOM of that side
        ic.IcPin(name="VSYS", side="left",  slot="2/2"),
        ic.IcPin(name="GND",  side="left",  slot="1/2"),
    ],
    edgepadW=1.6, edgepadH=0.8,   # internal padding -> block width/height around pins
    pinspacing=1.4,               # vertical gap between pins on a side
    leadlen=0.9,                  # length of the pin stub sticking out
    label="Raspberry\nPi Pico",   # multi-line with \n
    fill="#cfe0f5", color="#1b2536", lblcolor="#111111",
)
d += pico
```

Notes:
- `slot="n/total"` sets the pin's position on its side; **slot 1 is at the
  bottom**, slot `total` at the top. List pins in whatever order you like.
- `side` accepts `"left"`, `"right"`, `"top"`, `"bottom"`.
- `ic.Ic` forwards these styling kwargs even though they aren't in its direct
  signature — `edgepadW`, `edgepadH`, `pinspacing`, `leadlen`, `label`, `fill`,
  `color`, `lblcolor` all work.
- Widen a block with `edgepadW` if the center label crowds the pin labels.

## Placing blocks and reading pin coordinates

Each pin name becomes an attribute holding a `Point` (subscript `[0]`=x,
`[1]`=y):

```python
pico.GP0          # Point(x, y) at the pin's outer (lead) tip
pico.GP0[1]       # the y coordinate
```

Place a second block by anchoring one of *its* pins at an absolute point. To
make signal wires perfectly horizontal, anchor the peripheral so its first
signal pin lines up with the MCU pin, and give it the **same `pinspacing`**:

```python
enc = ic.Ic(pins=[...], pinspacing=1.4, ...).anchor("A").at((9.5, pico.GP12[1]))
d += enc
# now enc.A == pico.GP12 height, enc.B == pico.GP13 height, etc. -> straight wires
```

## Wires and orthogonal routing

`elm.Wire(shape)` draws an L/Z-shaped connector between two points — ideal for
hooking a pin to a rail without hand-computing corners:

```python
elm.Wire("-",  arrow="->").at(pico.GP0).to(neo.DIN)    # straight
elm.Wire("-|").at(pico.VSYS).to((x, y))                # horizontal then vertical
elm.Wire("|-").at(pico.GND).to((x, GROUND_Y))          # vertical then horizontal
```

Shapes: `"-"` straight, `"-|"` horizontal-then-vertical, `"|-"`
vertical-then-horizontal. Add `arrow="->"` to show signal direction (e.g. data
out of a GPIO into a strip's DIN).

For plain segments use `elm.Line()` with directional helpers:

```python
elm.Line().at(p).right(1.6)         # fixed length
elm.Line().up().toy(PWR_Y)          # until a y coordinate
elm.Line().tox(BATT_X)              # until an x coordinate
```

## Rails, dots, and grounds

A rail is just a thicker line; taps are dots:

```python
d += elm.Line().at((LEFT_X, GROUND_Y)).to((RIGHT_X, GROUND_Y)).color(GND).linewidth(3)
d += elm.Ground().at((mid_x, GROUND_Y)).color(GND)
d += elm.Dot().at((x, GROUND_Y)).color(GND)    # a real connection onto the rail
```

A reusable helper for dropping any pin straight down to the bottom rail:

```python
def drop_to_rail(anchor):
    d.add(elm.Wire("|-").at(anchor).to((anchor[0], GROUND_Y)).color(GND))
    d.add(elm.Dot().at((anchor[0], GROUND_Y)).color(GND))
```

## Battery and switch column

The power input is a vertical stack on the far left: it taps the top rail, runs
down through the switch and battery, and the negative terminal drops to the
ground rail. Give the switch and battery explicit lengths so they don't run
huge (the default element length is long):

```python
d += elm.Line().at((BATT_X, PWR_Y)).down(0.5).color(PWR)
d += (sw   := elm.Switch().down().length(1.3).color(PWR))
d += (batt := elm.Battery().down().length(1.6).color(PWR))
d += elm.Line().at(batt.end).toy(NGND_Y).color(GND)   # (-) down to the ground net
```

`batt.end` is the bottom (negative) end of a downward battery; `batt.center` is
handy for placing its label.

## Potentiometers and other analog / 3-terminal parts

A potentiometer is a **3-terminal voltage divider**: the two ends go across the
supply and the wiper (middle) reports a voltage the MCU reads on an ADC pin.

**Power it from 3V3, not VSYS/5 V.** The Pico's ADC reference is 3.3 V; feeding
a wiper from 5 V can push the ADC input out of its safe range. So a pot's ends
go to **3V3 and GND**, and the wiper goes to the ADC GPIO (e.g. GP26/ADC0,
GP27/ADC1). Confirm the pin is actually read as analog in the lab code
(`machine.ADC(...).read_u16()`).

schemdraw's built-in `elm.Potentiometer` is a 2-terminal element drawn
horizontally (`start`/`end`/`tap` anchors) — awkward to align to MCU pins in
the left-pins-facing-MCU layout. **Model each pot as a 3-pin `ic.Ic` block
instead**, exactly like any other peripheral, so it lines up and labels
cleanly:

```python
pot = ic.Ic(
    pins=[
        ic.IcPin(name="VC", side="left", slot="3/3"),   # top  -> 3V3
        ic.IcPin(name="SIG", side="left", slot="2/3"),   # wiper -> ADC GPIO
        ic.IcPin(name="GP", side="left", slot="1/3"),    # bottom -> GND
    ],
    edgepadW=1.6, edgepadH=0.5, pinspacing=1.2, leadlen=0.9,
    label="Pot 1\n(brightness)", fill="#f2e2c4", color=EDGE, lblcolor=LBL,
).anchor("SIG").at((PERIPH_X, pico.GP26[1]))
```

When several parts need 3V3, give it its own **red 3V3 bus** (a second power
rail). Routing it *below* the ground rail keeps the pot supply lines out of the
signal area; where a pot's 3V3/GND riser crosses the ground rail with no dot it
reads correctly as "not connected." Two multi-pin pots on adjacent ADC pins are
the classic overlap trap — spread the GPIO slots (see the ranked gotchas).

This same "model it as an `ic.Ic` block" approach works for any part with a
handful of named terminals (sensors, displays, driver modules).

## Labels (and the vertical-element gotcha)

Inline labels work well on horizontal elements and wires:

```python
elm.Wire("-").at(pico.GP12).to(enc.A).color(DATA).label("GP12 → A (CLK)", "top", ofst=0.12, color=DATA, fontsize=10)
```

**Gotcha:** on a *vertically* drawn element (`.down()`), the `loc="left"/"right"`
label sides are unreliable and often render off the left edge (clipped). For
switches/batteries in the vertical power column, skip the inline label and place
an explicit `Label` to the side with `halign`:

```python
d += elm.Label().at((BATT_X + 0.35, sw.center[1])).label("Power\nswitch",   halign="left", fontsize=10, color=LBL)
d += elm.Label().at((BATT_X + 0.35, batt.center[1])).label("3×AA\n4.5 V", halign="left", fontsize=10, color=LBL)
```

A free-floating title or legend entry is also just a `Label`:

```python
d += elm.Label().at((cx, PWR_Y + 4.4)).label("Kit Name — Wiring Diagram", fontsize=15, color="#111111")
```

## Colors / house style

```python
DATA = "#cc7a00"   # amber  - data / signal wires (incl. button lines)
PWR  = "#c81e1e"   # red    - power (VSYS / +5 V)
GND  = "#222222"   # black  - ground
LBL  = "#111111"   # dark text on light fills
# light pastel block fills, one hue per component class:
PICO_FILL = "#cfe0f5"   # light blue
NEO_FILL  = "#cdece6"   # light teal
ENC_FILL  = "#e6dcf3"   # light purple
EDGE      = "#1b2536"   # block outline
```

Apply per element with `.color(...)`; thicker lines with `.linewidth(n)`.

## Exporting with a white background

`Drawing.save(transparent=...)` defaults to **transparent**, which looks gray on
some viewers. Pass `transparent=False` for a clean white background, and emit
both formats (PNG for docs, SVG for crisp scaling):

```python
d.save("circuit-diagram.svg", transparent=False)
d.save("circuit-diagram.png", transparent=False)
```

## Gotchas, ranked

1. **`.lw()` is not an element method.** Use `.linewidth(n)` on elements;
   `lw=` only exists in `d.config(lw=...)`. Calling `.lw()` raises
   `AttributeError: lw not defined in Element`.
2. **Transparent by default.** Without `transparent=False` the background is
   not white.
3. **Vertical labels clip.** Place explicit `elm.Label()` for switch/battery in
   the vertical column instead of inline `loc="left"/"right"`.
4. **Mismatched `pinspacing` slants signal wires.** Give the MCU and the
   peripheral the same `pinspacing` and anchor them aligned so wires are
   straight.
5. **The first render always needs cleanup.** schemdraw does no auto-layout —
   open the PNG and fix overlaps/clips by nudging coordinates.
6. **Blocks placed at the same x overlap.** Two `ic.Ic` blocks anchored at the
   same column with overlapping y-ranges will collide; separate them in x or y,
   and route long ground returns *around* blocks (e.g. out the top), not
   through them.
7. **Adjacent-pin multi-pin peripherals collide by construction.** Aligning two
   multi-pin blocks to GPIO pins that are next to each other forces them to
   overlap. Add empty GPIO slots as spacers (lay out more slots than you use
   and leave gaps) so each block gets a row tall enough for its full height.
