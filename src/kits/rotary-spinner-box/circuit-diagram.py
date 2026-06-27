#!/usr/bin/env python3
"""Generate the wiring diagram for the Rotary Spinner Box kit.

Uses schemdraw to draw how the NeoPixel strip, rotary encoder, the extra push
button, the power switch, and the 3xAA battery pack connect to the Raspberry
Pi Pico.

Pin map (from src/kits/rotary-spinner-box/config.py):
    NeoPixel strip DIN .............. GP0
    Rotary encoder A (CLK) .......... GP12
    Rotary encoder B (DT) ........... GP13
    Encoder built-in button (SW) .... GP14   (config PUSH_BUTTON_PIN_1)
    Extra push button ............... GP15   (config PUSH_BUTTON_PIN_2)

The lab code turns on the Pico's internal PULL_UP resistors for the encoder
and both buttons, so the encoder common and every switch return goes to GND
(no external VCC / pull-ups needed). The NeoPixel strip is powered from VSYS
(~4.5 V on battery, ~5 V on USB) so it works on battery or USB. Everything
shares one common ground.

Outputs circuit-diagram.svg and circuit-diagram.png into
docs/kits/rotary-spinner-box/img/.

Run:  python3 circuit-diagram.py
"""

import os
import schemdraw
import schemdraw.elements as elm
from schemdraw.elements import intcircuits as ic

# ---- colors -----------------------------------------------------------------
PICO_FILL = "#cfe0f5"   # light blue
NEO_FILL = "#cdece6"    # light teal
ENC_FILL = "#e6dcf3"    # light purple
EDGE = "#1b2536"
LBL = "#111111"         # dark text on light fills
DATA = "#cc7a00"   # amber - data / signal wires
PWR = "#c81e1e"    # red   - power (VSYS / +5V)
GND = "#222222"    # black - ground

OUT_DIR = os.path.normpath(os.path.join(
    os.path.dirname(__file__),
    "..", "..", "..", "docs", "kits", "rotary-spinner-box", "img",
))
os.makedirs(OUT_DIR, exist_ok=True)


