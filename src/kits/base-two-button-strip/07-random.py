# 07-random color at a random location
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
# get the configuration information
import config

np = config.NUMBER_PIXELS
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), np)

while True:
    location = randint(0, np-1)
    red = randint(0, 256)
    green = randint(0, 256)
    blue = randint(0, 256)
    strip[location] = (red, green, blue)
    strip.write()
    sleep(.5)
    strip[location] = (0, 0, 0)
