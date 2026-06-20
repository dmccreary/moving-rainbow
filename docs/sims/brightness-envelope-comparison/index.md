---
title: Brightness Envelopes for Advanced Patterns
description: Analyzing - the student can match a brightness envelope shape to the visual effect it produces.
image: /sims/brightness-envelope-comparison/brightness-envelope-comparison.png
og:image: /sims/brightness-envelope-comparison/brightness-envelope-comparison.png
twitter:image: /sims/brightness-envelope-comparison/brightness-envelope-comparison.png
social:
   cards: false
library: Chart.js
status: implemented
---

# Brightness Envelopes for Advanced Patterns

<iframe src="main.html" width="100%" height="462px" scrolling="no"></iframe>

[Run the Brightness Envelopes for Advanced Patterns MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A tab-panel with four tabs, each showing the brightness envelope for one pattern:

**Learning objective:** Analyzing - the student can match a brightness envelope shape to the visual effect it produces.

## How to Use

Use the tabs to switch views and drag the sliders to change the inputs. The chart, the moving marker, and the readout all update live as you drag.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/brightness-envelope-comparison/main.html"
        height="462px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Analyzing - the student can match a brightness envelope shape to the visual effect it produces.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 14](../../chapters/14-advanced-animation-patterns/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 14: Advanced Animation Patterns — Comet, Scanner, and Heartbeat](../../chapters/14-advanced-animation-patterns/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: chart
**sim-id:** brightness-envelope-comparison
**Library:** Chart.js
**Status:** Specified

A tab-panel with four tabs, each showing the brightness envelope for one pattern:

1. **Heartbeat tab**: X axis = time steps (0–60), Y axis = brightness (0–255). Two narrow peaks (at t=6 and t=18) followed by a long flat zero section. Animates a moving dot.
2. **Comet Tail tab**: X axis = pixel index (0–29), Y axis = brightness. Exponential decay from a peak at position 20, falling toward zero to the left. A "head position" slider moves the peak.
3. **Larson Scanner tab**: X axis = pixel index, Y axis = brightness. A triangular peak centered at scan position. A "width" slider changes the peak width.
4. **Sine Breathing tab**: X axis = time, Y axis = brightness. Smooth sine curve, labeled with key points (peak, trough, half-way).

Each tab plays a live animation of the strip simulated below the chart. Canvas: 700 × 400 px. Responds to window resize.

Learning objective: Analyzing — the student can match a brightness envelope shape to the visual effect it produces.
```

</details>
