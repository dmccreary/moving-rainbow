---
title: HSV Color Space Explorer
description: Understanding — the student can predict how changing H, S, or V affects the output color.
status: scaffold
library: p5.js
bloom_level: TBD
---

# HSV Color Space Explorer



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 10: Advanced Color Theory — HSV, Gamma Correction, and Color Palettes](../../chapters/10-advanced-color-theory/index.md).

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

## Related Resources

- [Chapter 10: Advanced Color Theory — HSV, Gamma Correction, and Color Palettes](../../chapters/10-advanced-color-theory/index.md)
