# Lab 06: Up and Down

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Ready for a round trip? Our pixel will run up the strip and then come right back.
    Watch the two ends closely, because something sneaky happens there!

**Program file:** [`06-up-and-down.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/06-up-and-down.py)

## What you'll learn

- How to count backward through the pixels with `range(NUMBER_PIXELS-1, 0, -1)`
- How to put two loops one after the other, so a pixel moves up and then down
- Why the last pixel is number `NUMBER_PIXELS-1`, not `NUMBER_PIXELS`
- How to trace a loop by hand to see which pixel lights at each turning point

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- The ideas from [Lab 04: Dimmer](04-dimmer.md) (`range` with a step of `-1`) and [Lab 05: Move a Pixel](05-move.md) (write once per step)

## The program

This program sends one red pixel up the strip, and then back down, over and over.

```python title="06-up-and-down.py"
--8<-- "src/kits/moving-rainbow-base/06-up-and-down.py"
```

Run it. The pixel travels from the first pixel to the last, then turns around and comes back. One round trip takes about three seconds.

## How it works

### Up the strip

```python
# move up the strip
for i in range(0,NUMBER_PIXELS):
    strip[i] = (100,0,0)
    strip.write()
    sleep(.05)
    strip[i] = (0,0,0)
```

This is the same loop you met in Lab 05, with a faster `sleep`. The counter `i` runs from 0 to 29, and the strip shows one red pixel at a time. That is 30 steps of 0.05 seconds, or about 1.5 seconds.

### Down the strip

```python
# move down the strip
for i in range(NUMBER_PIXELS-1, 0, -1):
    strip[i] = (100,0,0)
    strip.write()
    sleep(.05)
    strip[i] = (0,0,0)
```

The body of this loop is the same. Only the `range` is new. It uses all three parts you met in Lab 04:

- **Start:** `NUMBER_PIXELS-1` is 29. Pixel numbers start at 0, so the last pixel on a 30-pixel strip is 29. Starting at `NUMBER_PIXELS` (30) would point past the end of the strip, where there is no pixel.
- **Stop:** 0, which is not included.
- **Step:** `-1`, which counts backward.

So `i` counts 29, 28, 27, and so on down to 1. That is 29 steps of 0.05 seconds, or about 1.45 seconds. A whole round trip is 59 steps, which adds up to about three seconds.

The two loops run one after the other. Then `while True:` sends the program back to the top to start the trip again. To see how each index points to a pixel, try the [Pixel Indexing Explorer](../sims/pixel-indexing-explorer/index.md).

### One write per step

```python
# Each step calls strip.write() once. Erasing a pixel does not need its own
# write - the next step's write shows it. (The strip can miss back-to-back writes.)
```

This comment sits above the loops. It is the same rule from Lab 05: write once per step, then sleep. The erase happens in memory, and the next step's write shows it.

### The two turn-around points

Now for the puzzle. Look at the ends of the strip, and trace the loops by hand.

**Pixel 0.** The down loop stops at 1, so pixel 0 is lit only on the way up. Here is why that helps. Imagine the down loop went all the way to 0. Pixel 0 would light at the end of the trip down.

Then the next trip up would light pixel 0 again as its first step. The strip would show no change between those two steps. So pixel 0 would stay lit twice as long, and the motion would seem to stall.

**Pixel 29.** The far end works differently. The up loop ends by lighting pixel 29. The down loop begins by lighting pixel 29 again. The strip shows no change between those two steps either. So pixel 29 stays lit for about 0.1 seconds, which is twice as long as the other pixels. Watch the far end to see if you can spot the tiny pause.

## Try it yourself

1. Use two colors. In the down loop, change `strip[i] = (100,0,0)` to `strip[i] = (0,0,100)`. Now the pixel is red going up and blue coming down. Which line is the down loop's? Look for the one after `# move down the strip`.
2. Solve the far-end puzzle. In the down loop, change `NUMBER_PIXELS-1` to `NUMBER_PIXELS-2`. Which pixels light on the way down now? Does the pause at the far end go away?

## Check your understanding

1. Which pixel numbers does `range(NUMBER_PIXELS-1, 0, -1)` make when `NUMBER_PIXELS` is 30?
2. Why does the down loop start at `NUMBER_PIXELS-1` instead of `NUMBER_PIXELS`?
3. Why is pixel 0 lit only on the way up, and why does that keep the motion smooth at the bottom?
4. About how long does one round trip take? Show your math.
5. Why does each step call `strip.write()` only once?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    Round trip complete! Two loops and a counting trick steered your pixel in both directions.

**What's next:** In [Lab 07: Color Wipe](07-color-wipe.md), a color fills the strip one pixel at a time, then a new color takes over.
