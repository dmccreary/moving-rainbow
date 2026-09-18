# Lab 08: Random
# Filename: 08-random.py
# Version: 1.0.0
#
# Light a pixel in a random color at a random location.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    location = randint(0, NUMBER_PIXELS-1)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    strip[location] = (red, green, blue)
    strip.write()
    sleep(.5)
    strip[location] = (0, 0, 0)