def build():
    d = schemdraw.Drawing()
    d.config(fontsize=12, lw=2)

    # ------------------------------------------------------------------- Pico
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
        label="Raspberry\nPi Pico",
        fill=PICO_FILL, color=EDGE, lblcolor=LBL,
    )
    d += pico

    ENC_X = 9.5
    NEO_X = 9.5

    # ------------------------------------------------------------- Encoder
    # A / B / SW aligned exactly with GP12 / GP13 / GP14 -> straight wires.
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
    ).anchor("A").at((ENC_X, pico.GP12[1]))
    d += enc

    # -------------------------------------------------------- NeoPixel strip
    # Lifted above everything; power & ground exit over the top to the left.
    neo = ic.Ic(
        pins=[
            ic.IcPin(name="V5", side="left", slot="3/3"),
            ic.IcPin(name="DIN", side="left", slot="2/3"),
            ic.IcPin(name="GNDN", side="left", slot="1/3"),
        ],
        edgepadW=2.0, edgepadH=0.6, pinspacing=1.3, leadlen=0.9,
        label="12-pixel\nNeoPixel strip\n(WS2812B)",
        fill=NEO_FILL, color=EDGE, lblcolor=LBL,
    ).anchor("V5").at((NEO_X, pico.GP0[1] + 3.0))
    d += neo

    GROUND_Y = -2.4
    PWR_Y = neo.DIN[1] + 1.6          # amber power bus, above the strip
    BATT_X = pico.VSYS[0] - 2.6       # battery column
    NGND_X = BATT_X - 1.4             # far-left lane for the NeoPixel ground return
    LEFT_X = NGND_X                   # rail starts here

    # ============================ data / signal wires (red) =================
    d += elm.Wire("|-", arrow="->").at(pico.GP0).to(neo.DIN).color(DATA).label(
        "GP0 → DIN", "top", ofst=0.15, color=DATA, fontsize=11)
    d += elm.Wire("-", arrow="->").at(pico.GP12).to(enc.A).color(DATA).label(
        "GP12 → A (CLK)", "top", ofst=0.12, color=DATA, fontsize=10)
    d += elm.Wire("-", arrow="->").at(pico.GP13).to(enc.B).color(DATA).label(
        "GP13 → B (DT)", "top", ofst=0.12, color=DATA, fontsize=10)
    d += elm.Wire("-", arrow="->").at(pico.GP14).to(enc.SW).color(DATA).label(
        "GP14 → SW (knob button)", "top", ofst=0.12, color=DATA, fontsize=10)

    # ---- extra push button: GP15 -> button -> ground rail ------------------
    d += elm.Line().at(pico.GP15).right(1.6).color(DATA)
    d += elm.Button().down().color(DATA).label(
        "Extra\npush button", "right", ofst=0.2, fontsize=10)
    d += elm.Line().down().toy(GROUND_Y).color(GND)
    btn_gnd_x = d.here[0]

    # ============================ ground rail (black) =======================
    rail_left = (LEFT_X, GROUND_Y)
    rail_right = (enc.C[0] + 0.4, GROUND_Y)
    d += elm.Line().at(rail_left).to(rail_right).color(GND).linewidth(3)
    d += elm.Ground().at((pico.GND[0] - 1.2, GROUND_Y)).color(GND)

    def drop_to_rail(anchor):
        d.add(elm.Wire("|-").at(anchor).to((anchor[0], GROUND_Y)).color(GND))
        d.add(elm.Dot().at((anchor[0], GROUND_Y)).color(GND))

    # Pico GND -> down the left side into the rail
    d += elm.Wire("|-").at(pico.GND).to((pico.GND[0], GROUND_Y)).color(GND)
    d += elm.Dot().at((pico.GND[0], GROUND_Y)).color(GND)
    # encoder common (C) and switch ground (SWG)
    drop_to_rail(enc.C)
    drop_to_rail(enc.SWG)
    # extra-button ground tap already meets the rail
    d += elm.Dot().at((btn_gnd_x, GROUND_Y)).color(GND)

    # NeoPixel GND: straight out the left, over the top, down the far-left lane
    d += elm.Line().at(neo.GNDN).tox(NGND_X).color(GND)
    d += elm.Line().toy(GROUND_Y).color(GND)
    d += elm.Dot().at((NGND_X, GROUND_Y)).color(GND)

    # ============================ power (amber) =============================
    # Battery (+) -> switch -> VSYS, and VSYS -> over the top -> NeoPixel +5V.
    d += elm.Dot().at(pico.VSYS).color(PWR)
    # up from VSYS to the power bus, then across to above the strip, down to V5
    d += elm.Wire("|-").at(pico.VSYS).to((pico.VSYS[0], PWR_Y)).color(PWR)
    d += elm.Line().at((pico.VSYS[0], PWR_Y)).tox(neo.V5[0]).color(PWR).label(
        "VSYS  (+5 V power)", "top", ofst=0.15, color=PWR, fontsize=11)
    d += elm.Wire("-|").at((neo.V5[0], PWR_Y)).to(neo.V5).color(PWR)
    d += elm.Dot().at(neo.V5).color(PWR)

    # battery + switch on the left feeding VSYS
    d += elm.Line().at(pico.VSYS).left(1.1).color(PWR)
    d += elm.Switch().left().color(PWR).label(
        "Power\nswitch", "top", ofst=0.15, fontsize=10)
    d += elm.Line().tox(BATT_X).color(PWR)
    d += elm.Line().down().toy(GROUND_Y + 1.3).color(PWR)
    d += (batt := elm.Battery().down().color(PWR).label(
        "3×AA\n4.5 V", "left", ofst=0.25, fontsize=10))
    d += elm.Line().at(batt.end).toy(GROUND_Y).color(GND)
    d += elm.Dot().at((batt.end[0], GROUND_Y)).color(GND)

    # ----------------------------------------------------------- legend
    lx, ly = LEFT_X, PWR_Y - 1.0
    d += elm.Label().at((lx, ly + 0.8)).label(
        "Wire colors", halign="left", fontsize=11, color=LBL)
    for clr, txt in ((DATA, "Data / signal"),
                     (PWR, "Power (VSYS / +5 V)"),
                     (GND, "Ground (GND)")):
        d += elm.Line().at((lx, ly)).right(1.0).color(clr).label(
            txt, "right", ofst=0.12, fontsize=10, color=LBL)
        ly -= 0.7

    # ----------------------------------------------------------- title
    d += elm.Label().at(((LEFT_X + rail_right[0]) / 2, PWR_Y + 1.4)).label(
        "Rotary Spinner Box — Wiring Diagram", fontsize=15, color="#111111")

    return d


def main():
    d = build()
    svg_path = os.path.join(OUT_DIR, "circuit-diagram.svg")
    png_path = os.path.join(OUT_DIR, "circuit-diagram.png")
    d.save(svg_path, transparent=False)
    d.save(png_path, transparent=False)
    print("wrote", svg_path)
    print("wrote", png_path)


if __name__ == "__main__":
    main()
