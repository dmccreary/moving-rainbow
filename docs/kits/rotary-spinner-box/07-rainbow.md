# Lab 7: The Rainbow

In this lab, you'll paint a full rainbow across all 12 pixels at once. The
strip will glow from one end to the other in smooth, shifting colors. To do it,
you'll meet a powerful idea in code: the **function** (a reusable tool you build
once and use again and again).

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    A whole rainbow on one strip — this is one of my favorite light shows! The
    secret is a little helper called a color wheel. You hand it a number, and it
    hands you back a color. We'll build it once, then use it 12 times. Let's
    light this up!

## What You'll Learn

By the end of this lab, you'll be able to:

- Explain what a **function** is and why it's useful
- Use the `color_wheel(pos)` function to turn one number into a color
- Spread evenly spaced colors across all 12 pixels
- Map a pixel's spot on the strip to a spot on the color wheel
- Describe what **abstraction** means in a program

## What You'll Need

- Your Rotary Spinner Box with the 12-pixel LED strip
- A USB cable to connect the box to your computer
- The Thonny program open on your computer

You won't need the knob or the buttons for this lab.

## Meet the Color Wheel

A **color wheel** is a circle of colors. It starts at red, flows through green
and blue, and loops back to red. Our program uses a **function** to do the same
thing in code. A function is a block of code you name and reuse. You give it
some input, and it gives you back a result.

Here is the function from `07-rainbow.py`. It is named `color_wheel`.

```python
# Give it a position from 0 to 255 and it returns an (r, g, b) color.
# As the position grows, the color moves through red, green, and blue.
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

When you call `color_wheel(0)`, you get bright red back. Different numbers give
you different colors from around the wheel.

## Why a Function Is a Reusable Tool

The math inside `color_wheel` looks busy. But here's the wonderful part: once
it works, you never have to think about that math again. You call the function
by its name, and it does the messy work for you.

Hiding messy details behind a simple name is called **abstraction**. Think of a
light switch. You flip it, and the room lights up. You don't think about the
wires in the wall. The switch *abstracts* away the hard parts. Our
`color_wheel` function does the same for color math.

!!! info "Pixel thinks..."
    <img src="../../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    The word `return` is the function's way of handing something back to you.
    When `color_wheel` reaches a `return` line, it stops and gives you an
    `(r, g, b)` color. You catch that color and use it however you like!

## Painting One Smooth Rainbow

Now we use our tool. The strip has 12 pixels. We want each pixel to show a
different color, evenly spaced around the wheel. That way the colors flow
smoothly from one end of the strip to the other.

Here is the loop that paints the rainbow.

```python
# Set each pixel to an evenly spaced color around the wheel, just once
for i in range(config.NUMBER_PIXELS):
    position = int(i * 256 / config.NUMBER_PIXELS)
    strip[i] = color_wheel(position)
strip.write()
```

When you run it, all 12 pixels light up at once and hold a still rainbow.

## How the Spacing Works

The loop runs once for each pixel. The variable `i` is the pixel's number,
counting `0, 1, 2,` and so on up to 11. Inside the loop, we turn that pixel
number into a spot on the color wheel.

- `config.NUMBER_PIXELS` is 12, the number of lights on the strip.
- The wheel has 256 spots, numbered 0 to 255.
- `int(i * 256 / config.NUMBER_PIXELS)` spreads those 256 spots evenly across
  the 12 pixels. The word `int` means we round to a **whole number** (a number
  with no decimal point), because pixels need whole positions.

So pixel 0 gets wheel spot 0, pixel 1 gets about 21, pixel 2 gets about 42, and
on across the strip. Each pixel steps a little further around the wheel. The
result is one rainbow, end to end. Our strip is a straight line, not a ring, so
the rainbow runs from the first pixel to the last.

!!! tip "Pixel's tip"
    <img src="../../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel shares a tip">
    Notice we call `strip.write()` *after* the loop, not inside it. We set all
    12 colors first, then send them to the strip in one go. That makes the whole
    rainbow appear together, in a single flash!

## Why It Holds Still

After the rainbow appears, nothing changes. The program reaches a loop that
only waits.

```python
# Nothing changes after this, so the main loop just waits
while True:
    sleep(1)
```

The strip keeps glowing with the same rainbow until you stop the program.

## Try It Yourself

1. **Reverse the rainbow.** Change `i * 256` to `(config.NUMBER_PIXELS - i) *
   256`. Which end starts with red now?
2. **Spread two rainbows.** Change `256` to `512` in the `position` line. What
   happens to the colors across the strip?
3. **Pick one color for all.** Replace the loop body with
   `strip[i] = color_wheel(100)`. Why do all the pixels match now?

## Check Your Understanding

1. What does a **function** do for you in a program?
2. What does `color_wheel(0)` give you back?
3. What does the word **abstraction** mean?
4. Why do we use `int` in the `position` line?
5. Why do we call `strip.write()` after the loop instead of inside it?

!!! success "Chapter complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    A full rainbow, built from one little function you can reuse forever — that's
    real coding power! You learned to hide messy math behind a simple name and
    let it do the heavy lifting. You're already glowing!

## What's Next

In [Lab 8: The Moving Rainbow](08-moving-rainbow.md), you'll make this rainbow
slide along the strip and come alive.
