---
title: Transistor Driver and Dimmer Circuit
description: Applying — the student can trace current flow through a transistor driver circuit and predict the LED brightness given a duty cycle.
status: scaffold
library: p5.js
bloom_level: TBD
---

# Transistor Driver and Dimmer Circuit



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 16: Circuit Assembly — Resistors, Transistors, and Circuit Types](../../chapters/16-circuit-assembly/index.md).

```text
Type: interactive-infographic
**sim-id:** transistor-circuit-diagrams
**Library:** p5.js
**Status:** Specified

A p5.js circuit diagram with two side-by-side panels, selectable via tabs:

**Tab 1 — Transistor Switch:** Shows a 2N2222 transistor schematic with labeled Base, Collector, Emitter. Connections shown: GP0 → 1kΩ resistor → Base; Collector → 220Ω resistor → LED → +5V; Emitter → GND. A toggle button labeled "GP0 HIGH / LOW" animates current flow (glowing arrows) and lights/dims the LED symbol. Clicking each component shows a tooltip: "1kΩ limits base current to ~2 mA", "220Ω limits LED current to ~14 mA", etc.

**Tab 2 — PWM Dimmer:** Same circuit but the toggle becomes a PWM duty cycle slider (0–100%). As the slider moves, the LED symbol changes brightness proportionally. Canvas: 700 × 400 px. Responds to window resize.

Learning objective: Applying — the student can trace current flow through a transistor driver circuit and predict the LED brightness given a duty cycle.
```

## Related Resources

- [Chapter 16: Circuit Assembly — Resistors, Transistors, and Circuit Types](../../chapters/16-circuit-assembly/index.md)
