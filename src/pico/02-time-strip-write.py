from neopixel import NeoPixel
from utime import sleep, ticks_us

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

start = ticks_us()
strip.write()
print(ticks_us() - start)
