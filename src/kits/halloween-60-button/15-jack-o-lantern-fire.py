# Lab 15: Jack-o'-Lantern Fire
# Filename: 15-jack-o-lantern-fire.py
# Version: 1.0.0
# Not yet tested on hardware.
#
# A flickering fire like the candle inside a jack-o'-lantern. Every pixel
# has a "heat" number from 0 to 255 kept in a list. Each step the heat
# cools, drifts up the strip and new sparks start at pixel 0. Then the
# heat of each pixel is turned into a color from dark red to yellow.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
from urandom import randint

DELAY = 0.03             # seconds between steps
COOLING = 55             # bigger numbers make shorter flames
SPARKING = 120           # bigger numbers (up to 255) make a busier fire

heat = [0] * NUMBER_PIXELS   # a list with one heat number for every pixel

# turn a heat number (0 to 255) into a fire color
def heat_to_color(t):
    if t < 85:
        # cool: black to red
        return (t * 3, 0, 0)
    elif t < 170:
        # warm: red to orange
        return (255, (t - 85) * 2, 0)
    else:
        # hot: orange to yellow
        return (255, 170 + (t - 170), (t - 170) // 2)

while True:
    # step 1: every pixel cools down a little
    for i in range(NUMBER_PIXELS):
        cooldown = randint(0, (COOLING * 10) // NUMBER_PIXELS + 2)
        heat[i] = max(0, heat[i] - cooldown)

    # step 2: heat drifts up the strip, mixing with the pixels below it
    for i in range(NUMBER_PIXELS - 1, 1, -1):
        heat[i] = (heat[i - 1] + heat[i - 2] * 2) // 3

    # step 3: sometimes a new spark lights near the bottom
    if randint(0, 255) < SPARKING:
        spot = randint(0, 6)
        heat[spot] = min(255, heat[spot] + randint(160, 255))

    # step 4: turn each heat number into a color and show it
    for i in range(NUMBER_PIXELS):
        r, g, b = heat_to_color(heat[i])
        strip[i] = (int(r * BRIGHTNESS), int(g * BRIGHTNESS), int(b * BRIGHTNESS))
    strip.write()
    sleep(DELAY)
