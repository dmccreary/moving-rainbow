#!/usr/bin/env python3
"""Build the printable Demo Mode Guide for the Tilt-a-Rainbow Mini kit.

1. Draws a picture of each of the 18 modes of 19-template-main.py by running
   the real mode modules from src/kits/8x8-matrix-accel on this computer.
   Stand-ins replace the Pico's hardware modules (machine, neopixel, utime,
   urandom, ustruct). The clock is pretend: sleep_ms() moves it forward at
   once, so a mode that runs for 6 seconds takes a moment. The tilt sensor
   reports whatever each scene asks for. Each picture is the last frame the
   mode wrote to the strip when its scene ended.
2. Puts those pictures and a QR code into demo-mode-guide.html, between the
   <!--M1--> ... <!--/M1--> and <!--QR--> ... <!--/QR--> markers.
3. Writes img/demo-modes.svg, the same pictures as one grid for the Lab 19 page.
4. Renders demo-mode-guide.pdf (US Letter) with the installed Google Chrome.

Requires: pip install segno playwright
Usage:    scripts/demo-mode-guide/build.sh
"""
import importlib
import io
import math
import random
import re
import struct
import sys
import types
from pathlib import Path

import segno
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
KIT_SRC = ROOT / "src" / "kits" / "8x8-matrix-accel"
KIT_DOCS = ROOT / "docs" / "kits" / "8x8-matrix-accel"
HTML = KIT_DOCS / "demo-mode-guide.html"
PDF = KIT_DOCS / "demo-mode-guide.pdf"
GRID_SVG = KIT_DOCS / "img" / "demo-modes.svg"
URL = "https://dmccreary.github.io/moving-rainbow/kits/8x8-matrix-accel/19-template-main/"


# ---------------------------------------------------------------- stand-ins

class Clock:
    now = 0


clock = Clock()
tilt = [0.0, 0.0]       # the pull the scene asks for: (gx, gy) in g, toward the low side


def ticks_ms():
    return clock.now


def ticks_diff(a, b):
    return a - b


def sleep_ms(ms):
    clock.now += ms


def sleep(seconds):
    clock.now += int(seconds * 1000)


class Pin:
    IN = 0
    OUT = 1
    PULL_UP = 1

    def __init__(self, *args, **kwargs):
        pass

    def value(self, *args):
        return 1        # a button that is never pressed


class I2C:
    def __init__(self, *args, **kwargs):
        pass

    def writeto_mem(self, *args):
        pass

    def readfrom_mem(self, address, register, count):
        # undo kit.py's SWAP_XY, FLIP_X and FLIP_Y so read_tilt() returns `tilt`
        kit = sys.modules["kit"]
        gx, gy = tilt
        if kit.FLIP_Y:
            gy = -gy
        if kit.FLIP_X:
            gx = -gx
        if kit.SWAP_XY:
            gx, gy = gy, gx
        counts = [max(-32768, min(32767, int(g * kit.COUNTS_PER_G))) for g in (gx, gy, 1.0)]
        return struct.pack("<hhh", *counts)


class NeoPixel:
    def __init__(self, pin, count):
        self.pixels = [(0, 0, 0)] * count
        self.shown = list(self.pixels)

    def __setitem__(self, i, color):
        self.pixels[i] = tuple(color)

    def __getitem__(self, i):
        return self.pixels[i]

    def __len__(self):
        return len(self.pixels)

    def write(self):
        self.shown = list(self.pixels)


def install_stand_ins():
    fakes = {
        "machine": {"Pin": Pin, "I2C": I2C},
        "neopixel": {"NeoPixel": NeoPixel},
        "utime": {"ticks_ms": ticks_ms, "ticks_diff": ticks_diff,
                  "sleep_ms": sleep_ms, "sleep": sleep},
        "urandom": {"randint": random.randint},
    }
    for name, members in fakes.items():
        module = types.ModuleType(name)
        module.__dict__.update(members)
        sys.modules[name] = module
    sys.modules["ustruct"] = struct
    sys.path.insert(0, str(KIT_SRC))


# ------------------------------------------------------------------- scenes

class SceneOver(Exception):
    pass


def steady(gx, gy):
    return lambda t: (gx, gy)


