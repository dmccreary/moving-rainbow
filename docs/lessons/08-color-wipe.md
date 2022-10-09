# Color Wipe

This lesson shows you how to change the color of the entire LED strip pixel by pixel.  There will be two delays that we can control:

1. the delay between each pixel update - this is usually about 1/20th of a second
2. the delay between colors - this is usually about 1 to 2 seconds

## A Simple Color Wipe Function

To write this program, we will create a simple Python function that will cycle through all the colors in a list.  Our color list will look like this:

```python
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
...etc...
colors = (red, orange, yellow, green, blue, cyan, indigo, violet, white)
```

Now with this list

```python
def color_wipe(delay, color_delay):
    for color in colors:
        for i in range(0, NUMBER_PIXELS):
            strip[i] = color
            strip.write()
            # the delay between each pixel draw
            sleep(delay)
        # how long to pause between color changes
        sleep(color_delay)
```

```python
from time import sleep

# most people have a heart rate of around 60-70 beats per minute
# If you add a once second deplay between "beats" you can make and LED
# look like a beating heart.

NUMBER_PIXELS = 60
LED_PIN = 0

strip = NeoPixel(machine.Pin(LED_PIN), NUMBER_PIXELS)

red = (255, 0, 0)
orange = (140, 60, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
white = (128, 128, 128)
colors = (red, orange, yellow, green, blue, cyan, indigo, violet, white)

def color_wipe(delay, color_delay):
    for color in colors:
        for i in range(0, NUMBER_PIXELS):
            strip[i] = color
            strip.write()
            sleep(delay)
        # how long to pause between color changes
        sleep(color_delay)

while True:
    color_wipe(.05, 1)
```