# Lab 14: Cauldron Bubbles
# Filename: 14-cauldron-bubbles.py
# Version: 1.0.0
# Not yet tested on hardware.
#
# A witch's potion bubbles. Green and purple bubbles appear at the bottom
# of the strip (pixel 0), rise up, grow brighter and then pop in a white
# flash. A list of bubbles grows when one is born and shrinks when one pops.

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

DELAY = 0.04             # seconds between steps
MAX_BUBBLES = 6          # never more bubbles than this at once
NEW_BUBBLE_CHANCE = 15   # percent chance of a new bubble each step

potion = (0, 60, 10)     # the dark green potion all bubbles float in
bubble_colors = [(0, 255, 40), (140, 0, 255)]
pop_color = (200, 255, 200)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the strip is safe on battery power
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

bubbles = []             # each bubble is a list: [position, color, pop height]
while True:
    # maybe a new bubble is born at the bottom
    if len(bubbles) < MAX_BUBBLES and randint(1, 100) <= NEW_BUBBLE_CHANCE:
        color = bubble_colors[randint(0, 1)]
        pop_height = randint(NUMBER_PIXELS // 3, NUMBER_PIXELS - 1)
        bubbles.append([0, color, pop_height])

    strip.fill(fade(potion, 1))
    # go through a copy of the list so we can remove bubbles that pop
    for bubble in bubbles[:]:
        position, color, pop_height = bubble
        if position >= pop_height:
            strip[position] = fade(pop_color, 1)   # pop!
            bubbles.remove(bubble)
        else:
            # bubbles get brighter as they rise
            strip[position] = fade(color, 0.3 + 0.7 * position / pop_height)
            bubble[0] = position + 1
    strip.write()
    sleep(DELAY)
