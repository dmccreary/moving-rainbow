# Lab 4: Test the Strip

This program checks every light on your strip. It turns all 12 pixels red,
then green, then blue, then white, then off. If every pixel lights up in the
right order, your strip is wired correctly and ready for the fun labs ahead.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Before we build a light show, let's make sure every light works! This lab
    is like a roll call for your pixels. We'll call each one by name and watch
    it shine. If one stays dark, we've found a puzzle to solve. Let's light
    this up!

## What You'll Learn

By the end of this lab, you'll be able to:

- Use a **`for` loop** (code that repeats once for each item) to touch every pixel
- Read a **pixel index**, the number that names each light (like `strip[0]`)
- Write a reusable **helper function** named `fill`
- Set a color with an **RGB tuple** like `(50, 0, 0)`
- Prove that all 12 pixels work and are in the right order

## What You'll Need

- Your Rotary Spinner Box with the 12-pixel LED strip connected
- A USB cable to connect the box to your computer
- The Thonny program open on your computer

You do **not** need the knob or the buttons for this lab.

## Setting Up the Strip

The **LED strip** (a line of 12 colored lights) plugs into pin 0 of the Pico.
Our program loads a few tools and then makes a strip object we can control.

```python
from neopixel import NeoPixel
import machine
from utime import sleep

import config

# Create the strip object so we can control all 12 lights
strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
```

When this runs, the program is ready to send colors to the strip, but nothing
lights up yet.

## A Helper That Fills the Strip

Each pixel has an **index** (a number that names it). The first pixel is
`strip[0]`, the next is `strip[1]`, and the last is `strip[11]`. Counting
starts at 0, so 12 pixels are numbered 0 through 11.

We want to set *every* pixel to the same color. Typing all 12 lines would take
a while. Instead, we write a **helper function** (a named block of code we can
reuse) called `fill`.

```python
# Helper: set every pixel to the same color and show it
def fill(color):
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()
```

When you call `fill`, every one of the 12 pixels turns the color you pass in.

!!! info "Pixel thinks..."
    <img src="../../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    The `for` loop is the star here. It runs the line `strip[i] = color` one
    time for each pixel. First `i` is 0, then 1, then 2, all the way to 11.
    Doing the same thing to every item in a list is called **iteration**. It's
    one of a coder's most powerful moves!

## How the Helper Works

Let's read the `for` loop line by line.

- `for i in range(config.NUMBER_PIXELS):` repeats the loop 12 times. Each time,
  `i` holds the next pixel index: 0, then 1, then 2, and so on.
- `strip[i] = color` sets the pixel at index `i` to the color we passed in.
- `strip.write()` runs once after the loop. It sends all the colors to the
  strip at the same time so they appear together.

Without that loop, we'd need 12 separate lines to fill the strip. With it, we
write the rule once and let the computer repeat it. That is the gift of
iteration.

## Painting the Strip in Colors

A color is an **RGB tuple** (three numbers for red, green, and blue). The
numbers go from 0 to 255. We use 50, a gentle brightness that's kind to your
eyes. Here is the main loop that paints the strip.

```python
while True:
    print('Red')
    fill((50, 0, 0))
    sleep(1)

    print('Green')
    fill((0, 50, 0))
    sleep(1)

    print('Blue')
    fill((0, 0, 50))
    sleep(1)

    print('White')
    fill((50, 50, 50))
    sleep(1)

    print('Off')
    fill((0, 0, 0))
    sleep(1)
```

The whole strip glows red for one second, then green, then blue, then white,
then goes dark, and the cycle repeats.

!!! warning "Watch out!"
    <img src="../../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    Watch the strip as it changes color. If one pixel stays dark or shows the
    wrong color, that's a clue! It may be a loose wire or a tired pixel. Note
    which pixel it is by counting from `strip[0]`. Finding it now saves you a
    head-scratch later.

## Try It Yourself

1. **Make it brighter.** Change each `50` to `100`. Watch how the colors get
   bolder. Try `200` next, but be ready for bright light.
2. **Add a new color.** After the white step, add `fill((50, 50, 0))` with its
   own `sleep(1)`. Mixing red and green gives you yellow!
3. **Slow it down.** Change each `sleep(1)` to `sleep(2)`. Now you have more
   time to check each pixel.

## Check Your Understanding

1. What does the `for` loop inside `fill` do?
2. What is the index of the very first pixel on the strip?
3. In the tuple `(50, 0, 0)`, which number controls the red light?
4. Why do we write a helper function instead of 12 separate lines?
5. What should you look for to know a pixel is broken?

!!! success "Chapter complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You tested all 12 pixels and they passed! You also met the `for` loop, the
    tool that lets one rule paint a whole strip. Almost every light show you
    build from here uses iteration. You're already glowing!

## What's Next

In [Lab 5: The Scanner](05-spinner.md), you'll move a single light along the
strip to make it look like it's running.
