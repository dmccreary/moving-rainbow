# Blink

Here is one of simplest moving rainbow programs.  It is our version of "Hello World!. 

Our first program will just blink the first pixel on and off every 1/2 second.

```py
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    # red is 10 of 255
    strip[i] = (10,0,0)

    # turn on for 1/2 second
    strip.write()
    sleep(.5)

    # turn off for 1/2 second
    strip[i] = (0,0,0)
    strip.write()
    sleep(.5)
```