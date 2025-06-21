from neopixel import NeoPixel
from utime import sleep
import config

# read parameters from hardware configuration file
NEOPIXEL_PIN = config.NEOPIXEL_PIN
NUMBER_PIXELS = config.NUMBER_PIXELS

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(wait, speed, skip):
    global NUMBER_PIXELS, strip
    # get a color - speed will skip intermediate colors for faster cycles
    for j in range(0, 255, speed):
        for i in range(0, NUMBER_PIXELS, skip):
            rc_index = (i * 256 // NUMBER_PIXELS) + j
            # print(rc_index)
            strip[i] = wheel(rc_index & 255)
        strip.write()
    sleep(wait)

# s[eed is an integer from 1 to 30
speed = 2
# skip = 1 is every pixel, 2 is every other pixel etc.
# the hither skip the lower the overall power
skip = 1
while True:
    rainbow_cycle(.01, speed, skip)