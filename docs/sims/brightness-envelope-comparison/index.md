---
title: Brightness Envelopes for Advanced Patterns
description: Analyzing — the student can match a brightness envelope shape to the visual effect it produces.
status: scaffold
library: Chart.js
bloom_level: TBD
---

# Brightness Envelopes for Advanced Patterns



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 14: Advanced Animation Patterns — Comet, Scanner, and Heartbeat](../../chapters/14-advanced-animation-patterns/index.md).

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

## Related Resources

- [Chapter 14: Advanced Animation Patterns — Comet, Scanner, and Heartbeat](../../chapters/14-advanced-animation-patterns/index.md)
