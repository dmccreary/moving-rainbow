# Cellular Automaton

What if a pattern could grow more complex over time, using nothing but one
tiny rule applied over and over? That's a **cellular automaton** — and
this lesson builds a famous one called Rule 30 using nothing but your LED
strip.

!!! tip "Pixel says..."
    This is one of my favorite kinds of pattern, because something this
    simple can grow so surprisingly complex. Mathematicians still study
    Rule 30 today!

## What you'll learn

- What a cellular automaton is
- How a **neighborhood** of three cells decides the next state of the middle one
- Why the rule is called "30," using binary from the last few lessons
- How to compute a whole new generation of pixels from the one before it

## What you'll need

- Your Pico and NeoPixel strip
- The kit's `config.py` file
- No buttons are needed for this lesson

## One Cell, Three Neighbors

Each pixel in this pattern is a **cell** that is either on (`1`) or off
(`0`). To decide whether a cell turns on in the *next* generation, the
rule looks at that cell and its two neighbors — three cells total, which
makes 8 possible patterns (`000` through `111`).

## Why It's Called "Rule 30"

Remember [Binary Counter](42-binary-counter.md)? The number 30 in binary
is `00011110`. Each one of those 8 bits answers "does this neighborhood
pattern turn on?" for one of the 8 possible 3-cell neighborhoods:

```python
new_cells[i] = (RULE >> pattern) & 1
```

`pattern` is a number from 0 to 7 built from the three neighbor cells.
Shifting `RULE` (which is `30`) right by `pattern` places, then checking
the last bit with `&`, reads exactly one answer out of those 8 bits.

## The Full Program

```python
# Rule 30: a simple rule turns one row of pixels into the next, one
# generation at a time. Watch the pattern grow more complex over time!
from machine import Pin
from neopixel import NeoPixel
from utime import sleep
import config

strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

ON_COLOR = (0, 150, 200)
OFF_COLOR = (0, 0, 0)

# Rule 30 is named after the number 30 itself: written in binary, 30 is
# 00011110. Each bit answers "does this 3-cell neighborhood turn on?" for
# one of the 8 possible neighborhoods (000 through 111).
RULE = 30


def next_generation(cells):
    n = len(cells)
    new_cells = [0] * n
    for i in range(n):
        left = cells[(i - 1) % n]
        center = cells[i]
        right = cells[(i + 1) % n]
        # turn the 3 neighbor cells into a number from 0 to 7
        pattern = (left << 2) | (center << 1) | right
        # look up that bit inside the number 30
        new_cells[i] = (RULE >> pattern) & 1
    return new_cells


def draw(cells):
    for i in range(len(cells)):
        strip[i] = ON_COLOR if cells[i] else OFF_COLOR
    strip.write()


# start with a single lit pixel in the middle
cells = [0] * config.NUMBER_PIXELS
cells[config.NUMBER_PIXELS // 2] = 1

while True:
    draw(cells)
    sleep(0.3)
    cells = next_generation(cells)
```

Run it and watch a single lit pixel grow into a triangular, almost random
looking pattern — from one simple rule, applied again and again.

!!! info "Pixel thinks..."
    The `% n` in `cells[(i - 1) % n]` wraps the strip into a loop, so the
    last pixel's right neighbor is pixel 0. Without it, the edges of the
    strip would crash the program by reaching for a pixel that doesn't exist.

## Try It Yourself

- Change `RULE = 30` to `RULE = 90` or `RULE = 110` — both are other
  famous automaton rules with very different-looking patterns.
- Start with two lit pixels instead of one, and see how the pattern changes.

## Check Your Understanding

1. What three things make up a "neighborhood" in this program?
2. Why is this rule called "Rule 30" specifically?
3. What does the `% n` do in `cells[(i - 1) % n]`?
4. What would happen if `RULE` were `0`?

!!! success "You've got this!"
    You just built a real, studied piece of computer science — not a
    light show effect, but an actual mathematical object. That's a huge
    step up in what your code can explore.

**What's next:** in [Sorting Visualizer](48-sorting-visualizer.md), you'll
watch a real sorting algorithm organize your pixels one comparison at a time.
