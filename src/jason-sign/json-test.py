# JASON LED Sign - Each letter a different color
# Pixel ranges: J(0-7), A(8-20), S(21-33), O(34-47), N(48-64)

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# Define pixel ranges for each letter (start, end) - end is inclusive
LETTERS = {
    'J': (0, 7),
    'A': (8, 20),
    'S': (21, 33),
    'O': (34, 47),
    'N': (48, 64)
}

# Define colors for each letter (R, G, B)
COLORS = {
    'J': (255, 0, 0),      # Red
    'A': (255, 128, 0),    # Orange
    'S': (0, 255, 0),      # Green
    'O': (0, 0, 255),      # Blue
    'N': (128, 0, 255)     # Purple
}

def clear_strip():
    """Turn off all pixels"""
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()

def light_letter(letter, color):
    """Light up a single letter with the given color"""
    start, end = LETTERS[letter]
    for i in range(start, end + 1):
        strip[i] = color
    strip.write()

def light_all_letters():
    """Light up all letters with their assigned colors"""
    for letter in LETTERS:
        start, end = LETTERS[letter]
        color = COLORS[letter]
        for i in range(start, end + 1):
            strip[i] = color
    strip.write()

# Main program
clear_strip()

# Light up all letters at once with their colors
light_all_letters()
