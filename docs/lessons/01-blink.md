# Blink

Here is one of simplest moving rainbow programs.  It is our version of "Hello World!. 

Our first program will just blink the first pixel on and off every 1/2 second.

```py
from neopixel import NeoPixel
from utime import sleep

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60

strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

while True:
    # turn first red pixel on for 1/2 second
    strip[0] = (255,0,0)
    strip.write()
    sleep(.5)

    # turn off for 1/2 second
    strip[0] = (0,0,0)
    strip.write()
    sleep(.5)
```

## Exercises

### Change the Color Lab
1. Change the line:<br/>
```strip[0] = (255,0,0)```
to be:<br/>
```strip[0] = (0,255,0)```

What happens?

### Change the Position Lab

1. Change the line:<br/>
```strip[0] = (255,0,0)```
to be:<br/>
strip[1] = (255,0,0)

What happens?

### Change the Sleep Time

What happens if you change the sleep time?

from:<br/>
```sleep(.5)```
to:<br/>
```sleep(.1)```

What is the smallest time you can use and still see flashing?

### RGB Lab

1. Change the line:<br/>
```strip[0] = (255,0,0)```
to be:
```python
strip[0] = (255,0,0)
strip[1] = (0,255,0)
strip[2] = (0,0,255)
```
and change the
```python
    strip[0] = (0,0,0)
    strip[1] = (0,0,0)
    strip[2] = (0,0,0)
```

What happened?

### Why Do We Need Strip.Write?

Try to remove one of the line that does strip.write().  What happens?  Why do you think we need this line?

### LED Strip State

What happens if you stop the program when the LED strip LEDs are on? 

### On Your Own

What if you extended the lab to more positions and colors?