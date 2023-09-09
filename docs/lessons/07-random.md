# Using Random Numbers

One fun way to spice up our LED strips is to randomly light
up a different pixel with a random color.  Here is how we do this.

First, We need to import the library that generate random numbers:

```py
from urandom import randint
```

Next, we need to generate a random number within a fixed range:

```py
    random_red_brightness = randint(0, 256)
```

Let's create a program that will briefly light up an random pixel
with a random color.  To do this we first generate a random location
on the LED strip, then we get a random value for the red, green and blue brightness:

```py
location = randint(0, NUMBER_PIXELS-1)
    red = randint(0, 256)
    green = randint(0, 256)
    blue = randint(0, 256)
```

Here is the full program.

```py
# 07-random color at a random location
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    location = randint(0, NUMBER_PIXELS-1)
    red = randint(0, 256)
    green = randint(0, 256)
    blue = randint(0, 256)
    strip[location] = (red, green, blue)
    strip.write()
    sleep(.5)
    strip[location] = (0, 0, 0)
```