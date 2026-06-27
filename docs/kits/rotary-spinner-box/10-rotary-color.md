# Lab 10: Knob Color

In Lab 9, the knob changed how *bright* your strip was. This time the knob
changes the *color*. Spin it one way and the colors march forward around the
rainbow. Spin it the other way and they march back. The best part: the colors
never run out. When you reach the end, they loop right back to the start.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Last lab, your knob was a brightness dial. Now it's a color dial! We'll spin
    around a whole rainbow with one finger. And here's the magic word for today:
    **wrap-around**. The colors will loop forever with no dead end. Let's light
    this up!

## What You'll Learn

By the end of this lab, you'll be able to:

- Store a color choice in a **parameter** (a value your program uses to make a picture)
- Move a position around a **color wheel** (the full circle of colors, 0 to 255)
- Use **modulo** (the remainder after dividing) to make values **wrap around**
- Explain how this lab reuses the same pattern as Lab 9, with a new parameter

## What You'll Need

- Your Rotary Spinner Box with the Pico inside
- The 12-pixel LED strip plugged in
- The **rotary encoder** (the knob you turn) plugged in
- A USB cable and the Thonny program on your computer

You'll use the strip and the knob for this lab. You won't need the buttons.

## The Same Pattern, a New Parameter

A **parameter** is a value your program reads to decide what to draw. In Lab 9,
the parameter was brightness. Here the parameter is a color. We store it in a
variable named `hue`.

```python
# The color parameter: a position on the color wheel (0-255)
hue = 0

# How many wheel steps each click of the knob moves
STEP = 8
```

`hue` starts at `0`, which is the very start of the color wheel. `STEP` is how
far each click of the knob moves us around that wheel.

## The Color Wheel

A **color wheel** is the full circle of rainbow colors. We give it a position
from `0` to `255`, and it hands back one color as red, green, and blue amounts.
You met this same idea back in Lab 7.

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

Small numbers give you reds and oranges. Middle numbers give greens. Large
numbers give blues and purples. Then it loops back to red.

!!! info "Pixel thinks..."
    <img src="../../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    A **function** is a mini-program with a name. We named ours `color_wheel`.
    We hand it one number and it hands back a color. Now we can ask for a color
    anytime by name. That saves us from writing the same math over and over.

## Painting the Whole Strip One Color

This part fills every pixel with the color for the current `hue`. It reuses the
`color_wheel` function we just read.

```python
# Fill the whole strip with the current color
def show_color():
    color = color_wheel(hue)
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()
```

The strip turns into one solid color. Every one of the 12 pixels shows the
exact same shade.

## Reading the Knob and Wrapping Around

Now the main loop watches the knob. When you turn it one click, the code adds
`STEP` to `hue`. When you turn it the other way, it subtracts `STEP`.

```python
while True:
    current_clk = clk.value()
    if current_clk != last_clk and current_clk == 0:
        if dt.value() != current_clk:
            hue = (hue + STEP) % 256   # clockwise
        else:
            hue = (hue - STEP) % 256   # counterclockwise
        print('hue:', hue)
        show_color()
    last_clk = current_clk
```

Each click nudges the color forward or back, and the whole strip shifts to the
new shade.

The star of this code is `% 256`. The `%` sign is **modulo** — it gives the
**remainder** after dividing. So `% 256` keeps `hue` between `0` and `255`. When
`hue` would go past `255`, it **wraps around** back to `0`. When it would go
below `0`, it wraps up to `255`. The color wheel becomes a real circle with no
end.

!!! tip "Pixel's tip"
    <img src="../../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel shares a clever idea">
    Think of `% 256` like a clock. After 12 o'clock comes 1, not 13. Modulo
    works the same way. After 255 comes 0, not 256. That tiny `% 256` is what
    lets your rainbow spin forever without ever hitting a wall.

## How This Is Different From Lab 9

Lab 9 and Lab 10 use the very same shape: a parameter, a knob, and a step. The
big difference is what happens at the edges.

- Lab 9 **clamped** the brightness. At the top, it stopped. It could not go higher.

- Lab 10 **wraps** the color. At the top, it loops back to the start. It never stops.

Clamping is right when a value has real limits, like brightness. Wrapping is
right when a value goes in a circle, like a color wheel.

## Try It Yourself

1. **Bigger jumps.** Change `STEP = 8` to `STEP = 32`. Now each click leaps
   farther around the wheel. How many clicks does one full rainbow take?

2. **Tiny steps.** Change `STEP` to `2`. The colors creep instead of jump.
   Which `STEP` feels best to your eye?

3. **Start somewhere else.** Change `hue = 0` to `hue = 170`. What color does
   the strip show before you ever touch the knob?

## Check Your Understanding

1. What is the parameter that the knob controls in this lab?

2. What range of numbers does the `color_wheel` function take in?

3. What does the `%` sign mean in `% 256`?

4. What does "wrap around" mean for the color when `hue` goes past 255?

5. How is this lab different from Lab 9 at the edges of the value?

!!! success "Chapter complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You turned a knob into a rainbow dial! You also learned the trick of
    **wrap-around** with modulo, which coders use all the time for clocks,
    circles, and color wheels. Same pattern as last lab, brand-new magic.
    You're glowing!

## What's Next

In [Lab 11: Button Speed](11-button-speed.md), you'll trade the knob for a
button and use it to control how *fast* a pattern moves.
