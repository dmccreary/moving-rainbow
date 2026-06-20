---
title: Advanced Color Theory — HSV, Gamma Correction, and Color Palettes
description: Learn the HSV color space, how gamma correction fixes perceived brightness, gamma lookup tables, saturation, and strategies for designing color palettes and sequences.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# Advanced Color Theory: HSV, Gamma Correction, and Color Palettes

## Summary

Introduces the HSV color space, gamma correction for perceptual accuracy, gamma lookup tables, color harmony principles, saturation, RGB-to-HSV and HSV-to-RGB conversions, named color constants, color sequences, and palette design strategies.

## Concepts Covered

This chapter covers the following 15 concepts from the learning graph:

1. Black Color
2. White Color
3. Named Color Constants
4. Color Mixing by Channel
5. Saturation
6. HSV Color Model
7. RGB to HSV Conversion
8. HSV to RGB Conversion
9. Color Harmony
10. Gamma Correction
11. Gamma Value
12. Gamma Lookup Table
13. Color Perception
14. Color Palette Design
15. Color Sequence Array

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 7: Color Theory: The RGB Color Model and Color Mixing](../07-rgb-color-theory/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 10! You know the RGB model. Now you'll learn its smarter sibling — HSV — and understand why LEDs look different from what the numbers say they should. This chapter makes your color choices intentional and precise. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Describe the HSV color model and its three components
- Explain what saturation means and how it affects color
- Convert between RGB and HSV using Python code
- Explain why gamma correction is needed and how it works
- Build and use a gamma lookup table
- Create named color constants for your projects
- Design a color palette and store it as a color sequence array

## What You'll Need

- Thonny IDE connected to your Pico
- NeoPixel strip wired and ready
- Chapter 7 concepts fresh in your mind

---

## Named Color Constants and Color Mixing by Channel

Before diving into HSV, let's establish a useful coding practice: **named color constants**.

Instead of writing `(255, 0, 0)` every time you want red, define constants at the top of your program:

```python
# Named color constants — define once, use anywhere
RED     = (200, 0, 0)
GREEN   = (0, 200, 0)
BLUE    = (0, 0, 200)
YELLOW  = (200, 200, 0)
CYAN    = (0, 200, 200)
MAGENTA = (200, 0, 200)
WHITE   = (200, 200, 200)
BLACK   = (0, 0, 0)        # off
ORANGE  = (200, 80, 0)
PURPLE  = (80, 0, 200)
```

Notice that **black** `(0, 0, 0)` is not a color of light — it's simply "off." And **white** `(200, 200, 200)` is all three channels equal and bright. Brightness is intentionally set to 200 here (not 255) to limit power draw.

**Color mixing by channel** means combining colors by adding or averaging their RGB components. Mixing red and blue: `((255+0)//2, (0+0)//2, (0+255)//2)` = `(127, 0, 127)` — a medium purple. This mathematical mixing lets you create smooth transitions between any two colors.

---

## The HSV Color Model

The **HSV color model** describes colors with three values that match how people naturally think about color:

- **H = Hue** — the color itself, expressed as a degree on a color wheel from 0° to 360°. Red is at 0°, green at 120°, blue at 240°, and red again at 360°.
- **S = Saturation** — how "pure" or "vivid" the color is, from 0.0 (gray/white) to 1.0 (fully saturated, pure hue).
- **V = Value** — how bright the color is, from 0.0 (black) to 1.0 (full brightness).

**Saturation** deserves a closer look. A fully saturated color (S=1.0) is a vivid, pure hue — like fire-truck red. A low-saturation color (S=0.2) looks washed out and pastel. At S=0, the hue doesn't matter — you get a shade of gray determined only by V.

The power of HSV is that you can change the hue smoothly to cycle through rainbow colors without touching saturation or brightness. In RGB, doing this requires complex three-channel math. In HSV, you just increment H from 0 to 360.

The table below compares how RGB and HSV describe the same colors:

| Color | RGB | HSV |
|---|---|---|
| Red | (255, 0, 0) | H=0°, S=1.0, V=1.0 |
| Yellow | (255, 255, 0) | H=60°, S=1.0, V=1.0 |
| Green | (0, 255, 0) | H=120°, S=1.0, V=1.0 |
| Cyan | (0, 255, 255) | H=180°, S=1.0, V=1.0 |
| Blue | (0, 0, 255) | H=240°, S=1.0, V=1.0 |
| Pastel pink | (255, 180, 200) | H=350°, S=0.29, V=1.0 |
| Dim gray | (60, 60, 60) | H=any, S=0, V=0.24 |

#### Diagram: HSV Color Space Explorer

<details markdown="1">
<summary>Interactive diagram: HSV color wheel and controls</summary>
Type: interactive-infographic
**sim-id:** hsv-color-explorer
**Library:** p5.js
**Status:** Specified

A p5.js MicroSim with three sliders:
- H (Hue): 0–360, default 180
- S (Saturation): 0.0–1.0, default 1.0
- V (Value/Brightness): 0.0–1.0, default 1.0

A large filled circle shows the current color. Below it, the corresponding RGB tuple is displayed as text: e.g., "RGB: (0, 255, 255)". A color wheel diagram on the side has a movable dot that tracks the H value. Moving the H slider moves the dot around the wheel. Moving S changes the dot's distance from the center (center = gray, edge = saturated). Moving V dims or brightens both the circle and the wheel. Canvas: 700 × 380 px. Responds to window resize.

Learning objective: Understanding — the student can predict how changing H, S, or V affects the output color.
</details>

---

## RGB to HSV and HSV to RGB Conversion

To use HSV in your NeoPixel programs, you need to convert between HSV and RGB. The Pico's `neopixel` library only accepts RGB tuples.

### HSV to RGB Conversion

This conversion function takes hue (0–360), saturation (0.0–1.0), and value (0.0–1.0) and returns an RGB tuple with values 0–255:

```python
def hsv_to_rgb(h, s, v):
    # h = hue (0-360), s = saturation (0-1), v = value (0-1)
    # returns (r, g, b) with values 0-255
    if s == 0:
        val = int(v * 255)
        return (val, val, val)   # gray

    h = h / 60.0
    i = int(h)
    f = h - i
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))

    if i == 0:   r, g, b = v, t, p
    elif i == 1: r, g, b = q, v, p
    elif i == 2: r, g, b = p, v, t
    elif i == 3: r, g, b = p, q, v
    elif i == 4: r, g, b = t, p, v
    else:        r, g, b = v, p, q

    return (int(r * 255), int(g * 255), int(b * 255))
```

Before testing this function, here's what it does: it takes the HSV values, applies a standard mathematical conversion, and returns the equivalent RGB tuple. The math inside handles six different "sectors" of the color wheel.

```python
print(hsv_to_rgb(0, 1.0, 1.0))    # red → (255, 0, 0)
print(hsv_to_rgb(120, 1.0, 1.0))  # green → (0, 255, 0)
print(hsv_to_rgb(240, 1.0, 1.0))  # blue → (0, 0, 255)
print(hsv_to_rgb(60, 0.5, 0.8))   # muted yellow
```

### Rainbow Effect with HSV

Now here's where HSV shines. To create a rainbow across your strip, just map each pixel's position to a hue from 0 to 360:

```python
for i in range(config.NUMBER_PIXELS):
    hue = (i / config.NUMBER_PIXELS) * 360    # map position to hue
    strip[i] = hsv_to_rgb(hue, 1.0, 0.5)     # full saturation, 50% brightness

strip.write()
```

You should see a smooth rainbow spread across the entire strip.

---

## Gamma Correction

This is one of the most important concepts for making LEDs look good.

As you learned in Chapter 7, your eyes don't respond to light in a straight line. They're more sensitive to changes in dark areas. This means:

- LED value `(30, 0, 0)` looks much brighter than "12% of maximum" — it looks more like 40%
- LED value `(200, 0, 0)` looks only slightly brighter than `(170, 0, 0)`

**Gamma correction** is a mathematical adjustment that fixes this mismatch. You apply a formula to your intended brightness values before sending them to the strip, so the *perceived* brightness changes linearly with your input.

The **gamma value** (typically 2.2) determines the shape of the correction:

\[ \text{corrected} = \left(\frac{\text{input}}{255}\right)^{\gamma} \times 255 \]

For a gamma of 2.2, an input of 128 (half scale) corrects to:

\[ \left(\frac{128}{255}\right)^{2.2} \times 255 \approx 55 \]

So instead of sending 128, you send 55. The LED outputs less light, but it *looks* like 50% brightness to your eye. Without correction, 128 looks much brighter than halfway.

!!! info "Pixel thinks..."
    <img src="../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    Gamma correction doesn't change what colors you want — it changes the numbers you send to the LED to get those colors. You think in "perceived brightness." The gamma function translates to "LED output." It's a translation layer between human vision and digital electronics.

---

## Gamma Lookup Table

Calculating the gamma formula for every pixel, every frame, on a microcontroller is slow. A smarter approach is a **gamma lookup table** — a pre-calculated list of 256 corrected values, one for each possible input.

You calculate this table once at startup, then use it with a simple index lookup (fast!) instead of computing the formula each time:

```python
import math

GAMMA = 2.2

# Build the lookup table once
gamma_table = [int((i / 255) ** GAMMA * 255 + 0.5) for i in range(256)]

def apply_gamma(r, g, b):
    return (gamma_table[r], gamma_table[g], gamma_table[b])

# Use it when setting pixels
strip[0] = apply_gamma(128, 0, 0)   # gamma-corrected dim red
strip.write()
```

The list comprehension `[int((i / 255) ** GAMMA * 255 + 0.5) for i in range(256)]` creates all 256 values at once. The `+ 0.5` rounds to the nearest integer.

---

## Color Perception Summary

**Color perception** is the study of how human eyes and brains interpret light. The key insights for LED programming:

- The eye is most sensitive to **green** light — green LEDs look brighter than red or blue at the same power level
- Brightness is perceived on a **logarithmic scale** — doubling light output doesn't double perceived brightness
- **Color adaptation** means the eye adjusts to ambient lighting — colors look different in a dark room vs. a bright room
- **Simultaneous contrast** means a color looks different depending on what surrounds it

These perceptual effects are why identical RGB values can produce visually different results in different contexts. Gamma correction addresses the most important effect (the logarithmic scale), but the others are worth knowing as you design animations.

---

## Color Palette Design and Color Sequence Arrays

A **color palette** is a carefully chosen set of colors that work well together. A well-designed palette makes your animation look professional instead of random.

A **color sequence array** stores your palette as a Python list of RGB tuples. Your animation code loops through the sequence:

```python
# A warm sunset palette
PALETTE = [
    (200, 10, 0),    # deep red
    (200, 60, 0),    # red-orange
    (200, 130, 0),   # orange
    (200, 200, 0),   # yellow
    (200, 200, 100), # warm yellow-white
]
```

Here's a program that cycles through the palette one color per frame, changing the whole strip each step:

```python
import utime

palette = [
    (200, 0, 0),
    (200, 100, 0),
    (200, 200, 0),
    (0, 200, 0),
    (0, 0, 200),
]

while True:
    for color in palette:
        for i in range(config.NUMBER_PIXELS):
            strip[i] = color
        strip.write()
        utime.sleep(0.5)   # hold each color for half a second
```

You should see the strip cycle through red, orange, yellow, green, and blue, holding each for half a second.

### Palette Design Strategies

Here are three reliable palette design approaches:

- **Analogous palette** — pick 4–6 adjacent colors on the color wheel. Looks harmonious and calm. Example: blues and teals for an ocean theme.
- **Complementary pair with neutrals** — one strong complementary pair (e.g., red and cyan) plus several neutrals (whites, grays). High impact without chaos.
- **Gradient palette** — interpolate between two endpoint colors with 8–12 steps. Use the color mixing technique from earlier in this chapter.

!!! tip "Pixel's tip"
    <img src="../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel points upward">
    Start with four colors maximum for your first palette. More is not always more — a focused palette with great transitions often looks better than ten random colors fighting for attention.

---

## Try It Yourself

1. **HSV rainbow:** Use `hsv_to_rgb()` to light each pixel a different hue, distributing hues evenly from 0 to 360. Try different values for S and V.

2. **Gamma compare:** Light pixel 0 with `(128, 0, 0)` (no gamma). Light pixel 1 with `apply_gamma(128, 0, 0)` (gamma corrected). Compare how they look side by side.

3. **Palette cycling:** Design your own 5-color palette with a theme (ocean, fire, forest). Implement the cycling program above with your palette.

4. **Color fade:** Use color mixing by channel to create a smooth fade from `RED = (200, 0, 0)` to `BLUE = (0, 0, 200)` across 20 steps. Store each step in a list.

---

## Check Your Understanding

1. What do H, S, and V stand for in the HSV color model?
2. What does saturation of 0.0 produce, regardless of hue?
3. Why is HSV easier than RGB for creating rainbow effects?
4. What is the gamma value typically used, and what does it represent?
5. Why is a gamma lookup table faster than calculating the formula each time?
6. What is a color sequence array?
7. Describe one color palette design strategy in your own words.

---

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You're thinking about color like a professional lighting designer! You can work in HSV to control hue, saturation, and brightness independently. You know why gamma correction matters and how to apply it. And you have a toolkit for building beautiful, intentional color palettes. Your animations are about to level up!

## What's Next

In [Chapter 11](../11-math-for-led-programming/index.md), you'll learn the mathematics that power animation effects — modulo arithmetic, linear interpolation, sine waves, exponential decay, and more. The math is simpler than it sounds, and the visual results are spectacular.
