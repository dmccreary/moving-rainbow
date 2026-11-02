# Lab 21: Ring Automaton
# Filename: 21-ring-automaton.py
# Version: 1.0.0
#
# A cellular automaton is a row of cells that are on or off. Each new
# generation, every cell looks at itself and its two neighbors and follows
# a rule. On a ring there are no edges, so every cell always has two
# neighbors. The rule number's bits hold the answer for each of the eight
# possible neighbor patterns. Rule 30 looks random even though it follows
# simple math. Each rule runs for a while, then the next rule starts.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS
TOP_PIXEL = config.TOP_PIXEL

DELAY = 0.2              # seconds between generations
GENERATIONS = 80         # how many generations each rule runs

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

rules = (30, 90, 110, 54, 150)

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

# start with one cell on, at the top of the ring
def first_generation():
    new_cells = [0] * NUMBER_PIXELS
    new_cells[TOP_PIXEL] = 1
    return new_cells

def next_generation(cells, rule):
    new_cells = [0] * NUMBER_PIXELS
    for i in range(NUMBER_PIXELS):
        left = cells[(i - 1) % NUMBER_PIXELS]
        right = cells[(i + 1) % NUMBER_PIXELS]
        # the three cells make a binary number from 0 to 7
        pattern = left * 4 + cells[i] * 2 + right
        # that number tells us which bit of the rule to look up
        new_cells[i] = (rule >> pattern) & 1
    return new_cells

rule_index = 0
generation = 0
cells = first_generation()
print('Rule', rules[rule_index])
while True:
    color = wheel(generation * 3 % 256)
    for i in range(NUMBER_PIXELS):
        strip[i] = fade(color, cells[i])
    strip.write()
    sleep(DELAY)
    cells = next_generation(cells, rules[rule_index])
    generation += 1
    if generation >= GENERATIONS:
        # time for the next rule
        rule_index = (rule_index + 1) % len(rules)
        generation = 0
        cells = first_generation()
        print('Rule', rules[rule_index])
    elif sum(cells) == 0:
        # every cell is off and would stay off, so start this rule again
        cells = first_generation()