def sketch_spiral(t):
    # Tilt-a-sketch takes one step every 140 ms at full tilt. Step k happens
    # at time 140 * k, so tip the board the way step k should go: a square
    # spiral out from the middle with a gap between its rings, then hold the
    # board flat. Each run ends right at an edge, so no step is blocked.
    turns = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    lengths = [2, 2, 4, 4, 5, 5, 7, 7]
    step = max(1, math.ceil(t / 140))
    for i, length in enumerate(lengths):
        if step <= length:
            dx, dy = turns[i % 4]
            return (0.9 * dx, 0.9 * dy)
        step -= length
    return (0.0, 0.0)


# (mode number, name, short label for the grid, module, settings,
# milliseconds to run, tilt over time). The settings match MODES in
# 19-template-main.py. The time picks a frame worth showing, for example the
# wink rather than the plain face.
SCENES = [
    (1, "Fill colors", "Fill", "fill_colors", None, 1000, None),
    (2, "Walk the pixels", "Walk", "walk_pixels", None, 2650, None),
    (3, "Row and column sweep", "Sweep", "row_column_sweep", None, 300, None),
    (4, "Winking face", "Wink", "winking_face", None, 3800, None),
    (5, "Picture show", "Pictures", "picture_show", None, 3500, None),
    (6, "Scrolling message", "Message", "scroll_text", {"text": "MOVING RAINBOW!", "speed": 9}, 940, None),
    (7, "Three dots", "Three dots", "bounce_dots", {"colors": "RGB", "speed": 2.5, "fade": 0}, 2000, None),
    (8, "Seven dots", "Seven dots", "bounce_dots", {"colors": "RAINBOW", "speed": 4, "fade": 0}, 2000, None),
    (9, "Colors with trails", "Trails", "bounce_dots", {"colors": "PALETTE", "speed": 5, "fade": 215}, 2500, None),
    (10, "Rainbow rain", "Rain", "rain", None, 3000, None),
    (11, "Ripple rings", "Rings", "rings", None, 2000, None),
    (12, "Accelerometer bubble", "Bubble", "accel_bubble", None, 500, steady(0.6, -0.5)),
    (13, "Tilt one dot", "Tilt one", "tilt_balls", {"colors": "BLUE"}, 700, steady(0.5, 0.5)),
    (14, "Tilt three dots", "Tilt three", "tilt_balls", {"colors": "RGB"}, 2500, steady(0.6, 0.4)),
    (15, "Tilt seven dots", "Tilt seven", "tilt_balls", {"colors": "RAINBOW"}, 3000, steady(0.3, 0.7)),
    (16, "Sloshing water", "Slosh", "sloshing_water", None, 1500, steady(0.45, 0.89)),
    (17, "Tilt-a-maze", "Maze", "tilt_a_maze", None, 1700, None),
    (18, "Tilt-a-sketch", "Sketch", "tilt_a_sketch", {"auto_color": True}, 5100, sketch_spiral),
]


def kit_colors(kit, name):
    return {"RGB": [kit.RED, kit.GREEN, kit.BLUE], "RAINBOW": kit.RAINBOW,
            "PALETTE": kit.PALETTE, "BLUE": [kit.BLUE]}[name]


def run_scene(kit, number, module_name, settings, run_ms, tilt_at):
    # a fresh copy of the module each time, like unload() in program 19
    for name in (module_name, "pictures"):
        sys.modules.pop(name, None)
    random.seed(number)
    clock.now = 0
    tilt[:] = [0.0, 0.0]
    kit.clear()
    kit.strip.write()
    if settings and isinstance(settings.get("colors"), str):
        settings = dict(settings, colors=kit_colors(kit, settings["colors"]))

    def check():
        if tilt_at:
            tilt[:] = tilt_at(clock.now)
        if clock.now >= run_ms:
            raise SceneOver()

    kit.check = check
    module = importlib.import_module(module_name)
    try:
        module.run(settings)
    except SceneOver:
        pass
    return list(kit.strip.shown)


def draw_all_modes():
    install_stand_ins()
    kit = importlib.import_module("kit")
    kit.mode_buttons_on = True      # as in program 19: the sketch leaves the buttons alone
    frames = {}
    for number, name, short, module_name, settings, run_ms, tilt_at in SCENES:
        frames[number] = (name, short, run_scene(kit, number, module_name, settings, run_ms, tilt_at))
    return kit, frames


# --------------------------------------------------------------- drawing

def screen_color(color):
    # LED color numbers are small (up to about 48), but a lit LED looks
    # bright. Stretch the brightest part to full, then dim faint pixels
    # (trails, water) a little so they still look faint.
    top = max(color)
    if top == 0:
        return None
    strength = 0.45 + 0.55 * min(1.0, top / 40) ** 0.5
    return "#%02x%02x%02x" % tuple(round(255 * c / top * strength) for c in color)


