# Twinkle

A twinkle is a light whose brightness varies repeatedly between bright and faint.

## Sample Twinkle Function

This 

```python
def twinkle(delay):
    random_index = randint(0, NUMBER_PIXELS);
    # turn on
    strip[random_index] = (255,255,255) 
    strip.write();
    sleep(delay);
    # turn off
    strip[random_index] = (0,0,0) 
    strip.write();
```

## Full Program

```python
from neopixel import NeoPixel
from utime import sleep, ticks_ms
from urandom import randint

NEOPIXEL_PIN = 0
NUMBER_PIXELS = 60
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)

def twinkle(delay):
    random_index = randint(0, NUMBER_PIXELS-1);
    # turn on
    strip[random_index] = (255,255,255) 
    strip.write();
    sleep(delay);
    # turn off
    strip[random_index] = (0,0,0) 
    strip.write();

while True:
    twinkle(.1)
    sleep(1)
```

## Exercises

1. Add a parameter to the ```twinkle()``` function to allow the caller to specify the color.
2. Make the brightness of the twinkle function a random value
3. Make the brightness of a twinkle ramp up and down

## Twinkle Random Color

```py
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

def twinkle(delay, color):
    random_index = randint(0, NUMBER_PIXELS-1);
    # turn on
    strip[random_index] = color 
    strip.write();
    sleep(delay);
    # turn off
    strip[random_index] = (0,0,0) 
    strip.write();

while True:
    twinkle(.1, colors[randint(0, color_count-1)])
    sleep(1)
```