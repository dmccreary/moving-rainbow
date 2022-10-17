# Red, Green and Blue

In this lesson, we will draw three different colors at three different locations on the LED strip.  We will then repeat this pattern down the strip.

Our first task is to draw the red, green and blue in the first three pixels of the LED strip.

Our main code will be the following

```python
# make the fist location red
strip[0] = (255,0,0)
# make the second location green
strip[1] = (0,255,0)
# make the third location blue
strip[2] = (0,0,255)
# update the strip
strip.write()
```

## Full Program

```python
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

# make the fist location red
strip[0] = (255,0,0)
# make the second location green
strip[1] = (0,255,0)
# make the third location blue
strip[2] = (0,0,255)
# update the strip
strip.write()
```

## Repeating the Pattern

Now, let's repeat this pattern over the entire strip.  We can do this by wrapping the three lines in a for loop like this:

```python
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
# count 0 to the end skipping every 3
for i in range(0, NUMBER_PIXELS-1, 3):
    strip[i] = (255,0,0)
    # make the second location green
    strip[i+1] = (0,255,0)
    # make the third location blue
    strip[i+2] = (0,0,255)
    # update the strip
strip.write()
```

Note here that the range function has a third parameter that tells us how many to skip in each iteration of the loop.  Since we have three colors, we can skip every three values of i.  I will get values of 0, 3, 6, 9, 12... etc.

## Excercises