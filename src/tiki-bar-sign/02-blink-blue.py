from neopixel import NeoPixel
from utime import sleep
import config

# read parameters from hardware configuration file
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Create a variable to store the delay 
delay = 1
while True:
    
    # turn all pixels on blue
    for i in range(0, NUMBER_PIXELS - 1):
        # turn index red pixel on for a short delay
        strip[i] = (0,0,10)
    strip.write()
    sleep(delay)

    # turn all pixels off
    for i in range(0, NUMBER_PIXELS - 1):
        # turn index red pixel on for a short delay
        strip[i] = (0,0,0)
    strip.write()
    sleep(delay)
    