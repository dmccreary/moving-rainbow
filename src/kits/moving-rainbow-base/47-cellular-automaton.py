# Rule 30: a simple rule turns one row of pixels into the next, one
# generation at a time. Watch the pattern grow more complex over time!
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

ON_COLOR = (0, 150, 200)
OFF_COLOR = (0, 0, 0)

# Rule 30 is named after the number 30 itself: written in binary, 30 is
# 00011110. Each bit answers "does this 3-cell neighborhood turn on?" for
# one of the 8 possible neighborhoods (000 through 111).
RULE = 30


def next_generation(cells):
    n = len(cells)
    new_cells = [0] * n
    for i in range(n):
        left = cells[(i - 1) % n]
        center = cells[i]
        right = cells[(i + 1) % n]
        # turn the 3 neighbor cells into a number from 0 to 7
        pattern = (left << 2) | (center << 1) | right
        # look up that bit inside the number 30
        new_cells[i] = (RULE >> pattern) & 1
    return new_cells


def draw(cells):
    for i in range(len(cells)):
        strip[i] = ON_COLOR if cells[i] else OFF_COLOR
    strip.write()


# start with a single lit pixel in the middle
cells = [0] * config.NUMBER_PIXELS
cells[config.NUMBER_PIXELS // 2] = 1

while True:
    draw(cells)
    sleep(0.3)
    cells = next_generation(cells)
