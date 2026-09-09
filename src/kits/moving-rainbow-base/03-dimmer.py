from machine import Pin
from neopixel import NeoPixel
from utime import sleep
# get the configuration information
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

while True:
    
    for i in range(0,100):
        strip[0] = (i,0,0)
        strip.write()
        sleep(.01)
    
    for i in range(100,0,-1):
        strip[0] = (i,0,0)
        strip.write()
        sleep(.01)