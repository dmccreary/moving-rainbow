# Test 07: X-Y Corners
# Filename: 07-xy-corners.py
# Version: 1.0.0
#
# Tests the xy() function that turns a column and row into a pixel number.
# Red is (0, 0), green is the far end of row 0, blue is the far end of
# column 0, and white is the opposite corner. If the corners are not in
# the right places, change SERPENTINE in config.py.
# Not yet tested on hardware.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

print("Test 07: X-Y Corners (version 1.0.0)")

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
MATRIX_WIDTH = config.MATRIX_WIDTH
MATRIX_HEIGHT = config.MATRIX_HEIGHT
SERPENTINE = config.SERPENTINE

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def xy(x, y):
    # row y starts at pixel y * width; odd rows run backwards on a zig-zag panel
    if SERPENTINE and y % 2 == 1:
        return y * MATRIX_WIDTH + (MATRIX_WIDTH - 1 - x)
    return y * MATRIX_WIDTH + x

last_x = MATRIX_WIDTH - 1
last_y = MATRIX_HEIGHT - 1

strip[xy(0, 0)] = (60, 0, 0)
strip[xy(last_x, 0)] = (0, 60, 0)
strip[xy(0, last_y)] = (0, 0, 60)
strip[xy(last_x, last_y)] = (40, 40, 40)
strip.write()
print("red = (0,0)  green = (%d,0)  blue = (0,%d)  white = (%d,%d)" % (last_x, last_y, last_x, last_y))

while True:
    sleep(1)
