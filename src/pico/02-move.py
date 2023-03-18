from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 12

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Create a varuabke to store the delay 
delay = .02
while True:
    for i in range(0, NUMBER_PIXELS - 1):
        # turn index red pixel on for and delay
        strip[i] = (255,0,0)
        strip.write()
        sleep(delay)

        # turn off
        strip[i] = (0,0,0)