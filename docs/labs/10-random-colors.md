# Lab 10: Random Colors

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Random places plus color wheel colors make confetti made of light! We'll toss a new dot onto the strip ten times every second. Let's see how it fills up!

**Program file:** [`10-random-colors.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/10-random-colors.py)

## What you'll learn

- How to pick a random place and a random color with `randint()`
- How to feed a random number into `wheel()` to get rich colors
- How a program can leave every dot lit, so the strip slowly fills up
- How a small function, such as `clear()`, does one job

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- The ideas from [Lab 08: Random](08-random.md) and [Lab 09: Color Wheel](09-color-wheel.md)

## The program

This program clears the strip, and then every tenth of a second it lights a random pixel with a random color from the wheel.

```python title="10-random-colors.py"
--8<-- "src/kits/moving-rainbow-base/10-random-colors.py"
```

Run it. Dots of color pop up all over the strip, and none of them turn off. After a few seconds, most of the strip glows.

## How it works

### The wheel is back

The file has a `wheel()` function. It is the same one you met in [Lab 09](09-color-wheel.md). It turns a number from 0 to 255 into a color.

The file also has other names, such as `levels` and `color_count`. The main loop does not use them, so you can skip over them.

### Draw one random color

This function picks a random pixel and a random spot on the wheel, and then lights the pixel.

```python
def draw_random_color():
    random_offset = randint(0, NUMBER_PIXELS-1)
    random_color = randint(0, 255)
    strip[random_offset] = wheel(random_color)
    strip.write()
```

`random_offset` is a pixel number from 0 to 29. `random_color` is a wheel position from 0 to 255. Then `wheel(random_color)` turns that position into red, green, and blue numbers.

Lab 08 picked three random numbers for a color. That can give pale colors. Here one number picks a spot on the wheel, and in every wheel color one of the three numbers is 0. So the colors look pure and bright.

### Start with a dark strip

This function turns every pixel off and writes the change.

```python
def clear():
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (0,0,0)
    strip.write()
```

A **function** is a named block of code. You define it once with `def`, and then you can call it by name. The next lines run `clear()` once at the start and then repeat the drawing forever.

```python
clear()
...
while True:
    draw_random_color()
    sleep(.1)
```

The `clear()` line runs one time. The loop then draws a dot, waits a tenth of a second, and draws another. That makes about ten dots every second.

### Nothing is erased

Look back at [Lab 08](08-random.md). It turned each pixel off after half a second. This program has no line that turns a pixel off.

So every dot stays lit. Sometimes the program picks a pixel that already glows. That pixel changes to a new color. Picking pixels by chance means it takes about 12 seconds, on average, to touch every pixel at least once. Then the strip keeps shimmering as pixels change color.

!!! warning "Power check"
    Once the whole strip is lit, all 30 pixels glow. Every wheel color adds up to 255, so each pixel draws about 20 mA. That makes about 600 mA for the strip, and a USB port supplies about 500 mA. See [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go) for the details. To cut the total to about 150 mA, divide each color number by 4.

Replace the line `strip[random_offset] = wheel(random_color)` with these two lines to dim every dot.

```python title="Your change"
red, green, blue = wheel(random_color)
strip[random_offset] = (red // 4, green // 4, blue // 4)
```

The first line splits the three numbers from `wheel()` into `red`, `green`, and `blue`. The `//` sign divides and drops any leftover decimal.

## Try it yourself

1. Change `sleep(.1)` to `sleep(.02)`. How many dots appear each second now? How fast does the strip fill?
2. Make each dot turn off after a pause. In [Lab 08](08-random.md), the pixel goes dark after half a second. Bring that idea here. Hint: the pixel number lives inside `draw_random_color()`, so try moving those lines into the `while True` loop.

## Check your understanding

1. Why does this strip fill up when the strip in Lab 08 did not?
2. What does `clear()` do, and how many times does it run?
3. Why do wheel colors look brighter than colors from three random numbers?
4. What does `randint(0, NUMBER_PIXELS-1)` pick, and why is there a `-1`?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You built a light confetti machine! Random places plus wheel colors make a fun mix, and you did it with two small functions.

**What's next:** In [Lab 11: Rainbow](11-rainbow.md), the pixels stop being random and line up in a real rainbow.
