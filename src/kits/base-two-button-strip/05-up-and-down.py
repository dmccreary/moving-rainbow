from machine import Pin
from neopixel import NeoPixel
from utime import sleep
# get the configuration information
import config

np = config.NUMBER_PIXELS
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), np)
while True:
    
    # move up the strip
    for i in range(0,np):
        strip[i] = (100,0,0)
        strip.write()
        sleep(.05)
        strip[i] = (0,0,0)
        strip.write()
    
        # move up the strip
    for i in range(np-1, 0, -1):
        strip[i] = (100,0,0)
        strip.write()
        sleep(.05)
        strip[i] = (0,0,0)
        strip.write()