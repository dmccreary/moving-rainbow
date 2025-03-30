from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 16
NUMBER_PIXELS = 1

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    # red is 10 of 255
    strip[0] = (10,0,0)
    strip.write()
    sleep(.5)
    
    ## off
    strip[0] = (0,0,0)
    strip.write()
    sleep(.5)
