---
title: Perceived vs. Linear Brightness
description: Understanding - explain why gamma correction is needed.
image: /sims/perceived-vs-linear-brightness/perceived-vs-linear-brightness.png
og:image: /sims/perceived-vs-linear-brightness/perceived-vs-linear-brightness.png
twitter:image: /sims/perceived-vs-linear-brightness/perceived-vs-linear-brightness.png
social:
   cards: false
library: Chart.js
status: implemented
---

# Perceived vs. Linear Brightness

<iframe src="main.html" width="100%" height="382px" scrolling="no"></iframe>

[Run the Perceived vs. Linear Brightness MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A line chart with two curves on the same axes. X-axis: "Linear LED value (0–255)".

**Learning objective:** Understanding - explain why gamma correction is needed.

## How to Use

Use the tabs to switch views and drag the sliders to change the inputs. The chart, the moving marker, and the readout all update live as you drag.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/perceived-vs-linear-brightness/main.html"
        height="382px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Understanding - explain why gamma correction is needed.

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
Type: chart
**sim-id:** perceived-vs-linear-brightness
**Library:** Chart.js
**Status:** Specified

A line chart with two curves on the same axes. X-axis: "Linear LED value (0–255)". Y-axis: "Perceived brightness (0–100%)". Curve 1 labeled "Linear (what the LED does)": a straight diagonal line from (0,0) to (255,100). Curve 2 labeled "Perceived (what your eye sees)": a concave curve that rises quickly at low values and slowly at high values, approximating a power function with gamma ~2.2. On hover, tooltips show: "LED value: X → Perceived brightness: Y%". A slider below lets users drag and see a dot move along both curves simultaneously, highlighting the gap between them. Canvas: 700 × 350 px. Responds to window resize.

Learning objective: Understanding — explain why gamma correction is needed.
```

</details>
