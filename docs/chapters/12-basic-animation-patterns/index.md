---
title: Basic LED Animation Patterns
description: Implement blink, rainbow, moving rainbow, rainbow cycle, twinkle, candle flicker, random colors, and clock display animations using frame-based techniques and position tracking.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# Basic LED Animation Patterns

## Summary

Implements the first wave of animation effects—blink, rainbow, moving rainbow, rainbow cycle, twinkle, candle flicker, random colors, and clock display—using frame-based animation, position tracking, direction variables, bounce logic, and modulo wrapping.

## Concepts Covered

This chapter covers the following 21 concepts from the learning graph:

1. Blink Pattern
2. Rainbow Static Pattern
3. Moving Rainbow Pattern
4. Rainbow Cycle
5. Twinkle Effect
6. Candle Flicker Animation
7. Random Colors Animation
8. Clock Display Animation
9. Frame-Based Animation
10. Animation Delay
11. Position Tracking Variable
12. Direction Variable
13. Bounce Logic
14. Modulo Wrapping
15. Pixel Offset Calculation
16. Sequential Pixel Lighting
17. Parallel Pixel Update
18. Timing with utime Module
19. Flicker Randomness
20. Step Size in Animation
21. Time-Based Animation

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 2: Python Basics: Variables, Data Types, and Operators](../02-python-variables-types-operators/index.md)
- [Chapter 3: Python Functions, Modules, and Programming Best Practices](../03-python-functions-modules-practices/index.md)
- [Chapter 4: Python Control Flow, Loops, and Error Handling](../04-python-control-flow-loops/index.md)
- [Chapter 6: MicroPython APIs, GPIO Control, and Electrical Fundamentals](../06-micropython-apis-and-electronics/index.md)
- [Chapter 7: Color Theory: The RGB Color Model and Color Mixing](../07-rgb-color-theory/index.md)
- [Chapter 9: NeoPixel Programming: Pixels, Colors, and the NeoPixel Library](../09-neopixel-programming/index.md)
- [Chapter 11: Mathematics for LED Programming](../11-math-for-led-programming/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 12! This is where the lights really come on. You've got all the building blocks — variables, loops, functions, the NeoPixel library, and the math. Now you'll combine them into real, beautiful animations. Eight patterns in one chapter. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Explain what frame-based animation means
- Implement the blink, rainbow, moving rainbow, and rainbow cycle patterns
- Build twinkle and candle flicker effects using randomness
- Create a random color animation
- Display a clock using the `localtime()` function
- Explain position tracking, direction variables, and bounce logic

## What You'll Need

- Raspberry Pi Pico with NeoPixel strip connected
- Thonny IDE connected
- `config.py` on the Pico with correct `NEOPIXEL_PIN` and `NUMBER_PIXELS`

---

## Frame-Based Animation

Every animation in this chapter uses **frame-based animation**: a loop that runs repeatedly, updating the LED strip on each iteration. Each iteration is one **frame**. The speed of the animation depends on the **animation delay** — how long the program waits between frames.

Before looking at any pattern, here's the standard frame structure all animations follow:

```python
# Standard animation loop structure
while True:
    # 1. Calculate what the LEDs should look like for this frame
    # 2. Set pixel colors
    # 3. Call strip.write() to push colors to hardware
    # 4. Wait (the animation delay)
    utime.sleep_ms(DELAY_MS)
```

Two types of time control appear in animations:

- **Timing with `utime.sleep_ms()`** — pauses for a fixed number of milliseconds. Simple and predictable.
- **Time-based animation** using `ticks_ms()` — tracks elapsed time so the animation speed doesn't depend on how long the calculation takes.

For the patterns in this chapter, `sleep_ms()` is sufficient.

---

## Pattern 1: Blink

The **Blink Pattern** turns the entire strip on, waits, then turns it off, then repeats.

This pattern introduces two key concepts: **parallel pixel update** (setting all pixels at once in a loop) and the simplest possible animation delay.

```python
import neopixel, machine, utime, config

strip = neopixel.NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

ON_COLOR  = (0, 150, 255)   # blue-white
OFF_COLOR = (0, 0, 0)

while True:
    for i in range(config.NUMBER_PIXELS):
        strip[i] = ON_COLOR      # all pixels on
    strip.write()
    utime.sleep_ms(500)

    for i in range(config.NUMBER_PIXELS):
        strip[i] = OFF_COLOR     # all pixels off
    strip.write()
    utime.sleep_ms(500)
```

You should see the strip blink on and off once per second.

---

## Pattern 2: Rainbow Static Pattern

The **Rainbow Static Pattern** spreads a full spectrum of colors across the strip simultaneously. Each pixel gets a different hue.

Before the code, here's the idea: divide 360 hue degrees evenly among all pixels. Pixel 0 gets hue 0 (red), the middle pixel gets hue 180 (cyan), and the last pixel gets hue 359 (almost-red again).

```python
import neopixel, machine, utime, config
import math

strip = neopixel.NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

def hsv_to_rgb(h, s, v):
    if s == 0:
        val = int(v * 255)
        return (val, val, val)
    h = h / 60.0
    i = int(h)
    f = h - i
    p, q, t = v*(1-s), v*(1-s*f), v*(1-s*(1-f))
    pairs = [(v,t,p),(q,v,p),(p,v,t),(p,q,v),(t,p,v),(v,p,q)]
    r, g, b = pairs[i % 6]
    return (int(r*255), int(g*255), int(b*255))

for i in range(config.NUMBER_PIXELS):
    hue = (i / config.NUMBER_PIXELS) * 360
    strip[i] = hsv_to_rgb(hue, 1.0, 0.5)

strip.write()
```

You should see a full rainbow spread across the strip and stay static.

---

## Pattern 3: Moving Rainbow Pattern

The **Moving Rainbow Pattern** is the same rainbow, but it scrolls. A **position offset** shifts all the hues together on each frame, creating the illusion of movement.

Two new concepts appear here:
- **Pixel Offset Calculation** — adding an offset to each pixel's hue shifts the entire rainbow
- **Modulo Wrapping** — `% 360` keeps the hue in the valid range when the offset grows large

```python
offset = 0     # tracks how far the rainbow has scrolled
STEP = 3       # degrees to shift per frame (step size)

while True:
    for i in range(config.NUMBER_PIXELS):
        hue = ((i / config.NUMBER_PIXELS) * 360 + offset) % 360
        strip[i] = hsv_to_rgb(hue, 1.0, 0.5)

    strip.write()
    offset = (offset + STEP) % 360   # advance offset, wrap at 360
    utime.sleep_ms(20)
```

You should see the rainbow smoothly scroll across the strip. Increase `STEP` to scroll faster.

---

## Pattern 4: Rainbow Cycle

The **Rainbow Cycle** is different from the moving rainbow. Instead of the rainbow being spread across the strip, each *individual pixel* cycles through the full spectrum at its own speed. The offset between pixels determines the visual pattern.

```python
offset = 0

while True:
    for i in range(config.NUMBER_PIXELS):
        hue = (offset + i * 10) % 360   # each pixel offset by 10 degrees
        strip[i] = hsv_to_rgb(hue, 1.0, 0.5)

    strip.write()
    offset = (offset + 2) % 360
    utime.sleep_ms(15)
```

You should see a cycling, spinning pattern — similar to the moving rainbow but with a different relationship between adjacent pixels.

!!! info "Pixel thinks..."
    <img src="../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    The difference between Moving Rainbow and Rainbow Cycle is in how the offset is applied. Moving Rainbow: all pixels shift *together* (same offset for all). Rainbow Cycle: each pixel gets a *different* offset based on its index. Two patterns, one math tool.

---

## Pattern 5: Twinkle Effect

The **Twinkle Effect** randomly picks a few pixels and flashes them bright, creating a starfield look.

**Flicker randomness** is the key technique — using `urandom` to pick both *which* pixels light up and *what color* they use.

Before the code, here's the algorithm:
1. Each frame, dim all pixels slightly (so previous twinkles fade)
2. Pick 3 random pixels and set them to bright colors
3. Write and wait

```python
import urandom

# Start with all pixels off
for i in range(config.NUMBER_PIXELS):
    strip[i] = (0, 0, 0)

while True:
    # Dim all pixels by multiplying by 0.8
    for i in range(config.NUMBER_PIXELS):
        r, g, b = strip[i]
        strip[i] = (int(r * 0.8), int(g * 0.8), int(b * 0.8))

    # Twinkle: light 3 random pixels
    for _ in range(3):
        pixel = urandom.randint(0, config.NUMBER_PIXELS - 1)
        r = urandom.randint(100, 255)
        g = urandom.randint(100, 255)
        b = urandom.randint(100, 255)
        strip[pixel] = (r, g, b)

    strip.write()
    utime.sleep_ms(50)
```

You should see random pixels sparkling with random colors, each briefly bright before fading.

---

## Pattern 6: Candle Flicker Animation

The **Candle Flicker Animation** simulates a flame: mostly warm yellow-orange with random dips to red or orange, and random brightness variation.

The key ideas: warm colors (no blue), and random variation in brightness on every frame.

```python
import urandom

while True:
    for i in range(config.NUMBER_PIXELS):
        # Flame colors: orange to yellow, randomized
        r = urandom.randint(150, 255)
        g = urandom.randint(50, 130)
        b = 0                            # no blue in a candle!
        strip[i] = (r, g, b)

    strip.write()
    utime.sleep_ms(urandom.randint(30, 80))   # random delay = irregular flicker
```

You should see the strip rippling with warm orange-yellow flickers. The random delay (30–80 ms) makes the rhythm irregular — just like a real candle.

---

## Pattern 7: Random Colors Animation

The **Random Colors Animation** assigns a new random color to every pixel on every frame. It's energetic and chaotic — good for party effects.

```python
import urandom

while True:
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (
            urandom.randint(0, 200),
            urandom.randint(0, 200),
            urandom.randint(0, 200)
        )
    strip.write()
    utime.sleep_ms(100)
```

You should see the entire strip flash with new random colors every 100 ms.

#### Diagram: Animation Pattern Comparison

<details markdown="1">
<summary>Interactive comparison: six animation patterns side by side</summary>
Type: interactive-infographic
**sim-id:** animation-pattern-comparison
**Library:** p5.js
**Status:** Specified

Six rows of small LED strip simulations (10 pixels each), each labeled with its pattern name:
1. Blink — alternates all-on / all-off every 500 ms
2. Rainbow Static — shows fixed rainbow
3. Moving Rainbow — rainbow scrolls left at adjustable speed
4. Twinkle — random pixels flash bright on a dark background
5. Candle Flicker — warm colors randomly varying brightness
6. Random Colors — all pixels flash random colors each frame

A global **Play/Pause** button runs or pauses all six simultaneously. A **Speed** slider (slow/medium/fast) adjusts all animation speeds together. Each row has a label and a brief description on the right. Canvas: 700 × 500 px. Responds to window resize.

Learning objective: Analyzing — the student can visually match a running LED pattern to its name and algorithm.
</details>

---

## Pattern 8: Clock Display Animation

The **Clock Display Animation** uses `utime.localtime()` to read the current time and map it to pixels on the strip. This turns your LED strip into a clock!

`localtime()` returns a tuple. The relevant fields are:
- `t[4]` — hours (0–23)
- `t[5]` — minutes (0–59)
- `t[6]` — seconds (0–59)

Before the code, here's the mapping scheme: divide the strip into three segments. The first third shows hours, the second shows minutes, the third shows seconds.

```python
import utime

N = config.NUMBER_PIXELS
THIRD = N // 3   # pixels per segment

while True:
    t = utime.localtime()   # get current time
    hours   = t[4]           # 0–23
    minutes = t[5]           # 0–59
    seconds = t[6]           # 0–59

    # Map time values to pixel counts within each segment
    hour_pixels = int((hours / 24) * THIRD)
    min_pixels  = int((minutes / 60) * THIRD)
    sec_pixels  = int((seconds / 60) * THIRD)

    for i in range(N):
        if i < THIRD:
            # Hours segment: red
            strip[i] = (150, 0, 0) if i < hour_pixels else (0, 0, 0)
        elif i < 2 * THIRD:
            # Minutes segment: green
            j = i - THIRD
            strip[i] = (0, 150, 0) if j < min_pixels else (0, 0, 0)
        else:
            # Seconds segment: blue
            j = i - 2 * THIRD
            strip[i] = (0, 0, 150) if j < sec_pixels else (0, 0, 0)

    strip.write()
    utime.sleep(1)   # update once per second
```

You should see three segments of red, green, and blue that grow and shrink like clock hands. The blue segment resets every 60 seconds, the green every hour.

!!! warning "Watch out!"
    <img src="../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    The Pico doesn't have a battery-backed real-time clock (RTC). When you unplug it, `localtime()` resets to a default time. For the clock animation to show the correct time, you need to set it first in Thonny with: `import utime; utime.set_time(...)` or use an RTC module. For this course, the animation pattern itself is the learning goal — exact time accuracy is optional.

---

## Try It Yourself

1. **Color blink:** Modify the blink pattern to cycle through three colors instead of just on/off: red blink, green blink, blue blink.

2. **Fast rainbow:** Increase the moving rainbow `STEP` value from 3 to 20. How does the visual feel change?

3. **Gentle twinkle:** Change the twinkle pattern to use only white pixels `(200, 200, 200)` instead of random colors. This makes a starfield effect.

4. **Clock minutes:** Modify the clock display to use the full strip just for minutes — 60 pixels all green, with the lit portion showing how many minutes have passed this hour.

---

## Check Your Understanding

1. What is frame-based animation? What does each "frame" do?
2. In the moving rainbow, what is the role of the `offset` variable?
3. How does twinkle use randomness differently from random colors?
4. What makes the candle flicker look natural? (Name two sources of randomness.)
5. What does `utime.localtime()` return?
6. What is the step size in an animation, and how does it affect speed?
7. What is the difference between sequential and parallel pixel updates?

---

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    Eight patterns! Blink, static rainbow, moving rainbow, rainbow cycle, twinkle, candle flicker, random colors, and a clock display. You built every one of them from scratch. Your strip is doing real things now. These patterns are the foundation for everything more complex coming up in the next two chapters!

## What's Next

In [Chapter 13](../13-intermediate-animations/index.md), you'll build more complex animations — fade in/out, theater chase, ripple, bounce, and moving bands — and learn how to control animation speed, trail fading, and multi-parameter patterns.
