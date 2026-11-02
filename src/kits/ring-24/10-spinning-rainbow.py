# Lab 10: Spinning Rainbow
# Filename: 10-spinning-rainbow.py
# Version: 1.0.0
#
# The color wheel from Lab 09 spins around the ring. Each step shifts every
# color along by one pixel. Try making it spin the other way!

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.05             # seconds between steps - smaller is faster

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

offset = 0
while True:
    for i in range(NUMBER_PIXELS):
        color = wheel(i * 256 // NUMBER_PIXELS)
        strip[(i + offset) % NUMBER_PIXELS] = fade(color, 1)
    strip.write()
    sleep(DELAY)
    offset = (offset + 1) % NUMBER_PIXELS
