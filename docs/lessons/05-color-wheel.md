# Color Wheel Lab

<iframe src="../../sims/color-wheel/main.html" height="450px" scrolling="no"></iframe>

What if we wanted to slowly vary the color of one of our pixels through all the colors of the rainbow?  What we would like is a function that would take in an number from 0 to 255 and walk around the color wheel as you change the input value.  This is known as the ```wheel`` function:

```py
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
```

If you follow the code, you will see that the colors range from red through green and to blue and back to red:

```py
wheel(1) = (255, 0, 0) # red
wheel(85) = (0,255, 0) # green
wheel(170) = (0, 0, 255) # blue
wheel(255) = (255, 0, 0) # red
```

## Full Program

This program will continue rotating the first pixel through all the colors.

```py
import machine
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 1

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
        
counter = 0
while True:
    strip[0] = wheel(counter)
    strip.write()
    sleep(.01)
    counter += 1
    # reset the counter
    if counter == 255:
        counter = 0
```