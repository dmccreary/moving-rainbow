---
title: Animation Pattern Comparison
description: Analyzing — the student can visually match a running LED pattern to its name and algorithm.
status: scaffold
library: p5.js
bloom_level: TBD
---

# Animation Pattern Comparison



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 12: Basic LED Animation Patterns](../../chapters/12-basic-animation-patterns/index.md).

```text
Type: interactive-infographic
**sim-id:** animation-pattern-comparison
**Library:** p5.js
**Status:** Specified

Six rows of small LED strip simulations (10 pixels each), each labeled with its pattern name:
1. Blink — alternates all-on / all-off every 500 ms
2. Rainbow Static — shows fixed rainbow
3. Moving Rainbow — rainbow scrolls left at adjustable speed
4. Twinkle — random pixels flash bright on a dark background
5. Candle Flicker — warm colors randomly varying brightness
6. Random Colors — all pixels flash random colors each frame

A global **Play/Pause** button runs or pauses all six simultaneously. A **Speed** slider (slow/medium/fast) adjusts all animation speeds together. Each row has a label and a brief description on the right. Canvas: 700 × 500 px. Responds to window resize.

Learning objective: Analyzing — the student can visually match a running LED pattern to its name and algorithm.
```

## Related Resources

- [Chapter 12: Basic LED Animation Patterns](../../chapters/12-basic-animation-patterns/index.md)
