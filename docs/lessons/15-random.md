# Random Drawing

In this lesson we will introduce the ability to draw random colors at random pixels.  This allows us to create more natural patterns such as the flicking light of a candle.

## The Random Functions

We need a function that will generate a random integer between a range of values. This is called the ```randint()``` function and it takes either one or two parameters.  In our case, we can just pass in the minimum and maximum values:

```python
randint(0, 256)
```

You can read more about MicroPython random functions [here](https://docs.micropython.org/en/latest/library/random.html)

To use the random function we first need to import the function from the library:

```python
from urandom import randint
```

Here is a sample loop that sets each pixel to a random color using the wheel() function:

```python
for i in range(0, NUMBER_PIXELS):
    random_color = randint(0, 256)
    strip[i] = wheel(random_color)
    strip.write()
    sleep(.1)
```

## Full Program

```python
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

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
    
def clear():
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,0,0)
    strip.write()

# setup
counter = 0
clear()

# main loop
while True:
    for i in range(0, NUMBER_PIXELS):
        random_color = randint(0, 256)
        strip[i] = wheel(random_color)
        strip.write()
        sleep(.1)
```

## Exercises

1. Instead of updating a single pixel in consecutive sequences, can you also use the
```randint()``` function to update a random pixel?
2. What if you have a small fixed list of colors to pick from.  How can you use ```randint()``` to pick a color from this list?
