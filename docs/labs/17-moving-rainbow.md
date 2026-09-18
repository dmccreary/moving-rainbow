# Lab 17: Moving Rainbow with a Color List

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    A rainbow on the move! This time we'll write out each color by hand. Then we'll slide the
    whole rainbow down the strip.

**Program file:** [`17-moving-rainbow.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/17-moving-rainbow.py)

## What you'll learn

- How to keep seven colors in a tuple and step through them
- How `strip[index + i]` draws the rainbow starting at any pixel
- Why the last position needs extra clean-up
- How this list version differs from the color wheel version in Lab 13

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

## The program

This program draws a seven-color rainbow at the start of the strip, slides it to the far end, erases it, and starts over.

```python title="17-moving-rainbow.py"
--8<-- "src/kits/moving-rainbow-base/17-moving-rainbow.py"
```

Run it. A rainbow of seven pixels appears at the start of the strip and slides toward the other end. Then it vanishes and appears at the start again.

[Lab 13](13-moving-rainbow.md) also slides a short rainbow, but it makes its colors with the `wheel()` function. Here you choose every color yourself, so you control every number.

## How it works

### A tuple of colors

```python
color_names = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
num_colors = len(color_names)
colors = (red, orange, yellow, green, blue, indigo, violet)
```

A **tuple** is an ordered group of values inside parentheses. Each item has a position number that starts at 0. So `colors[0]` is red, and `colors[6]` is violet. Each color is itself a tuple of red, green, and blue amounts.

The `len()` function counts the items in a tuple. The `color_names` tuple exists only so `num_colors` can count to 7.

### Draw the rainbow at a starting pixel

```python
index = 0
# draw the rainbow
for color in colors:
    strip[index + i] = colors[index]
    index += 1
strip.write()
```

The variable `i` (from the outer loop below) is the starting pixel. The variable `index` counts from 0 to 6. Each time around, `strip[index + i]` puts color number `index` on pixel `i + index`. When `i` is 5, red lands on pixel 5, orange on 6, and so on up to violet on 11.

The loop variable `color` is not used. The code picks each color with `colors[index]` instead. After all seven colors are set, one `strip.write()` shows them.

### Slide the rainbow

```python
for i in range(0, NUMBER_PIXELS - num_colors + 1):
```

This loop gives `i` the values 0 to 23. The last spot where all seven pixels fit is 23 to 29. The math is 30 - 7 + 1 = 24, and `range` stops one number short of 24.

```python
sleep(.05)
# erase the current pixel
strip[i] = (0,0,0)
```

After a short pause, `strip[i] = (0,0,0)` turns off the rainbow's first pixel, the red one. This only changes the Pico's memory. On the next pass, the rainbow draws on pixels `i+1` to `i+7`, which covers the other six pixels. Pixel `i` stays dark, so the rainbow moves one step. One trip takes 24 steps of 0.05 seconds, about 1.2 seconds.

### Erase the last rainbow

```python
if i == NUMBER_PIXELS - num_colors:
    strip[i+1] = (0,0,0)
    strip[i+2] = (0,0,0)
    ...
    strip[i+6] = (0,0,0)
    strip.write()
```

At the last spot, `i` is 23. The line above cleared only pixel 23. Pixels 24 to 29 would stay lit. These six lines turn them off, and then `strip.write()` sends the dark strip. The `for` loop ends, and the `while True:` loop starts again with `i` at 0.

This rainbow does not wrap around like the bands in [Lab 15](15-moving-band.md). It disappears at the end and appears at the start.

!!! warning "Heads up"
    The six erase lines match exactly seven colors. With eight colors, the last pixel stays lit. With six colors, the program stops with an `IndexError`, because the strip has no pixel 30. The second challenge below fixes this.

## Try it yourself

1. Write the colors in reverse order. Change the `colors = ...` line so `violet` comes first and `red` comes last. Which end of the rainbow leads now?
2. Replace the six erase lines with a loop, so the program works for any number of colors. Try it on your own first. Then compare your loop with this one.

```python title="Your change"
if i == NUMBER_PIXELS - num_colors:
    for k in range(1, num_colors):
        strip[i+k] = (0,0,0)
    strip.write()
```

## Check your understanding

1. What is `colors[2]`?
2. Why does the loop stop at `i` equal to 23 on a 30-pixel strip?
3. What does `strip[i] = (0,0,0)` erase? Why do the other rainbow pixels not need erasing?
4. Why does the program need six extra erase lines at the end?
5. Does this rainbow wrap around the end of the strip like the bands in Lab 15?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You built a rainbow from a list and sent it sliding down the strip! Tuples and loops work as a team.

**What's next:** In [Lab 18: Candle Flicker](18-candle-flicker.md), random numbers make the strip glow like a candle flame.
