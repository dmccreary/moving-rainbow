# BOOKSTORE LED Sign - Each letter a different color
# Filename: bookstore-colors.py
#
# The word "BOOKSTORE" has 9 letters laid out across 134 pixels.
# Because the letter 'O' appears THREE times, we cannot key the data by
# letter in a dictionary (dictionary keys must be unique).  Instead we use
# one ordered LIST where each item carries the letter, its pixel range
# (start, end - inclusive) and its color (R, G, B).  The colors run through
# a rainbow from left to right.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# Initialize the LED strip
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# (letter, start, end, color) - end is inclusive, color is (R, G, B)
LETTER_LAYOUT = [
    ('B',   0,  19, (255,   0,   0)),  # Red
    ('O',  20,  33, (255, 128,   0)),  # Orange
    ('O',  34,  47, (255, 255,   0)),  # Yellow
    ('K',  48,  61, (  0, 255,   0)),  # Green
    ('S',  62,  77, (  0, 255, 255)),  # Cyan
    ('T',  78,  87, (  0,   0, 255)),  # Blue
    ('O',  88, 101, (255,   0, 255)),  # Purple
    ('R', 102, 118, (255,  50,  50)),  # Pink
    ('E', 119, 133, (255, 255, 255)),  # White
]


def clear_strip():
    """Turn off all pixels."""
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()


def light_all_letters():
    """Light up every letter with its assigned color."""
    for letter, start, end, color in LETTER_LAYOUT:
        for i in range(start, end + 1):
            strip[i] = color
    strip.write()


# Main program
clear_strip()
light_all_letters()

# Print what we lit up so students can see the layout
for letter, start, end, color in LETTER_LAYOUT:
    print('Letter', letter, 'pixels', start, 'to', end, 'color', color)
