from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    # turn first red pixel on for 1/2 second
    strip[0] = (255,0,0)
    strip[1] = (0,255,0)
    strip[2] = (0,0,255)
    strip.write()
    sleep(.5)

    # turn off for 1/2 second
    strip[0] = (0,0,0)
    strip[1] = (0,0,0)
    strip[2] = (0,0,0)
    strip.write()
    sleep(.5)