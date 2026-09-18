# Count up in binary, using the first 5 pixels as bits.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

NUM_BITS = 5    # 5 bits can count from 0 to 31
ON_COLOR = (0, 150, 0)
OFF_COLOR = (0, 0, 0)


def show_binary(n):
    for bit in range(NUM_BITS):
        # (1 << bit) makes a mask like 00001, 00010, 00100...
        # n & mask checks if that one bit is a 1 or a 0
        if n & (1 << bit):
            strip[bit] = ON_COLOR
        else:
            strip[bit] = OFF_COLOR
    strip.write()


count = 0
while True:
    show_binary(count)
    print(count, "=", bin(count))
    sleep(1)
    count = (count + 1) % (2 ** NUM_BITS)   # wrap back to 0 after 31
