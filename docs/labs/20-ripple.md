# Lab 20: Ripple

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Splash! We'll drop a light onto the strip and watch the ripples spread out both ways, like a
    pebble in a pond.

**Program file:** [`20-ripple.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/20-ripple.py)

## What you'll learn

- How a function with three parameters draws a ripple of any size, color, and speed
- How to pick a random starting spot that keeps the ripple on the strip
- How to light pixels on both sides of a center pixel
- Why each step erases the pixels it lit

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

## The program

This program drops a ripple at a random spot, first in red, then in green, then in blue, and repeats forever.

```python title="20-ripple.py"
--8<-- "src/kits/moving-rainbow-base/20-ripple.py"
```

Run it. Two lit pixels start at one spot and move apart, one pixel at a time. Each ripple takes about five seconds. Then a new ripple starts somewhere else.

## How it works

### One function draws a ripple

The `ripple` function has three **parameters** (named slots for values you hand to a function). The `size` says how many steps the ripple takes. The `color` says what color to use. The `delay` says how many seconds to wait at each step.

### Pick a starting spot

```python
def ripple(size, color, delay):
    # start at a random location within size of the ends
    start = randint(size, NUMBER_PIXELS - size)
```

The call `randint(a, b)` gives a random whole number from `a` to `b`, and both ends can appear. With `size` equal to 10, the call is `randint(10, 20)`. So `start` is a number from 10 to 20.

Why not pick any pixel? The ripple grows up to nine pixels in each direction. The largest start is 20, and 20 + 9 is 29, the last pixel. The smallest start is 10, and 10 - 9 is 1. Both sides stay on the strip.

### Spread out both ways

```python
for i in range(0, size):
    strip[start+i] = color
    strip[start-i] = color
    strip.write()
    sleep(delay)
    strip[start+i] = (0,0,0)
    strip[start-i] = (0,0,0)
```

The variable `i` is the distance from the start. The first two lines light one pixel on each side. At `i` equal to 0, both lines light the same pixel. Then `strip.write()` shows the pair, and `sleep(delay)` holds it.

The last two lines erase the pair in the Pico's memory. The next `strip.write()` sends the erase and the new pair together. So only one pair is lit at a time.

Here is a ripple that starts at pixel 15:

| Step `i` | Pixels lit |
|---|---|
| 0 | 15 |
| 1 | 14 and 16 |
| 2 | 13 and 17 |
| 9 | 6 and 24 |

The ripple takes 10 steps of 0.5 seconds, which is 5 seconds. You can see how a ripple grows in the [Ripple Animation Mechanics](../sims/ripple-animation-sim/index.md) MicroSim.

### The main loop

```python
delay = 0.5
while True:
    ripple(10, red, delay)
    ripple(10, green, delay)
    ripple(10, blue, delay)
```

The `10` in each call is the `size`. Each call picks a new random start. One trip through the loop takes about 15 seconds, because there are three ripples of five seconds each.

The program also defines other colors and a `colors` tuple near the top. The ripples use only `red`, `green`, and `blue`. The rest is waiting for you in the challenges.

## Try it yourself

1. Change `delay = 0.5` to `delay = 0.1`. Then change the `10` in each `ripple(...)` line to `15`, the biggest size that fits on 30 pixels. How long does one ripple take now?
2. Pick a random color for each ripple. Replace the whole `while True:` block with this one, which uses the `colors` tuple from the program.

```python title="Your change"
while True:
    ripple(10, colors[randint(0, color_count - 1)], delay)
```

## Check your understanding

1. What are the smallest and largest values `start` can have when `size` is 10?
2. Why does the code keep `start` away from the ends of the strip?
3. Which pixels light at step `i` equal to 2 if `start` is 15?
4. About how long does one ripple take?
5. Why does the loop erase the pair with `(0,0,0)` after each step?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You made light ripple across the strip! Randomness plus a little arithmetic keeps every ripple fresh.

**What's next:** In [Lab 21: Twinkle Colors](21-twinkle-colors.md), single pixels flash in random colors like stars.
