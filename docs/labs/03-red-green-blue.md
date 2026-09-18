# Lab 03: Red, Green and Blue

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Every color on a screen is a mix of three lights: red, green, and blue.
    I have all three inside me, right in the middle of my body. Let's light them up!

**Program file:** [`03-red-green-blue.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/03-red-green-blue.py)

## What you'll learn

- How red, green, and blue light are the three ingredients of every pixel color
- How the order of the three numbers in `(100,0,0)` picks the color
- How to change a pixel's color by setting `strip[0]` again
- How light colors add together to make new colors

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

## The program

This program shows the first pixel red for one second, then green for one second, then blue for one second, and repeats.

```python title="03-red-green-blue.py"
--8<-- "src/kits/moving-rainbow-base/03-red-green-blue.py"
```

Run it. The first pixel cycles through red, green, and blue. One full cycle takes three seconds.

## How it works

### The setup is the same as Lab 02

The lines before `while True:` build the `strip` object from the pin number and pixel count in `config.py`. You met them in [Lab 02: Blink](02-blink.md). The new ideas are all inside the loop.

### Three numbers make a color

```python
strip[0] = (100,0,0)
strip.write()
sleep(1)
```

Each pixel has three tiny lights inside it: one red, one green, and one blue. The three numbers in parentheses set how bright each one is. A group of values in parentheses like this is called a **tuple**. The order is always red, green, blue.

| Numbers | Red | Green | Blue | What you see |
|---------|-----|-------|------|--------------|
| `(100,0,0)` | 100 | 0 | 0 | red |
| `(0,100,0)` | 0 | 100 | 0 | green |
| `(0,0,100)` | 0 | 0 | 100 | blue |

We use 100 instead of 255. That is bright, and still gentle on your eyes and your USB port.

### The same recipe, three times

Each block in the loop follows one recipe: set the color, write, wait. Here is the second block.

```python
strip[0] = (0,100,0)
strip.write()
sleep(1)
```

All three blocks change pixel `0`. A new color replaces the old one, so the pixel stays lit in between. After the third block, `while True:` jumps back to the top and starts red again.

!!! bug "Known issue"
    In the source file, the comment above the third block says "green". The code below it sets `(0,0,100)`, which is blue. The code is right, and the comment has a typo.

### Colors add together

Light mixes by **adding**. Turn on red and green together, and your eyes see yellow. Red and blue make magenta. Green and blue make cyan. All three at once make white.

This works differently from mixing paint. You can explore both in the [Additive vs. Subtractive Color Mixing](../sims/additive-subtractive-mixing/index.md) MicroSim. [Chapter 7](../chapters/07-rgb-color-theory/index.md) tells the full story of RGB color.

!!! warning "Heads up"
    If red and green look swapped on your strip, it uses a different color order. The [When Something Doesn't Work](../kits/moving-rainbow-base/index.md#when-something-doesnt-work) table shows the fix.

## Try it yourself

1. Change the third block from `(0,0,100)` to `(100,100,0)`. What color do you get? Try `(0,100,100)`, `(100,0,100)`, and `(100,100,100)` too.
2. Add a fourth color. Copy the last three lines (`strip[0] = ...`, `strip.write()`, and `sleep(1)`) and paste them below the third block. Keep them inside the `while True:` loop. Then change the numbers to make your favorite color.

## Check your understanding

1. In `(0,100,0)`, which light is on? How do you know?
2. What color do you expect from `(100,100,0)`?
3. How long does one full red, green, blue cycle take?
4. Why does the pixel not need to turn off between one color and the next?
5. Why does each block call `strip.write()`?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You mixed light! Red, green, and blue are the building blocks for every color in this book.

**What's next:** In [Lab 04: Dimmer](04-dimmer.md), one pixel fades smoothly from dark to bright and back again.
