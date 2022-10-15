# Larson Scanner

The Larson Scanner is a light pattern special effect named after [Glen A. Larson](https://en.wikipedia.org/wiki/Glen_A._Larson).  Larson used this pattern to give his [Battlestar Galactica Cylon](https://en.wikipedia.org/wiki/Cylon_(Battlestar_Galactica)) and [KITT](https://en.wikipedia.org/wiki/KITT) robot eyes a sense of sentience.  See [Knight Rider](https://en.wikipedia.org/wiki/Knight_Rider_(1982_TV_series)) for the backstory.

## Description

A set of usually red pixels moves back and forth over the LED strip.  The pixels are brighter in the center and are dimmer at the edges of the set.  You can see an example of this in the [Larson Scanner Pumpkin Kit](https://www.coderdojotc.org/micropython/kits/larson-scanner/01-intro/)

## Color RGB values

We will need a set of predefined colors for various brightness of red:

```python
red = (255, 0, 0)
red_med = (32, 0, 0)
red_light = (8, 0, 0)
off = (0,0,0)
```

Note that the color levels are not linear.  You can adjust these and add more intermediate levels for wider patterns.

## Full Source Code

```python
# Larson Scanner - five pixels
from machine import Pin
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

red = (255, 0, 0)
red_med = (32, 0, 0)
red_light = (8, 0, 0)
off = (0,0,0)

delay = .05
while True:
    # forward loop
    for i in range(2, NUMBER_PIXELS-2):
        strip[i-2] = red_light
        strip[i-1] = red_med
        strip[i] = red
        strip[i+1] = red_med
        strip[i+2] = red_light
        # erase the trailing pixel
        if i > 0:
            strip[i-3] = off
        strip.write()
        sleep(delay)
    # backward loop
    for i in range(NUMBER_PIXELS-4, 1, -1):
        # erase the trailing pixel
        if i < NUMBER_PIXELS-2:
            strip[i+3] = off
        strip[i-2] = red_light
        strip[i-1] = red_med
        strip[i] = red
        strip[i+1] = red_med
        strip[i+2] = red_light
        strip.write()
        sleep(delay)
```

## Exercises

1. Turn the code into a function with delay as a patter
2. Add a color parameter
3. Add a parameter for the width of the pattern