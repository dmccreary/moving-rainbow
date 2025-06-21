from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 119

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Create a variable to store the delay 
delay = .03
while True:
    for i in range(0, NUMBER_PIXELS - 1):
        # turn index red pixel on for a short delay
        strip[i] = (255,0,0)
        strip.write()
        sleep(delay)

        # turn off
        strip[i] = (0,0,0)