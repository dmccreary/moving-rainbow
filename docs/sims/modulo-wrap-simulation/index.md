---
title: Modulo Wrap-Around Animation
description: Understanding — the student can explain why modulo creates wrap-around behavior.
status: scaffold
library: p5.js
bloom_level: TBD
---

# Modulo Wrap-Around Animation



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 11: Mathematics for LED Programming](../../chapters/11-math-for-led-programming/index.md).

```text
Type: interactive-infographic
**sim-id:** modulo-wrap-simulation
**Library:** p5.js
**Status:** Specified

A row of 10 pixel circles representing a NeoPixel strip. A "position" counter is shown above. Controls: a **Step** button advances `pos` by 1, a **Auto** toggle runs it continuously at 5 steps/second. As `pos` increments, the current pixel lights red and the previous one turns off. When `pos` reaches 10 (end of strip), the next step shows the modulo calculation: `10 % 10 = 0` in an overlay, and the first pixel lights up again. Below the strip, the formula `pos = (pos + 1) % 10` is displayed with current values substituted in. Canvas: 700 × 300 px. Responds to window resize.

Learning objective: Understanding — the student can explain why modulo creates wrap-around behavior.
```

## Related Resources

- [Chapter 11: Mathematics for LED Programming](../../chapters/11-math-for-led-programming/index.md)
