# random bounce
# pixels appear to bounce around on the LED strip as they move back-and-forth
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint
import config

NUMBER_PIXELS = config.NUMBER_PIXELS
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), NUMBER_PIXELS)

loc = int(NUMBER_PIXELS/2)
while True:
    strip[loc % NUMBER_PIXELS] = (10,10,10)
    strip.write()
    sleep(.1)
    strip[loc % NUMBER_PIXELS] = (0,0,0)
    move_dir = randint(0,1)
    if move_dir == 0:
        loc -= 1
    else:
        loc += 1
    