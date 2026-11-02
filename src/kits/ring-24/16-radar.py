# Lab 16: Radar
# Filename: 16-radar.py
# Version: 1.0.0
#
# A green beam sweeps the ring like a radar screen. Each hidden target
# lights up red when the beam passes over it and then slowly fades. The
# targets drift a little between sweeps, just like airplanes.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.07             # seconds between steps - smaller is faster
TAIL_LENGTH = 12         # how many pixels long the beam's glow is
TARGET_COUNT = 3         # how many hidden targets there are
GLOW_FADE = 0.93         # each step a target keeps this much of its glow

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

green = (0, 255, 0)
red = (255, 0, 0)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

targets = []
for t in range(TARGET_COUNT):
    targets.append(randint(0, NUMBER_PIXELS - 1))
glow = [0.0] * NUMBER_PIXELS  # how brightly each pixel's target is glowing

beam = 0
while True:
    strip.fill((0, 0, 0))
    # draw the beam and the glow behind it
    for t in range(TAIL_LENGTH):
        strip[(beam - t) % NUMBER_PIXELS] = fade(green, (1 - t / TAIL_LENGTH) ** 3)
    # the beam lights up any target it touches
    if beam in targets:
        glow[beam] = 1.0
    # draw the glowing targets on top of the beam and fade them
    for i in range(NUMBER_PIXELS):
        if glow[i] > 0.02:
            strip[i] = fade(red, glow[i])
            glow[i] = glow[i] * GLOW_FADE
        else:
            glow[i] = 0.0
    strip.write()
    sleep(DELAY)
    beam = (beam + 1) % NUMBER_PIXELS
    if beam == 0:
        # the sweep is done, so each target drifts one pixel at most
        for t in range(TARGET_COUNT):
            targets[t] = (targets[t] + randint(-1, 1)) % NUMBER_PIXELS
