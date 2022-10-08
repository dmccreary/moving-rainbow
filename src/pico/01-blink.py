from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    # red is 10 of 255
    strip[0] = (255,0,0)

    # turn on for 1/2 second
    strip.write()
    sleep(.5)

    # turn off for 1/2 second
    strip[0] = (0,0,0)
    strip.write()
    sleep(.5)