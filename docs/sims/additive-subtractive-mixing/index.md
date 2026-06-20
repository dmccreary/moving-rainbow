---
title: Additive vs. Subtractive Color Mixing
description: Understanding — explain why light mixing and paint mixing produce different results.
status: scaffold
library: p5.js
bloom_level: TBD
---

# Additive vs. Subtractive Color Mixing



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 7: Color Theory — The RGB Color Model and Color Mixing](../../chapters/07-rgb-color-theory/index.md).

```text
Type: interactive-infographic
**sim-id:** additive-subtractive-mixing
**Library:** p5.js
**Status:** Specified

Two side-by-side panels. Left panel labeled "Additive (Light — LEDs)": three overlapping circles in red, green, and blue on a black background. Where red and green overlap: yellow. Where green and blue overlap: cyan. Where red and blue overlap: magenta. Where all three overlap: white. Right panel labeled "Subtractive (Paint — Pigments)": three overlapping circles in red (magenta-red), blue (cyan-blue), and yellow on a white background. Where they overlap, colors darken toward brown/gray/black. Hovering over any overlap region shows a tooltip: "Red + Green light = Yellow" or "Red + Blue paint = Purple-brown". A toggle button switches between "Light Mode" and "Paint Mode" to emphasize the difference. Canvas: 700 × 350 px. Responds to window resize.

Learning objective: Understanding — explain why light mixing and paint mixing produce different results.
```

## Related Resources

- [Chapter 7: Color Theory — The RGB Color Model and Color Mixing](../../chapters/07-rgb-color-theory/index.md)
