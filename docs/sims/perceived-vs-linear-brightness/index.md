---
title: Perceived vs. Linear Brightness
description: Understanding — explain why gamma correction is needed.
status: scaffold
library: Chart.js
bloom_level: TBD
---

# Perceived vs. Linear Brightness



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 7: Color Theory — The RGB Color Model and Color Mixing](../../chapters/07-rgb-color-theory/index.md).

```text
Type: chart
**sim-id:** perceived-vs-linear-brightness
**Library:** Chart.js
**Status:** Specified

A line chart with two curves on the same axes. X-axis: "Linear LED value (0–255)". Y-axis: "Perceived brightness (0–100%)". Curve 1 labeled "Linear (what the LED does)": a straight diagonal line from (0,0) to (255,100). Curve 2 labeled "Perceived (what your eye sees)": a concave curve that rises quickly at low values and slowly at high values, approximating a power function with gamma ~2.2. On hover, tooltips show: "LED value: X → Perceived brightness: Y%". A slider below lets users drag and see a dot move along both curves simultaneously, highlighting the gap between them. Canvas: 700 × 350 px. Responds to window resize.

Learning objective: Understanding — explain why gamma correction is needed.
```

## Related Resources

- [Chapter 7: Color Theory — The RGB Color Model and Color Mixing](../../chapters/07-rgb-color-theory/index.md)
