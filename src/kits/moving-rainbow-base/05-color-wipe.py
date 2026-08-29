import machine
from neopixel import NeoPixel
from time import sleep
import config

# most people have a heart rate of around 60-70 beats per minute
# If you add a once second deplay between "beats" you can make and LED
# look like a beating heart.

NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255, 0, 0)
orange = (140, 60, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
white = (128, 128, 128)
colors = (red, orange, yellow, green, blue, cyan, indigo, violet, white)

def color_wipe():
    for color in colors:
        for i in range(0, NUMBER_PIXELS):
            strip[i] = color
            strip.write()
            sleep(.01)
        sleep(1)

while True:
    color_wipe()
