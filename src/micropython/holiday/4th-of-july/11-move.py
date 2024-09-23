from machine import Pin
from utime import sleep
from neopixel import NeoPixel

NUMBER_PIXELS = 64
LED_PIN = 6
strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

# lower left = 0
# lower ight = 7
# upper right = 56
# upper right = 63
while True:
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (255,0,0)
        strip.write()
        sleep(.02)
        strip[i] = (0,0,0)
        strip.write()
