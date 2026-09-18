# Lab 03: Red, Green and Blue
# Filename: 03-red-green-blue.py
# Version: 1.0.0
#
# The first pixel turns red, then green, then blue, one second each.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    
    # turn the first pixel red
    strip[0] = (100,0,0)
    strip.write()
    sleep(1)
    
    # turn the first pixel green
    strip[0] = (0,100,0)
    strip.write()
    sleep(1)
    
    # turn the first pixel green
    strip[0] = (0,0,100)
    strip.write()
    sleep(1)
