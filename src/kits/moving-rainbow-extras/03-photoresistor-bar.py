# Extras Lab 03: Photoresistor Bar
# Filename: 03-photoresistor-bar.py
# Version: 1.0.0
#
# Show the light level as a bar of colored pixels: the brighter the room,
# the longer the bar. Needs a photoresistor (an extra part) and the extras
# config.py.
# Not yet tested on hardware: adapt for your setup.

from machine import Pin, ADC
from neopixel import NeoPixel
from utime import sleep
import config

# hardware settings from config.py
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS
PHOTORESISTOR_PIN = config.PHOTORESISTOR_PIN

strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
photo = ADC(PHOTORESISTOR_PIN)

DARK_VALUE = 2000      # change to the number you wrote down for a dark room
BRIGHT_VALUE = 55000   # change to the number you wrote down for a bright room
BAR_PIXELS = 12        # the bar can be up to 12 pixels long

while True:
    light_value = photo.read_u16()

    # turn the light level into a bar length from 0 to BAR_PIXELS
    if light_value <= DARK_VALUE:
        lit = 0
    elif light_value >= BRIGHT_VALUE:
        lit = BAR_PIXELS
    else:
        lit = int((light_value - DARK_VALUE) / (BRIGHT_VALUE - DARK_VALUE) * BAR_PIXELS)

    for i in range(NUMBER_PIXELS):
        if i >= lit:
            strip[i] = (0, 0, 0)       # off
        elif i < 4:
            strip[i] = (0, 0, 25)      # low light: blue
        elif i < 8:
            strip[i] = (0, 25, 0)      # medium light: green
        else:
            strip[i] = (25, 0, 0)      # high light: red
    strip.write()
    sleep(0.2)
