# Lab 17: Planets
# Filename: 17-planets.py
# Version: 1.0.0
#
# Four planets orbit at different speeds, so they keep passing each other.
# Each planet's position is a decimal number like 7.25. To show that spot,
# 75% of its light goes on pixel 7 and 25% on pixel 8, so a planet can glide
# smoothly between pixels even when it moves slowly.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

DELAY = 0.03             # seconds between steps - smaller is faster

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

# share one color between the two pixels closest to a decimal position
def draw_soft(position, color):
    lower = int(position)
    upper = (lower + 1) % NUMBER_PIXELS
    part = position - lower
    strip[lower] = mix(strip[lower], fade(color, 1 - part))
    strip[upper] = mix(strip[upper], fade(color, part))

# each planet is a list: [position, pixels moved per step, color]
planets = [
    [0.0, 0.32, (255, 150, 0)],    # fast and orange
    [6.0, 0.20, (255, 255, 255)],  # white
    [12.0, 0.13, (0, 80, 255)],    # blue
    [18.0, 0.08, (255, 0, 0)],     # slow and red
]

while True:
    strip.fill((0, 0, 0))
    for planet in planets:
        draw_soft(planet[0], planet[2])
        planet[0] = (planet[0] + planet[1]) % NUMBER_PIXELS
    strip.write()
    sleep(DELAY)
