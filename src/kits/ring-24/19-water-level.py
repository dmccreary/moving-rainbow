# Lab 19: Water Level
# Filename: 19-water-level.py
# Version: 1.0.0
#
# Water fills the ring from the bottom, climbing up both sides at once,
# and then drains away again. Each pixel only needs to know how far it
# is from the bottom. The left and right sides are mirror images.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS
TOP_PIXEL = config.TOP_PIXEL

DELAY = 0.18             # seconds between steps - smaller is faster

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

deep_water = (0, 40, 255)
surface = (120, 220, 255)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# turn a position counted clockwise from the top into a pixel number
def pixel_at(position):
    return (TOP_PIXEL + position) % NUMBER_PIXELS

BOTTOM = NUMBER_PIXELS // 2    # the position at 6 o'clock
FULL = BOTTOM + 1              # the water level when the whole ring is full

step = 0
while True:
    # level counts 0, 1, ... FULL, then back down to 0
    level = FULL - abs(step - FULL)
    for position in range(NUMBER_PIXELS):
        distance = abs(position - BOTTOM)    # how far above the bottom this pixel is
        if distance < level - 1:
            strip[pixel_at(position)] = fade(deep_water, 1)
        elif distance == level - 1:
            strip[pixel_at(position)] = fade(surface, 1)   # the top of the water
        else:
            strip[pixel_at(position)] = (0, 0, 0)
    strip.write()
    sleep(DELAY)
    step = (step + 1) % (FULL * 2)
