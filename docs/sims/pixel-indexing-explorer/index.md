---
title: Pixel Indexing on a NeoPixel Strip
description: Applying - the student can predict which physical pixel will light up given an index in code.
image: /sims/pixel-indexing-explorer/pixel-indexing-explorer.png
og:image: /sims/pixel-indexing-explorer/pixel-indexing-explorer.png
twitter:image: /sims/pixel-indexing-explorer/pixel-indexing-explorer.png
social:
   cards: false
library: p5.js
status: implemented
---

# Pixel Indexing on a NeoPixel Strip

<iframe src="main.html" width="100%" height="292px" scrolling="no"></iframe>

[Run the Pixel Indexing on a NeoPixel Strip MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A row of 10 colored LED circles representing pixels 0–9 on a strip. Each circle has its index number displayed below it.

**Learning objective:** Applying - the student can predict which physical pixel will light up given an index in code.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/pixel-indexing-explorer/main.html"
        height="292px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Applying - the student can predict which physical pixel will light up given an index in code.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 9](../../chapters/09-neopixel-programming/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 9: NeoPixel Programming — Pixels, Colors, and the NeoPixel Library](../../chapters/09-neopixel-programming/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: interactive-infographic
**sim-id:** pixel-indexing-explorer
**Library:** p5.js
**Status:** Specified

A row of 10 colored LED circles representing pixels 0–9 on a strip. Each circle has its index number displayed below it. A text input field lets the user type an index (0–9) and a color (as a preset from a dropdown: red, green, blue, white, yellow, off). Clicking "Set Pixel" colors that circle and shows the Python code that would produce that effect: `strip[3] = (0, 255, 0)`. A "Clear All" button resets all circles to off. A "Write" button (highlighted) sends the colors (animates a signal wave moving from pixel 0 to pixel 9). Canvas: 700 × 280 px. Responds to window resize.

Learning objective: Applying — the student can predict which physical pixel will light up given an index in code.
```

</details>
