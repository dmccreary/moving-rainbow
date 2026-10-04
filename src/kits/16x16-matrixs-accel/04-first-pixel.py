# Test 04: First Pixel
# Filename: 04-first-pixel.py
# Version: 1.0.0
#
# Lights pixel 0 red, then green, then blue. If the colors come out in
# the wrong order, your pixels use a different color order.
# Not yet tested on hardware.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

print("Test 04: First Pixel (version 1.0.0)")

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

colors = [("red", (40, 0, 0)), ("green", (0, 40, 0)), ("blue", (0, 0, 40))]

while True:
    for name, color in colors:
        print("Pixel 0 should be", name)
        strip[0] = color
        strip.write()
        sleep(1)
