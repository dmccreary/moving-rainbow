---
title: Math Functions in Animation
description: Analyzing - the student can match a math function to the visual LED effect it produces.
image: /sims/animation-math-explorer/animation-math-explorer.png
og:image: /sims/animation-math-explorer/animation-math-explorer.png
twitter:image: /sims/animation-math-explorer/animation-math-explorer.png
social:
   cards: false
library: Chart.js
status: implemented
---

# Math Functions in Animation

<iframe src="main.html" width="100%" height="432px" scrolling="no"></iframe>

[Run the Math Functions in Animation MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A tab-panel with three tabs labeled "Sine Wave", "Linear Interpolation", and "Exponential Decay". Each tab shows an animated line chart on the X axis (frame number 0–100) and Y axis (value 0–255).

**Learning objective:** Analyzing - the student can match a math function to the visual LED effect it produces.

## How to Use

Use the tabs to switch views and drag the sliders to change the inputs. The chart, the moving marker, and the readout all update live as you drag.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/animation-math-explorer/main.html"
        height="432px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Analyzing - the student can match a math function to the visual LED effect it produces.

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
Type: chart
**sim-id:** animation-math-explorer
**Library:** Chart.js
**Status:** Specified

A tab-panel with three tabs labeled "Sine Wave", "Linear Interpolation", and "Exponential Decay". Each tab shows an animated line chart on the X axis (frame number 0–100) and Y axis (value 0–255).

Sine Wave tab: A sine curve plotted from frame 0 to 100, with `time_step` incremented by 0.2 per frame. Y value shown as brightness (0–255). A slider controls the speed (0.05–0.4 step size).

Linear Interpolation tab: A straight diagonal line from (0, 0) to (100, 255). A movable dot on the line shows the current t value and interpolated output. Sliders for `a` (start value) and `b` (end value) change the line endpoints.

Exponential Decay tab: A decaying curve from (0, 255) approaching 0. A slider controls the DECAY factor (0.7–0.99). Canvas: 700 × 380 px. Responds to window resize.

Learning objective: Analyzing — the student can match a math function to the visual LED effect it produces.
```

</details>
