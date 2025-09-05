from machine import Pin
from neopixel import NeoPixel
from utime import sleep
# get the configuration information
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# the delay time between the on and off events
delay = .5

# repeat the indented code forever
while True:
    
    # Turn LED on
    # set the first pixel on red, but not too bright
    strip[0] = (25,0,0)
    # send the data to the LED strip
    strip.write()
    # go to sleep for the time in the delay (1/2 second)
    sleep(delay)
    
    # Turn LED off
    # set the first pixel off
    strip[0] = (0,0,0)
    # send the data to the LED strip
    strip.write()
    # go to sleep for the time in the delay (1/2 second)
    sleep(delay)