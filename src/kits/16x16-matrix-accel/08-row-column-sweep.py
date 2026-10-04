# Test 08: Row and Column Sweep
# Filename: 08-row-column-sweep.py
# Version: 1.0.0
#
# A bar of light sweeps down the rows and then across the columns.
# Both sweeps should look like straight lines.
# Not yet tested on hardware.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

print("Test 08: Row and Column Sweep (version 1.0.0)")

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
MATRIX_WIDTH = config.MATRIX_WIDTH
MATRIX_HEIGHT = config.MATRIX_HEIGHT
SERPENTINE = config.SERPENTINE
LEVEL = config.LEVEL

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def xy(x, y):
    if SERPENTINE and y % 2 == 1:
        return y * MATRIX_WIDTH + (MATRIX_WIDTH - 1 - x)
    return y * MATRIX_WIDTH + x

def clear():
    for i in range(NUMBER_PIXELS):
        strip[i] = (0, 0, 0)

while True:
    for y in range(MATRIX_HEIGHT):
        clear()
        for x in range(MATRIX_WIDTH):
            strip[xy(x, y)] = (0, LEVEL, 0)
        strip.write()
        sleep(0.12)
    for x in range(MATRIX_WIDTH):
        clear()
        for y in range(MATRIX_HEIGHT):
            strip[xy(x, y)] = (0, 0, LEVEL)
        strip.write()
        sleep(0.12)
