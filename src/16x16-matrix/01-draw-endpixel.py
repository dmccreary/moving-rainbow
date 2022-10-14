from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 256

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# Create a varuabke to store the delay 
delay = .003

for i in range(0, NUMBER_PIXELS):
    # turn index red pixel on for and delay
    strip[i] = (1,0,0)
    strip.write()
    sleep(delay)

# turn last pixel green
strip[NUMBER_PIXELS-1] = (0,10,0)
strip.write()