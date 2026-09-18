# Lab 21: Twinkle Colors

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Twinkle, twinkle, little pixel! We'll make a star pop up anywhere on the strip, in any
    color, and then vanish.

**Program file:** [`21-twinkle-colors.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/21-twinkle-colors.py)

## What you'll learn

- How to pick a random pixel and a random color
- How to write a function with two parameters, `delay` and `color`
- How to pull one random item out of a tuple
- How the length of each `sleep` shapes the feel of a pattern

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

## The program

This program lights one random pixel in a random color for a tenth of a second. Then it turns the pixel off and waits a second before the next twinkle.

```python title="21-twinkle-colors.py"
--8<-- "src/kits/moving-rainbow-base/21-twinkle-colors.py"
```

Run it. A single pixel flashes somewhere on the strip and vanishes. About one second later, another pixel flashes in a new color.

## How it works

### The twinkle function

```python
def twinkle(delay, color):
    random_index = randint(0, NUMBER_PIXELS-1);
    # turn on
    strip[random_index] = color
    strip.write();
    sleep(delay);
    # turn off
    strip[random_index] = (0,0,0)
    strip.write();
```

A **function** is a named block of code you can run again and again. This one has two **parameters** (named slots for values you hand to the function): `delay` and `color`.

The steps go in this order:

1. Pick a random pixel number from 0 to 29. The top number is `NUMBER_PIXELS-1` because the pixels start at 0.
2. Give that pixel the `color`, and write it to the strip.
3. Wait for `delay` seconds.
4. Set the pixel to `(0,0,0)`, which is off, and write again.

There are two `strip.write()` calls. The first shows the twinkle. The second hides it.

Some lines end with a semicolon (`;`). Python allows this but does not need it. Your code works the same without the semicolons.

### A random color from the tuple

```python
colors = (red, orange, yellow, green, blue, cyan, indigo, violet)
color_count = len(colors)
```

The `colors` tuple holds eight colors. A **tuple** is an ordered group of values inside parentheses. The `len()` function counts them, so `color_count` is 8.

```python
while True:
    twinkle(.1, colors[randint(0, color_count-1)])
    sleep(1)
```

Read the color part from the inside out. The call `randint(0, color_count-1)` gives a random position from 0 to 7. Then `colors[...]` looks up the color at that position. That color goes into `twinkle` as `color`.

### Timing

Each twinkle stays on for `.1` seconds, which is a tenth of a second. Then the program waits `sleep(1)` for one more second. So you see about one twinkle every 1.1 seconds. Only one pixel is lit at any moment.

The program defines a few more names, such as `levels` and `red_med`, that it does not use. They are safe to ignore. [Chapter 12](../chapters/12-basic-animation-patterns/index.md) builds a busier twinkle with several pixels at once.

## Try it yourself

1. Change `sleep(1)` to `sleep(.2)`. How often does a twinkle happen now? Then try changing `.1` in `twinkle(.1, ...)` to `.5`.
2. Make the gap between twinkles random. Replace the `while True:` block with this one. The `/` symbol divides and gives a decimal answer, so the gap is 0.1 to 2.0 seconds.

```python title="Your change"
while True:
    twinkle(.1, colors[randint(0, color_count-1)])
    sleep(randint(1, 20) / 10)
```

Want the stars to fade out smoothly instead of switching off? [Lab 24: Fading Stars](24-fading-stars.md) shows how.

## Check your understanding

1. Why is the top number `NUMBER_PIXELS-1` and not `NUMBER_PIXELS`?
2. What does `colors[randint(0, color_count-1)]` give you?
3. About how much time passes from one twinkle to the next?
4. Why does `twinkle` call `strip.write()` two times?
5. How many pixels are lit at the same time?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You made a night sky out of random numbers! Picking both the place and the color by chance is a trick you'll use again.

**What's next:** In [Lab 22: Random Walk](22-random-walk.md), a dim pixel wanders left and right, one random step at a time.
