# Lab 04: Move a Pixel
# Filename: 04-move-pixel.py
# Version: 1.0.0
#
# A single orange pixel moves down all 60 pixels of the strip, one pixel
# at a time, then starts again at the beginning.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.05             # seconds between steps - smaller is faster

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# pumpkin orange, made dimmer by BRIGHTNESS so it is safe on battery power
orange = (int(255 * BRIGHTNESS), int(80 * BRIGHTNESS), 0)
off = (0, 0, 0)

while True:
    for i in range(NUMBER_PIXELS):
        strip[i] = orange       # turn on the pixel at position i
        strip.write()           # show it
        sleep(DELAY)
        # erase it in memory only - the next write() shows the change
        strip[i] = off
