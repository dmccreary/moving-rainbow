# Lab 12: Blood Drip
# Filename: 12-blood-drip.py
# Version: 1.0.0
# Not yet tested on hardware.
#
# Red drops form at pixel 0, grow, then fall faster and faster down the
# strip like real drops. Each drop lands in a pool at the far end that
# slowly fills up, then drains away so it can fill again.
# A float (a number with a decimal point) holds the drop's speed.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

DELAY = 0.03             # seconds between steps
GRAVITY = 0.04           # how much faster the drop falls each step
POOL_MAX = 15            # the pool drains when it is this many pixels deep
GROW_STEPS = 30          # how many steps a drop takes to form

red = (255, 0, 0)
dark_red = (90, 0, 0)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the strip is safe on battery power
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

pool = 0                 # how many pixels deep the pool is
while True:
    # part 1: the drop slowly forms at the top
    for step in range(GROW_STEPS):
        strip[0] = fade(red, step / GROW_STEPS)
        strip.write()
        sleep(DELAY)

    # part 2: the drop falls, speeding up as it goes
    position = 0.0
    speed = 0.0
    bottom = NUMBER_PIXELS - 1 - pool    # the top of the pool
    while position < bottom:
        speed += GRAVITY                 # gravity speeds the drop up
        position += speed
        strip.fill((0, 0, 0))
        head = min(int(position), bottom)
        strip[head] = fade(red, 1)
        if head > 0:
            strip[head - 1] = fade(red, 0.3)   # a short streak behind the drop
        for p in range(pool):                  # draw the pool at the far end
            strip[NUMBER_PIXELS - 1 - p] = fade(dark_red, 1)
        strip.write()
        sleep(DELAY)

    # part 3: the drop joins the pool
    pool += 1
    if pool > POOL_MAX:
        # the pool drains away one pixel at a time
        while pool > 0:
            pool -= 1
            strip[NUMBER_PIXELS - 1 - pool] = (0, 0, 0)
            strip.write()
            sleep(DELAY * 3)
