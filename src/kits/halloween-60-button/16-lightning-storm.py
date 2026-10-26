# Lab 16: Lightning Storm
# Filename: 16-lightning-storm.py
# Version: 1.0.0
# Not yet tested on hardware.
#
# A haunted thunderstorm. Dark purple clouds slowly roll along the strip.
# Every few seconds lightning strikes one part of the sky: it flashes
# white two or three times and leaves a glow that fades out.
# The program is a state machine (a program that is always in one of a
# few named states): "calm", "flash", "dark" between flashes, and "glow".

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
BRIGHTNESS = config.BRIGHTNESS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
from utime import ticks_ms, ticks_diff
from urandom import randint
from math import sin

DELAY = 0.02             # seconds between steps

cloud = (60, 0, 120)     # dark purple storm clouds
lightning = (255, 255, 255)
glow = (120, 60, 255)    # the purple-white afterglow

# return a color scaled by a number from 0.0 (off) to 1.0 (full),
# and also by BRIGHTNESS so the strip is safe on battery power
def fade(color, amount):
    scale = amount * BRIGHTNESS
    return (int(color[0] * scale), int(color[1] * scale), int(color[2] * scale))

state = "calm"
next_strike = ticks_ms() + randint(2000, 5000)   # when lightning strikes next
flashes_left = 0
state_end = 0            # when the current flash, dark or glow part is over
bolt_start = 0           # the first pixel the bolt lights up
bolt_end = 0
glow_level = 0.0
cloud_time = 0.0

while True:
    now = ticks_ms()

    # draw the rolling clouds: a sine wave makes soft bright and dark patches
    cloud_time += 0.05
    for i in range(NUMBER_PIXELS):
        wave = (sin(i * 0.3 + cloud_time) + 1) / 2      # 0.0 to 1.0
        strip[i] = fade(cloud, 0.1 + 0.4 * wave)

    if state == "calm":
        if ticks_diff(now, next_strike) >= 0:
            # pick a random part of the sky for the bolt
            bolt_start = randint(0, NUMBER_PIXELS - 10)
            bolt_end = bolt_start + randint(5, 20)
            flashes_left = randint(2, 3)
            state = "flash"
            state_end = now + 60

    elif state == "flash":
        for i in range(bolt_start, min(bolt_end, NUMBER_PIXELS)):
            strip[i] = fade(lightning, 1)
        if ticks_diff(now, state_end) >= 0:
            flashes_left -= 1
            if flashes_left > 0:
                state = "dark"
                state_end = now + randint(50, 150)
            else:
                state = "glow"
                glow_level = 1.0

    elif state == "dark":
        # a short dark gap between flashes makes the lightning flicker
        if ticks_diff(now, state_end) >= 0:
            state = "flash"
            state_end = now + 40

    elif state == "glow":
        for i in range(bolt_start, min(bolt_end, NUMBER_PIXELS)):
            strip[i] = fade(glow, glow_level)
        glow_level -= 0.03
        if glow_level <= 0:
            state = "calm"
            next_strike = now + randint(2000, 6000)

    strip.write()
    sleep(DELAY)
