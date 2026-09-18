# Lab 23: Heartbeat
# Filename: 23-heartbeat.py
# Version: 1.0.0
#
# The first pixel beats like a heart: a strong pulse, a softer pulse,
# and then a rest.

from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

STEP = 10           # how much the brightness changes at each step
RAMP_DELAY = 0.01   # seconds between steps: a small number makes a quick pulse

def pulse(peak):
    # brightness rises up to the peak...
    for level in range(0, peak, STEP):
        strip[0] = (level, 0, 0)
        strip.write()
        sleep(RAMP_DELAY)
    # ...and then falls back down to dark
    for level in range(peak, 0, -STEP):
        strip[0] = (level, 0, 0)
        strip.write()
        sleep(RAMP_DELAY)
    strip[0] = (0, 0, 0)
    strip.write()

while True:
    pulse(120)      # "lub": the strong beat
    sleep(0.1)
    pulse(80)       # "dub": the softer beat
    sleep(0.4)      # rest before the next heartbeat
