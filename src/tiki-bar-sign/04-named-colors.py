from neopixel import NeoPixel
from utime import sleep
import config

# read parameters from hardware configuration file
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

max_val = 50
red = (max_val, 0, 0)
orange = (140, 60, 0)
yellow = (max_val, max_val, 0)
green = (0, max_val, 0)
blue = (0, 0, max_val)
cyan = (0, max_val, max_val)
indigo = (75, 0, 130)
violet = (138, 43, 226)
white = (max_val, max_val, max_val)
colors = (red, orange, yellow, green, blue, cyan, indigo, violet, white)

def strip_off():
    for i in range(0, NUMBER_PIXELS - 1):
        # turn index red pixel on for a short delay
        strip[i] = (0,0,0)
    strip.write()
    
def color_wipe(color):
    for i in range(0, NUMBER_PIXELS):
        strip[i] = color
    strip.write()

on_delay = 1.5
off_delay = .5
while True:
    for i in range(0, len(colors)):
        color_wipe(colors[i])
        sleep(on_delay)
        strip_off()
        sleep(off_delay)
    