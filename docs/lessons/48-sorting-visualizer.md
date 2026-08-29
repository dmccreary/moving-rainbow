# Sorting Visualizer

You've written plenty of code that reacts to input. This lesson is
different — it's about watching an **algorithm** (a step-by-step recipe
for solving a problem) work, one small decision at a time.

!!! tip "Pixel says..."
    Sorting is something computers do constantly — contact lists, game
    scores, search results. Now you get to *watch* it happen instead of
    just trusting that it does.

## What you'll learn

- What a sorting algorithm is
- How **bubble sort** compares and swaps neighboring values
- How to represent numeric values as pixel brightness
- Why highlighting the pair being compared makes an algorithm easier to follow

## What you'll need

- Your Pico and NeoPixel strip
- The kit's `config.py` file
- No buttons are needed for this lesson

## Values as Brightness

This program fills a list called `values` with random numbers from 10 to
255 — one per pixel. Instead of drawing colors directly, it draws
*brightness*: a bigger number means a brighter green pixel. A sorted strip
should look like it fades smoothly from dim to bright.

## Bubble Sort, One Comparison at a Time

**Bubble sort** repeatedly looks at two neighboring values. If they're in
the wrong order, it swaps them. Doing this over and over, over the whole
list, slowly "bubbles" the largest values toward the end:

```python
if values[i] > values[i + 1]:
    values[i], values[i + 1] = values[i + 1], values[i]
```

## The Full Program

```python
# Watch a bubble sort in action! Each pixel's brightness represents a
# random value. On every pass, neighboring values are compared and
# swapped if they're out of order, until the whole strip is sorted.
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
from urandom import randint
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
n = config.NUMBER_PIXELS

values = [randint(10, 255) for _ in range(n)]


def draw(highlight_a=None, highlight_b=None):
    for i in range(n):
        brightness = values[i]
        if i == highlight_a or i == highlight_b:
            strip[i] = (brightness, 0, 0)   # the pair being compared: red
        else:
            strip[i] = (0, brightness, 0)   # everything else: green
    strip.write()


draw()
sleep(1)

# bubble sort: repeatedly compare neighbors and swap them if out of order
for pass_num in range(n - 1):
    swapped = False
    for i in range(n - 1 - pass_num):
        draw(i, i + 1)
        sleep(0.03)
        if values[i] > values[i + 1]:
            values[i], values[i + 1] = values[i + 1], values[i]
            swapped = True
            draw(i, i + 1)
            sleep(0.03)
    if not swapped:
        break   # nothing moved this pass - the list is already sorted

draw()   # final result: sorted dimmest to brightest
print("sorted!", values)
```

Run it and watch two red pixels sweep down the strip, comparing
neighbors. When a swap happens, you'll see the brightness pattern shift.
After several passes, the whole strip settles into a smooth dim-to-bright
gradient.

!!! info "Pixel thinks..."
    Watch `swapped`. If a whole pass goes by without a single swap, the
    list must already be sorted — so the program stops early instead of
    wasting time on more passes. That's a small optimization with a big
    name: it turns a slow algorithm into a slightly smarter one.

## Try It Yourself

- Remove the `if not swapped: break` early-exit and count how many total
  passes the unsorted version takes.
- Change the color scheme so the *smallest* value ends up brightest instead of dimmest.

## Check Your Understanding

1. What does a bigger number in the `values` list mean when it's drawn to the strip?
2. What does `values[i], values[i + 1] = values[i + 1], values[i]` do?
3. Why does the outer loop run `n - 1` times?
4. How does the program know when the list is fully sorted, before finishing all possible passes?

!!! success "You've got this!"
    You just visualized a real algorithm that runs, in some form, inside
    almost every piece of software you've ever used.

**What's next:** in [Binary Search Visualizer](49-binary-search-visualizer.md),
you'll flip the challenge around — the *program* will search for a number
using your button presses as clues.
