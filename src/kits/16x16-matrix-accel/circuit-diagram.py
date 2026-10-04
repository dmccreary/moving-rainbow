#!/usr/bin/env python3
"""Wiring diagram for the 16x16 Matrix Accelerometer Kit (Moving Rainbow house style).

Draws the Pico, the 16x16 NeoPixel matrix, the LIS3DH accelerometer and the two
mode buttons. Pins come from config.py:
    NEOPIXEL_PIN = 0, BUTTON_PIN_1 = 14, BUTTON_PIN_2 = 15,
    ACCEL_SDA_PIN = 16, ACCEL_SCL_PIN = 17

Run it from this folder (needs schemdraw):

    python3 circuit-diagram.py

It writes circuit-diagram.png and circuit-diagram.svg into docs/kits/16x16-matrix-accel/img/.
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
MATRIX_FILL = "#cdece6"  # light teal
ACCEL_FILL = "#e6dcf3"   # light purple

OUT_DIR = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..",
    "docs", "kits", "16x16-matrix-accel", "img"))
TITLE = "16x16 Matrix Tilt Kit - Wiring Diagram"


def build():
    d = schemdraw.Drawing()
    d.config(fontsize=12, lw=2)

    # =====================================================================
    # 1. COMPONENTS
    # =====================================================================
    # Raspberry Pi Pico. Signal pins on the right, power pins on the left.
    # (3V3 sits on the right so its wire to the accelerometer is a straight line.)
    pico = ic.Ic(
        pins=[
            ic.IcPin(name="GP0", side="right", slot="9/9"),
            ic.IcPin(name="3V3", side="right", slot="6/9"),
            ic.IcPin(name="GP17", side="right", slot="5/9"),
            ic.IcPin(name="GP16", side="right", slot="4/9"),
            ic.IcPin(name="GP14", side="right", slot="2/9"),
            ic.IcPin(name="GP15", side="right", slot="1/9"),
            ic.IcPin(name="VBUS", side="left", slot="2/2"),
            ic.IcPin(name="GND", side="left", slot="1/2"),
        ],
        edgepadW=2.2, edgepadH=0.8, pinspacing=1.3, leadlen=0.9,
        label="Raspberry\nPi Pico", fill=PICO_FILL, color=EDGE, lblcolor=LBL,
    )
    d += pico

    PERIPH_X = 10.5   # x column for the parts on the right

    # LIS3DH accelerometer. SCL and SDA line up with GP17 and GP16 (same pinspacing),
    # so the signal wires are straight horizontal runs.
    accel = ic.Ic(
        pins=[
            ic.IcPin(name="VIN", side="left", slot="4/4"),
            ic.IcPin(name="SCL", side="left", slot="3/4"),
            ic.IcPin(name="SDA", side="left", slot="2/4"),
            ic.IcPin(name="GND", side="left", slot="1/4"),
        ],
        edgepadW=3.0, edgepadH=0.6, pinspacing=1.3, leadlen=0.9,
        label="LIS3DH\naccelerometer\n(tilt sensor)",
        fill=ACCEL_FILL, color=EDGE, lblcolor=LBL,
    ).anchor("SCL").at((PERIPH_X, pico.GP17[1]))
    d += accel

    # 16x16 NeoPixel matrix: +5 on top, DIN in the middle, GND on the bottom.
    # Lifted high so its ground wire can exit left OVER the top of the Pico.
    matrix = ic.Ic(
        pins=[
            ic.IcPin(name="V5", side="left", slot="3/3"),
            ic.IcPin(name="DIN", side="left", slot="2/3"),
            ic.IcPin(name="GNDM", side="left", slot="1/3"),
        ],
        edgepadW=3.2, edgepadH=0.6, pinspacing=1.3, leadlen=0.9,
        label="16x16\nNeoPixel matrix\n(256 pixels)",
        fill=MATRIX_FILL, color=EDGE, lblcolor=LBL,
    ).anchor("V5").at((PERIPH_X, pico.GP0[1] + 4.6))
    d += matrix

    # Layout reference lines (rails / columns).
    GROUND_Y = -2.4                  # bottom ground rail
    PWR_Y = matrix.V5[1] + 1.6       # top power rail
    LEFT_X = pico.VBUS[0] - 3.0      # far-left column: shared power and ground
    rail_right = (accel.SCL[0] + 4.4, GROUND_Y)

    # =====================================================================
    # 2. SIGNAL WIRING (amber, straight where possible)
    # =====================================================================
    d += elm.Wire("|-", arrow="->").at(pico.GP0).to(matrix.DIN).color(DATA).label(
        "GP0 → DIN", "top", ofst=0.15, color=DATA, fontsize=11)
    d += elm.Wire("-", arrow="->").at(pico.GP17).to(accel.SCL).color(DATA).label(
        "GP17 → SCL (clock)", "top", ofst=0.12, color=DATA, fontsize=10)
    d += elm.Wire("-", arrow="<->").at(pico.GP16).to(accel.SDA).color(DATA).label(
        "GP16 ↔ SDA (data)", "top", ofst=0.12, color=DATA, fontsize=10)

    # Two mode buttons: GPIO pin -> button -> ground rail.
    d += elm.Line().at(pico.GP14).right(1.4).color(DATA)
    d += elm.Button().down().color(DATA).label(
        "Button 1\n(GP14)", "right", ofst=0.2, fontsize=10)
    d += elm.Line().down().toy(GROUND_Y).color(GND)
    btn1_gnd_x = d.here[0]
    d += elm.Line().at(pico.GP15).right(3.6).color(DATA)
    d += elm.Button().down().color(DATA).label(
        "Button 2\n(GP15)", "right", ofst=0.2, fontsize=10)
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

    # accelerometer ground: leaves its pin to the left, then drops to the rail
    acc_gnd_x = accel.GND[0] - 0.7
    d += elm.Line().at(accel.GND).tox(acc_gnd_x).color(GND)
    d += elm.Line().at((acc_gnd_x, accel.GND[1])).toy(GROUND_Y).color(GND)
    d += elm.Dot().at((acc_gnd_x, GROUND_Y)).color(GND)
    d += elm.Dot().at(accel.GND).color(GND)

    # matrix ground exits left, over the top of the Pico, down the far-left column
    MGND_Y = matrix.GNDM[1]
    d += elm.Line().at(matrix.GNDM).tox(LEFT_X).color(GND)
    d += elm.Line().at((LEFT_X, MGND_Y)).toy(GROUND_Y).color(GND)
    d += elm.Dot().at((LEFT_X, GROUND_Y)).color(GND)
    d += elm.Dot().at(matrix.GNDM).color(GND)

    # --- 3.3 V power (red): Pico 3V3 -> accelerometer VIN, a straight run ---
    d += elm.Wire("-", arrow="->").at(pico["3V3"]).to(accel.VIN).color(PWR).label(
        "3V3 → VIN (3.3 V)", "top", ofst=0.12, color=PWR, fontsize=10)

    # --- 5 V power (red) along the top: USB 5 V on VBUS feeds the matrix ---
    d += elm.Dot().at((LEFT_X, PWR_Y)).color(PWR)
    d += elm.Line().at((LEFT_X, PWR_Y)).tox(matrix.V5[0]).color(PWR).label(
        "VBUS  (+5 V from the USB cable)", "top", ofst=0.15, color=PWR, fontsize=11)
    d += elm.Wire("|-").at(pico.VBUS).to((pico.VBUS[0], PWR_Y)).color(PWR)
    d += elm.Dot().at((pico.VBUS[0], PWR_Y)).color(PWR)
    d += elm.Dot().at(pico.VBUS).color(PWR)
    d += elm.Wire("-|").at((matrix.V5[0], PWR_Y)).to(matrix.V5).color(PWR)
    d += elm.Dot().at(matrix.V5).color(PWR)

    # =====================================================================
    # LEGEND (top-left, above the power rail) + TITLE
    # =====================================================================
    lx, ly = LEFT_X, PWR_Y + 2.6
    d += elm.Label().at((lx - 0.2, ly + 0.8)).label(
        "Wire colors", halign="left", fontsize=11, color=LBL)
    for clr, txt in ((PWR, "Power (+5 V and +3.3 V)"),
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
