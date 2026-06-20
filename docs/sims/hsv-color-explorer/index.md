---
title: HSV Color Space Explorer
description: Understanding - the student can predict how changing H, S, or V affects the output color.
image: /sims/hsv-color-explorer/hsv-color-explorer.png
og:image: /sims/hsv-color-explorer/hsv-color-explorer.png
twitter:image: /sims/hsv-color-explorer/hsv-color-explorer.png
social:
   cards: false
library: p5.js
status: implemented
---

# HSV Color Space Explorer

<iframe src="main.html" width="100%" height="392px" scrolling="no"></iframe>

[Run the HSV Color Space Explorer MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A p5.js MicroSim with three sliders:

**Learning objective:** Understanding - the student can predict how changing H, S, or V affects the output color.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/hsv-color-explorer/main.html"
        height="392px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Understanding - the student can predict how changing H, S, or V affects the output color.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 10](../../chapters/10-advanced-color-theory/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 10: Advanced Color Theory — HSV, Gamma Correction, and Color Palettes](../../chapters/10-advanced-color-theory/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
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
```

</details>
