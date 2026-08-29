# Modes

So far, every program has run exactly one pattern. In this lesson, one
program holds *several* patterns, and a **mode variable** decides which one
is currently running.

!!! tip "Pixel says..."
    This is the trick behind every "multi-pattern" light show you've ever
    seen. It's not magic — it's just one number telling the program which
    pattern to run next!

## What you'll learn

- What a mode variable is and why programs use one
- How to store multiple patterns as separate functions
- How to switch modes automatically using a timer

## What you'll need

- Your Pico and NeoPixel strip
- The kit's `config.py` file

## One Variable, Many Patterns

A **mode variable** is just an integer that stands for "which pattern is
active right now." Mode `0` might mean solid red, mode `1` might mean solid
green, and so on. A function called `run_mode` looks at the mode variable
and runs the matching pattern:

```python
def run_mode(mode):
    if mode == 0:
        fill_strip((200, 0, 0))    # mode 0: solid red
    elif mode == 1:
        fill_strip((0, 200, 0))    # mode 1: solid green
    else:
        fill_strip((0, 0, 200))    # mode 2: solid blue
```

This lesson switches modes automatically, using a timer. The next lesson
adds buttons so *you* get to decide when to switch.

## The Full Program

```python
# Automatically cycle through three light patterns, staying on each one
# for a few seconds before moving to the next.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep, ticks_ms
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

SECONDS_PER_MODE = 4   # how long to stay on each mode before switching
NUM_MODES = 3


def fill_strip(color):
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()


def run_mode(mode):
    if mode == 0:
        fill_strip((200, 0, 0))    # mode 0: solid red
    elif mode == 1:
        fill_strip((0, 200, 0))    # mode 1: solid green
    else:
        fill_strip((0, 0, 200))    # mode 2: solid blue


mode = 0
run_mode(mode)
mode_start_time = ticks_ms()

while True:
    elapsed_seconds = (ticks_ms() - mode_start_time) / 1000

    if elapsed_seconds >= SECONDS_PER_MODE:
        mode = (mode + 1) % NUM_MODES   # advance to the next mode, then wrap
        run_mode(mode)
        mode_start_time = ticks_ms()
        print("mode:", mode)

    sleep(0.1)
```

Run it and watch the strip. Every four seconds it should switch from red,
to green, to blue, and back to red again.

!!! info "Pixel thinks..."
    `mode_start_time` is the key to the timer. Every loop checks how much
    time has passed *since the mode last changed* — not since the program
    started. That's what lets each mode get its own fair four seconds.

## Try It Yourself

- Change `SECONDS_PER_MODE` to `1` for a faster show.
- Add a fourth mode that fills the strip with a color of your choice, and
  update `NUM_MODES` to match.

## Check Your Understanding

1. What does the mode variable actually store?
2. What is the job of the `run_mode` function?
3. How does the program know when four seconds have passed?
4. What would happen if you forgot to update `NUM_MODES` after adding a new mode?

!!! success "You've got this!"
    You just built a program with more than one personality. Next, you'll
    hand the controls to your buttons.

**What's next:** in [Button Modes](29-button-modes.md), Button 1 and
Button 2 take over mode switching from the timer.
