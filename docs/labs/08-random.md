# Lab 08: Random

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    This time the computer chooses, and even we can't guess what comes next. We'll light one surprise pixel at a time. Ready to roll the light dice?

**Program file:** [`08-random.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/08-random.py)

## What you'll learn

- How `randint()` picks a random whole number
- Why the top of the range is `NUMBER_PIXELS-1`
- How three random numbers make a random color
- How to turn a pixel off in memory and let the next `strip.write()` show it

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

## The program

This program lights one random pixel in a random color, waits half a second, and then picks again.

```python title="08-random.py"
--8<-- "src/kits/moving-rainbow-base/08-random.py"
```

Run it. One pixel at a time flashes in a surprising color at a surprising spot. You can't predict where the next one will land.

## How it works

### Get the random tool

This line loads `randint` so the program can use it.

```python
from urandom import randint
```

A **random number** is a number picked by chance, so nobody can predict it. The `randint(a, b)` function gives you a random **integer** (a whole number) from `a` to `b`. It can return `a`, it can return `b`, and it can return anything between. So `randint(1, 6)` works like rolling a die.

### Pick a place

This line picks which pixel will light up.

```python
location = randint(0, NUMBER_PIXELS-1)
```

The pixels are numbered 0 to 29, so the last one is `NUMBER_PIXELS-1`. We subtract 1 because `randint` includes the top number. With `randint(0, NUMBER_PIXELS)`, the program could pick 30, and there is no pixel 30.

### Pick a color

These lines pick a random amount of red, green, and blue, and then color the pixel.

```python
red = randint(0, 255)
green = randint(0, 255)
blue = randint(0, 255)
strip[location] = (red, green, blue)
```

Each number can be anything from 0 to 255, the full range you met in [Lab 02](02-blink.md). Three random numbers can make about 16 million different colors.

You may notice that many of the colors look pale. When the three numbers are close in size, the light looks whitish. [Lab 10](10-random-colors.md) uses the color wheel to fix that.

### Show it, then erase it

These lines show the pixel, hold it for half a second, and then turn it off.

```python
strip.write()
sleep(.5)
strip[location] = (0, 0, 0)
```

The pixel glows for half a second. Then `(0, 0, 0)` sets red, green, and blue all to zero. That only changes the note in the Pico's memory. No `strip.write()` comes right after it.

The next trip around the loop calls `strip.write()`. That one write shows the old pixel going dark and the new pixel lighting up at the same moment. So only one pixel glows at a time.

Sometimes the loop picks the same pixel twice in a row. Then the pixel does not go dark. It changes to its new color instead.

## Try it yourself

1. Change `sleep(.5)` to `sleep(.1)`. How does the light show feel now?
2. Change `randint(0, NUMBER_PIXELS-1)` to `randint(0, 9)`. Which pixels flash now?

## Check your understanding

1. Why does the program use `NUMBER_PIXELS-1` and not `NUMBER_PIXELS`?
2. Which numbers can `randint(0, 255)` return?
3. How many pixels glow at the same time? Why?
4. The line `strip[location] = (0, 0, 0)` has no `strip.write()` after it. What makes the pixel go dark?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You taught the computer to surprise you! Games, art, and music all use random numbers, and now you can too.

**What's next:** In [Lab 09: Color Wheel](09-color-wheel.md), one pixel walks through every color in order.
