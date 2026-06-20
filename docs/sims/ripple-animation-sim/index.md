---
title: Ripple Animation Mechanics
description: Analyzing — the student can explain how phase and distance combine to produce the ripple pattern.
status: scaffold
library: p5.js
bloom_level: TBD
---

# Ripple Animation Mechanics



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 13: Intermediate Animation Techniques](../../chapters/13-intermediate-animations/index.md).

```text
Type: interactive-infographic
**sim-id:** ripple-animation-sim
**Library:** p5.js
**Status:** Specified

A p5.js MicroSim showing a horizontal row of 20 pixel circles. A center pixel is marked with a small dot. A **Pulse** button triggers a ripple — a brightness wave that expands from the center outward. As the wave passes each pixel, that pixel brightens then dims. The wave reaches the strip edges and disappears. Controls: a **Decay** slider (0.2–0.9) showing how quickly the ripple fades with distance; a **Speed** slider (slow/fast); a **Loop** checkbox for continuous pulsing. A live formula display shows the current brightness for the highlighted pixel based on `cos((distance - phase) * decay_rate)`. Canvas: 700 × 280 px. Responds to window resize.

Learning objective: Analyzing — the student can explain how phase and distance combine to produce the ripple pattern.
```

## Related Resources

- [Chapter 13: Intermediate Animation Techniques](../../chapters/13-intermediate-animations/index.md)
