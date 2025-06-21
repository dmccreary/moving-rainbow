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


def rainbow_cycle(offset):
    # how much to step through the color wheel for each pixel
    step = int(255/NUMBER_PIXELS)
    for i in range(0, NUMBER_PIXELS-1):
        strip[i] = wheel((int(i*step)+offset) & 255)
    strip.write()
    
while True:
    for offset in range(0, 255):
        rainbow_cycle(offset)
        sleep(.02)
print("done")  
