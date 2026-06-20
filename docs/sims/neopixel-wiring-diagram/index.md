---
title: NeoPixel Wiring Diagram
description: Applying — the student can wire a NeoPixel strip from a diagram.
status: scaffold
library: p5.js
bloom_level: TBD
---

# NeoPixel Wiring Diagram



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 8: NeoPixel LED Hardware — WS2812B, Wiring, and Form Factors](../../chapters/08-neopixel-led-hardware/index.md).

```text
Type: interactive-infographic
**sim-id:** neopixel-wiring-diagram
**Library:** p5.js
**Status:** Specified

An interactive wiring diagram showing a Raspberry Pi Pico on the left and a 10-pixel NeoPixel strip on the right. Three colored wires connect them:
- Red wire from VSYS (Pico) to +5V (strip)
- Black wire from GND (Pico) to GND (strip)
- Green wire from GP0 (Pico) to DIN/DATA (strip)

Each wire is clickable: clicking opens a tooltip explaining "What this wire does" and "What happens if you forget this wire." An arrow on the strip shows the data direction. A small inset shows the WS2812B chip inside one pixel with labels: "RGB LEDs", "Control IC", "DIN", "DOUT". Hovering over a pixel on the strip shows its index number (0, 1, 2...). Canvas: 700 × 400 px. Responds to window resize.

Learning objective: Applying — the student can wire a NeoPixel strip from a diagram.
```

## Related Resources

- [Chapter 8: NeoPixel LED Hardware — WS2812B, Wiring, and Form Factors](../../chapters/08-neopixel-led-hardware/index.md)
