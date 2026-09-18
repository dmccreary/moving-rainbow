# Lab 09: Color Wheel

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Every color on the wheel has an address, a number from 0 to 255. Today we'll walk all the way around it, and you'll see every stop. Let's light this up!

**Program file:** [`09-color-wheel.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/09-color-wheel.py)

## What you'll learn

- How a **function** takes an input and hands back an answer with `return`
- How `wheel()` turns a number from 0 to 255 into a color
- Why every color from the wheel adds up to 255
- How a `for` loop over `range(0, 256)` walks once around the wheel

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- Optional: the [Color Wheel MicroSim](../sims/color-wheel/index.md), which shows the wheel on your screen

## The program

This program lights the first pixel and slowly changes its color, one wheel position at a time, all the way around the wheel.

```python title="09-color-wheel.py"
--8<-- "src/kits/moving-rainbow-base/09-color-wheel.py"
```

Run it. Pixel 0 glows red, then slides through orange, yellow, green, blue, and purple. It comes back to red and starts again.

## How it works

### A function that turns a number into a color

This function is the heart of the lab. You give it a position number, and it gives back a color.

```python
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
```

`pos` is the function's **parameter** (the input it receives). It is short for *position*. The `return` word sends a color, three numbers in parentheses, back to the code that called the function. Calling `wheel(85)` gives you `(0, 255, 0)`.

The first `if` is a safety net. A number below 0 or above 255 is off the wheel, so the function returns `(0, 0, 0)`, which is dark.

### Three slices of the wheel

The wheel has three slices, and each slice is about 85 steps long. In each slice, one color fades out while the next fades in. The third color stays at 0.

| Slice | Positions | Red | Green | Blue |
|-------|-----------|-----|-------|------|
| 1 | 0 to 84 | 255 down to 3 | 0 up to 252 | stays 0 |
| 2 | 85 to 169 | stays 0 | 255 down to 3 | 0 up to 252 |
| 3 | 170 to 255 | 0 up to 255 | stays 0 | 255 down to 0 |

Here is how the code makes that happen:

- `pos * 3` climbs from 0 in steps of 3. After 85 steps it reaches 255.
- `255 - pos * 3` falls from 255 the same way.
- `return` ends the function right away. So Python reaches the second `if` only when `pos` is 85 or more.
- `pos -= 85` means `pos = pos - 85`. It slides the number back to 0, so the same math works in slice 2. The line `pos -= 170` does the same for slice 3.

Here are a few stops along the wheel:

| Position | Color returned | What you see |
|----------|----------------|--------------|
| 0 | `(255, 0, 0)` | Red |
| 32 | `(159, 96, 0)` | Orange |
| 64 | `(63, 192, 0)` | Yellow-green |
| 85 | `(0, 255, 0)` | Green |
| 127 | `(0, 129, 126)` | Teal |
| 170 | `(0, 0, 255)` | Blue |
| 213 | `(129, 0, 126)` | Purple |
| 255 | `(255, 0, 0)` | Red again |

!!! info "Key idea"
    Add up the three numbers in any color from the table above. You always get 255. Two colors trade off while the third stays at 0. So every wheel color is pure, and each one draws about the same power. You will use `wheel()` again in Labs 10, 11, 12, and 13.

### Walk around the wheel

This loop gives pixel 0 every color on the wheel, one after another.

```python
while True:
    for color_index in range(0,256):
        # print(color_index, wheel(color_index))
        strip[0] = wheel(color_index)
        strip.write()
        sleep(.03)
```

`range(0,256)` counts from 0 up to 255. That is 256 positions in all. For each one, the program asks `wheel()` for a color, puts it on pixel 0, writes it, and waits .03 seconds.

One trip around the wheel takes 256 × .03 = 7.68 seconds. Position 255 is red, and so is position 0, so the color flows around without a jump. Then `while True` starts the next trip.

Only pixel 0 changes, so this program draws very little power. To learn how red, green, and blue mix, read [Chapter 7: RGB Color Theory](../chapters/07-rgb-color-theory/index.md).

## Try it yourself

1. Remove the `#` from the start of the line `# print(color_index, wheel(color_index))`. A `#` turns a line into a **comment** (a note that Python skips). Run the program and watch the numbers scroll in the Shell as the color changes.
2. Change `sleep(.03)` to `sleep(.01)`. How long is one trip around the wheel now?

## Check your understanding

1. What does the number you give to `wheel()` mean?
2. Which color does `wheel(85)` return? Which channels are 0?
3. Why do the three numbers from `wheel()` always add up to 255?
4. Why does the color flow smoothly when the loop goes from position 255 back to position 0?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You walked all the way around the color wheel! `wheel()` is your new helper, and it will light up the next few labs.

**What's next:** In [Lab 10: Random Colors](10-random-colors.md), random pixels glow with colors from the wheel.
