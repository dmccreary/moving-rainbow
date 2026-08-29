# 06-color-wipe.py
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
# get the configuration information
import config

np = config.NUMBER_PIXELS
strip = NeoPixel(Pin(config.NEOPIXEL_PIN), np)
while True:
    
    # make the strip red
    for i in range(0,np):
        strip[i] = (100,0,0)
        strip.write()
        sleep(.05)
   
    # make the strip green
    for i in range(0,np):
        strip[i] = (0,100,0)
        strip.write()
        sleep(.05)

    # make the strip blue
    for i in range(0,np):
        strip[i] = (0,0,100)
        strip.write()
        sleep(.05)