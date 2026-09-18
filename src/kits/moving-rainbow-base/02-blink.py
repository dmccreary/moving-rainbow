# Lab 02: Blink
# Filename: 02-blink.py
# Version: 1.0.0
#
# Blink the first pixel red: one second on, one second off.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    
    # turn the first pixel on
    strip[0] = (100,0,0)
    strip.write()
    sleep(1)
    
    # turn the first pixel off
    strip[0] = (0,0,0)
    strip.write()
    sleep(1)
