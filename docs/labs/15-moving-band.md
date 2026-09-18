# Lab 15: Moving Band

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    The bands are going for a walk! One growing number makes every band slide along the strip.
    Let's get moving!

**Program file:** [`15-moving-band.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/15-moving-band.py)

## What you'll learn

- How adding a growing number to every band position makes the bands slide
- How the modulo operator `%` wraps a band from the end of the strip back to the start
- Why this pattern needs no erasing
- How `sleep(.03)` sets the speed of the animation

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- [Lab 14: Band](14-band.md) finished, because this lab reuses its `draw_band` function

## The program

This program draws the six bands from Lab 14, slides them one pixel, and draws them again, forever.

!!! warning "Power check"
    The bands cover all 30 pixels, so this program draws about 780 mA at every step. A USB port supplies about 500 mA. Read [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go) for the details. To fix it, divide every number in the six color lines by 4, for example `red = (64, 0, 0)`. That lowers the estimate to about 195 mA.

```python title="15-moving-band.py"
--8<-- "src/kits/moving-rainbow-base/15-moving-band.py"
```

Run it. The six bands slide toward the far end of the strip. Each band that leaves the end appears again at the start.

## How it works

### The same function as Lab 14

```python
def draw_band(start, end, color):
    # draw the band from start to end
    for i in range(start, end+1):
        # use the modulo to round to within the range of the strip
        strip[i % NUMBER_PIXELS] = color
    strip.write()
```

This function fills the pixels from `start` to `end` with one color. See [Lab 14](14-band.md) for the details. Each call ends with `strip.write()`, so the strip updates six times in every step.

### Add an offset

```python
i=0
while True:
    draw_band(0+i, 4+i, red)
    draw_band(5+i, 9+i, orange)
    ...
    i += 1
    sleep(.03)
```

The variable `i` is the **offset** (how far the pattern has moved). It starts at 0. Every band position has `i` added to it.

The `while True:` line starts a **loop** (code that repeats). Each time around, `i += 1` adds 1 to `i`. So the red band covers pixels 0 to 4 at first, then 1 to 5, then 2 to 6. The whole pattern slides toward higher pixel numbers.

### Wrap around with modulo

The variable `i` keeps growing, but the strip only has pixels 0 to 29. The `%` inside `draw_band` solves this. Try `i` equal to 27. The red band asks for pixels 27, 28, 29, 30, and 31. Since `30 % 30` is 0 and `31 % 30` is 1, red lands on pixels 27, 28, 29, 0, and 1. The end of the band wraps to the start.

Without `%`, the second step would already fail. The purple band would ask for pixel 30 when `i` is 1, and the strip has no pixel 30.

You can watch this in the [Modulo Wrap-Around Animation](../sims/modulo-wrap-simulation/index.md) MicroSim.

### No erasing needed

Six bands of five pixels cover all 30 pixels at every step. Every pixel gets a new color each time, so nothing is left behind. Later labs light only a few pixels, and those need an erase step.

### Speed

The `sleep(.03)` line pauses for 0.03 seconds after each step. One lap around a 30-pixel strip takes 30 steps. That's 0.9 seconds of pausing, plus a little time for writing to the strip.

## Try it yourself

1. Change `sleep(.03)` to `sleep(.1)` for a slow crawl. Then try `.005`. How does the speed change?
2. Change `i += 1` to `i -= 1`. Which way do the bands slide now? Python's `%` turns a negative number such as -1 into a pixel number at the end of the strip.

## Check your understanding

1. Which line makes the bands move?
2. Which pixels does the red band light when `i` is 27?
3. Why does this program need no erasing?
4. How many steps make one lap of a 30-pixel strip? About how long does a lap take?
5. What would go wrong if we removed `% NUMBER_PIXELS`?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You made a whole rainbow of blocks glide around the strip! A growing offset plus modulo is a trick you can reuse in many patterns.

**What's next:** In [Lab 16: Comet](16-comet.md), a bright head with a fading tail streaks along the strip.
