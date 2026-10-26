# Lab 13: Bat Swarm
# Filename: 13-bat-swarm.py
# Version: 1.0.0
# Not yet tested on hardware.
#
# A swarm of purple bats flutters along the strip. Every bat has its own
# position and its own speed, stored in two lists, so they all fly
# differently. When a bat leaves one end it comes back in at the other.

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

DELAY = 0.03             # seconds between steps
NUMBER_OF_BATS = 6

bat_color = (140, 0, 255)
moon_color = (40, 30, 0) # a dim yellow glow behind the bats

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the strip is safe on battery power
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# make the lists: one position and one speed for every bat
positions = []
speeds = []
for b in range(NUMBER_OF_BATS):
    positions.append(randint(0, NUMBER_PIXELS - 1))
    # speed is in pixels per step; a negative speed flies backward
    speed = randint(10, 40) / 100
    if randint(0, 1) == 0:
        speed = -speed
    speeds.append(speed)

flap = 0
while True:
    strip.fill(fade(moon_color, 1))     # the night sky
    flap += 1
    for b in range(NUMBER_OF_BATS):
        positions[b] = (positions[b] + speeds[b]) % NUMBER_PIXELS
        index = int(positions[b])
        # bats flap: every few steps a bat is a little dimmer
        if (flap + b) % 6 < 3:
            strip[index] = fade(bat_color, 1)
        else:
            strip[index] = fade(bat_color, 0.4)
        # each bat has a wing on the pixel next to it
        strip[(index + 1) % NUMBER_PIXELS] = fade(bat_color, 0.2)
    strip.write()
    sleep(DELAY)
