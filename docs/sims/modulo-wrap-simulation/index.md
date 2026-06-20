---
title: Modulo Wrap-Around Animation
description: Understanding - the student can explain why modulo creates wrap-around behavior.
image: /sims/modulo-wrap-simulation/modulo-wrap-simulation.png
og:image: /sims/modulo-wrap-simulation/modulo-wrap-simulation.png
twitter:image: /sims/modulo-wrap-simulation/modulo-wrap-simulation.png
social:
   cards: false
library: p5.js
status: implemented
---

# Modulo Wrap-Around Animation

<iframe src="main.html" width="100%" height="302px" scrolling="no"></iframe>

[Run the Modulo Wrap-Around Animation MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A row of 10 pixel circles representing a NeoPixel strip. A "position" counter is shown above.

**Learning objective:** Understanding - the student can explain why modulo creates wrap-around behavior.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/modulo-wrap-simulation/main.html"
        height="302px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Understanding - the student can explain why modulo creates wrap-around behavior.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 11](../../chapters/11-math-for-led-programming/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 11: Mathematics for LED Programming](../../chapters/11-math-for-led-programming/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: interactive-infographic
**sim-id:** modulo-wrap-simulation
**Library:** p5.js
**Status:** Specified

A row of 10 pixel circles representing a NeoPixel strip. A "position" counter is shown above. Controls: a **Step** button advances `pos` by 1, a **Auto** toggle runs it continuously at 5 steps/second. As `pos` increments, the current pixel lights red and the previous one turns off. When `pos` reaches 10 (end of strip), the next step shows the modulo calculation: `10 % 10 = 0` in an overlay, and the first pixel lights up again. Below the strip, the formula `pos = (pos + 1) % 10` is displayed with current values substituted in. Canvas: 700 × 300 px. Responds to window resize.

Learning objective: Understanding — the student can explain why modulo creates wrap-around behavior.
```

</details>
