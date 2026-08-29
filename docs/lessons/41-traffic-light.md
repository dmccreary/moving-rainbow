# Traffic Light

You've built plenty of patterns that treat every step the same way. A real
traffic light doesn't — it stays red a long time, green a long time, and
yellow for just a moment. In this lesson you'll build one using three
pixels and three different wait times.

!!! tip "Pixel says..."
    You already know everything you need for this one — colors and
    `sleep()`. The only new idea is that different states don't have to
    last the same amount of time!

## What you'll learn

- How to represent a real-world object (a traffic light) as a program
- How to give different states different durations
- How a helper function can turn on-or-off logic into one readable line

## What you'll need

- Your Pico and NeoPixel strip
- The kit's `config.py` file
- No buttons are needed for this lesson

## Three Pixels, Three States

This program uses the first three pixels as the red, yellow, and green
lights. A `show()` function turns each one on or off, so the main loop
just has to say which lights should be lit:

```python
show(True, False, False)   # red on, yellow off, green off
```

## The Full Program

```python
# Simulate a traffic light using the first three pixels of the strip.
# Each color stays on for a different amount of time, just like a real
# traffic light.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

RED_PIXEL, YELLOW_PIXEL, GREEN_PIXEL = 0, 1, 2
OFF = (0, 0, 0)


def clear_strip():
    for i in range(config.NUMBER_PIXELS):
        strip[i] = OFF


def show(red_on, yellow_on, green_on):
    clear_strip()
    strip[RED_PIXEL] = (200, 0, 0) if red_on else OFF
    strip[YELLOW_PIXEL] = (200, 160, 0) if yellow_on else OFF
    strip[GREEN_PIXEL] = (0, 200, 0) if green_on else OFF
    strip.write()


while True:
    show(True, False, False)    # red - stop
    sleep(4)
    show(False, False, True)    # green - go
    sleep(4)
    show(False, True, False)    # yellow - slow down
    sleep(1)
```

Run it and watch the first three pixels. Red stays lit the longest, then
green, then a quick flash of yellow before it cycles back to red.

!!! info "Pixel thinks..."
    This is a **state machine**, just like the button-driven ones you
    built earlier — except this one switches states using a timer instead
    of a button press. Compare it to
    [Modes](28-modes.md) and see how similar the pattern really is.

## Try It Yourself

- Make yellow last 2 seconds instead of 1.
- Add a fourth pixel that blinks only while the light is red, like a
  pedestrian "don't walk" signal.

## Check Your Understanding

1. Why does red stay lit longer than yellow in this program?
2. What does the `show()` function do that saves you from repeating code?
3. What would happen if you swapped the order of the `sleep(4)` calls?
4. How is this state machine similar to the one in the Modes lesson? How is it different?

!!! success "You've got this!"
    You just modeled a real-world machine with code. Traffic lights,
    crosswalk signals, and elevator doors all run on this same idea.

**What's next:** in [Binary Counter](42-binary-counter.md), you'll use
pixels to represent numbers instead of real-world objects.
