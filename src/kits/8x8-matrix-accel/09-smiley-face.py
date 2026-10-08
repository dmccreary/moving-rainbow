# Lab 09: Smiley Face
# Filename: 09-smiley-face.py
# Version: 1.0.0
#
# Draws a smiley face. The picture is 8 lines of text, one line for each
# row of the matrix. Each letter stands for a color in the color key.
# Change the letters to draw your own picture.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

print("Lab 09: Smiley Face (version 1.0.0)")

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

# the picture: 8 rows of 8 letters
SMILEY = [
    "..YYYY..",
    ".YYYYYY.",
    "YYBYYBYY",
    "YYYYYYYY",
    "YRYYYYRY",
    "YYRRRRYY",
    ".YYYYYY.",
    "..YYYY..",
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

draw(SMILEY)

while True:
    sleep(1)
