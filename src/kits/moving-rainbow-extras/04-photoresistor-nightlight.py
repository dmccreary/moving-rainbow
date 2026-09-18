# Extras Lab 04: Photoresistor Nightlight
# Filename: 04-photoresistor-nightlight.py
# Version: 1.0.0
#
# A nightlight: the strip glows a dim, warm color when the room gets dark
# and turns off when the room is bright. Needs a photoresistor (an extra
# part) and the extras config.py.
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

LIGHT_THRESHOLD = 10000    # below this number, the room is "dark"
GLOW = (20, 10, 0)         # a dim, warm color

while True:
    if photo.read_u16() < LIGHT_THRESHOLD:
        color = GLOW           # dark room: turn the nightlight on
    else:
        color = (0, 0, 0)      # bright room: turn it off
    for i in range(NUMBER_PIXELS):
        strip[i] = color
    strip.write()
    sleep(0.5)
