# Lab 04: Dimmer

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Ready to make a light glow softly, like a sleepy sunrise? We'll use a loop to
    count up and down, and the pixel will follow along. Let's light this up!

**Program file:** [`04-dimmer.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/04-dimmer.py)

## What you'll learn

- How a `for` loop counts with `range(start, stop)`
- Why `range` stops one number before the `stop` value
- How to count backward with a step of `-1`
- How one number in a color sets a pixel's brightness
- Why equal steps of brightness look uneven to our eyes

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico

## The program

This program fades the first pixel from dark up to bright red, then back down to dark, again and again.

```python title="04-dimmer.py"
--8<-- "src/kits/moving-rainbow-base/04-dimmer.py"
```

Run it. The first pixel slowly glows brighter for a little over one second, then dims for a little over one second. Each `strip.write()` takes a moment too, which is why each fade lasts a bit longer than one second.

## How it works

### Count with a for loop

```python
for i in range(0,100):
    strip[0] = (i,0,0)
    strip.write()
    sleep(.01)
```

A **for loop** repeats its indented lines once for each number in a list. The variable `i` holds the current number. Each time around the loop, `i` is one bigger than before.

The red number in `(i,0,0)` is `i`. When `i` is small, the pixel is dim. When `i` is big, the pixel is bright. Green and blue stay at 0. Each trip writes the color and then sleeps for `.01` seconds, which is one hundredth of a second.

### What range() makes

`range(start, stop, step)` builds the list of numbers to count through.

- `start` is the first number.
- `stop` is where counting ends. **The stop number is not included.**
- `step` is how much to add each time. If you leave it out, it is 1.

So `range(0,100)` gives 0, 1, 2, and so on up to 99. That is 100 numbers. The loop runs 100 times, and 100 steps of `.01` seconds add up to one second.

!!! info "Key idea"
    `range` stops right before the `stop` number. To count all the way to 100, you would write `range(0,101)`.

### Count backward

```python
for i in range(100,0,-1):
    strip[0] = (i,0,0)
    strip.write()
    sleep(.01)
```

This loop uses all three parts of `range`. It starts at 100, stops before 0, and uses a step of `-1`. A negative step counts down: 100, 99, 98, and so on down to 1. The pixel gets dimmer with each step.

Look at the top of the fade. The first loop ends at 99, and the second loop starts at 100. So the brightest moment is `(100,0,0)`. At the bottom, the first loop starts at 0, so the pixel goes fully dark for one step.

### Two loops inside one loop

Both `for` loops sit inside `while True:`. A loop inside another loop is called a **nested loop**. The outer loop repeats "fade up, then fade down" forever. Press **Stop** in Thonny to end it.

## Going further

### A heartbeat pattern

A real heart thumps instead of glowing slowly. It makes two quick pulses, then rests. You can copy that with the tools you already have.

The third number in `range` is the **step**. A bigger step skips numbers, so the fade finishes sooner:

```python title="Your change"
for i in range(0,100,10):
    strip[0] = (i,0,0)
    strip.write()
    sleep(.01)
```

This counts 0, 10, 20, and so on up to 90. That is only 10 steps instead of 100. A fast fade up and a fast fade down make one pulse. Do it twice, then add a longer `sleep` in the dark, and you have a heartbeat. [Lab 23: Heartbeat](23-heartbeat.md) is a finished version to compare with yours.

### Our eyes see brightness unevenly

Going from 0 to 1 to 2 adds the same amount of light each step. But your eyes see it differently. They notice small changes in dim light much more than the same changes in bright light. So a fade made of equal number steps can look uneven, with the dim part changing faster than the bright part.

Fixing this is called **gamma correction** (changing the numbers so the brightness looks smooth to our eyes). Explore the idea in the [Perceived vs. Linear Brightness](../sims/perceived-vs-linear-brightness/index.md) MicroSim. Then read [Gamma Correction](../led-noodles/gamma-correction.md) to see how the fix works. In [Lab 26: Breathing Wave](26-breathing-wave.md), a sine wave gives a fade that eases in and out.

## Try it yourself

1. Change the color. In both loops, change `(i,0,0)` to `(0,i,0)` to fade green, or `(0,0,i)` to fade blue. Both loops need the same change.
2. Build a heartbeat. Use a step of 10 in both `range` calls. Wrap the up loop and the down loop in one more `for` loop that runs twice, using `range(2)`. Then turn the pixel off and add `sleep(1)` at the end of the `while True:` loop. How long is the rest between beats?
3. Watch a normal fade closely. Does the pixel seem to change faster while it is dim, or while it is bright? Compare what you see with the MicroSim linked above.

## Check your understanding

1. What numbers does `range(0,100)` make? What is the last one?
2. In `range(100,0,-1)`, what are the first and last numbers? What does the `-1` do?
3. Why does the pixel get brighter as `i` gets bigger?
4. About how long does the fade up take, and how did you work that out?
5. Why can equal number steps look like unequal brightness steps?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You made light breathe! Counting up and down with `range` is a skill you'll use in almost every pattern to come.

**What's next:** In [Lab 05: Move a Pixel](05-move.md), one lit pixel travels down the whole strip.