def matrix_svg(kit, pixels, size_attrs='viewBox="0 0 84 84"'):
    # an 8x8 panel: dark board, dim dots for off pixels, glowing dots for lit ones
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" %s>' % size_attrs,
             '<rect x="0" y="0" width="84" height="84" rx="7" fill="#12151b"/>']
    for y in range(kit.HEIGHT):
        for x in range(kit.WIDTH):
            cx = 7 + 10 * x
            cy = 7 + 10 * y
            color = screen_color(pixels[kit.xy(x, y)])
            if color is None:
                parts.append('<circle cx="%d" cy="%d" r="3.2" fill="#2a2f39"/>' % (cx, cy))
            else:
                parts.append('<circle cx="%d" cy="%d" r="5" fill="%s" fill-opacity="0.35"/>' % (cx, cy, color))
                parts.append('<circle cx="%d" cy="%d" r="3.6" fill="%s"/>' % (cx, cy, color))
                parts.append('<circle cx="%d" cy="%d" r="1.3" fill="#fff" fill-opacity="0.55"/>' % (cx, cy))
    parts.append("</svg>")
    return "".join(parts)


def grid_svg(kit, frames):
    # all 18 modes, 6 across, each with its number and name above it
    across = 6
    cell_w, cell_h = 104, 112
    rows = math.ceil(len(frames) / across)
    width = across * cell_w + 8
    height = rows * cell_h + 8
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">' % (width, height, width * 2, height * 2),
             '<rect width="100%" height="100%" fill="#ffffff"/>']
    for i, number in enumerate(sorted(frames)):
        name, short, pixels = frames[number]
        left = 8 + (i % across) * cell_w
        top = 8 + (i // across) * cell_h
        parts.append('<text x="%d" y="%d" font-family="Helvetica, Arial, sans-serif" font-size="10" fill="#1d2733">%d %s</text>'
                     % (left, top + 10, number, short))
        inner = matrix_svg(kit, pixels, 'x="%d" y="%d" width="94" height="94" viewBox="0 0 84 84"' % (left, top + 16))
        parts.append(inner.replace(' xmlns="http://www.w3.org/2000/svg"', ""))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def qr_svg():
    buf = io.BytesIO()
    segno.make(URL, error="m").save(
        buf, kind="svg", scale=1, border=1, xmldecl=False, svgns=True,
        dark="#14325c", light="#ffffff", omitsize=True, lineclass=None,
    )
    return buf.getvalue().decode()


def fill_markers(kit, frames):
    text = HTML.read_text()
    for number, (name, short, pixels) in frames.items():
        block = "<!--M%d-->%s<!--/M%d-->" % (number, matrix_svg(kit, pixels), number)
        text, found = re.subn(r"<!--M%d-->.*?<!--/M%d-->" % (number, number),
                              lambda m: block, text, flags=re.S)
        if found != 1:
            sys.exit("demo-mode-guide.html needs exactly one <!--M%d--><!--/M%d--> marker" % (number, number))
    text, found = re.subn(r"<!--QR-->.*?<!--/QR-->", lambda m: "<!--QR-->%s<!--/QR-->" % qr_svg(),
                          text, flags=re.S)
    if found != 1:
        sys.exit("demo-mode-guide.html needs exactly one <!--QR--><!--/QR--> marker")
    HTML.write_text(text)


def render_pdf():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        page = browser.new_page()
        page.goto(HTML.as_uri())
        page.wait_for_load_state("networkidle")
        page.pdf(path=str(PDF), width="8.5in", height="11in",
                 print_background=True, prefer_css_page_size=True)
        browser.close()


if __name__ == "__main__":
    kit, frames = draw_all_modes()
    for number, (name, short, pixels) in sorted(frames.items()):
        lit = sum(1 for c in pixels if c != (0, 0, 0))
        print("mode %2d %-22s %2d pixels lit" % (number, name, lit))
    GRID_SVG.write_text(grid_svg(kit, frames))
    print("Wrote", GRID_SVG.relative_to(ROOT))
    if "--pictures-only" in sys.argv:
        sys.exit(0)
    fill_markers(kit, frames)
    print("Updated", HTML.relative_to(ROOT))
    render_pdf()
    print("Wrote", PDF.relative_to(ROOT))
