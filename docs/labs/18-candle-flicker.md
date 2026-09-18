# Lab 18: Candle Flicker

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Warm light, and no wax needed! We'll use random numbers to make the strip flicker like a
    candle flame. Let's light this up!

**Program file:** [`18-candle-flicker.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/18-candle-flicker.py)

## What you'll learn

- How `randint()` picks a random whole number
- How red and green light mix to make orange and yellow
- How to change a random pixel on the strip
- Why a program with no erase step can still look alive

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

## The program

This program gives random pixels random warm colors, over and over, so the strip flickers like a flame.

!!! warning "Power check"
    After a moment, nearly all 30 pixels hold a warm color. On average the strip then draws about 690 mA, and bright picks push it higher. A USB port supplies about 500 mA. Read [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go) for the details. To fix it, change the pixel line to `strip[randint(0,NUMBER_PIXELS - 1)] = (red // 4, green // 4, 0)`. The `//` symbol divides and drops the remainder. That lowers the average to about 175 mA.

```python title="18-candle-flicker.py"
--8<-- "src/kits/moving-rainbow-base/18-candle-flicker.py"
```

Run it. The strip fills with orange and yellow lights that keep changing.

## How it works

### Random numbers

```python
from urandom import randint
```

A **random number** is a number the computer picks by chance. The call `randint(a, b)` gives back a random whole number from `a` to `b`. Both ends can appear. So `randint(0,155)` can give 0, 155, or anything in between.

### Warm colors

```python
green = 50 + randint(0,155)
red = green + randint(25,50)
```

The first line makes `green` a random number from 50 to 205. The second line makes `red` bigger than `green` by 25 to 50. The biggest possible red is 205 + 50, which is exactly 255.

A mix of red and green light with more red than green looks orange. When both numbers are high, it looks yellow. When both are low, it looks like dim orange. The blue amount stays 0, so every color stays in the orange and yellow family. [Chapter 12](../chapters/12-basic-animation-patterns/index.md) shows another way to build a candle flicker.

### Pick a random pixel

```python
strip[randint(0,NUMBER_PIXELS - 1)] = (red, green, 0)
strip.write()
sleep(delay)
```

The first line picks a random pixel number and gives that pixel the new color. The pixels are numbered 0 to 29, and `randint` can return its top number. That's why the code uses `NUMBER_PIXELS - 1`, which is 29. Then `strip.write()` shows the change, and `sleep(delay)` pauses.

### Thirty changes in one call

```python
def candle(delay):
    for i in range(0, NUMBER_PIXELS):
```

A **function** is a named block of code you can reuse. The `candle` function has one **parameter** (a named slot for a value), called `delay`. It repeats the three lines above 30 times. The same pixel can be picked twice in one call, and some pixels get skipped. That's what random means.

```python
while True:
    candle(.001)
```

The main loop calls `candle` forever with a delay of `.001`, which is one thousandth of a second. Each change pauses for that long, so the strip can change up to about 1,000 times a second. Writing to the strip takes some time too, so it changes a little less often.

### Nothing gets erased

No line in this program turns a pixel off. New random colors replace old ones. Within a moment or two every pixel holds a warm color, and every pixel keeps changing. That's why the whole strip looks like a field of flickering oranges.

### A leftover variable

```python
counter = 0
while True:
    candle(.001)
    # wrap
    counter = counter % (NUMBER_PIXELS-1)
    counter += 1
```

The `counter` lines do nothing useful. No other line reads `counter`. The program behaves the same with or without them.

## Try it yourself

1. Change `candle(.001)` to `candle(.05)`. Does the flicker look more like a candle or less? Try `.02` too.
2. Make the flame redder and dimmer. Change `green = 50 + randint(0,155)` to `green = 20 + randint(0,60)`. What colors can you get now? Dimmer numbers also draw less current.

## Check your understanding

1. Which numbers can `randint(25,50)` give?
2. Why is `red` always bigger than `green`? What color family does that give?
3. Why does the code write `NUMBER_PIXELS - 1` in `randint(0,NUMBER_PIXELS - 1)`?
4. Do lit pixels ever turn off in this program? What happens to them instead?
5. What does the `counter` variable do?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You made a flame out of random numbers! A little bit of chance turns plain colors into something that feels alive.

**What's next:** In [Lab 19: Theater Chase](19-theater-chase.md), every fourth pixel lights up and the pattern marches along the strip like a marquee sign.
