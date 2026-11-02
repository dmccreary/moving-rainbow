# Lab 20: Ring of Fire
# Filename: 20-ring-of-fire.py
# Version: 1.0.0
#
# A ring of flickering flames. Each pixel remembers how hot it is. Heat
# spreads to the pixels on each side, every pixel cools a little at
# random, and new sparks keep the fire going. There are no ends on a ring,
# so pixel 23 and pixel 0 share heat just like any other neighbors.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.05             # seconds between steps - smaller is faster
COOLING = 36             # the most heat a pixel can lose per step - try 20 or 60
SPARKS = 2               # how many new sparks start on each step

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# turn a heat from 0 to 255 into a color: dark red, then orange, then yellow
def heat_to_color(heat_value):
    if heat_value < 85:
        return (heat_value * 3, 0, 0)
    if heat_value < 170:
        return (255, (heat_value - 85) * 2, 0)
    return (255, 170 + (heat_value - 170), (heat_value - 170) // 2)

heat = [0] * NUMBER_PIXELS
while True:
    new_heat = [0] * NUMBER_PIXELS
    for i in range(NUMBER_PIXELS):
        # % makes the neighbors wrap around the ring
        left = heat[(i - 1) % NUMBER_PIXELS]
        right = heat[(i + 1) % NUMBER_PIXELS]
        # the average of this pixel and its neighbors, minus some cooling
        new_heat[i] = max(0, (left + heat[i] * 2 + right) // 4 - randint(0, COOLING))
    for s in range(SPARKS):
        spot = randint(0, NUMBER_PIXELS - 1)
        new_heat[spot] = min(255, new_heat[spot] + randint(120, 255))
    heat = new_heat
    for i in range(NUMBER_PIXELS):
        strip[i] = fade(heat_to_color(heat[i]), 1)
    strip.write()
    sleep(DELAY)
