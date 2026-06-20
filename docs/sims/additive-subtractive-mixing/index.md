---
title: Additive vs. Subtractive Color Mixing
description: Understanding - explain why light mixing and paint mixing produce different results.
image: /sims/additive-subtractive-mixing/additive-subtractive-mixing.png
og:image: /sims/additive-subtractive-mixing/additive-subtractive-mixing.png
twitter:image: /sims/additive-subtractive-mixing/additive-subtractive-mixing.png
social:
   cards: false
library: p5.js
status: implemented
---

# Additive vs. Subtractive Color Mixing

<iframe src="main.html" width="100%" height="362px" scrolling="no"></iframe>

[Run the Additive vs. Subtractive Color Mixing MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

Two side-by-side panels. Left panel labeled "Additive (Light - LEDs)": three overlapping circles in red, green, and blue on a black background.

**Learning objective:** Understanding - explain why light mixing and paint mixing produce different results.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/additive-subtractive-mixing/main.html"
        height="362px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Understanding - explain why light mixing and paint mixing produce different results.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 7](../../chapters/07-rgb-color-theory/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 7: Color Theory — The RGB Color Model and Color Mixing](../../chapters/07-rgb-color-theory/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: interactive-infographic
**sim-id:** additive-subtractive-mixing
**Library:** p5.js
**Status:** Specified

Two side-by-side panels. Left panel labeled "Additive (Light — LEDs)": three overlapping circles in red, green, and blue on a black background. Where red and green overlap: yellow. Where green and blue overlap: cyan. Where red and blue overlap: magenta. Where all three overlap: white. Right panel labeled "Subtractive (Paint — Pigments)": three overlapping circles in red (magenta-red), blue (cyan-blue), and yellow on a white background. Where they overlap, colors darken toward brown/gray/black. Hovering over any overlap region shows a tooltip: "Red + Green light = Yellow" or "Red + Blue paint = Purple-brown". A toggle button switches between "Light Mode" and "Paint Mode" to emphasize the difference. Canvas: 700 × 350 px. Responds to window resize.

Learning objective: Understanding — explain why light mixing and paint mixing produce different results.
```

</details>
