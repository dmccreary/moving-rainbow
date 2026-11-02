# Lab 12: Loading Spinner
# Filename: 12-loading-spinner.py
# Version: 1.0.0
#
# The busy spinner you see on a phone. An arc of light grows and shrinks
# while it goes around. While the arc grows its head runs ahead of its
# tail. While it shrinks its tail catches up.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.05             # seconds between steps - smaller is faster
SHORTEST = 2             # the arc never gets shorter than this
LONGEST = 20             # the arc never gets longer than this
COLOR_STEP = 40          # how far along the color wheel each new arc moves

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

tail = 0
length = SHORTEST
growing = True
hue = 0
while True:
    color = wheel(hue)
    strip.fill((0, 0, 0))
    for t in range(length):
        # dim at the tail, bright at the head
        amount = (t + 1) / length
        strip[(tail + t) % NUMBER_PIXELS] = fade(color, amount)
    strip.write()
    sleep(DELAY)
    if growing:
        tail = (tail + 1) % NUMBER_PIXELS
        length += 1
        if length >= LONGEST:
            growing = False
    else:
        tail = (tail + 2) % NUMBER_PIXELS
        length -= 1
        if length <= SHORTEST:
            growing = True
            hue = (hue + COLOR_STEP) % 256
