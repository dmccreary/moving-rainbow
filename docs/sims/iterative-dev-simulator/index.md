---
title: Iterative Development Simulator
description: Students will *apply* (Bloom's Level 3) the iterative development process by constructing a working LED animation through four small, independently testable stages.
status: scaffold
library: p5.js
bloom_level: TBD
---

# Iterative Development Simulator



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 1: Introduction and Computational Thinking Foundations](../../chapters/01-intro-and-computational-thinking/index.md).

```text
Type: MicroSim
**sim-id:** iterative-dev-simulator<br/>
**Library:** p5.js<br/>
**Status:** Specified

**Learning Objective:** Students will *apply* (Bloom's Level 3) the iterative development process by constructing a working LED animation through four small, independently testable stages.

**Description:** A p5.js canvas showing a row of 10 simulated LED circles on a dark background. A step panel on the right guides the student through four build stages. Each stage adds exactly one new feature and produces visible, verifiable output.

**Canvas:** 760 × 380 px, responsive (responds to window resize events via `updateCanvasSize()` called first in `setup()`). Canvas parented to `document.querySelector('main')`.

**Step Panel (right side, ~240 px wide):**
- Title: "Build It Step by Step"
- Numbered list showing all four steps. Current active step highlighted with teal (#41BAC1) background.
- `createButton("Apply Next Step")` — advances to the next step and updates the LED display and status message.
- `createButton("Reset")` — returns to the initial state (all LEDs off, Step 1 highlighted).

**Steps:**

1. **Step 1 – One Pixel On:** LED at index 0 lights up red `(255, 0, 0)`. All others remain dark.
   Status message: "One pixel on! We can control a single LED."

2. **Step 2 – All Pixels One Color:** All 10 LEDs light up red.
   Status message: "All 10 pixels on! We extended the same idea to the whole strip."

3. **Step 3 – Rainbow Spread:** Each LED gets a unique hue: `hue = (i / 10.0) * 360`, converted to RGB.
   Status message: "Each pixel has its own hue — that's a rainbow!"

4. **Step 4 – Animate:** The rainbow scrolls using `offset`, incrementing by 1 each `draw()` frame. Pixel hue: `hue = ((i + offset) / 10.0) * 360 % 360`.
   Status message: "It's moving! A full animation built in four tested steps."

**Edge Case Panel (visible only after Step 4 is applied):**
- Section header: "Try some edge cases:"
- `createSlider("Pixels", 1, 30, 10, 1)` — adjusts the number of active LED circles. Extremes labeled "1 (edge)" and "30 (edge)". At 1 pixel, show the single-pixel animation so students see the degenerate case.
- `createSlider("Speed", 1, 20, 4, 1)` — controls offset increment per frame. At value 20, the animation jumps too fast to look smooth (intentional edge case demonstration).
- Text note below sliders: "Extreme values are called edge cases. Testing them now beats discovering them at the demo."

Implementation: p5.js, vanilla JavaScript. HSV-to-RGB conversion inline (no external library). All controls created with p5.js built-in `createButton` and `createSlider`. Canvas parented to `document.querySelector('main')`.
```

## Related Resources

- [Chapter 1: Introduction and Computational Thinking Foundations](../../chapters/01-intro-and-computational-thinking/index.md)
