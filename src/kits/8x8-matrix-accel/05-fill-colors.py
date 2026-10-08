# Lab 05: Fill Colors
# Filename: 05-fill-colors.py
# Version: 1.0.0
#
# Fills all 64 pixels with red, green, blue and white in turn.
# The color numbers stay small (LEVEL in config.py) because every pixel
# is lit at once.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

print("Lab 05: Fill Colors (version 1.0.0)")

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
LEVEL = config.LEVEL

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

colors = [
    ("red", (LEVEL, 0, 0)),
    ("green", (0, LEVEL, 0)),
    ("blue", (0, 0, LEVEL)),
    ("white", (LEVEL, LEVEL, LEVEL)),
]

while True:
    for name, color in colors:
        print("Fill:", name)
        for i in range(NUMBER_PIXELS):
            strip[i] = color
        strip.write()
        sleep(1.5)
