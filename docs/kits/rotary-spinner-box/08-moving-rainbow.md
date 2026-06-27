# Lab 8: The Moving Rainbow

In Lab 7 you painted a rainbow across all 12 pixels. It looked great, but it
stayed still. In this lab you'll make that rainbow **move**. It will slide
along your strip like the lights on a movie marquee. The secret is one number
that grows a little bit each step.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    A still rainbow is pretty. A moving rainbow is magic! Today we'll teach
    your colors to walk down the strip. The trick is so small it's almost
    sneaky. Let's light this up!

## What You'll Learn

By the end of this lab, you'll be able to:

- Use a **variable** that changes over time to make an **animation**
- Add an **offset** (a shift amount) to scroll your rainbow along the strip
- Use **modulo** (`%`) so a number wraps back around to the start
- Connect the `color_wheel` function from Lab 7 to moving light

## What You'll Need

- Your Rotary Spinner Box with the 12-pixel LED strip
- A USB cable to connect the box to your computer
- The Thonny program open on your computer

You do **not** need the knob or the buttons for this lab.

## What Is an Animation?

An **animation** is a picture that changes a little bit, over and over, fast
enough that it looks like motion. A cartoon works this way. So does our moving
rainbow. We draw the rainbow, shift it a tiny step, and draw it again. Your
eyes blend those steps into smooth movement.

To shift the rainbow, we use one number. We call it the **offset** (the amount
we slide the colors by). The offset starts at `0` and grows each step.

## The Color Wheel, Back Again

This is the same `color_wheel` function from Lab 7. It takes a **position**
(a number from 0 to 255) and returns an `(r, g, b)` color.

```python
# The color wheel: position 0-255 in, an (r,g,b) color out
def color_wheel(pos):
    pos = pos % 256
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)
```

When you give it a position, it hands back a rainbow color for that spot.

## Setting Up the Moving Parts

Before the rainbow can move, we set up two things: how long to wait between
steps, and the offset that does the sliding.

```python
# How long to wait between steps, in seconds
DELAY = 0.03

# This grows each step to make the rainbow move
offset = 0
```

`DELAY` is a short pause, and `offset` starts at zero so the rainbow begins
right where Lab 7 left it.

!!! info "Pixel thinks..."
    <img src="../../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    The `offset` is the star of this show. It's one little number that changes
    every loop. When a variable changes over time like this, it can bring a
    whole strip of lights to life. One number, twelve dancing pixels!

## Making the Rainbow Scroll

Here is the main loop. It paints all 12 pixels, then grows the offset so the
next painting is shifted a little.

```python
while True:
    for i in range(config.NUMBER_PIXELS):
        # spread the rainbow along the strip, then shift it by the offset
        position = int(i * 256 / config.NUMBER_PIXELS) + offset
        strip[i] = color_wheel(position)
    strip.write()
    sleep(DELAY)

    # grow the offset so the rainbow moves next time (wrap at 255)
    offset = (offset + 2) % 256
```

Every time through the loop, the whole rainbow takes one small step along the
strip.

## How It Works, Line by Line

Let's read the moving part slowly.

- `for i in range(config.NUMBER_PIXELS):` walks through each pixel, from 0 to
  11. The number `i` is the pixel we're working on.
- `int(i * 256 / config.NUMBER_PIXELS)` spreads the rainbow evenly across the
  strip. This is the same spacing you used in Lab 7.
- `+ offset` is the new part. It shifts every pixel's color by the same amount.
  Add a bigger offset, and every color slides further along.
- `strip[i] = color_wheel(position)` sets that pixel to its rainbow color.
- `strip.write()` sends all the colors to the strip at once.
- `offset = (offset + 2) % 256` grows the offset by 2 for the next step.

Because **every** pixel gets the same `+ offset`, the whole pattern shifts
together. That's what makes it look like the rainbow is gliding down the strip.

## Why We Use Modulo

The offset keeps growing: 2, 4, 6, and up and up. If it grew forever, the
number would get huge. So we use **modulo** (the `%` sign), which gives the
**remainder** after dividing. `offset = (offset + 2) % 256` keeps the offset
between 0 and 255.

When the offset reaches 256, modulo wraps it back to 0. The rainbow loops
around smoothly and never runs out of room.

!!! tip "Pixel's tip"
    <img src="../../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel shares a tip">
    Think of `% 256` like a clock. After 12 o'clock, the hands don't go to 13
    — they wrap back around. Our offset wraps at 256 the same way. That wrap
    is what makes the rainbow flow forever with no jump.

## Try It Yourself

1. **Change the speed.** Make the rainbow move faster by changing `DELAY` from
   `0.03` to `0.01`. Then try a slow crawl with `DELAY = 0.2`.
2. **Change the step size.** In `offset = (offset + 2) % 256`, change the `2`
   to a `6`. How does a bigger step change the way the rainbow moves?
3. **Run it backward.** Try `offset = (offset - 2) % 256`. Which way does the
   rainbow scroll now?

## Check Your Understanding

1. What does the word **animation** mean?
2. What does the `offset` variable do to the rainbow?
3. Why do we add `offset` to every pixel's position?
4. What does modulo (`%`) do to the offset when it reaches 256?
5. Which line decides how fast the rainbow moves?

!!! success "Chapter complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You made a rainbow move with one tiny number! Animation is just drawing,
    shifting, and drawing again, fast. You now hold the secret behind every
    light show that flows. You're already glowing!

## What's Next

In [Lab 9: Knob Brightness](09-rotary-brightness.md), you'll turn the knob on
your box to make your lights dim and bright.
