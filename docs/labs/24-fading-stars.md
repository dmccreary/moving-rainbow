# Lab 24: Fading Stars

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Time to paint the night sky! Stars will flare up at random places and then fade
    away softly. Let's light this up!

**Program file:** [`24-fading-stars.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/24-fading-stars.py)

## What you'll learn

- How a list can remember one brightness number for every pixel
- How to give an event a percent chance with `randint`
- How to fade a number toward zero with `level * 3 // 4`
- What `//` (whole-number division) does
- How to change every pixel and then call `strip.write()` once per frame

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- The random pixel idea from [Lab 21: Twinkle Colors](21-twinkle-colors.md)

## The program

This program makes white stars flare up at random places on the strip, and each star then fades away smoothly.

```python title="24-fading-stars.py"
--8<-- "src/kits/moving-rainbow-base/24-fading-stars.py"
```

Run it. Stars pop up at random spots along the strip. Each one fades out in a little under a second, and a few glow at the same time. Press **Stop** in Thonny to end it.

## How it works

### A list with one number for every pixel

```python
brightness = [0] * NUMBER_PIXELS
```

A **list** is an ordered group of values inside square brackets. The `*` repeats a list, so `[0] * NUMBER_PIXELS` is a list of 30 zeros. The item `brightness[5]` holds the brightness of pixel 5, and 0 means dark.

This kind of list is a **brightness array** (one brightness number for every pixel). It is the program's own memory of how bright each pixel should be. [Chapter 13](../chapters/13-intermediate-animations/index.md) uses the same idea to fade a trail behind a moving pixel.

Lab 21's twinkle switched a pixel on and then straight off. [Lab 16](16-comet.md) faded a tail with a fixed list of levels. Here every pixel keeps its own number, and that number shrinks a little each frame.

### Start a star at random

```python
if randint(1, 100) <= STAR_CHANCE:
    brightness[randint(0, NUMBER_PIXELS - 1)] = STAR_BRIGHTNESS
```

An `if` runs the indented line only when its test is true. The call `randint(1, 100)` picks a whole number from 1 to 100, and both ends count. `STAR_CHANCE` is 20, so the test is true for 1 to 20. That is 20 chances out of 100, or a 20 percent chance: about one frame in five.

When the test is true, `randint(0, NUMBER_PIXELS - 1)` picks a random pixel from 0 to 29, as in Lab 21. The program sets that pixel's number to `STAR_BRIGHTNESS`, which is 120. Only the list changes here. Nothing is drawn yet.

### Show every pixel, then fade it

```python
for i in range(NUMBER_PIXELS):
    level = brightness[i]
    strip[i] = (level, level, level)
    brightness[i] = level * 3 // 4   # keep three quarters of the brightness
strip.write()
sleep(FRAME_DELAY)
```

This `for` loop visits all 30 pixels. The variable `level` reads one pixel's number from the list. Equal amounts of red, green, and blue make white, so `(level, level, level)` is a white glow. A big `level` is bright, a small one is faint, and 0 is off.

The last line inside the loop stores a smaller number for the next frame. The `//` symbol is **floor division**: it divides and drops any leftover fraction, so the answer is a whole number. Color numbers must be whole numbers. Python does `level * 3` first and then `// 4`, so `120 * 3 // 4` is `360 // 4`, which is 90.

The `strip.write()` line sits *outside* the loop, with less indent. It runs once, after all 30 pixels are set. One trip through `while True:` draws one **frame** (a single picture of the whole strip). With `FRAME_DELAY` at 0.05 seconds, that is about 20 frames a second.

A new star appears in the same frame that creates it, at full brightness 120. It starts to fade in the next frame.

### How long does a star last?

Follow one star. Each frame the program shows the level and then keeps three quarters of it, with decimals dropped. Here are the levels the strip shows:

`120, 90, 67, 50, 37, 27, 20, 15, 11, 8, 6, 4, 3, 2, 1`

For example, `90 * 3` is 270, and `270 // 4` is 67, because 67.5 loses its .5. When the level is 1, `1 * 3 // 4` is `3 // 4`, which is 0, and the star is gone.

That is 15 frames. At 0.05 seconds a frame, a star lasts about 15 × 0.05 = 0.75 seconds. The change is big while the star is bright (120 to 90) and tiny when it is faint (3 to 2). Our eyes notice small changes in dim light, as Lab 04 showed, so this fade looks smooth.

How many stars glow at once? A new star starts in about one frame out of five, and each star lasts 15 frames. So about 0.2 × 15 = 3 stars glow at any moment. Only a few pixels are lit, and none is brighter than 120, so the strip stays far below the 500 mA a USB port supplies.

## Try it yourself

1. Change how fast stars fade. Replace `level * 3 // 4` with `level // 2` for quick sparks. Then try `level * 7 // 8` for slow, dreamy fades. Describe the difference. To check your tracing, a star should last 7 frames with `level // 2` and 25 frames with `level * 7 // 8`.
2. Make warm stars. Change `(level, level, level)` to `(level, level * 3 // 4, level // 2)`. Red stays the strongest, green is three quarters of it, and blue is half. What color are the stars now?
3. Solve a puzzle. A friend suggests fading by taking away a quarter: `level - level // 4`. Before you run it, work out by hand what happens when `level` is 3. Then replace the fade line, run it, and watch the strip for a minute. Do the stars ever go fully dark?

```python title="Your change"
brightness[i] = level - level // 4
```

!!! info "Key idea"
    Floor division rounds down, so a small level can lose nothing. When `level` is 3, `3 // 4` is 0, and `3 - 0` is still 3. The star gets stuck at 3 and stays faintly lit forever. With `level * 3 // 4`, the 3 becomes `9 // 4`, which is 2, so every level of 1 or more gets smaller. Multiply first, then divide.

## Check your understanding

1. What does `[0] * NUMBER_PIXELS` make?
2. What is the chance of a new star in each frame? How does `randint(1, 100) <= STAR_CHANCE` give that chance?
3. What does `//` do? What is `50 * 3 // 4`?
4. Why is there one `strip.write()` after the `for` loop instead of one inside it?
5. About how long does a star last, and how did you work it out?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You built a night sky from one list and a little arithmetic! Keeping a number for every pixel lets you make many kinds of fading light.

**What's next:** In [Lab 25: Bouncing Ball](25-bouncing-ball.md), a ball drops, speeds up, and bounces a little lower each time.
