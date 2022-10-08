from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Create a varuabke to store the delay 
delay = .01
while True:
    # turn first red pixel on for 1/2 second
    strip[0] = (255,0,0)
    strip.write()
    sleep(delay)

    # turn off for 1/2 second
    strip[0] = (0,0,0)
    strip.write()
    sleep(delay)