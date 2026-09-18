# Lab 14: Band

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Time to paint with blocks of color! We'll write one small function and use it six times
    to fill the whole strip. Let's light this up!

**Program file:** [`14-band.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/14-band.py)

## What you'll learn

- How to write a function that paints one band of color
- How `range(start, end+1)` counts through the pixels in a band
- How the modulo operator `%` keeps a pixel number on the strip
- Why a program can end by itself and leave the lights on

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

## The program

This program paints six bands of color, five pixels wide each, and then it ends.

!!! warning "Power check"
    This program lights all 30 pixels at once. With the six colors near the top, the strip draws about 780 mA. A USB port supplies about 500 mA. Read [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go) for the details. To fix it, divide every number in the six color lines by 4, for example `red = (64, 0, 0)`. That lowers the estimate to about 195 mA.

```python title="14-band.py"
--8<-- "src/kits/moving-rainbow-base/14-band.py"
```

Run it. Six bands appear from one end of the strip to the other: red, orange, yellow, green, blue, and purple.

## How it works

### Name the colors

```python
red = (255, 0, 0)
orange = (140, 60, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
```

Each color is a **tuple** (a group of values inside parentheses). The three numbers are the amounts of red, green, and blue, as in [Lab 02](02-blink.md). Giving each color a name lets us write `red` later instead of typing the numbers again.

### Paint one band with a function

```python
def draw_band(start, end, color):
    # draw the band from start to end
    for i in range(start, end+1):
        # use the modulo to round to within the range of the strip
        strip[i % NUMBER_PIXELS] = color
    strip.write()
```

A **function** is a named block of code you can run again and again. The word `def` creates one. This function has three **parameters** (named slots for values you hand to the function): `start`, `end`, and `color`.

The `for` line starts a **for loop**, which repeats its indented lines once for each number in the range. The variable `i` holds the current pixel number. The `range` function stops one number short of its second value. That's why we write `end+1`: it makes the band include the `end` pixel.

When the loop finishes, `strip.write()` sends the new colors to the strip.

### Keep the pixel on the strip

The strip has pixels 0 to 29, so pixel 30 does not exist. The **modulo** operator `%` gives the remainder after a division. It turns any number into a valid pixel number.

- `29 % 30` is 29, so pixel 29 stays pixel 29.
- `30 % 30` is 0, so the count wraps back to the first pixel.
- `31 % 30` is 1, so 31 lands on pixel 1.

In this lab every band fits on the strip, so `%` changes nothing. It matters in [Lab 15](15-moving-band.md), when the bands slide. You can watch wrap-around happen in the [Modulo Wrap-Around Animation](../sims/modulo-wrap-simulation/index.md) MicroSim.

### Six bands, six calls

```python
draw_band(0, 4, red)
draw_band(5, 9, orange)
draw_band(10, 14, yellow)
draw_band(15, 19, green)
draw_band(20, 24, blue)
draw_band(25, 29, purple)
```

Each call paints five pixels: pixels 0 to 4 are red, 5 to 9 are orange, and so on. Six bands of five pixels make 30 pixels, which is the whole strip.

### Changing the strip length

These numbers are made for a 30-pixel strip. If your strip is different, set `NUMBER_PIXELS` in `config.py`, then think about what changes.

- On a longer strip, pixels past number 29 stay dark, because no band reaches them.
- On a shorter strip, the later bands wrap around with `%` and paint over the first bands. On a 20-pixel strip, blue lands on pixels 0 to 4 and covers the red band.

### The program ends by itself

There is no `while True:` in this program. After the last `draw_band` call, the program reaches the bottom and stops. The strip keeps showing the bands. Press **Run** in Thonny to draw them again.

## Try it yourself

1. Change `purple = (255, 0, 255)` to `purple = (64, 0, 64)`. Then pick a new color of your own and give it a name.
2. Replace the six `draw_band` lines with three wider bands. What happens to the strip?

```python title="Your change"
draw_band(0, 9, red)
draw_band(10, 19, green)
draw_band(20, 29, blue)
```

## Check your understanding

1. Why does `draw_band` use `end+1` inside `range`?
2. What is `31 % 30`? Which pixels would `draw_band(28, 31, red)` light?
3. Which pixels are in the green band?
4. Why does the program stop by itself instead of running forever?
5. What would you see on a 20-pixel strip?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    One small function painted a whole rainbow of blocks! Functions let us reuse a good idea. Next, we make these bands move.

**What's next:** In [Lab 15: Moving Band](15-moving-band.md), the same six bands slide along the strip and wrap around the end.
