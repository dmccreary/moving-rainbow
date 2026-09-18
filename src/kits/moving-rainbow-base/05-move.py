# Lab 05: Move a Pixel
# Filename: 05-move.py
# Version: 1.0.0
#
# A single red pixel moves along the strip, one pixel at a time.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    for i in range(0,NUMBER_PIXELS):
        strip[i] = (100,0,0)
        strip.write()
        sleep(.1)
        # erase the pixel. The next strip.write() shows the change, so we
        # do not write again right away (the strip can miss back-to-back writes)
        strip[i] = (0,0,0)
    
