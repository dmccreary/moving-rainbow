---
title: Math Functions in Animation
description: Analyzing — the student can match a math function to the visual LED effect it produces.
status: scaffold
library: Chart.js
bloom_level: TBD
---

# Math Functions in Animation



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 11: Mathematics for LED Programming](../../chapters/11-math-for-led-programming/index.md).

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

## Related Resources

- [Chapter 11: Mathematics for LED Programming](../../chapters/11-math-for-led-programming/index.md)
