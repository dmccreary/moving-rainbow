# Lab 16: Comet

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Look up! A comet is zooming by. We'll build one with a bright head and a tail that fades
    away. Let's light this up!

**Program file:** [`16-comet.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/16-comet.py)

## What you'll learn

- How a list of brightness levels makes a tail that fades
- How to scale a color by a number between 0 and 1
- How `%` lets the comet wrap around the strip
- How nested loops step through colors and positions

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

## The program

This program sends a comet around the strip once for each of nine colors, then starts over.

```python title="16-comet.py"
--8<-- "src/kits/moving-rainbow-base/16-comet.py"
```

Run it. A bright head with a short fading tail travels along the strip. The comet changes color after every lap.

## How it works

### Nine brightness levels

```python
levels = [255, 128, 64, 32, 16, 8, 4, 2, 1]
level_count = len(levels)
```

A **list** is an ordered group of values inside square brackets. This list holds nine brightness levels. Each number is about half of the one before it. The value 255 is full brightness, and 1 is almost off.

The `len()` function counts the items in a list, so `level_count` is 9. Every pixel in the comet gets one level. Your eyes see brightness on a curve, not a straight line, so halving looks like a smooth fade. The [Perceived vs. Linear Brightness](../sims/perceived-vs-linear-brightness/index.md) MicroSim shows why.

### Scale a color

```python
scale = (levels[i] / 255)
strip[target] = (int(color[0]*scale), int(color[1]*scale), int(color[2]*scale))
```

The first line turns a level into a number between 0 and 1. Level 255 gives 1.0, level 128 gives about 0.5, and level 1 gives about 0.004.

The second line multiplies each part of the color by `scale`. In a color, `color[0]` is the red amount, `color[1]` is green, and `color[2]` is blue. The `int()` function drops the decimal part, because color numbers must be whole numbers. Yellow `(255, 255, 0)` at level 64 becomes about `(64, 64, 0)`.

### Find the head and the tail

```python
def draw_comet_tail(offset, color, delay):
    offset = offset % NUMBER_PIXELS
    for i in range(0, color_count):
        target = ((level_count - i - 1) + offset) % NUMBER_PIXELS
```

The `offset` tells where the comet is. The loop runs nine times, once for each pixel in the comet. Since `level_count` is 9, the `target` is `offset + 8 - i`. The head (level 255) is at `offset + 8`. Each pixel behind it is one step lower and one level dimmer. The `%` wraps any number past the end of the strip back to the start.

Here is the comet when `offset` is 0:

| Loop count `i` | Pixel `target` | Level |
|---|---|---|
| 0 | 8 (the head) | 255 |
| 1 | 7 | 128 |
| 2 | 6 | 64 |
| 3 | 5 | 32 |
| 4 | 4 | 16 |
| 5 | 3 | 8 |
| 6 | 2 | 4 |
| 7 | 1 | 2 |
| 8 | 0 (the tail end) | 1 |

Each pass through the loop ends with `strip.write()` and `sleep(delay)`. The comet appears one pixel at a time, head first. Nine pauses of 0.005 seconds add up to about 0.045 seconds per comet position.

### Erase the old tail

```python
if offset > 0:
    strip[offset-1] = (0,0,0)
if offset == NUMBER_PIXELS-1:
    strip[offset] = (0,0,0)
```

The comet moves one pixel at a time. The pixel right behind the new tail end belongs to the old comet, so the first `if` turns it off. At `offset` 29, the tail ends on pixel 29 and the next comet starts at offset 0. The second `if` turns pixel 29 off, so no light gets left behind at the wrap.

### The main loop

```python
counter = 0
clear()
...
while True:
    for color_index in range(0, color_count):
        for i in range(0, NUMBER_PIXELS):
            draw_comet_tail(counter, colors[color_index], .005)
            counter += 1
```

The `clear()` function turns every pixel off before the show starts. The loop on `color_index` picks each of the nine colors in turn. The loop on `i` moves the comet 30 times, which is one full lap.

The variable `counter` is the offset. It grows forever, and the `%` inside `draw_comet_tail` keeps it on the strip. A lap is exactly 30 steps, so each new color starts with the comet back at offset 0.

Each lap has 30 steps with nine pauses each. That's 1.35 seconds of pausing, plus the time to write to the strip. Nine colors take at least 12 seconds before the show repeats.

### Two things to notice

The program defines a `wheel()` function that came from the color wheel labs. No line in this program calls it, so you can ignore it.

Look at `for i in range(0, color_count)` in `draw_comet_tail`. The tail has one pixel for each level, so `level_count` might seem like the right name. The loop still works because `colors` and `levels` both hold exactly nine items. The second challenge below is a puzzle about this.

## Try it yourself

1. Change the `.005` in `draw_comet_tail(counter, colors[color_index], .005)` to `.02`. The comet slows down. Then try `.001`.
2. This one might feel tricky at first, and that's normal. Replace the `colors = ...` line with these two lines to add a tenth color, then run the program.

```python title="Your change"
pink = (255, 20, 147)
colors = (red, orange, yellow, green, blue, indigo, violet, cyan, white, pink)
```

The program stops with an `IndexError`, which means the code asked a list for an item that is not there. That's a puzzle to solve! Find the `range(0, color_count)` line in `draw_comet_tail` and change `color_count` to `level_count`. Then explain why the fix works.

## Check your understanding

1. What does the `levels` list hold? Which pixel gets level 255?
2. What color do you get if `scale` is 0.5 and the color is `(200, 100, 0)`?
3. When `offset` is 5, which pixel is the head? Which pixel is the tail end?
4. Why does the code use `%` on `target`?
5. How many steps make one lap for each color?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You built a comet with real fading light! Scaling a color by a number between 0 and 1 is a trick you'll use again and again.

**What's next:** In [Lab 17: Moving Rainbow with a Color List](17-moving-rainbow.md), a rainbow you build by hand slides down the strip.
