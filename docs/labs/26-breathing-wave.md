# Lab 26: Breathing Wave

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Ready to make your whole strip breathe? A soft wave of light will roll along the pixels like a wave rolling onto a beach. Let's light this up!

**Program file:** [`26-breathing-wave.py`](https://github.com/dmccreary/moving-rainbow/blob/master/src/kits/moving-rainbow-base/26-breathing-wave.py)

## What you'll learn

- What a **sine wave** is, and how `math.sin()` makes one
- How to turn a number from -1 to 1 into a number from 0 to 1
- How giving each pixel a different starting point makes a wave travel
- How `%` keeps the `phase` number from growing forever

## What you'll need

- Your base kit: a Pico, a breadboard, and the 30-pixel LED strip, wired as shown in the [Kit User's Guide](../kits/moving-rainbow-base/index.md)
- The `config.py` file saved on the Pico (see [Getting Code onto the Kit](../kits/moving-rainbow-base/index.md#getting-code-onto-the-kit))
- Thonny open and connected to your Pico
- The fade from [Lab 04: Dimmer](04-dimmer.md), because this lab makes a smoother kind of fade

## The program

This program makes every pixel glow brighter and dimmer. Each pixel runs a little behind its neighbor, so a wave of teal-blue light travels along the strip.

```python title="26-breathing-wave.py"
--8<-- "src/kits/moving-rainbow-base/26-breathing-wave.py"
```

Run it. A wave of teal-blue light rolls along the strip toward the end where your wires connect. This program keeps going until you press **Stop**.

## How it works

### Bring in the math toolbox

This is the first program in the book that needs a new toolbox. The line loads Python's math tools.

```python
import math
```

An **import** brings in code that other people already wrote. We need two tools from `math`: the function `math.sin()` and the number `math.pi`.

### What is a sine wave?

A **sine wave** is a smooth curve that goes up and down, up and down. The function `math.sin()` takes a number that says how far around a circle you are. It gives back a number from -1 to 1.

A trip all the way around a circle is 2 × pi, which is about 6.28. `math.pi` is Python's name for pi, which is about 3.14. As the number you give `math.sin()` grows from 0 to 6.28, the answer rises to 1, falls to -1, and returns to where it started. That is one full wave.

The fade in [Lab 04](04-dimmer.md) changes brightness by the same amount every step, then turns around sharply at the top and the bottom. A sine wave slows down as it nears the top and the bottom. The light eases in and out (it changes gently at the start and the end), like a slow breath. You can watch the curve in the [Math Functions in Animation](../sims/animation-math-explorer/index.md) MicroSim, and [Chapter 11](../chapters/11-math-for-led-programming/index.md) explains the math in more detail.

### From -1 to 1 into 0 to 1

A pixel cannot have a brightness below 0. So the program squeezes the answer from `math.sin()` into the range 0 to 1 with two steps: add 1, then divide by 2.

```python
wave = (math.sin(phase + i * WAVE_SPACING) + 1) / 2
```

Follow three sample answers through the two steps.

| `math.sin()` gives | After adding 1 | After dividing by 2 |
|--------------------|----------------|---------------------|
| -1 | 0 | 0 |
| 0 | 1 | 0.5 |
| 1 | 2 | 1 |

In MicroPython, the `/` sign gives a decimal number, so `wave` can be 0.5 or 0.37 or any value from 0 to 1.

### From 0 to 1 into a color

These two lines turn `wave` into a pixel color.

```python
level = int(wave * MAX_BRIGHTNESS)
strip[i] = (0, level // 2, level)
```

Multiplying by `MAX_BRIGHTNESS`, which is 60, stretches 0 to 1 into 0 to about 60. The `int()` function cuts off the decimals, so `level` is a whole number and the top is usually 59.

The color is `(0, level // 2, level)`. Red is 0, blue is `level`, and green is half of `level`. The `//` sign divides and drops any leftover decimal. A little green mixed into blue gives a teal-blue.

!!! info "Key idea"
    The brightness cap of 60 is on purpose. If all 30 pixels were at their very brightest at the same moment, the strip would draw about 210 mA. A USB port supplies about 500 mA. Read more in [How Bright Can You Go?](../kits/moving-rainbow-base/index.md#how-bright-can-you-go)

### Make the wave travel

The `phase + i * WAVE_SPACING` part is what makes the wave move along the strip. Every pixel uses the same `phase`, but each one adds a different amount.

```python
for i in range(NUMBER_PIXELS):
    wave = (math.sin(phase + i * WAVE_SPACING) + 1) / 2
```

Pixel 0 adds 0. Pixel 1 adds 0.3. Pixel 2 adds 0.6, and so on. So every pixel sits at a different spot on the sine wave, a little behind its neighbor. It is like the wave that a crowd makes at a stadium, where each person stands up right after the person next to them.

The 30 pixels together cover 30 × 0.3 = 9 units of the wave. A full wave is about 6.28 units long. That means about 1.4 waves fit on the strip at once.

Each frame, `phase` gets bigger. Over time, each pixel shows what the pixel with the next higher number showed a moment before. So the bright peak slides toward pixel 0.

### Move the wave forward

At the end of each frame, these two lines add a small step to `phase` and then wait.

```python
phase = (phase + WAVE_SPEED) % (2 * math.pi)
sleep(FRAME_DELAY)
```

`WAVE_SPEED` is 0.06, so `phase` grows by 0.06 each frame. The `%` sign is the **modulo** operator, which gives the remainder after dividing. As in [Lab 12](12-rainbow-cycle.md), it wraps a number back to 0. Here it wraps `phase` back to 0 after one full circle (2 × pi).

A sine wave repeats every 2 × pi, so wrapping does not change what you see. It keeps the `phase` number small instead of letting it grow for as long as the program runs. You can see wrapping in the [Modulo Wrap-Around](../sims/modulo-wrap-simulation/index.md) MicroSim.

### One picture at a time

Each trip through `while True:` makes one **frame** (one picture on the strip). The `for` loop sets all 30 colors first. Then `strip.write()` runs one time and sends them all together.

```python
while True:
    for i in range(NUMBER_PIXELS):
        ...
        strip[i] = (0, level // 2, level)
    strip.write()
```

The `strip.write()` line sits outside the `for` loop, because the strip only needs to hear the new colors once per frame.

### How long is one breath?

One full wave is about 6.28 long, and `phase` grows by 0.06 each frame. So one breath takes 6.28 ÷ 0.06, or about 105 frames. Each frame waits `FRAME_DELAY`, which is 0.03 seconds. So 105 × 0.03 is about 3 seconds per breath. Writing to the strip adds a tiny bit more time.

## Try it yourself

1. Change `WAVE_SPACING` and watch the wave. Try `0`, then `0.6`, then `0.1`. With `0`, every pixel adds the same amount, so what should happen? With `0.6`, how many waves fit on the strip? Work it out with 30 × 0.6 ÷ 6.28. With `0.1`, the wave is long and lazy.
2. Reverse the direction. In the `wave` line, change `phase + i * WAVE_SPACING` to `phase - i * WAVE_SPACING`. The wave now travels the other way.
3. Advanced: make the dark parts last longer. Add a second line right after the `wave` line that multiplies `wave` by itself.

Here is the `wave` line for challenge 2.

```python title="Your change"
wave = (math.sin(phase - i * WAVE_SPACING) + 1) / 2
```

Here are the two lines for challenge 3.

```python title="Your change"
wave = (math.sin(phase + i * WAVE_SPACING) + 1) / 2
wave = wave * wave
```

Squaring a number between 0 and 1 makes it smaller, so 0.5 becomes 0.25. The numbers 0 and 1 stay the same. The dim parts of the breath now last longer.

Challenge 3 is an idea to try. Your eyes notice changes in dim light more than changes in bright light, as you saw at the end of [Lab 04](04-dimmer.md). Read about it in [Perceived vs. Linear Brightness](../sims/perceived-vs-linear-brightness/index.md), then decide which version you like better.

## Check your understanding

1. What range of numbers does `math.sin()` give back?
2. Why does the program add 1 and then divide by 2?
3. What happens when `WAVE_SPACING` is `0`, and why?
4. About how many frames does one full breath take, and about how many seconds?
5. What does the `%` do to `phase` in the last lines of the loop?

!!! success "Lab complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel celebrates">
    You used real math to make light breathe! A sine wave is the secret behind lots of smooth, natural-looking glows.

**What's next:** In [Lab 27: Sunrise](27-sunrise.md), the whole strip blends slowly from night colors to sunrise colors.
