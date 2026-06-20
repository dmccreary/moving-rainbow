---
title: Pixel Indexing on a NeoPixel Strip
description: Applying — the student can predict which physical pixel will light up given an index in code.
status: scaffold
library: p5.js
bloom_level: TBD
---

# Pixel Indexing on a NeoPixel Strip



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 9: NeoPixel Programming — Pixels, Colors, and the NeoPixel Library](../../chapters/09-neopixel-programming/index.md).

```text
Type: interactive-infographic
**sim-id:** pixel-indexing-explorer
**Library:** p5.js
**Status:** Specified

A row of 10 colored LED circles representing pixels 0–9 on a strip. Each circle has its index number displayed below it. A text input field lets the user type an index (0–9) and a color (as a preset from a dropdown: red, green, blue, white, yellow, off). Clicking "Set Pixel" colors that circle and shows the Python code that would produce that effect: `strip[3] = (0, 255, 0)`. A "Clear All" button resets all circles to off. A "Write" button (highlighted) sends the colors (animates a signal wave moving from pixel 0 to pixel 9). Canvas: 700 × 280 px. Responds to window resize.

Learning objective: Applying — the student can predict which physical pixel will light up given an index in code.
```

## Related Resources

- [Chapter 9: NeoPixel Programming — Pixels, Colors, and the NeoPixel Library](../../chapters/09-neopixel-programming/index.md)
