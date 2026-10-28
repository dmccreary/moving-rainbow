# Module: Fill Colors (the demo version of program 05, used by program 14)
# Filename: fill_colors.py
# Version: 1.0.0
#
# Fills all 256 pixels with red, green, blue and white in turn, like
# program 05. It sleeps with kit.wait() in place of sleep(), so a press of
# a mode button in program 14 stops it right away. It does not use the tilt.

import config
import kit

# every pixel is lit at once, so the color numbers stay small
LEVEL = config.LEVEL
HOLD_MS = 1500          # how long each color stays

COLORS = [
    (LEVEL, 0, 0),          # red
    (0, LEVEL, 0),          # green
    (0, 0, LEVEL),          # blue
    (LEVEL, LEVEL, LEVEL),  # white
]

def run(settings=None):
    while True:
        for color in COLORS:
            for i in range(kit.NUMBER_PIXELS):
                kit.strip[i] = color
            kit.strip.write()
            kit.wait(HOLD_MS)
