# Rotary Spinner Box - Comet
# Filename: 06-comet.py
#
# This pattern is a scanner with a glowing tail, like a comet flying back and
# forth along the strip.  The head is bright and each pixel behind it is a
# little dimmer.
#
# Because this is a straight strip (not a ring), the comet turns around when it
# reaches an end.  The tail always trails BEHIND the head, so when the comet
# reverses direction the tail flips to the other side of the head.
#
# New idea in this lab: instead of lighting one pixel at a time, we figure out
# a color for EVERY pixel on each step, based on how far it is behind the head.

from neopixel import NeoPixel
import machine
from utime import sleep

import config

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# The base color of the comet head
HEAD_COLOR = (0, 80, 120)

# How many pixels long the fading tail is
TAIL_LENGTH = 5

# How long to wait between steps, in seconds
DELAY = 0.06

# Where the bright head is, and which way it is moving
head = 0
direction = 1

print('Comet running. Watch the glowing tail follow the head back and forth.')

while True:
    # Figure out the color of every pixel for this step
    for i in range(config.NUMBER_PIXELS):
        # "behind" counts how many pixels pixel i is behind the head, measured
        # in the direction the comet is moving.  0 is the head itself.
        behind = (head - i) * direction
        if 0 <= behind < TAIL_LENGTH:
            # brightness fades from 1.0 at the head to near 0 at the tail end
            fade = (TAIL_LENGTH - behind) / TAIL_LENGTH
            strip[i] = (int(HEAD_COLOR[0] * fade),
                        int(HEAD_COLOR[1] * fade),
                        int(HEAD_COLOR[2] * fade))
        else:
            # pixels ahead of the head or past the tail are off
            strip[i] = (0, 0, 0)
    strip.write()
    sleep(DELAY)

    # if we are at either end, turn around
    if head == 0:
        direction = 1
    elif head == config.NUMBER_PIXELS - 1:
        direction = -1

    # move the head one step in the current direction
    head = head + direction
