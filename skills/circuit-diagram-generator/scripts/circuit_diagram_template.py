#!/usr/bin/env python3
"""TEMPLATE: a Moving Rainbow house-style wiring diagram.

Copy this file next to a kit's source (the repo convention is
`src/kits/<kit>/circuit-diagram.py`) and adapt the three sections marked
`### EDIT`:
    1. COMPONENTS  - the blocks (microcontroller + peripherals) and their pins
    2. SIGNAL WIRING - data/button wires from GPIO pins to peripheral pins
    3. POWER & GROUND - the top power rail, bottom ground rail, battery column

House style (see SKILL.md):
    * white background
    * RED power rail across the TOP, BLACK ground rail across the BOTTOM
    * AMBER data/signal wires
    * light pastel component blocks with dark text
    * a wire-color legend top-left and a title on top
    * outputs circuit-diagram.svg AND circuit-diagram.png

As shipped it renders a representative example (Pico + 12-pixel NeoPixel strip
+ rotary encoder + extra push button + 3xAA pack). Run it to see the style,
then edit it to match your kit:

    python3 circuit_diagram_template.py
"""

import os
import schemdraw
import schemdraw.elements as elm
from schemdraw.elements import intcircuits as ic

# --- house-style colors ------------------------------------------------------
DATA = "#cc7a00"   # amber - data / signal wires (including button lines)
PWR = "#c81e1e"    # red   - power (VSYS / +5 V)
GND = "#222222"    # black - ground
LBL = "#111111"    # dark text on light fills
EDGE = "#1b2536"   # block outline
PICO_FILL = "#cfe0f5"   # light blue
NEO_FILL = "#cdece6"    # light teal
ENC_FILL = "#e6dcf3"    # light purple

# Where the PNG/SVG go. The template writes next to itself so it runs anywhere.
# When adapting for a kit, point this at the kit's docs image folder, e.g.:
#   OUT_DIR = os.path.normpath(os.path.join(
#       os.path.dirname(__file__), "..", "..", "..",
#       "docs", "kits", "<kit>", "img"))
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
TITLE = "Kit Name — Wiring Diagram"


