---
title: Color Theory — The RGB Color Model and Color Mixing
description: Explore the RGB additive color model, the color wheel, complementary and analogous colors, color temperature, and color psychology for LED design.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# Color Theory: The RGB Color Model and Color Mixing

## Summary

Explores the RGB additive color model, primary light colors, the color wheel, spectral sequence, complementary and analogous colors, warm and cool colors, color temperature, color contrast, and the psychological effects of color choices.

## Concepts Covered

This chapter covers the following 20 concepts from the learning graph:

1. RGB Color Model
2. Additive Color Mixing
3. Subtractive Color Mixing
4. Red as Primary Light Color
5. Green as Primary Light Color
6. Blue as Primary Light Color
7. Color Wheel
8. Spectral Color Sequence
9. Hue
10. Value (Brightness Level)
11. Complementary Colors
12. Analogous Colors
13. Color Temperature
14. Warm Colors
15. Cool Colors
16. Color Contrast
17. Perceived Brightness
18. Linear Brightness
19. Color Psychology
20. Triadic Color Scheme

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 2: Python Basics: Variables, Data Types, and Operators](../02-python-variables-types-operators/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 7! This chapter is all about color — what it is, how light mixes, and how to pick colors that look amazing together. Artists spend years learning this. You're going to learn the part that matters most for LED design in one chapter. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Explain how the RGB additive color model works
- Describe the difference between additive (light) and subtractive (paint) color mixing
- Identify the color wheel and name complementary, analogous, and triadic color schemes
- Choose warm vs. cool colors intentionally
- Explain the difference between perceived brightness and linear brightness
- Describe how color affects mood and how to use that in your LED projects

## What You'll Need

- No hardware required for this chapter — it's all about understanding color!
- Optional: A NeoPixel strip to test the color examples as you read

---

## How Light Makes Color: The RGB Color Model

When you look at a screen, a TV, or an LED, the colors you see are made of light — not paint. That changes *everything* about how colors mix.

The **RGB color model** describes colors using three **primary light colors**: **red**, **green**, and **blue**. Every color your LED strip can make is a combination of those three.

Each channel — red, green, and blue — has a value from **0 to 255**:

- **0** means that channel is completely off (contributes no light)
- **255** means that channel is at full brightness

Here are some key colors expressed as RGB tuples:

| Color | Red | Green | Blue | Tuple |
|---|---|---|---|---|
| Red | 255 | 0 | 0 | `(255, 0, 0)` |
| Green | 0 | 255 | 0 | `(0, 255, 0)` |
| Blue | 0 | 0 | 255 | `(0, 0, 255)` |
| White | 255 | 255 | 255 | `(255, 255, 255)` |
| Black (off) | 0 | 0 | 0 | `(0, 0, 0)` |
| Yellow | 255 | 255 | 0 | `(255, 255, 0)` |
| Cyan | 0 | 255 | 255 | `(0, 255, 255)` |
| Magenta | 255 | 0 | 255 | `(255, 0, 255)` |
| Orange | 255 | 128 | 0 | `(255, 128, 0)` |

Notice that **white** is all three channels at maximum. Black is all channels at zero — the LED is simply off.

### Additive vs. Subtractive Color Mixing

Here's the surprising part: **light mixes differently from paint**.

**Additive color mixing** is what LEDs do. You start with darkness and *add* light. Adding red + green light makes yellow. Adding all three makes white. The more light you add, the brighter the result.

**Subtractive color mixing** is what paint and ink do. You start with white paper and *subtract* light by applying pigments. Mixing red and green paint makes a muddy brown. The more pigments you add, the darker the result gets.

This is why you can't just use your childhood knowledge of paint mixing to predict LED colors. In LED-world: red + green = yellow. That surprises almost everyone the first time!

#### Diagram: Additive vs. Subtractive Color Mixing

<details markdown="1">
<summary>Interactive diagram: additive and subtractive color mixing side by side</summary>
Type: interactive-infographic
**sim-id:** additive-subtractive-mixing
**Library:** p5.js
**Status:** Specified

Two side-by-side panels. Left panel labeled "Additive (Light — LEDs)": three overlapping circles in red, green, and blue on a black background. Where red and green overlap: yellow. Where green and blue overlap: cyan. Where red and blue overlap: magenta. Where all three overlap: white. Right panel labeled "Subtractive (Paint — Pigments)": three overlapping circles in red (magenta-red), blue (cyan-blue), and yellow on a white background. Where they overlap, colors darken toward brown/gray/black. Hovering over any overlap region shows a tooltip: "Red + Green light = Yellow" or "Red + Blue paint = Purple-brown". A toggle button switches between "Light Mode" and "Paint Mode" to emphasize the difference. Canvas: 700 × 350 px. Responds to window resize.

Learning objective: Understanding — explain why light mixing and paint mixing produce different results.
</details>

---

## The Color Wheel and Spectral Sequence

The **spectral color sequence** is the order colors appear in a rainbow: red → orange → yellow → green → cyan → blue → indigo → violet. This sequence matches the wavelengths of visible light, from longest (red, ~700 nm) to shortest (violet, ~400 nm).

A **color wheel** arranges these colors in a circle so you can see the relationships between them. Understanding the color wheel helps you choose colors that work well together.

A **hue** is the pure color itself — where it sits on the wheel (red, blue, orange, etc.) without considering brightness or how much white or black is mixed in.

**Value** (also called **brightness level**) describes how light or dark a color is. A high-value color is bright; a low-value color is dark. In RGB, you control value by scaling all three channels up or down equally. For example, dim red is `(60, 0, 0)` and bright red is `(255, 0, 0)`.

!!! info "Pixel thinks..."
    <img src="../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    Hue is the "what color" — red, blue, green, orange. Value is the "how bright" — dim, medium, full blast. You control both with RGB numbers. Hue comes from the *ratio* of R:G:B. Value comes from how *large* those numbers are.

---

## Color Relationships: Complementary, Analogous, and Triadic

Artists use color relationships to create effects. Here are the three most useful for LED design.

### Complementary Colors

**Complementary colors** are opposite each other on the color wheel. Placing them together creates strong visual contrast — each color makes the other look more vivid.

The main complementary pairs:

- Red ↔ Cyan
- Green ↔ Magenta
- Blue ↔ Yellow

In RGB, the complement of a color is simply `(255-r, 255-g, 255-b)`. The complement of red `(255, 0, 0)` is cyan `(0, 255, 255)`.

### Analogous Colors

**Analogous colors** sit next to each other on the color wheel. They blend smoothly and feel harmonious. A red → orange → yellow sequence is analogous. Use analogous colors for smooth gradient effects and calm, cohesive lighting.

### Triadic Color Scheme

A **triadic color scheme** uses three colors evenly spaced around the color wheel — 120° apart. The classic example is red, green, and blue — which happen to be your three RGB primaries! Triadic schemes feel balanced and energetic.

The table below compares the three relationships:

| Scheme | Description | Feel | LED Use |
|---|---|---|---|
| Complementary | Two opposite colors | High contrast, vibrant | Alert patterns, attention-grabbing effects |
| Analogous | Adjacent colors | Smooth, harmonious | Gradients, calm ambient lighting |
| Triadic | Three evenly spaced colors | Balanced, energetic | Rainbow effects, party lighting |

---

## Warm, Cool, and Color Temperature

Colors carry emotional weight. Understanding this helps you choose the right mood for your projects.

### Warm Colors

**Warm colors** — reds, oranges, and yellows — feel energetic, exciting, or cozy. Think of fire, sunsets, and candlelight. They tend to "advance" visually, meaning they seem closer to the viewer.

In RGB, warm colors have high red and moderate-to-high green values, with low or zero blue.

### Cool Colors

**Cool colors** — blues, greens, and cyans — feel calm, peaceful, or refreshing. Think of ocean water, moonlight, and clear sky. They tend to "recede" visually, seeming farther away.

In RGB, cool colors have high blue or green values with low red.

### Color Temperature

**Color temperature** is the warmth or coolness of a white or near-white light, measured in Kelvin (K). Warmer whites (2700 K) look orange-ish, like candlelight. Cooler whites (6500 K) look blue-white, like an overcast day. You can simulate color temperature on your LED strip by adjusting the ratio of red to blue in your white color value. A warm white might be `(255, 200, 100)`, while a cool white might be `(200, 220, 255)`.

---

## Perceived Brightness vs. Linear Brightness

Here's a fact that surprises most people: **your eyes don't respond to light in a straight line**.

**Linear brightness** is the actual physical light output of the LED. Doubling the RGB value doubles the light output.

**Perceived brightness** is how bright *your eye thinks* something is. Because of how human vision works, doubling the physical brightness does not make something look twice as bright. The eye is more sensitive to changes in dark areas than bright ones.

This means that the difference between `(0, 0, 0)` and `(30, 0, 0)` *looks* much bigger than the difference between `(200, 0, 0)` and `(230, 0, 0)` — even though both are a change of 30 units.

**Color contrast** is the difference in hue, value, or both between two colors that appear next to each other. High contrast (dark background, bright foreground) makes patterns easy to see. Low contrast creates subtle, blended effects.

You'll learn how to correct for perceived brightness in Chapter 10, where we cover gamma correction.

#### Diagram: Perceived vs. Linear Brightness

<details markdown="1">
<summary>Interactive chart: how perceived brightness differs from linear brightness</summary>
Type: chart
**sim-id:** perceived-vs-linear-brightness
**Library:** Chart.js
**Status:** Specified

A line chart with two curves on the same axes. X-axis: "Linear LED value (0–255)". Y-axis: "Perceived brightness (0–100%)". Curve 1 labeled "Linear (what the LED does)": a straight diagonal line from (0,0) to (255,100). Curve 2 labeled "Perceived (what your eye sees)": a concave curve that rises quickly at low values and slowly at high values, approximating a power function with gamma ~2.2. On hover, tooltips show: "LED value: X → Perceived brightness: Y%". A slider below lets users drag and see a dot move along both curves simultaneously, highlighting the gap between them. Canvas: 700 × 350 px. Responds to window resize.

Learning objective: Understanding — explain why gamma correction is needed.
</details>

---

## Color Psychology: Color Affects Mood

**Color psychology** is the study of how color influences how people feel. As an LED designer, you can use this knowledge intentionally.

Here are common associations (these vary by culture, so treat them as tendencies, not rules):

- **Red** — energy, excitement, urgency, warmth
- **Orange** — enthusiasm, creativity, friendliness
- **Yellow** — happiness, optimism, attention
- **Green** — nature, calm, growth, safety
- **Blue** — trust, calm, focus, cool professionalism
- **Purple / Violet** — creativity, mystery, luxury
- **White** — cleanliness, clarity, openness
- **Warm orange-white** — cozy, homey, relaxed (candlelight feel)
- **Cool blue-white** — alert, clinical, modern

When you design a costume or room light, think about the feeling you want to create. A Halloween costume might use deep reds and flickering orange. A study lamp might use cool blue-white. A party display might cycle through triadic colors quickly to create excitement.

!!! tip "Pixel's tip"
    <img src="../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel points upward">
    Before you write any animation code, ask yourself: "What do I want this light to feel like?" Cozy? Exciting? Mysterious? Pick your colors based on the answer. The code comes after the design choice.

---

## Putting Color Theory Into Code

Now that you understand color relationships, let's put them to use. Here's a program that displays a complementary pair — red and cyan — alternating across the strip.

The key idea: red is `(255, 0, 0)`. Its complement is `(255-255, 255-0, 255-0)` = `(0, 255, 255)` (cyan).

```python
import neopixel
import machine
import utime
import config

strip = neopixel.NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

red = (200, 0, 0)
cyan = (0, 200, 200)   # complement of red

for i in range(config.NUMBER_PIXELS):
    if i % 2 == 0:
        strip[i] = red    # even pixels: red
    else:
        strip[i] = cyan   # odd pixels: cyan

strip.write()
```

You should see alternating red and cyan pixels — a strong complementary contrast pattern.

---

## Try It Yourself

1. **Warm sunset:** Create a "sunset" on your strip using five warm colors from dark red through orange to yellow. Set groups of pixels to each color.

2. **Complement finder:** Write a Python function `complement(r, g, b)` that returns the complementary color. Test it with a few colors.

3. **Triadic display:** Set your strip to thirds — one third red, one third green, one third blue. Observe the triadic balance.

4. **Mood selector:** Pick a mood (calm, excited, cozy, alert). Choose colors that match. Write the code to display them.

---

## Check Your Understanding

1. What are the three primary light colors in the RGB model?
2. What color do you get when red and green light are at full brightness and blue is at zero?
3. What is the difference between additive and subtractive color mixing?
4. What does "complementary colors" mean? Give one example pair.
5. What are analogous colors? Why do they look smooth together?
6. What is the difference between hue and value?
7. Why doesn't doubling the LED brightness value make the LED look twice as bright?

---

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You're now thinking like an LED artist! You know why light mixes differently from paint, how to find complementary and analogous colors, and how to use warm and cool colors intentionally. Your animations are about to get a lot more intentional — and a lot more beautiful.

## What's Next

In [Chapter 8](../08-neopixel-led-hardware/index.md), you'll go deep on the WS2812B hardware itself — how these chips work, how to wire them, and what all those form factors (strips, rings, matrices) can do.
