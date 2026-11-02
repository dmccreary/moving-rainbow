# Lab 18: Pendulum
# Filename: 18-pendulum.py
# Version: 1.0.0
#
# A ball swings back and forth along the bottom of the ring like a
# pendulum. It moves fastest at the bottom and slows down at each end,
# because its position comes from a sine wave. Each swing is a little
# smaller. When the ball has almost stopped it gets a new push and color.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from math import sin
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS
TOP_PIXEL = config.TOP_PIXEL

DELAY = 0.03             # seconds between steps
BIGGEST_SWING = 10.0     # pixels from the bottom at the start - less than 12
SWING_SPEED = 0.07       # bigger numbers swing faster
SWING_DECAY = 0.997      # each step the swing keeps this much of its size

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 60, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
violet = (138, 43, 226)
colors = (red, orange, green, cyan, violet)
color_count = len(colors)

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the ring is comfortable to look at
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

# share one color between the two pixels closest to a decimal position
def draw_soft(position, color):
    lower = int(position)
    upper = (lower + 1) % NUMBER_PIXELS
    part = position - lower
    strip[lower] = fade(color, 1 - part)
    strip[upper] = fade(color, part)

BOTTOM = TOP_PIXEL + NUMBER_PIXELS // 2  # the pixel number at 6 o'clock

swing = BIGGEST_SWING
time_counter = 0.0
color_index = 0
while True:
    strip.fill((0, 0, 0))
    strip[TOP_PIXEL] = fade(white, 0.1)   # the point the pendulum hangs from
    draw_soft((BOTTOM + swing * sin(time_counter)) % NUMBER_PIXELS, colors[color_index])
    strip.write()
    sleep(DELAY)
    time_counter += SWING_SPEED
    swing = swing * SWING_DECAY
    if swing < 0.5:
        # the pendulum has nearly stopped, so give it a new push
        swing = BIGGEST_SWING
        time_counter = 0.0
        color_index = (color_index + 1) % color_count
