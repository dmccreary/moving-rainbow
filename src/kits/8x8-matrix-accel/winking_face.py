# Module: Winking Face (the demo version of programs 09 and 11, used by program 19)
# Filename: winking_face.py
# Version: 1.0.0
#
# The smiley face from program 09 blinks, then winks at you, like program
# 11. It sleeps with kit.wait() in place of sleep(), so a press of a mode
# button in program 19 stops it right away. It does not use the tilt.

import kit

# the color key: which color each letter stands for
COLORS = {
    ".": (0, 0, 0),         # off
    "Y": (28, 22, 0),       # yellow
    "B": (0, 0, 32),        # blue
    "R": (32, 0, 0),        # red
}

# three pictures of the same face. Only row 2, the eyes, is different.
FACE = [
    "..YYYY..",
    ".YYYYYY.",
    "YYBYYBYY",
    "YYYYYYYY",
    "YRYYYYRY",
    "YYRRRRYY",
    ".YYYYYY.",
    "..YYYY..",
]

BLINK = [
    "..YYYY..",
    ".YYYYYY.",
    "Y..YY..Y",
    "YYYYYYYY",
    "YRYYYYRY",
    "YYRRRRYY",
    ".YYYYYY.",
    "..YYYY..",
]

WINK = [
    "..YYYY..",
    ".YYYYYY.",
    "YYBYY..Y",
    "YYYYYYYY",
    "YRYYYYRY",
    "YYRRRRYY",
    ".YYYYYY.",
    "..YYYY..",
]

# the animation: (picture, milliseconds to show it)
FRAMES = [
    (FACE, 2000),
    (BLINK, 150),
    (FACE, 1500),
    (WINK, 500),
]

def draw(picture):
    # look at every letter and give the pixel in the same spot its color
    for y in range(kit.HEIGHT):
        for x in range(kit.WIDTH):
            kit.strip[kit.xy(x, y)] = COLORS[picture[y][x]]
    kit.strip.write()

def run(settings=None):
    while True:
        for picture, ms in FRAMES:
            draw(picture)
            kit.wait(ms)
