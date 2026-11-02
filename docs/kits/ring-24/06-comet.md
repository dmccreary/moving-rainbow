# Lab 6: Comet

A bright comet with a fading tail circles the ring. After every lap, the comet changes to the next color of the rainbow.

!!! tip "Pixel says..."
    <img src="../../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Our dot is growing a tail! Watch it streak around the ring like a tiny shooting star.

**Program file:** [`06-comet.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/ring-24/06-comet.py)

![A cyan comet near the top of the ring with a tail that fades out behind it](img/06-comet.png){ width="260" }

*Drawn by a ring simulator on a computer, so your real ring may look a little different. On the real ring it moves.*

## What You'll Learn

- Draw a tail with a `for` loop inside the main loop
- Make a **fade** (a color that gets dimmer step by step) along the tail
- Use `%` to wrap the tail across pixel 0
- Pick colors from a **tuple** (a list of values that cannot change) with an index

## What You'll Need

- Your ring kit with the ring on GPIO 0
- `config.py` saved on the Pico

## The Program

This program draws a 10-pixel comet that goes around clockwise and changes color each lap.

```python
--8<-- "src/kits/ring-24/06-comet.py"
```

You should see a red comet circle the ring, then orange, yellow, green, cyan, blue and violet, and then red again.

## How It Works

`strip.fill((0, 0, 0))` clears the ring in memory at the start of each step. Then the `for` loop draws the comet, one pixel for each value of `t` from 0 to 9.

`t` is how far a pixel is behind the head. `(1 - t / TAIL_LENGTH) ** 2` gives 1 for the head and smaller numbers for the tail. The `** 2` means "squared" (times itself). Squaring makes the tail fade away faster, so it looks more like a real comet. The last tail pixel is so dim that it rounds down to off.

`(position - t) % NUMBER_PIXELS` finds the spot behind the head. When the head is at pixel 2, the tail reaches back to pixels 1, 0, 23, 22 and so on. The `%` turns -1 into 23, so the tail wraps with no gap.

When `position` comes back to 0, one lap is done. `color_index` moves to the next color in `colors`, and `% color_count` sends it back to red after violet.

## Try It Yourself

1. Change `TAIL_LENGTH` to `20`. Then try `4`. How does the comet change?
2. Take out the `** 2` part. Does the tail look brighter or dimmer?

## Check Your Understanding

1. What does `strip.fill((0, 0, 0))` do at the start of each step?
2. How many colors does the comet use before it starts over?
3. What is `-1 % 24`?

!!! success "Lab complete!"
    <img src="../../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrating">
    Your comet is a real star! Seven colors and not one gap in the tail.

## What's Next

Go on to [Lab 7: Two Comets](07-two-comets.md).