def build():
    d = schemdraw.Drawing()
    d.config(fontsize=12, lw=2)

    # =====================================================================
    # 1. COMPONENTS                                                ### EDIT
    # =====================================================================
    # Microcontroller: signal pins on the RIGHT, power pins on the LEFT.
    # slot="n/total" places a pin; slot 1 is the BOTTOM of that side.
    pico = ic.Ic(
        pins=[
            ic.IcPin(name="GP0", side="right", slot="5/5"),
            ic.IcPin(name="GP12", side="right", slot="4/5"),
            ic.IcPin(name="GP13", side="right", slot="3/5"),
            ic.IcPin(name="GP14", side="right", slot="2/5"),
            ic.IcPin(name="GP15", side="right", slot="1/5"),
            ic.IcPin(name="VSYS", side="left", slot="2/2"),
            ic.IcPin(name="GND", side="left", slot="1/2"),
        ],
        edgepadW=2.2, edgepadH=0.8, pinspacing=1.4, leadlen=0.9,
        label="Raspberry\nPi Pico", fill=PICO_FILL, color=EDGE, lblcolor=LBL,
    )
    d += pico

    PERIPH_X = 9.5   # x column for the peripherals on the right

    # Rotary encoder: A / B / SW aligned with GP12 / GP13 / GP14 (same
    # pinspacing as the Pico) so the signal wires are straight horizontals.
    # C (rotation common) and SWG (switch return) go to ground.
    enc = ic.Ic(
        pins=[
            ic.IcPin(name="A", side="left", slot="5/5"),
            ic.IcPin(name="B", side="left", slot="4/5"),
            ic.IcPin(name="SW", side="left", slot="3/5"),
            ic.IcPin(name="C", side="left", slot="2/5"),
            ic.IcPin(name="SWG", side="left", slot="1/5"),
        ],
        edgepadW=1.9, edgepadH=0.6, pinspacing=1.4, leadlen=0.9,
        label="Rotary\nencoder\n(knob +\nbutton)",
        fill=ENC_FILL, color=EDGE, lblcolor=LBL,
    ).anchor("A").at((PERIPH_X, pico.GP12[1]))
    d += enc

    # NeoPixel strip: +5 on top, DIN in the middle, GND on the bottom. Lifted
    # high so its ground wire can exit left OVER the top of the Pico.
    neo = ic.Ic(
        pins=[
            ic.IcPin(name="V5", side="left", slot="3/3"),
            ic.IcPin(name="DIN", side="left", slot="2/3"),
            ic.IcPin(name="GNDN", side="left", slot="1/3"),
        ],
        edgepadW=2.0, edgepadH=0.6, pinspacing=1.3, leadlen=0.9,
        label="12-pixel\nNeoPixel strip\n(WS2812B)",
        fill=NEO_FILL, color=EDGE, lblcolor=LBL,
    ).anchor("V5").at((PERIPH_X, pico.GP0[1] + 4.6))
    d += neo

    # Layout reference lines (rails / columns).
    GROUND_Y = -2.4                 # bottom ground rail
    PWR_Y = neo.V5[1] + 1.6         # top power rail
    BATT_X = pico.VSYS[0] - 3.0     # far-left column: power input + shared ground
    rail_right = (enc.C[0] + 0.4, GROUND_Y)

    # =====================================================================
    # 2. SIGNAL WIRING (amber, straight where possible)            ### EDIT
    # =====================================================================
    d += elm.Wire("|-", arrow="->").at(pico.GP0).to(neo.DIN).color(DATA).label(
        "GP0 → DIN", "top", ofst=0.15, color=DATA, fontsize=11)
    d += elm.Wire("-", arrow="->").at(pico.GP12).to(enc.A).color(DATA).label(
        "GP12 → A (CLK)", "top", ofst=0.12, color=DATA, fontsize=10)
    d += elm.Wire("-", arrow="->").at(pico.GP13).to(enc.B).color(DATA).label(
        "GP13 → B (DT)", "top", ofst=0.12, color=DATA, fontsize=10)
    d += elm.Wire("-", arrow="->").at(pico.GP14).to(enc.SW).color(DATA).label(
        "GP14 → SW (knob button)", "top", ofst=0.12, color=DATA, fontsize=10)

    # Extra push button: GP15 -> button -> ground rail.
    d += elm.Line().at(pico.GP15).right(1.6).color(DATA)
    d += elm.Button().down().color(DATA).label(
        "Extra\npush button", "right", ofst=0.2, fontsize=10)
    d += elm.Line().down().toy(GROUND_Y).color(GND)
    btn_gnd_x = d.here[0]

    # =====================================================================
    # 3. POWER & GROUND                                            ### EDIT
    # =====================================================================
    # --- ground rail (black) along the bottom ---
    rail_left = (BATT_X, GROUND_Y)
    d += elm.Line().at(rail_left).to(rail_right).color(GND).linewidth(3)
    d += elm.Ground().at((pico.GND[0] - 1.2, GROUND_Y)).color(GND)

    def drop_to_rail(anchor):
        d.add(elm.Wire("|-").at(anchor).to((anchor[0], GROUND_Y)).color(GND))
        d.add(elm.Dot().at((anchor[0], GROUND_Y)).color(GND))

    d += elm.Wire("|-").at(pico.GND).to((pico.GND[0], GROUND_Y)).color(GND)
    d += elm.Dot().at((pico.GND[0], GROUND_Y)).color(GND)
    drop_to_rail(enc.C)
    drop_to_rail(enc.SWG)
    d += elm.Dot().at((btn_gnd_x, GROUND_Y)).color(GND)

    # NeoPixel ground exits left, over the top of the Pico, down the far-left
    # column, where it joins the battery's (-) terminal on the way to the rail.
    # NOTE: the battery (-) below is tied to NGND_Y because of this shared
    # column. If you reroute the strip ground straight down to the bottom rail
    # instead, repoint the battery (-) to GROUND_Y so it doesn't dangle.
    NGND_Y = neo.GNDN[1]
    d += elm.Line().at(neo.GNDN).tox(BATT_X).color(GND)
    d += elm.Line().at((BATT_X, NGND_Y)).toy(GROUND_Y).color(GND)
    d += elm.Dot().at((BATT_X, GROUND_Y)).color(GND)
    d += elm.Dot().at((BATT_X, NGND_Y)).color(GND)

    # --- power rail (red) along the top ---
    # The bus runs from the far-left column across to the NeoPixel +5 V; the
    # Pico's VSYS taps up into it.
    d += elm.Dot().at((BATT_X, PWR_Y)).color(PWR)
    d += elm.Line().at((BATT_X, PWR_Y)).tox(neo.V5[0]).color(PWR).label(
        "VSYS  (+5 V power)", "top", ofst=0.15, color=PWR, fontsize=11)
    d += elm.Wire("|-").at(pico.VSYS).to((pico.VSYS[0], PWR_Y)).color(PWR)
    d += elm.Dot().at((pico.VSYS[0], PWR_Y)).color(PWR)
    d += elm.Dot().at(pico.VSYS).color(PWR)
    d += elm.Wire("-|").at((neo.V5[0], PWR_Y)).to(neo.V5).color(PWR)
    d += elm.Dot().at(neo.V5).color(PWR)

    # power input stack on the far left: bus -> switch -> battery -> (-) to gnd
    d += elm.Line().at((BATT_X, PWR_Y)).down(0.5).color(PWR)
    d += (sw := elm.Switch().down().length(1.3).color(PWR))
    d += (batt := elm.Battery().down().length(1.6).color(PWR))
    d += elm.Line().at(batt.end).toy(NGND_Y).color(GND)
    d += elm.Label().at((BATT_X + 0.35, sw.center[1])).label(
        "Power\nswitch", halign="left", fontsize=10, color=LBL)
    d += elm.Label().at((BATT_X + 0.35, batt.center[1])).label(
        "3×AA\n4.5 V", halign="left", fontsize=10, color=LBL)

    # =====================================================================
    # LEGEND (top-left, above the power rail) + TITLE
    # =====================================================================
    lx, ly = BATT_X, PWR_Y + 2.6
    d += elm.Label().at((lx - 0.2, ly + 0.8)).label(
        "Wire colors", halign="left", fontsize=11, color=LBL)
    for clr, txt in ((PWR, "Power (+5 V)"),
                     (DATA, "Data / signal"),
                     (GND, "Ground (GND)")):
        d += elm.Line().at((lx, ly)).right(1.0).color(clr).label(
            txt, "right", ofst=0.12, fontsize=10, color=LBL)
        ly -= 0.7

    d += elm.Label().at((((BATT_X + 2) + rail_right[0]) / 2, PWR_Y + 4.4)).label(
        TITLE, fontsize=15, color=LBL)

    return d


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    d = build()
    svg_path = os.path.join(OUT_DIR, "circuit-diagram.svg")
    png_path = os.path.join(OUT_DIR, "circuit-diagram.png")
    d.save(svg_path, transparent=False)
    d.save(png_path, transparent=False)
    print("wrote", svg_path)
    print("wrote", png_path)


if __name__ == "__main__":
    main()
