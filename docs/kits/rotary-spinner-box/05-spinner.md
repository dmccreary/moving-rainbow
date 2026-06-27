# Lab 5: The Scanner

This lab makes a single bright dot travel back and forth along your strip.
It is the signature pattern of the box. The dot moves one pixel at a time,
then bounces off each end, like the scanning eye of a robot.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    This is one of my favorite patterns. A little dot zips down the strip,
    hits the end, and turns right around. To make it move, we'll use a
    **variable** — a name that holds a value that can change. Let's light
    this up!

## What You'll Learn

By the end of this lab, you'll be able to:

- Use a `position` variable to track where the dot is
- Use a `direction` variable to track which way the dot moves
- Move the dot one pixel each step
- Explain why the dot **bounces** off the ends instead of wrapping around

## What You'll Need

- Your Rotary Spinner Box with the 12-pixel LED strip
- A USB cable to connect the box to your computer
- The Thonny program open on your computer

You do **not** need the knob or the buttons for this lab.

## The Big Idea: Variables That Change

A **variable** is a name that holds a value. The value can change while the
program runs. This program uses two variables to move the dot.

- `position` holds the pixel number the dot is on right now.
- `direction` holds which way the dot is moving. `+1` means forward. `-1` means backward.

Each time through the loop, we add `direction` to `position`. That moves the
dot one pixel in the current direction.

## A First Look at the Code

The program lives in the file `05-spinner.py`. It loads `config.py`, which holds
the pin number and pixel count for your box. The strip is on **GPIO 0** (a pin
on the chip) and has 12 pixels.

Here is the setup at the top of the file.

```python
from neopixel import NeoPixel
import machine
from utime import sleep

import config

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# The color of the moving dot
DOT_COLOR = (0, 60, 80)

# How long the dot stays on each pixel, in seconds
DELAY = 0.06

# Start the dot at pixel 0, moving toward the far end
position = 0
direction = 1
```

This makes a `strip` we can control, picks a soft blue-green dot color, and
starts the dot at pixel 0 moving forward.

!!! info "Pixel thinks..."
    <img src="../../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    `DOT_COLOR = (0, 60, 80)` is a **color** — three numbers for red, green,
    and blue. Zero red, a little green, more blue. That gives us a calm
    blue-green glow. Try your own three numbers later!

## How the Dot Moves

Here is the main loop. A **loop** is code that repeats. This one repeats forever.

```python
while True:
    # turn every pixel off, then light only the current one
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip[position] = DOT_COLOR
    strip.write()
    sleep(DELAY)
```

Each pass turns all 12 pixels off, lights the one pixel at `position`, and
then waits a short moment. You see one bright dot sitting on the strip.

The first three lines clear the strip. `(0, 0, 0)` means off, or black. We
clear every pixel so the old dot does not stay behind. Then `strip[position]`
lights up just the current pixel. `strip.write()` sends the colors to the
lights.

## The Bounce: Boundaries Matter

Now comes the clever part. This code decides when to turn around.

```python
    # if we are at either end, turn around
    if position == 0:
        direction = 1
    elif position == config.NUMBER_PIXELS - 1:
        direction = -1

    # take one step in the current direction
    position = position + direction
```

When the dot reaches an end, we flip `direction`. Then `position = position +
direction` moves the dot one step. The dot now heads back the other way.

The ends of the strip are its **boundaries** (the edges where the strip stops).
Pixel 0 is one boundary. Pixel 11 is the other. `config.NUMBER_PIXELS - 1`
equals 11, because we count pixels starting at 0. At each boundary the dot
bounces back.

!!! warning "Watch out!"
    <img src="../../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    Your strip is a straight line, not a ring. If the dot ran off the end and
    reappeared at pixel 0, it would seem to **jump** across your box. That
    looks wrong on a straight strip. Bouncing keeps the motion smooth, like a
    scanning eye sweeping back and forth.

## Try It Yourself

1. **Change the dot color.** Set `DOT_COLOR = (255, 0, 0)` for a bright red
   dot. What three numbers would make it green?
2. **Speed it up or slow it down.** Change `DELAY = 0.06` to `DELAY = 0.2`.
   The dot moves slower. Now try `DELAY = 0.02`. What changes?
3. **Start in the middle.** Change `position = 0` to `position = 6`. Where does
   the dot begin its first trip?

## Check Your Understanding

1. What does the `position` variable hold?
2. What do the values `+1` and `-1` mean for `direction`?
3. What line moves the dot one pixel each step?
4. Why does the dot bounce instead of wrapping back to pixel 0?
5. Why is the largest pixel number 11 and not 12?

!!! success "Chapter complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You made a dot scan back and forth all on its own! You used a changing
    variable to move it and a boundary check to bounce it. That same idea
    powers games, robots, and animations everywhere. You're glowing!

## What's Next

In [Lab 6: The Comet](06-comet.md), you'll give the moving dot a glowing tail
that fades out behind it.
