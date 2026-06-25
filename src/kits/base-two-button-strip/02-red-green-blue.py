from machine import Pin
from neopixel import NeoPixel
from utime import sleep
# get the configuration information
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

while True:
    
    # turn the first pixel red
    strip[0] = (100,0,0)
    strip.write()
    sleep(1)
    
    # turn the first pixel green
    strip[0] = (0,100,0)
    strip.write()
    sleep(1)
    
    # turn the first pixel green
    strip[0] = (0,0,100)
    strip.write()
    sleep(1)