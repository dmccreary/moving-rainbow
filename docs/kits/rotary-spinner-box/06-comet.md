# Lab 6: The Comet

In this lab you'll make a glowing comet fly back and forth along your strip.
The comet has a bright **head** and a **tail** that fades out behind it. Up to
now, you've lit one pixel at a time. This program does something new. It works
out a color for *every* pixel on each step.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    A comet is one bright dot with a glowing trail behind it. To draw it, we
    can't just think about one pixel. We have to ask each pixel a question:
    "How far are you behind the head?" That's a big idea called
    **decomposition** — breaking a hard job into one small job per pixel. Let's
    light this up!

## What You'll Learn

By the end of this lab, you'll be able to:

- Use **decomposition** to solve one pixel at a time
- Measure how far each pixel is **behind** the comet head
- **Fade** a color by multiplying it by a fraction
- Make the comet **bounce** off the ends of a straight strip

## What You'll Need

- Your Rotary Spinner Box with the Pico inside
- The 12-pixel LED strip plugged in
- A USB cable to connect the box to your computer
- The Thonny program open on your computer

You don't need the knob or the buttons for this lab.

## A First Look at the Code

The program is the file `06-comet.py`. It loads `config.py`, which holds your
pin number and pixel count. The strip is on GPIO pin 0 and has 12 pixels.

Here are the settings at the top of the program.

```python
from neopixel import NeoPixel
import machine
from utime import sleep
import config

strip = NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# The base color of the comet head
HEAD_COLOR = (0, 80, 120)

# How many pixels long the fading tail is
TAIL_LENGTH = 5

# How long to wait between steps, in seconds
DELAY = 0.06

# Where the bright head is, and which way it is moving
head = 0
direction = 1
```

These lines set the comet's color, its tail length, its speed, and where it
starts.

## One Job Per Pixel

Here's the new idea. Instead of lighting one pixel, the program loops over
**every** pixel each step. For each pixel, it asks one question: how far behind
the head are you?

```python
while True:
    # Figure out the color of every pixel for this step
    for i in range(config.NUMBER_PIXELS):
        # how many pixels pixel i is behind the head
        behind = (head - i) * direction
        if 0 <= behind < TAIL_LENGTH:
            ...
        else:
            # pixels ahead of the head or past the tail are off
            strip[i] = (0, 0, 0)
```

The `for` loop (code that repeats once per pixel) runs 12 times. The variable
`behind` is **0** at the head itself and gets bigger toward the tail. If a pixel
is too far behind, or ahead of the head, it stays off.

!!! info "Pixel thinks..."
    <img src="../../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    Why multiply by `direction`? When the comet moves right, the tail is to the
    left. When it moves left, the tail is to the right. Multiplying by
    `direction` (which is `1` or `-1`) flips the math so "behind" always points
    the right way. One small change handles both directions!

## Fading the Tail

A comet's tail is bright near the head and fades to dark at the end. We get
that fade by multiplying the color by a **fraction** (a number between 0 and 1).

```python
            # brightness fades from 1.0 at the head to near 0 at the tail end
            fade = (TAIL_LENGTH - behind) / TAIL_LENGTH
            strip[i] = (int(HEAD_COLOR[0] * fade),
                        int(HEAD_COLOR[1] * fade),
                        int(HEAD_COLOR[2] * fade))
```

At the head, `behind` is 0, so `fade` is 1.0 and the color is full bright.
Farther back, `behind` grows, so `fade` shrinks toward 0 and the color gets
dimmer. The `int()` turns each result into a whole number, because a pixel
color must be a whole number from 0 to 255.

## Moving and Bouncing

After drawing all the pixels and writing them out, the program moves the head.
Your strip is **straight**, not a ring, so the comet bounces off each end.

```python
    strip.write()
    sleep(DELAY)

    # if we are at either end, turn around
    if head == 0:
        direction = 1
    elif head == config.NUMBER_PIXELS - 1:
        direction = -1

    # move the head one step in the current direction
    head = head + direction
```

When the head reaches pixel 0 or pixel 11, `direction` flips. Because the tail
always trails behind the head, the tail jumps to the other side when the comet
turns around.

!!! warning "Watch out!"
    <img src="../../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    On a ring, a comet could loop forever in one direction. Your strip has two
    ends, so the comet has to turn around. If your comet runs off the end and
    never comes back, check that both the `if` and the `elif` lines are there to
    flip the `direction`.

## Try It Yourself

1. **Grow the tail.** Change `TAIL_LENGTH = 5` to `TAIL_LENGTH = 10`. How long
   does the glowing trail get now?
2. **Change the comet's color.** Change `HEAD_COLOR = (0, 80, 120)` to
   `(120, 0, 0)` for a red comet, or pick your own three numbers.
3. **Speed it up.** Change `DELAY = 0.06` to `DELAY = 0.02`. How fast can the
   comet fly and still look like a comet?

## Check Your Understanding

1. What does **decomposition** mean in this program?
2. What does the variable `behind` measure?
3. When `behind` is 0, what is the value of `fade`?
4. Why does the program multiply the color by `fade`?
5. Why does the comet bounce instead of looping around?

!!! success "Chapter complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You did it — you drew a whole moving comet by solving one pixel at a time!
    That's decomposition in action. Almost every light show that fills the
    strip uses this same trick. You're already glowing!

## What's Next

In [Lab 7: The Rainbow](07-rainbow.md), you'll give every pixel its own color
and paint a full rainbow across the strip.
