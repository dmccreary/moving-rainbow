---
title: Mathematics for LED Programming
description: Learn the math that powers LED effects — modulo arithmetic, linear interpolation, sine waves, exponential decay, normalization, range mapping, and color gradients.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# Mathematics for LED Programming

## Summary

Covers the mathematical concepts powering LED effects: modulo arithmetic, linear interpolation, normalization, sine wave functions, exponential decay, range mapping, random number generation, brightness gamma functions, and the math behind color interpolation and smooth color transitions.

## Concepts Covered

This chapter covers the following 30 concepts from the learning graph:

1. Modulo Arithmetic
2. Integer Arithmetic
3. Floating-Point Arithmetic
4. Linear Interpolation
5. Sine Wave Function
6. math.pow() Function
7. Normalization (0.0 to 1.0)
8. Mapping Value Ranges
9. Random Number Generation
10. Pseudorandom Numbers
11. Uniform Distribution
12. Weighted Random Selection
13. Array Index Calculation
14. Percentage Calculations
15. Ratio and Proportion
16. Sequence Generation
17. Step Size Calculation
18. Phase Offset Calculation
19. Exponential Decay
20. Brightness Gamma Function
21. Coordinate Mapping
22. Wrap-Around Arithmetic
23. Scaling Between Ranges
24. Floor and Ceiling Functions
25. Absolute Value Function
26. Color Interpolation
27. Smooth Color Transition
28. Normalized Color Values
29. Color Fade Effect
30. Color Gradient

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 2: Python Basics: Variables, Data Types, and Operators](../02-python-variables-types-operators/index.md)
- [Chapter 3: Python Functions, Modules, and Programming Best Practices](../03-python-functions-modules-practices/index.md)
- [Chapter 4: Python Control Flow, Loops, and Error Handling](../04-python-control-flow-loops/index.md)
- [Chapter 6: MicroPython APIs, GPIO Control, and Electrical Fundamentals](../06-micropython-apis-and-electronics/index.md)
- [Chapter 7: Color Theory: The RGB Color Model and Color Mixing](../07-rgb-color-theory/index.md)
- [Chapter 9: NeoPixel Programming: Pixels, Colors, and the NeoPixel Library](../09-neopixel-programming/index.md)
- [Chapter 10: Advanced Color Theory: HSV, Gamma Correction, and Color Palettes](../10-advanced-color-theory/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 11! Math powers every animation effect. The comet tail, the breathing glow, the smooth rainbow scroll — they're all math dressed up as light. Don't worry if math isn't your favorite subject. Each concept here connects directly to something visual you can watch on your strip. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Use modulo arithmetic for wrap-around motion and repeating patterns
- Apply linear interpolation to create smooth transitions between two values
- Use sine waves to create breathing and pulsing effects
- Normalize values to the 0.0–1.0 range and map them to new ranges
- Apply exponential decay to create fading trail effects
- Generate and use random numbers for randomized animations
- Blend between two colors using color interpolation
- Build smooth color fades and gradients across a strip

## What You'll Need

- Thonny IDE connected to your Pico
- NeoPixel strip wired and ready
- `import math` available in MicroPython

---

## Integer and Floating-Point Arithmetic

Two types of numbers appear throughout animation code. Understanding them prevents surprises.

**Integer arithmetic** works with whole numbers. In Python 3, dividing two integers with `/` gives a float even if the result is whole: `10 / 2` = `5.0`. The `//` operator gives integer (floor) division: `10 // 2` = `5`. Use `//` when you need a result suitable for a pixel index.

**Floating-point arithmetic** works with decimal numbers like `0.5`, `3.14`, `0.001`. Most animation math uses floats for precision. Before sending values to the NeoPixel strip, convert them to integers with `int()`.

The key rule: **pixel indexes must be integers**. Color values must be integers in the range 0–255. Everything else (intermediate calculations, step sizes, timing) can be float.

---

## Modulo Arithmetic and Wrap-Around

**Modulo arithmetic** computes the *remainder* after division. The operator in Python is `%`.

- `10 % 3` = `1` (10 divided by 3 is 3 with remainder 1)
- `7 % 7` = `0`
- `8 % 7` = `1`
- `14 % 7` = `0`

The magic for LED animations: modulo creates **wrap-around arithmetic**. When a pixel position `pos` reaches the end of the strip, `pos % NUM_PIXELS` wraps it back to the beginning.

```python
NUM_PIXELS = 30
pos = 0

while True:
    strip[pos] = (200, 0, 0)   # light the current pixel
    strip.write()
    utime.sleep(0.05)
    strip[pos] = (0, 0, 0)    # erase it

    pos = (pos + 1) % NUM_PIXELS   # advance, wrapping at end
```

You should see a single red pixel travel around the strip in a continuous loop — never stopping at the end. Without the `% NUM_PIXELS`, `pos` would grow past 29 and cause an `IndexError`.

**Sequence generation** using modulo also creates repeating color patterns. The expression `i % len(PALETTE)` cycles through a palette for any number of pixels.

#### Diagram: Modulo Wrap-Around Animation


<iframe src="../../sims/modulo-wrap-simulation/main.html" width="100%" height="302px" scrolling="no"></iframe>
[Run Modulo Wrap-Around Animation Fullscreen](../../sims/modulo-wrap-simulation/main.html)

<details markdown="1">
<summary>Interactive simulation: modulo wrap-around on a strip</summary>
Type: interactive-infographic
**sim-id:** modulo-wrap-simulation
**Library:** p5.js
**Status:** Specified

A row of 10 pixel circles representing a NeoPixel strip. A "position" counter is shown above. Controls: a **Step** button advances `pos` by 1, a **Auto** toggle runs it continuously at 5 steps/second. As `pos` increments, the current pixel lights red and the previous one turns off. When `pos` reaches 10 (end of strip), the next step shows the modulo calculation: `10 % 10 = 0` in an overlay, and the first pixel lights up again. Below the strip, the formula `pos = (pos + 1) % 10` is displayed with current values substituted in. Canvas: 700 × 300 px. Responds to window resize.

Learning objective: Understanding — the student can explain why modulo creates wrap-around behavior.
</details>

---

## Normalization and Mapping Value Ranges

Two operations appear together constantly in animation code: **normalization** and **mapping value ranges**.

**Normalization** converts a value from any range to the **0.0 to 1.0 range**. A value expressed as 0.0–1.0 is called a **normalized value**. The formula is:

\[ \text{normalized} = \frac{\text{value} - \text{min}}{\text{max} - \text{min}} \]

For example, normalizing a pixel index `i` on a 30-pixel strip:

```python
normalized = i / (config.NUMBER_PIXELS - 1)   # 0.0 at pixel 0, 1.0 at pixel 29
```

**Mapping value ranges** (also called **scaling between ranges**) converts a normalized value (or any value) to a new range. The general formula:

\[ \text{output} = \text{out\_min} + \text{normalized} \times (\text{out\_max} - \text{out\_min}) \]

For example, mapping a pixel's position to a hue from 0 to 360:

```python
hue = (i / config.NUMBER_PIXELS) * 360   # maps 0..29 → 0..360
```

**Percentage calculations** and **ratio and proportion** are just specialized forms of this mapping. 30% brightness means multiplying by 0.3. A ratio of 1:3 means the first value is 25% of the total.

**Coordinate mapping** applies this idea to pixel positions on 2D grids (like matrices). To map row `r` and column `c` of an 8×8 matrix to a single strip index:

```python
index = r * 8 + c   # row-major order
```

---

## Linear Interpolation (LERP)

**Linear interpolation** — often shortened to **LERP** — calculates a value that is a certain fraction of the way between two endpoints.

Before the formula, here's the concept: if you're traveling from point A (value 0) to point B (value 100), after going 30% of the way, you're at 30. After 70%, you're at 70. The formula:

\[ \text{lerp}(a, b, t) = a + t \times (b - a) \]

Where `t` goes from 0.0 (start at `a`) to 1.0 (arrive at `b`).

```python
def lerp(a, b, t):
    return a + t * (b - a)

# 50% of the way from 0 to 255
print(lerp(0, 255, 0.5))   # → 127.5
```

**Color interpolation** applies lerp to each RGB channel separately. This creates a **smooth color transition** between two colors:

```python
def lerp_color(color_a, color_b, t):
    r = int(lerp(color_a[0], color_b[0], t))
    g = int(lerp(color_a[1], color_b[1], t))
    b = int(lerp(color_a[2], color_b[2], t))
    return (r, g, b)

RED  = (200, 0, 0)
BLUE = (0, 0, 200)

# Create a 10-step gradient from red to blue
for i in range(10):
    t = i / 9   # 0.0 at i=0, 1.0 at i=9
    strip[i] = lerp_color(RED, BLUE, t)

strip.write()
```

You should see a smooth gradient from red through purple to blue across the first 10 pixels.

A **color gradient** extends this to any number of steps across the full strip. A **color fade effect** applies the same idea over time — the same color at different brightness levels.

!!! tip "Pixel's tip"
    <img src="../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel points upward">
    The `t` value in LERP is always between 0.0 and 1.0. If you compute `t = i / (N - 1)` for pixels 0 through N-1, pixel 0 gets the starting color and pixel N-1 gets the ending color. Pixels in between get a smooth blend. Perfect gradients, every time!

---

## Sine Wave Function

The **sine wave function** produces a smoothly oscillating value that cycles between -1.0 and 1.0. Import it from Python's `math` module:

```python
import math
value = math.sin(angle_in_radians)   # returns a float from -1.0 to 1.0
```

A **radian** is a unit of angle. One full revolution = 2π radians ≈ 6.28 radians. As the angle increases from 0 to 6.28, `math.sin()` produces one complete wave.

The key use in LED programming: drive a breathing (pulsing) brightness effect.

Before the code, here's the recipe:
- `time_step` increases over each loop iteration
- `math.sin(time_step)` produces a value from -1 to +1
- We convert that to a brightness from 0 to 255

```python
import math
import utime

time_step = 0.0

while True:
    # math.sin gives -1 to 1; convert to 0 to 1
    normalized = (math.sin(time_step) + 1) / 2   # now 0.0 to 1.0
    brightness = int(normalized * 200)            # scale to 0–200

    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, brightness, brightness)   # cyan breathing

    strip.write()
    time_step += 0.1    # advance the wave
    utime.sleep_ms(20)  # ~50 frames per second
```

You should see the entire strip breathing in and out — brightening and dimming smoothly in a wave pattern. This is called a **sine-based breathing effect**.

**Phase offset** lets you shift the wave for different pixels. Adding `(i / NUM_PIXELS) * 2 * math.pi` to the angle for pixel `i` makes the brightness wave roll across the strip instead of the whole strip pulsing at once.

---

## Exponential Decay and Brightness Formulas

**Exponential decay** describes how something fades over time at a decreasing rate — like a comet tail. Each step, the brightness is multiplied by a factor less than 1.0. After many steps, it approaches zero.

The formula: `brightness = initial × decay^step`

For LED trail effects, you keep a brightness array for each pixel:

```python
trail = [0] * config.NUMBER_PIXELS   # brightness level for each pixel
DECAY = 0.8    # each step, brightness drops to 80% of previous

pos = 0

while True:
    # Decay all existing brightness values
    for i in range(config.NUMBER_PIXELS):
        trail[i] = int(trail[i] * DECAY)

    # Set the head pixel to full brightness
    trail[pos] = 200

    # Update the strip
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (trail[i], 0, 0)   # red trail

    strip.write()
    pos = (pos + 1) % config.NUMBER_PIXELS
    utime.sleep_ms(50)
```

You should see a red pixel moving across the strip leaving a fading red tail. The tail length is controlled by DECAY — a value closer to 1.0 gives a longer tail.

**Step size calculation** determines how fast the position or brightness changes per frame. For the breathing effect: `time_step += 0.1` means one full breath takes about 63 frames (2π / 0.1 ≈ 63). Larger step sizes = faster breathing.

---

## Random Numbers for Animations

**Random number generation** in Python uses the `urandom` module on MicroPython. A key concept: computers can't produce truly random numbers — they produce **pseudorandom numbers** that appear random but are generated by a formula.

**Uniform distribution** means every value in the range is equally likely. `urandom.randint(0, 255)` has equal probability of returning 0, 127, or 255 — or any other value in between.

**Weighted random selection** makes some outcomes more likely. One simple approach: build a list with the most common value repeated multiple times, then pick randomly from it:

```python
import urandom

# Red appears 5× more often than blue or green
weighted_choices = [(200, 0, 0)] * 5 + [(0, 200, 0)] * 1 + [(0, 0, 200)] * 1
color = weighted_choices[urandom.randint(0, len(weighted_choices) - 1)]
```

**Array index calculation** for random patterns: use `urandom.randint(0, config.NUMBER_PIXELS - 1)` to pick a random pixel index.

---

## Floor, Ceiling, and Absolute Value

Three math functions appear frequently in animation code.

**Floor function** `int()` or `math.floor()` — rounds a float *down* to the nearest integer. Use it when you need a valid pixel index from a float calculation:

```python
index = int(4.9)   # → 4 (rounded down)
```

**Ceiling function** `math.ceil()` — rounds *up* to the nearest integer:

```python
import math
index = math.ceil(4.1)   # → 5 (rounded up)
```

**Absolute value function** `abs()` — returns the non-negative version of a number. Use it to measure distance without caring about direction:

```python
distance = abs(pixel_pos - center)   # distance from center, always positive
```

**math.pow() function** — raises a number to a power. `math.pow(2, 8)` = 256.0. Used in gamma correction and exponential calculations.

#### Diagram: Math Functions in Animation


<iframe src="../../sims/animation-math-explorer/main.html" width="100%" height="432px" scrolling="no"></iframe>
[Run Math Functions in Animation Fullscreen](../../sims/animation-math-explorer/main.html)

<details markdown="1">
<summary>Interactive chart: sine wave, lerp, and exponential decay visualized</summary>
Type: chart
**sim-id:** animation-math-explorer
**Library:** Chart.js
**Status:** Specified

A tab-panel with three tabs labeled "Sine Wave", "Linear Interpolation", and "Exponential Decay". Each tab shows an animated line chart on the X axis (frame number 0–100) and Y axis (value 0–255).

Sine Wave tab: A sine curve plotted from frame 0 to 100, with `time_step` incremented by 0.2 per frame. Y value shown as brightness (0–255). A slider controls the speed (0.05–0.4 step size).

Linear Interpolation tab: A straight diagonal line from (0, 0) to (100, 255). A movable dot on the line shows the current t value and interpolated output. Sliders for `a` (start value) and `b` (end value) change the line endpoints.

Exponential Decay tab: A decaying curve from (0, 255) approaching 0. A slider controls the DECAY factor (0.7–0.99). Canvas: 700 × 380 px. Responds to window resize.

Learning objective: Analyzing — the student can match a math function to the visual LED effect it produces.
</details>

---

## Putting It Together: Smooth Gradient with Breathing

This final example combines normalization, LERP, and sine waves to create a gradient that breathes:

```python
import math
import utime

time_step = 0.0

while True:
    breath = (math.sin(time_step) + 1) / 2   # 0.0 to 1.0

    for i in range(config.NUMBER_PIXELS):
        t = i / (config.NUMBER_PIXELS - 1)   # position 0.0 to 1.0
        # Lerp from blue to green, then scale by breathing level
        r = 0
        g = int(lerp(0, 200, t) * breath)
        b = int(lerp(200, 0, t) * breath)
        strip[i] = (r, g, b)

    strip.write()
    time_step += 0.05
    utime.sleep_ms(20)
```

You should see a blue-to-green gradient that slowly breathes in and out. Every pixel's brightness pulses together.

---

## Try It Yourself

1. **Modulo pattern:** Use `i % 5` to create a repeating 5-color pattern across the strip. (Every 5th pixel should have the same color.)

2. **LERP fade:** Create a 20-step fade from black `(0,0,0)` to white `(200,200,200)` using `lerp_color`.

3. **Breathing speed:** Modify the breathing example to take exactly 3 seconds per full breath. (Hint: one full sine wave = 2π radians. At 20 ms per frame, how many frames is 3 seconds? What step size gets there in that many frames?)

4. **Long comet tail:** Change the DECAY value from 0.8 to 0.95 in the comet tail example. How does a larger decay value change the tail length?

---

## Check Your Understanding

1. What does `15 % 7` evaluate to?
2. Why is modulo useful for wrap-around pixel motion?
3. What is the output of `lerp(0, 100, 0.75)`?
4. What range does `math.sin()` produce?
5. What is the formula for exponential decay?
6. What is the difference between `int(4.9)` and `math.ceil(4.9)`?
7. How would you map a pixel index (0 to 29) to a hue value (0 to 360)?

---

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You've got the math toolkit! Modulo for wrap-around. LERP for smooth transitions. Sine for breathing. Exponential decay for trails. Normalization for flexible scaling. These seven tools cover 90% of the math in every animation you'll ever see. The effects in the next chapters are just creative combinations of what you learned here.

## What's Next

In [Chapter 12](../12-basic-animation-patterns/index.md), you'll implement your first complete animation effects — blink, rainbow, moving rainbow, twinkle, candle flicker, and more — applying the math you just learned to create visual magic on your strip.
