# Lab 07: Color Wipe

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Ready to paint the whole strip? We'll sweep one color down all 30 pixels, then the next, then the next. Let's light this up!

**Program file:** [`07-color-wipe.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/07-color-wipe.py)

## What you'll learn

- How to store a color in a **tuple** (a fixed group of values in parentheses) and give it a name
- How a loop inside a loop, called a **nested loop**, paints every pixel with every color
- How to put code in a **function** (a named block of code) and run it by name
- How two different delays change the look of the wipe

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- A quick look back at [Lab 05: Move a Pixel](05-move.md), which uses a `for` loop to visit each pixel

## The program

This program fills the strip with red, one pixel at a time, then does the same with eight more colors, and starts over.

```python title="07-color-wipe.py"
--8<-- "src/kits/moving-rainbow-base/07-color-wipe.py"
```

Run it. Red sweeps from pixel 0 to pixel 29. After a one-second pause, orange sweeps down the strip, and so on through nine colors.

## How it works

### Load the tools

This lab loads its tools a little differently from the earlier ones.

```python
import machine
...
strip = NeoPixel(machine.Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
```

`import machine` brings in the whole `machine` module, so the code writes `machine.Pin` where other labs write `Pin`. The lab also gets `sleep` from `time`, where other labs use `utime`. Both ways work.

### Name your colors

These lines give each color a name and gather all nine into one group.

```python
red = (255, 0, 0)
orange = (140, 60, 0)
...
white = (128, 128, 128)
colors = (red, orange, yellow, green, blue, cyan, indigo, violet, white)
```

Each color is three numbers: red, green, and blue, as in [Lab 02](02-blink.md). The parentheses make each one a tuple. A name like `red` is easier to read than `(255, 0, 0)`.

The last line makes a tuple of tuples. The order of names in `colors` is the order of the wipes. Notice that `white` is `(128, 128, 128)`, only half of full white, which is gentler on your USB port.

### A loop inside a loop

This function does the wipe. The outer loop picks a color, and the inner loop paints the pixels.

```python
def color_wipe():
    for color in colors:
        for i in range(0, NUMBER_PIXELS):
            strip[i] = color
            strip.write()
            sleep(.01)
        sleep(1)
```

Read it from the top:

1. `def color_wipe():` starts the function. Nothing inside it runs until something **calls** it (runs it by name).
2. `for color in colors:` is the outer loop. It hands over one color at a time, from `red` to `white`.
3. `for i in range(0, NUMBER_PIXELS):` is the inner loop. The number `i` counts from 0 to 29, and `range` stops before 30.
4. The inner loop paints pixel `i`, writes it to the strip, and waits `.01` seconds.
5. `sleep(1)` waits one second after all 30 pixels have the new color.

Look at where `sleep(1)` sits. It lines up with the inner `for`, so it belongs to the outer loop. That is why it runs once per color and not once per pixel.

!!! info "Key idea"
    The inner loop finishes all 30 laps before the outer loop moves to the next color. One trip through the list paints 9 colors × 30 pixels = 270 pixels.

Two delays shape the wipe. `sleep(.01)` sets how fast each color sweeps along. `sleep(1)` sets how long you can admire the full strip.

The wipe takes 30 × .01 = .3 seconds. With the one-second pause, each color lasts a little over 1.3 seconds, so all nine take about 12 seconds. The strip is not erased between wipes. Each wipe paints over the last color.

!!! warning "Power check"
    Yellow `(255, 255, 0)` and cyan `(0, 255, 255)` each use two full color channels. With all 30 pixels lit, the strip draws about 1,200 mA (30 pixels × 40 mA). A USB port supplies about 500 mA. Read [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go) for the details. To bring the peak down to about 300 mA, divide every color number by 4. For example, change `yellow = (255, 255, 0)` to `yellow = (64, 64, 0)`.

### Repeat forever

These two lines call the function over and over.

```python
while True:
    color_wipe()
```

`color_wipe()` runs the function once. Because it sits inside `while True`, the program plays the nine wipes again and again. Press the **Stop** button in Thonny to end it.

## Try it yourself

1. Change `sleep(.01)` to `sleep(.1)`. How long does one wipe take now? Then try `sleep(.001)`.
2. Add a color of your own. Under `white`, add the line `pink = (100, 20, 40)`. Then add `pink` to the end of the `colors = (...)` line.

## Check your understanding

1. What does `for color in colors:` do?
2. How many pixels does the inner loop visit each time it runs?
3. Why does `sleep(1)` run once per color and not once per pixel?
4. What would you see if you removed the `strip.write()` line? Why?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You wiped nine colors across the strip with a loop inside a loop! That's a big idea packed into a short program.

**What's next:** In [Lab 08: Random](08-random.md), the computer picks the pixel and the color for you.
