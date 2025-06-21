from neopixel import NeoPixel
from utime import sleep
import config

# read parameters from hardware configuration file
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def strip_off():
    for i in range(0, NUMBER_PIXELS - 1):
        # turn index red pixel on for a short delay
        strip[i] = (0,0,0)
    strip.write()

# Create a variable to store the delay 
delay = 1
max_brightness = 10;
while True:
    
    # turn all pixels on red
    for i in range(0, NUMBER_PIXELS - 1):
        # turn index red pixel on for a short delay
        strip[i] = (max_brightness,0,0)
    strip.write()
    sleep(delay)

    # turn all pixels off
    strip_off()
    sleep(delay)
    
    # turn all pixels on green
    for i in range(0, NUMBER_PIXELS - 1):
        # turn index red pixel on for a short delay
        strip[i] = (0,max_brightness,0)
    strip.write()
    sleep(delay)

    # turn all pixels off
    strip_off()
    sleep(delay)
    
    # turn all pixels on blue
    for i in range(0, NUMBER_PIXELS - 1):
        # turn index red pixel on for a short delay
        strip[i] = (0,0,max_brightness)
    strip.write()
    sleep(delay)

    # turn all pixels off
    strip_off()
    sleep(delay)
    