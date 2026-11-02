# Lab 03: Clock Positions
# Filename: 03-clock-positions.py
# Version: 1.0.0
#
# Marks four places on the ring like a clock dial: 12 o'clock is red,
# 3 is green, 6 is blue and 9 is yellow. If red is not at the top, change
# TOP_PIXEL in config.py and run this program again.
#
# The function pixel_at() is the big idea. It lets us count "positions"
# clockwise from the top of the ring, no matter which pixel is really
# at the top. Many of the later labs use it.

from machine import Pin
from neopixel import NeoPixel
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS
TOP_PIXEL = config.TOP_PIXEL

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 150, 0)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# turn a position counted clockwise from the top into a pixel number
def pixel_at(position):
    return (TOP_PIXEL + position) % NUMBER_PIXELS

QUARTER = NUMBER_PIXELS // 4   # how many pixels make a quarter of the ring

strip[pixel_at(0)] = fade(red, 1)
strip[pixel_at(QUARTER)] = fade(green, 1)
strip[pixel_at(QUARTER * 2)] = fade(blue, 1)
strip[pixel_at(QUARTER * 3)] = fade(yellow, 1)
strip.write()

print("12 o'clock is pixel", pixel_at(0))
print(" 3 o'clock is pixel", pixel_at(QUARTER))
print(" 6 o'clock is pixel", pixel_at(QUARTER * 2))
print(" 9 o'clock is pixel", pixel_at(QUARTER * 3))
