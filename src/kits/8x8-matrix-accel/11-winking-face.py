# Lab 11: Winking Face
# Filename: 11-winking-face.py
# Version: 1.0.0
#
# An animation: the smiley face blinks, then winks at you. An animation is
# a list of pictures, called frames, shown one after another. Each frame
# has a picture and the number of seconds it stays on the matrix.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

print("Lab 11: Winking Face (version 1.0.0)")

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
MATRIX_WIDTH = config.MATRIX_WIDTH
MATRIX_HEIGHT = config.MATRIX_HEIGHT
SERPENTINE = config.SERPENTINE

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

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

# the animation: (picture, seconds to show it)
FRAMES = [
    (FACE, 2.0),
    (BLINK, 0.15),
    (FACE, 1.5),
    (WINK, 0.5),
]

def xy(x, y):
    if SERPENTINE and y % 2 == 1:
        return y * MATRIX_WIDTH + (MATRIX_WIDTH - 1 - x)
    return y * MATRIX_WIDTH + x

def draw(picture):
    # look at every letter and give the pixel in the same spot its color
    for y in range(MATRIX_HEIGHT):
        for x in range(MATRIX_WIDTH):
            letter = picture[y][x]
            strip[xy(x, y)] = COLORS[letter]
    strip.write()

while True:
    for picture, seconds in FRAMES:
        draw(picture)
        sleep(seconds)
