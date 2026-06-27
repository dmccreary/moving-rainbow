# Rotary Spinner Box - Comet
# Filename: 06-comet.py
#
# This pattern is a spinner with a glowing tail, like a comet flying around
# the ring.  The head is bright and each pixel behind it is a little dimmer.
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

# Where the bright head is right now
head = 0

print('Comet running. Watch the glowing tail follow the head.')

while True:
    # Figure out the color of every pixel for this step
    for i in range(config.NUMBER_PIXELS):
        # distance is how many pixels this one is behind the head
        distance = (head - i) % config.NUMBER_PIXELS
        if distance < TAIL_LENGTH:
            # brightness fades from 1.0 at the head to near 0 at the tail end
            fade = (TAIL_LENGTH - distance) / TAIL_LENGTH
            strip[i] = (int(HEAD_COLOR[0] * fade),
                        int(HEAD_COLOR[1] * fade),
                        int(HEAD_COLOR[2] * fade))
        else:
            # pixels outside the tail are off
            strip[i] = (0, 0, 0)
    strip.write()
    sleep(DELAY)

    # move the head forward one pixel, wrapping at the end
    head = (head + 1) % config.NUMBER_PIXELS
