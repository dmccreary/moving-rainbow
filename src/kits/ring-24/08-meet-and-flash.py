# Lab 08: Meet and Flash
# Filename: 08-meet-and-flash.py
# Version: 1.0.0
#
# Two dots leave the top of the ring and go around opposite sides. The
# whole ring flashes when they meet at the bottom and again when they get
# back to the top. One dot adds to its position and the other subtracts.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS
TOP_PIXEL = config.TOP_PIXEL

DELAY = 0.08             # seconds between steps - smaller is faster

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

cyan = (0, 255, 255)
violet = (138, 43, 226)
white = (255, 255, 255)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# turn a position counted clockwise from the top into a pixel number
def pixel_at(position):
    return (TOP_PIXEL + position) % NUMBER_PIXELS

HALF = NUMBER_PIXELS // 2

distance = 0
while True:
    if distance % HALF == 0:
        # the dots are in the same place: at the top or at the bottom
        strip.fill(fade(white, 0.5))
    else:
        strip.fill((0, 0, 0))
        strip[pixel_at(distance)] = fade(cyan, 1)    # goes clockwise
        strip[pixel_at(-distance)] = fade(violet, 1) # goes counter-clockwise
    strip.write()
    sleep(DELAY)
    distance = (distance + 1) % NUMBER_PIXELS
