# Lab 06: Walk the Pixels
# Filename: 06-walk-pixels.py
# Version: 1.0.0
#
# Lights one pixel at a time in strip order, from pixel 0 to pixel 63.
# Watch the path. A zig-zag path means the panel is serpentine wired.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

print("Lab 06: Walk the Pixels (version 1.0.0)")

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    for i in range(NUMBER_PIXELS):
        strip[i] = (40, 0, 40)
        strip.write()
        sleep(0.1)
        strip[i] = (0, 0, 0)    # erased by the next write()
