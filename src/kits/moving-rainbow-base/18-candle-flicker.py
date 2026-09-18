# Lab 18: Candle Flicker
# Filename: 18-candle-flicker.py
# Version: 1.0.0
#
# A warm, random flicker like a candle flame.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
# https://docs.micropython.org/en/latest/library/random.html
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def candle(delay):
    for i in range(0, NUMBER_PIXELS):
         green = 50 + randint(0,155)
         red = green + randint(25,50)
         strip[randint(0,NUMBER_PIXELS - 1)] = (red, green, 0)
         strip.write()
         sleep(delay)

counter = 0
while True:
   candle(.001)
   # wrap
   counter = counter % (NUMBER_PIXELS-1)
   counter += 1
