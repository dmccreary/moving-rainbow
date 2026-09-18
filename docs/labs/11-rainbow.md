# Lab 11: Rainbow

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Time for the real thing: a rainbow across the whole strip! We'll give every pixel its own spot on the color wheel. Let's light this up!

**Program file:** [`11-rainbow.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/11-rainbow.py)

## What you'll learn

- How to spread the color wheel evenly across all 30 pixels
- How `int(256 / NUMBER_PIXELS)` works out the size of each step
- How a variable that grows by a step each time moves you around the wheel
- How `print()` lets you look inside a running program
- That a program can end by itself and leave its lights on

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico, with the Shell visible at the bottom
- The `wheel()` function from [Lab 09: Color Wheel](09-color-wheel.md)

## The program

This program draws a still rainbow, one pixel at a time, from pixel 0 to pixel 29.

```python title="11-rainbow.py"
--8<-- "src/kits/moving-rainbow-base/11-rainbow.py"
```

Run it. The rainbow draws itself in less than a second, from red at pixel 0 to a deep pink-red at pixel 29. Then the program ends, and the rainbow stays on.

## How it works

### The same wheel

The middle of the file holds the `wheel()` function from [Lab 09](09-color-wheel.md). You give it a position from 0 to 255, and it gives back a color. This lab uses it to pick a different position for each pixel.

### Work out the step size

This line decides how far apart the pixels sit on the color wheel.

```python
color_wheel_step = int(256 / NUMBER_PIXELS)
```

The wheel has 256 positions, and the strip has 30 pixels. Dividing 256 by 30 gives about 8.53. The `int()` function chops off the decimals and keeps the whole number, so the step is 8. Each pixel sits 8 positions further around the wheel than the pixel before it.

Because `int()` chops off the leftover, 30 pixels × 8 = 240, which is a little short of the full circle. The last pixel gets `wheel(232)`, a deep pink-red, right before the wheel returns to red.

### Draw the rainbow

This loop gives each pixel a color, then moves to the next spot on the wheel.

```python
current_color = 0
print('Drawing rainbow in', NUMBER_PIXELS, 'steps with step size of: ', color_wheel_step)
for i in range(0,NUMBER_PIXELS):
    strip[i] = wheel(current_color)
    current_color = current_color + color_wheel_step
    print(i, current_color, wheel(current_color))
    strip.write()
    sleep(.03)
```

The variable `current_color` starts at 0, which is red. On each trip through the loop, pixel `i` gets `wheel(current_color)`. Then `current_color` grows by 8, ready for the next pixel. The `strip.write()` line shows the pixel, and `sleep(.03)` waits a moment.

The loop runs 30 times, and 30 × .03 = .9 seconds. That is why you see the rainbow draw itself pixel by pixel.

### Look inside with print

The `print()` function sends text to the **Shell**, the text area at the bottom of Thonny. This program prints one line before the loop and one line per pixel. In the Shell you will see lines like these:

```text
Drawing rainbow in 30 steps with step size of:  8
0 8 (231, 24, 0)
1 16 (207, 48, 0)
2 24 (183, 72, 0)
```

Each line shows the pixel number, a wheel position, and a color.

!!! bug "Known issue"
    The `print` line runs after `current_color` has grown by 8. So each Shell line shows the color for the next pixel, not the color pixel `i` received. For example, pixel 0 gets red, `(255, 0, 0)`, but its Shell line prints the color for position 8.

### The program ends by itself

There is no `while True` in this program. After pixel 29, the program ends. The pixels keep their colors as long as the strip has power, so the rainbow stays on.

To run it again, press **Run**. The strip already glows with the same colors, so the second run looks the same. Unplug the USB cable and plug it in again first if you want to watch the rainbow draw itself from a dark strip.

!!! warning "Power check"
    This program lights all 30 pixels. Every wheel color adds up to 255, so each pixel draws about 20 mA. That makes about 600 mA for the strip, and a USB port supplies about 500 mA. See [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go) for the details. To cut the total to about 150 mA, divide each color number by 4.

Replace the line `strip[i] = wheel(current_color)` with these two lines to dim the rainbow.

```python title="Your change"
red, green, blue = wheel(current_color)
strip[i] = (red // 4, green // 4, blue // 4)
```

The first line splits the three numbers from `wheel()` into `red`, `green`, and `blue`. The `//` sign divides and drops any leftover decimal.

## Try it yourself

1. Change `sleep(.03)` to `sleep(.1)`. Run it again from a dark strip and watch the rainbow draw itself slowly.
2. Change the line `color_wheel_step = int(256 / NUMBER_PIXELS)` to `color_wheel_step = 16`. Predict which pixels will light before you run it. Then check. Hint: look at the first `if` in `wheel()`.

## Check your understanding

1. Why is `color_wheel_step` 8 and not 8.53?
2. What color does pixel 0 get? Which line decides that?
3. Why does this program stop by itself, while Lab 09 kept going?
4. Look at the first Shell line for pixel 0. Why do its numbers not match pixel 0's color?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    A real rainbow, and you spread 256 colors across 30 pixels to get it! Next, we'll set that rainbow spinning.

**What's next:** In [Lab 12: Rainbow Cycle](12-rainbow-cycle.md), the rainbow rotates around the strip.
