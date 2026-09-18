# Lab 06: Up and Down
# Filename: 06-up-and-down.py
# Version: 1.0.0
#
# A red pixel moves up the strip and then back down again.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
while True:
    
    # Each step calls strip.write() once. Erasing a pixel does not need its own
    # write - the next step's write shows it. (The strip can miss back-to-back writes.)
    # move up the strip
    for i in range(0,NUMBER_PIXELS):
        strip[i] = (100,0,0)
        strip.write()
        sleep(.05)
        strip[i] = (0,0,0)
    
    # move down the strip
    for i in range(NUMBER_PIXELS-1, 0, -1):
        strip[i] = (100,0,0)
        strip.write()
        sleep(.05)
        strip[i] = (0,0,0)
