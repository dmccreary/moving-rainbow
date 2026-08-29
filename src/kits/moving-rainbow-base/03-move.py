from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    for i in range(0, NUMBER_PIXELS):
        # red is 10 of 255
        strip[i] = (10,0,0)
        strip.write()
        sleep(.05)
        strip[i] = (0,0,0)
