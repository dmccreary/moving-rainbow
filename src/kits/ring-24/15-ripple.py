# Lab 15: Ripples
# Filename: 15-ripple.py
# Version: 1.0.0
#
# Drops land at random places. A ripple spreads out both ways from each
# drop, and the two sides of the ripple crash together on the far side
# of the ring. Where lights overlap, their colors add up.

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
DROP_CHANCE = 12         # percent chance of a new drop on each step
MOST_RIPPLES = 3         # the most ripples at one time
DIM = 0.6                # each step every pixel keeps this much of its light

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# add two colors together, keeping each part at 255 or less
def mix(color1, color2):
    return (min(color1[0] + color2[0], 255),
            min(color1[1] + color2[1], 255),
            min(color1[2] + color2[2], 255))

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

HALF = NUMBER_PIXELS // 2

ripples = []             # each ripple is a list: [center pixel, radius, color]
while True:
    # dim the whole ring a little so each ripple leaves a short trail
    for i in range(NUMBER_PIXELS):
        r, g, b = strip[i]
        strip[i] = (int(r * DIM), int(g * DIM), int(b * DIM))
    # maybe drop a new ripple
    if len(ripples) < MOST_RIPPLES and randint(1, 100) <= DROP_CHANCE:
        ripples.append([randint(0, NUMBER_PIXELS - 1), 0, wheel(randint(0, 255))])
    # draw every ripple and make it bigger
    for ripple in ripples[:]:   # [:] loops over a copy so we can remove items
        center, radius, color = ripple
        amount = 1 - 0.7 * radius / HALF    # ripples get dimmer as they spread
        for pixel in (center + radius, center - radius):
            pixel = pixel % NUMBER_PIXELS
            strip[pixel] = mix(strip[pixel], fade(color, amount))
        if radius >= HALF:
            ripples.remove(ripple)      # the two sides have met on the far side
        else:
            ripple[1] = radius + 1
    strip.write()
    sleep(DELAY)
