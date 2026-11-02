#!/usr/bin/env python3
"""Wiring diagram for the Ring 24 Kit (Moving Rainbow house style).

Draws the Pico, the 24-pixel NeoPixel ring and the two buttons. Pins come
from config.py:
    NEOPIXEL_PIN = 0, BUTTON_PIN_1 = 15, BUTTON_PIN_2 = 14

Run it from this folder (needs schemdraw):

    python3 circuit-diagram.py

It writes circuit-diagram.png and circuit-diagram.svg into docs/kits/ring-24/img/.
This file runs on your computer, not on the Pico, so upload-code.sh skips it.
"""

import os
import schemdraw
import schemdraw.elements as elm
from schemdraw.elements import intcircuits as ic

# --- house-style colors ------------------------------------------------------
DATA = "#cc7a00"   # amber - data / signal wires (including button lines)
PWR = "#c81e1e"    # red   - power
GND = "#222222"    # black - ground
LBL = "#111111"    # dark text on light fills
EDGE = "#1b2536"   # block outline
PICO_FILL = "#cfe0f5"   # light blue
RING_FILL = "#cdece6"   # light teal

OUT_DIR = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..",
    "docs", "kits", "ring-24", "img"))
TITLE = "Ring 24 Kit - Wiring Diagram"


def build():
    d = schemdraw.Drawing()
    d.config(fontsize=12, lw=2)

    # =====================================================================
    # 1. COMPONENTS
    # =====================================================================
    # Raspberry Pi Pico. Signal pins on the right, power pins on the left.
    # GP14 sits above GP15 so the two button wires never cross.
    pico = ic.Ic(
        pins=[
            ic.IcPin(name="GP0", side="right", slot="5/5"),
            ic.IcPin(name="GP14", side="right", slot="2/5"),
            ic.IcPin(name="GP15", side="right", slot="1/5"),
            ic.IcPin(name="VBUS", side="left", slot="2/2"),
            ic.IcPin(name="GND", side="left", slot="1/2"),
        ],
        edgepadW=2.2, edgepadH=0.8, pinspacing=1.3, leadlen=0.9,
        label="Raspberry\nPi Pico", fill=PICO_FILL, color=EDGE, lblcolor=LBL,
    )
    d += pico

    PERIPH_X = 10.5   # x column for the ring

    # 24-pixel NeoPixel ring: +5 on top, DIN in the middle, GND on the bottom.
    # DIN lines up with GP0 (same pinspacing), so the data wire is straight.
    ring = ic.Ic(
        pins=[
            ic.IcPin(name="V5", side="left", slot="3/3"),
            ic.IcPin(name="DIN", side="left", slot="2/3"),
            ic.IcPin(name="GNDR", side="left", slot="1/3"),
        ],
        edgepadW=3.2, edgepadH=0.6, pinspacing=1.3, leadlen=0.9,
        label="24-pixel\nNeoPixel ring",
        fill=RING_FILL, color=EDGE, lblcolor=LBL,
    ).anchor("DIN").at((PERIPH_X, pico.GP0[1]))
    d += ring

    # Layout reference lines (rails / columns).
    GROUND_Y = pico.GP15[1] - 3.0    # bottom ground rail, below the buttons
    PWR_Y = ring.V5[1] + 1.6         # top power rail
    LEFT_X = pico.VBUS[0] - 3.0      # far-left column
    rail_right = (ring.DIN[0] + 4.4, GROUND_Y)

    # =====================================================================
    # 2. SIGNAL WIRING (amber, straight where possible)
    # =====================================================================
    d += elm.Wire("-", arrow="->").at(pico.GP0).to(ring.DIN).color(DATA).label(
        "GP0 → DIN", "top", ofst=0.15, color=DATA, fontsize=11)

    # Two buttons: GPIO pin -> button -> ground rail (internal pull-ups).
    d += elm.Line().at(pico.GP15).right(1.2).color(DATA)
    d += elm.Button().down().color(DATA).label(
        "Button 1\n(GP15)", "right", ofst=0.2, fontsize=10)
    d += elm.Line().down().toy(GROUND_Y).color(GND)
    btn1_gnd_x = d.here[0]
    d += elm.Line().at(pico.GP14).right(3.0).color(DATA)
    d += elm.Button().down().color(DATA).label(
        "Button 2\n(GP14)", "right", ofst=0.2, fontsize=10)
    d += elm.Line().down().toy(GROUND_Y).color(GND)
    btn2_gnd_x = d.here[0]

    # =====================================================================
    # 3. POWER & GROUND
    # =====================================================================
    # --- ground rail (black) along the bottom ---
    d += elm.Line().at((LEFT_X, GROUND_Y)).to(rail_right).color(GND).linewidth(3)
    d += elm.Ground().at((pico.GND[0] - 1.2, GROUND_Y)).color(GND)
    d += elm.Wire("|-").at(pico.GND).to((pico.GND[0], GROUND_Y)).color(GND)
    d += elm.Dot().at((pico.GND[0], GROUND_Y)).color(GND)
    d += elm.Dot().at((btn1_gnd_x, GROUND_Y)).color(GND)
    d += elm.Dot().at((btn2_gnd_x, GROUND_Y)).color(GND)

    # ring ground: leaves its pin to the left, then drops to the rail
    ring_gnd_x = ring.GNDR[0] - 0.7
    d += elm.Line().at(ring.GNDR).tox(ring_gnd_x).color(GND)
    d += elm.Line().at((ring_gnd_x, ring.GNDR[1])).toy(GROUND_Y).color(GND)
    d += elm.Dot().at((ring_gnd_x, GROUND_Y)).color(GND)
    d += elm.Dot().at(ring.GNDR).color(GND)

    # --- 5 V power (red) along the top: USB 5 V on VBUS feeds the ring ---
    d += elm.Line().at((pico.VBUS[0], PWR_Y)).tox(ring.V5[0]).color(PWR).label(
        "VBUS  (+5 V from the USB cable)", "top", ofst=0.15, color=PWR, fontsize=11)
    d += elm.Wire("|-").at(pico.VBUS).to((pico.VBUS[0], PWR_Y)).color(PWR)
    d += elm.Dot().at(pico.VBUS).color(PWR)
    d += elm.Wire("-|").at((ring.V5[0], PWR_Y)).to(ring.V5).color(PWR)
    d += elm.Dot().at(ring.V5).color(PWR)

    # =====================================================================
    # LEGEND (top-left, above the power rail) + TITLE
    # =====================================================================
    lx, ly = LEFT_X, PWR_Y + 2.6
    d += elm.Label().at((lx - 0.2, ly + 0.8)).label(
        "Wire colors", halign="left", fontsize=11, color=LBL)
    for clr, txt in ((PWR, "Power (+5 V)"),
                     (DATA, "Data / signal"),
                     (GND, "Ground (GND)")):
        d += elm.Line().at((lx, ly)).right(1.0).color(clr).label(
            txt, "right", ofst=0.12, fontsize=10, color=LBL)
        ly -= 0.7

    d += elm.Label().at((((LEFT_X + 2) + rail_right[0]) / 2 + 2, PWR_Y + 4.4)).label(
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
