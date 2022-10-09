# Rainbow Cycle

In this lesson we will use the wheel function to slowly cycle each pixel in a range through each of the colors of the rainbow.

## The Rainbow Cycle Function
We create a function called ```rainbow_cycle()``` that has three parameters.  The first is a delay, the second is a number that increase the precision of the color changes which impacts the speed, the third is how many pixels to skip over.

```python
def rainbow_cycle(wait, speed, skip):
    global NUMBER_PIXELS, strip
    # get a color - speed will skip intermediate colors for faster cycles
    for j in range(0, 255, speed):
        for i in range(0, NUMBER_PIXELS, skip):
            rc_index = (i * 256 // NUMBER_PIXELS) + j
            # print(rc_index)
            strip[i] = wheel(rc_index & 255)
        strip.write()
    sleep(wait)
```

Next, we place a ```while True()``` loop at end and call the function repeatedly.  

## Power Considerations

This program has the ability to drive every single pixel on the strip.  This has the disadvantage that it will drain batteries too quickly or exceed the power levels of a USB power supply.

To get around this you can up the ```skip``` parameter to only turn on every 2nd, 3rd or 4th pixel.

The entire rainbow cycle loop takes a few seconds to run, so be aware of this limitation if you are adding controls or interrupts.

## Full Program

Here is the full program you can run.  Make sure to change the NUMBER_PIXELS parameter to match the length of your LED strip.

```python
from machine import Pin
from neopixel import NeoPixel
from utime import sleep

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

def rainbow_cycle(wait, speed, skip):
    global NUMBER_PIXELS, strip
    # get a color - speed will skip intermediate colors for faster cycles
    for j in range(0, 255, speed):
        for i in range(0, NUMBER_PIXELS, skip):
            rc_index = (i * 256 // NUMBER_PIXELS) + j
            # print(rc_index)
            strip[i] = wheel(rc_index & 255)
        strip.write()
    sleep(wait)

# s[eed is an integer from 1 to 30
speed = 2
# skip = 1 is every pixel, 2 is every other pixel etc.
# the hither skip the lower the overall power
skip = 3
while True:
    rainbow_cycle(.01, speed, skip)
```