# Lab 04: Dimmer
# Filename: 04-dimmer.py
# Version: 1.0.0
#
# The first pixel fades up to red and back down again.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    
    for i in range(0,100):
        strip[0] = (i,0,0)
        strip.write()
        sleep(.01)
    
    for i in range(100,0,-1):
        strip[0] = (i,0,0)
        strip.write()
        sleep(.01)
