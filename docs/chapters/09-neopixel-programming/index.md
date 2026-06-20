---
title: NeoPixel Programming — Pixels, Colors, and the NeoPixel Library
description: Master the NeoPixel library — pixel indexing, RGB tuples, strip.write(), clearing pixels, power scaling, segmentation, and pixel group operations.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# NeoPixel Programming: Pixels, Colors, and the NeoPixel Library

## Summary

Teaches the NeoPixel class: pixel indexing, RGB tuple format, strip.write(), 24-bit color data, NeoPixel class instantiation, setting individual pixels, clearing pixels, LED power scaling, strip segmentation, and pixel group operations.

## Concepts Covered

This chapter covers the following 20 concepts from the learning graph:

1. 24-Bit Color Data Format
2. LED Data Chaining
3. Data Stripping
4. Pixel Indexing
5. strip.write() Method
6. RGB Tuple Format
7. Color Value Range
8. 8-Bit Color Depth
9. Number of Pixels Parameter
10. Data Pin Parameter
11. NeoPixel Class Instantiation
12. Setting Individual Pixels
13. Clearing All Pixels
14. Maximum Strip Brightness
15. LED Power Scaling
16. LED Chain Data Timing
17. Level Shifter for 5V Data
18. LED Strip Segmentation
19. Pixel Group Operations
20. NeoPixel Library Overview

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 5: Raspberry Pi Pico Hardware and Development Environment](../05-raspberry-pi-pico-hardware/index.md)
- [Chapter 6: MicroPython APIs, GPIO Control, and Electrical Fundamentals](../06-micropython-apis-and-electronics/index.md)
- [Chapter 7: Color Theory: The RGB Color Model and Color Mixing](../07-rgb-color-theory/index.md)
- [Chapter 8: NeoPixel LED Hardware: WS2812B, Wiring, and Form Factors](../08-neopixel-led-hardware/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 9! You've got your hardware wired up and you know your RGB colors. Now you're going to put it all together with the NeoPixel library. Every animation you'll ever write starts with the skills in this chapter. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Create a NeoPixel strip object with the right parameters
- Use pixel indexing to address individual LEDs
- Set pixel colors using RGB tuples
- Call `strip.write()` to push colors to the hardware
- Clear all pixels and set group operations
- Scale power by limiting maximum brightness
- Segment a single strip into logical sections

## What You'll Need

- Raspberry Pi Pico with MicroPython installed, connected to Thonny
- NeoPixel strip wired to GP0 (data), VSYS (power), and GND
- `config.py` on your Pico with `NEOPIXEL_PIN = 0` and `NUMBER_PIXELS` set to your strip length

---

## The 24-Bit Color Data Format

Before diving into code, let's understand what data the Pico actually sends to the strip.

Each pixel's color is stored as **24-bit color data**: 8 bits for red, 8 bits for green, and 8 bits for blue. This is called **8-bit color depth** per channel.

- 8 bits can hold values 0–255 (that's 2⁸ = 256 possible values)
- With 3 channels of 256 values each, you can make 256 × 256 × 256 = **16,777,216 different colors**

This is why RGB values run from 0 to 255 — not 0 to 100 or any other range. The hardware literally uses 8-bit numbers.

When you write `strip[0] = (255, 0, 0)`, the NeoPixel library converts that tuple to a 24-bit binary number and sends it to the strip. You never need to handle the binary yourself — the library does it for you.

---

## NeoPixel Library Overview and Instantiation

The **NeoPixel library** in MicroPython (`neopixel` module) handles all communication with WS2812B strips. It takes care of the precise timing the chip requires so you can focus on colors and patterns.

Before creating a strip object, here are the two required parameters:

- **Data Pin Parameter** — the `machine.Pin` object for the GPIO pin your data wire connects to
- **Number of Pixels Parameter** — how many LEDs are on your strip

The `config.py` file stores these values so you can change them once and have all your programs update automatically:

```python
# config.py — saved on the Pico
NEOPIXEL_PIN = 0       # GP0 is the data line
NUMBER_PIXELS = 30     # 30-pixel strip
```

**NeoPixel Class Instantiation** — creating the strip object:

```python
import neopixel
import machine
import config

strip = neopixel.NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
```

After this line, `strip` is a list-like object. Each element represents one pixel. The strip is indexed from `0` (the pixel closest to the Pico's data wire) to `config.NUMBER_PIXELS - 1` (the last pixel).

---

## Pixel Indexing: Addressing Individual Pixels

**Pixel indexing** works just like indexing a Python list. The first pixel is at index `0`, not index `1`. This is called **zero-based indexing**.

```python
strip[0] = (255, 0, 0)    # first pixel: red
strip[1] = (0, 255, 0)    # second pixel: green
strip[29] = (0, 0, 255)   # 30th pixel (last on a 30-pixel strip): blue
```

The valid index range for a 30-pixel strip is **0 to 29**. Trying to access `strip[30]` raises an `IndexError` — there is no pixel 30.

The **RGB Tuple Format** is `(red, green, blue)` with each value in the **color value range** 0–255:

- `(255, 0, 0)` = full red
- `(0, 255, 0)` = full green
- `(0, 0, 255)` = full blue
- `(0, 0, 0)` = off (black)
- `(255, 255, 255)` = full white

#### Diagram: Pixel Indexing on a NeoPixel Strip


<iframe src="../../sims/pixel-indexing-explorer/main.html" width="100%" height="292px" scrolling="no"></iframe>
[Run Pixel Indexing on a NeoPixel Strip Fullscreen](../../sims/pixel-indexing-explorer/main.html)

<details markdown="1">
<summary>Interactive diagram: pixel index numbers on a strip</summary>
Type: interactive-infographic
**sim-id:** pixel-indexing-explorer
**Library:** p5.js
**Status:** Specified

A row of 10 colored LED circles representing pixels 0–9 on a strip. Each circle has its index number displayed below it. A text input field lets the user type an index (0–9) and a color (as a preset from a dropdown: red, green, blue, white, yellow, off). Clicking "Set Pixel" colors that circle and shows the Python code that would produce that effect: `strip[3] = (0, 255, 0)`. A "Clear All" button resets all circles to off. A "Write" button (highlighted) sends the colors (animates a signal wave moving from pixel 0 to pixel 9). Canvas: 700 × 280 px. Responds to window resize.

Learning objective: Applying — the student can predict which physical pixel will light up given an index in code.
</details>

---

## The strip.write() Method

Setting pixels does *not* change the LEDs immediately. The NeoPixel library holds the color data in memory on the Pico. You have to call **`strip.write()`** to actually send the data to the strip.

This two-step process is intentional:

1. Set all the pixel colors you want in one loop
2. Call `strip.write()` once to push them all to the hardware simultaneously

This prevents partial updates — you never see half the strip at the old colors while the other half updates.

```python
# Step 1: set all colors
for i in range(config.NUMBER_PIXELS):
    strip[i] = (100, 0, 200)   # purple

# Step 2: push to hardware — all pixels change at once
strip.write()
```

You should see the entire strip turn purple at once.

!!! warning "Watch out!"
    <img src="../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    Forgetting `strip.write()` is one of the most common first-week mistakes. If your LEDs aren't responding to your code, check that `strip.write()` is there. Your code may be updating the in-memory buffer perfectly — but nothing will appear until you write to the hardware.

---

## Clearing All Pixels

To turn off all LEDs, set every pixel to `(0, 0, 0)` and call `strip.write()`. Clearing is useful at the start of an animation and to reset between patterns.

```python
def clear_strip(strip):
    for i in range(len(strip)):
        strip[i] = (0, 0, 0)
    strip.write()
```

The `len(strip)` call returns the number of pixels — the same value as `config.NUMBER_PIXELS`. Using `len(strip)` in a helper function makes the function work for any strip length without needing to import `config`.

Call it like this:

```python
clear_strip(strip)   # all LEDs off
```

---

## LED Power Scaling: Controlling Maximum Brightness

**Maximum strip brightness** and **LED power scaling** are important for wearable projects and for keeping your power supply happy.

As you learned in Chapter 8, a 30-pixel strip at full white draws 600 mA — close to the limit of a USB port. The easiest fix is to limit maximum brightness: instead of setting any channel to 255, set the maximum to something lower.

A **brightness scale factor** from 0.0 to 1.0 lets you scale all colors down proportionally:

```python
BRIGHTNESS = 0.3   # 30% brightness — safe for USB-powered strips

def scale_color(r, g, b):
    return (int(r * BRIGHTNESS), int(g * BRIGHTNESS), int(b * BRIGHTNESS))

strip[0] = scale_color(255, 0, 0)    # red at 30% brightness = (76, 0, 0)
strip.write()
```

You should see a dim red — much easier on the power supply and comfortable to wear near your body.

The table below shows peak current at different brightness levels for a 30-pixel strip:

| Brightness | Scale Factor | Peak Current (mA) | Safe from USB? |
|---|---|---|---|
| Full | 1.0 | 600 | Marginal |
| 50% | 0.5 | 300 | Yes |
| 30% | 0.3 | 180 | Yes |
| 10% | 0.1 | 60 | Yes |

---

## LED Chain Data Timing

The WS2812B chip requires very precise timing on the data line. The NeoPixel library handles this automatically, but understanding one key constraint helps you write better animation code.

**LED Chain Data Timing** means `strip.write()` takes a fixed amount of time based on the number of pixels. For 30 pixels, it takes about 1.2 milliseconds. For 300 pixels, it takes about 12 milliseconds. This is not a problem for most animations, but it means:

- `strip.write()` is not instantaneous
- Very fast loops that call `strip.write()` every iteration may be limited by this timing
- For complex animations, calculate all pixel values first, then call `strip.write()` once

After `strip.write()` sends data, there's a brief **reset period** (about 50 microseconds) before you can send the next frame. The library handles this automatically — you don't need to add any delay for this.

---

## LED Strip Segmentation

**LED strip segmentation** means treating different sections of one physical strip as independent zones. For example, you might have a 30-pixel strip sewn into a costume and want the top 10 pixels to show one pattern while the bottom 20 show another.

Before reading the code, here are the key terms:
- `start` — the first pixel index in a segment
- `end` — one past the last pixel in a segment (to match Python's `range()` convention)

```python
def fill_segment(strip, start, end, color):
    for i in range(start, end):
        strip[i] = color

# Fill the first 10 pixels red (segment 0: pixels 0–9)
fill_segment(strip, 0, 10, (200, 0, 0))

# Fill the next 10 pixels green (segment 1: pixels 10–19)
fill_segment(strip, 10, 20, (0, 200, 0))

# Fill the last 10 pixels blue (segment 2: pixels 20–30)
fill_segment(strip, 20, 30, (0, 0, 200))

strip.write()   # push all three segments at once
```

You should see your strip divided into red, green, and blue thirds.

### Pixel Group Operations

**Pixel group operations** extend segmentation to more complex patterns. For example, setting every other pixel to a different color creates a striped effect:

```python
for i in range(config.NUMBER_PIXELS):
    if i % 2 == 0:
        strip[i] = (200, 0, 0)    # even pixels: red
    else:
        strip[i] = (0, 0, 200)    # odd pixels: blue

strip.write()
```

You should see alternating red and blue pixels across the entire strip.

!!! tip "Pixel's tip"
    <img src="../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel points upward">
    The modulo operator `%` is your segmentation superpower. `i % 2 == 0` catches every other pixel. `i % 3 == 0` catches every third pixel. `i % 5 < 3` catches groups of 3 on, 2 off. Try different modulo patterns and watch what happens!

---

## Level Shifter for 5V Data

Most NeoPixel strips respond correctly to the Pico's 3.3 V data signal. However, some strips — especially those sold for 5 V systems — require a true 5 V data signal to work reliably.

A **level shifter** is a small electronic component that converts the 3.3 V signal from the Pico's GPIO to a 5 V signal. Common level shifters used in hobby projects include the 74HCT125 and the TXS0108E. One output channel connects between GP0 and the LED strip's data input.

If your strip works fine with 3.3 V data, you don't need a level shifter. If you see pixel color errors or missing updates despite correct wiring, try adding one.

---

## Putting It Together: Rainbow Segment Display

Here's a program that uses pixel indexing, segmentation, and group operations to display a five-color rainbow across any strip length:

Before reading the code, the key idea: we divide the strip into 5 equal segments and give each a different color from the rainbow.

```python
import neopixel
import machine
import config

strip = neopixel.NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

rainbow = [
    (200, 0, 0),     # red
    (200, 100, 0),   # orange
    (200, 200, 0),   # yellow
    (0, 200, 0),     # green
    (0, 0, 200),     # blue
]

segment_size = config.NUMBER_PIXELS // len(rainbow)   # integer division

for seg, color in enumerate(rainbow):
    start = seg * segment_size
    end = start + segment_size
    for i in range(start, end):
        strip[i] = color

strip.write()
```

You should see your strip divided into five colored bands: red, orange, yellow, green, and blue.

---

## Try It Yourself

1. **Single pixel test:** Light up only pixel 5 in white. All other pixels should stay off. Confirm with `clear_strip()` first.

2. **Color gradient:** Set pixels 0–9 to progressively brighter red. Pixel 0 = `(25, 0, 0)`, pixel 1 = `(50, 0, 0)`, ..., pixel 9 = `(250, 0, 0)`.

3. **Alternating thirds:** Use `i % 3` to create a three-color repeating pattern across the strip.

4. **Scaled white:** Modify the `scale_color` function to accept a single brightness argument and apply it to a `(255, 255, 255)` white color. Test at 10%, 30%, and 100% brightness.

---

## Check Your Understanding

1. What does "24-bit color" mean in terms of bits per channel?
2. What is the valid index range for a 30-pixel NeoPixel strip?
3. Why does `strip.write()` exist? Why doesn't setting a pixel change it immediately?
4. How do you turn off all pixels on a strip?
5. What does a brightness scale factor of `0.3` do to an RGB value of `(200, 100, 50)`?
6. What does "LED strip segmentation" mean?
7. Write the code to set every third pixel (0, 3, 6, …) to green.

---

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You can now control every pixel on your strip with precision! You know how 24-bit color works, how to address pixels by index, how to call `strip.write()` at the right moment, how to scale power safely, and how to segment your strip. Every animation pattern in the rest of this course builds directly on these skills.

## What's Next

In [Chapter 10](../10-advanced-color-theory/index.md), you'll go deeper into color — learning the HSV color space, how gamma correction fixes perceived brightness, and how to design harmonious color palettes for your animations.
