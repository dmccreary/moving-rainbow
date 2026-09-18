# Lab 45: Sorting Visualizer
# Filename: 45-sorting-visualizer.py
# Version: 1.0.0
#
# Watch a bubble sort in action! Each pixel's brightness represents a
# random value. On every pass, neighboring values are compared and
# swapped if they are out of order, until the whole strip is sorted.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

values = [randint(10, 255) for _ in range(NUMBER_PIXELS)]


def draw(highlight_a=None, highlight_b=None):
    for i in range(NUMBER_PIXELS):
        brightness = values[i]
        if i == highlight_a or i == highlight_b:
            strip[i] = (brightness, 0, 0)   # the pair being compared: red
        else:
            strip[i] = (0, brightness, 0)   # everything else: green
    strip.write()


draw()
sleep(1)

# bubble sort: repeatedly compare neighbors and swap them if out of order
for pass_num in range(NUMBER_PIXELS - 1):
    swapped = False
    for i in range(NUMBER_PIXELS - 1 - pass_num):
        draw(i, i + 1)
        sleep(0.03)
        if values[i] > values[i + 1]:
            values[i], values[i + 1] = values[i + 1], values[i]
            swapped = True
            draw(i, i + 1)
            sleep(0.03)
    if not swapped:
        break   # nothing moved this pass - the list is already sorted

draw()   # final result: sorted dimmest to brightest
print("sorted!", values)
