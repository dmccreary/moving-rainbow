# Lab 02: Blink

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    This is the "Hello, World!" of light. We're going to make one pixel blink,
    and it's the same trick every big light show starts with. Let's light this up!

**Program file:** [`02-blink.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/02-blink.py)

## What you'll learn

- How to point at one pixel with `strip[0]`
- How a color is made from three numbers: red, green, and blue
- Why `strip.write()` is the line that actually changes the lights
- How `while True` repeats your code forever

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

## The program

This program turns the first pixel on, waits one second, turns it off, waits one second, and does it all again.

```python title="02-blink.py"
--8<-- "src/kits/moving-rainbow-base/02-blink.py"
```

Run it. The first pixel on your strip blinks red: one second on, one second off.

## How it works

### Set up the strip

```python
strip = NeoPixel(Pin(NEOPIXEL_PIN), NUMBER_PIXELS)
```

This line builds a `strip` object. It tells the Pico which pin sends data to the strip (`NEOPIXEL_PIN`) and how many pixels are on it (`NUMBER_PIXELS`). Both numbers come from `config.py`, so you never have to type a pin number yourself.

### Pick a pixel and give it a color

```python
strip[0] = (100,0,0)
```

The number in the square brackets is the pixel's **index** (its position on the strip). Computers start counting at 0, so `strip[0]` is the *first* pixel.

The three numbers in parentheses are the amounts of **red**, **green**, and **blue** light, in that order. Each one can be anything from 0 (none) to 255 (as bright as it gets). So `(100,0,0)` is red with no green or blue mixed in.

We picked 100 on purpose. It is gentle on your eyes and on your USB port. You can read more about brightness in [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go)

### Write, then wait

```python
strip.write()
sleep(1)
```

Setting `strip[0]` only changes a note in the Pico's memory. The strip has not heard about it yet. `strip.write()` sends the note down the wire, and the pixel lights up. Then `sleep(1)` pauses the program for one second so your eyes can see it.

### Repeat forever

`while True:` starts a **loop** (code that repeats). Because `True` is always true, the loop never stops. When the program reaches the bottom of the loop, it jumps back to the top and blinks again. Press the **Stop** button in Thonny to end it.

!!! warning "Heads up"
    If the pixel does not blink, check the wiring first. The most common cause is a strip connected backwards. See [When Something Doesn't Work](../kits/moving-rainbow-base/index.md#when-something-doesnt-work) for the full checklist.

## Try it yourself

1. Change `(100,0,0)` to `(0,100,0)`. What color do you get? Try `(0,0,100)` too.
2. Change both `sleep(1)` lines to `sleep(0.1)`. What is the smallest time you can use and still see the blink? Try `0.05` and `0.01`.

## Check your understanding

1. What does the `0` in `strip[0]` mean?
2. In `(100,0,0)`, which number controls the red light?
3. What happens if you remove one of the `strip.write()` lines? Why?
4. Why does the program keep blinking instead of stopping?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You told a real light what to do! Setting a color, writing it, and waiting: that's the recipe for almost every pattern in this book.

**What's next:** In [Lab 03: Red, Green and Blue](03-red-green-blue.md), one pixel steps through all three primary colors.
