# Ripple Patterns

```python
# moving rainbow
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)


red = (255, 0, 0)
red_med = (32, 0, 0)
red_light = (8, 0, 0)
off = (0, 0, 0)
orange = (140, 60, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
white = (128, 128, 128)
colors = (red, orange, yellow, green, blue, cyan, indigo, violet)
color_count = len(colors)
levels = [255, 128, 64, 32, 16, 8, 4, 2, 1]
level_count = len(levels)

def ripple(size, color, delay):
    # start at a random location within size of the ends
    start = randint(size, NUMBER_PIXELS - size)
    for i in range(0, size):
        strip[start+i] = color
        strip[start-i] = color
        strip.write()
        sleep(delay)
        strip[start+i] = (0,0,0)
        strip[start-i] = (0,0,0)

delay = 0.2
while True:
    ripple(10, red, delay)
    ripple(10, green, delay)
    ripple(10, blue, delay)
```

## Exercises

1. Make the color random
2. Make the size of the ripple random
3. Add randomness to the delay
4. Use the wheel function to pick a random color
5. Make the pixel intensity get lower as the ripple expands