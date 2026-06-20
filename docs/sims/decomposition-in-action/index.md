---
title: Decomposition in Action
description: Students will *understand* (Bloom's Level 2) how a complex LED animation can be decomposed into discrete, independently solvable sub-problems.
status: scaffold
library: p5.js
bloom_level: TBD
---

# Decomposition in Action



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 1: Introduction and Computational Thinking Foundations](../../chapters/01-intro-and-computational-thinking/index.md).

```text
Type: MicroSim
**sim-id:** decomposition-in-action<br/>
**Library:** p5.js<br/>
**Status:** Specified

**Learning Objective:** Students will *understand* (Bloom's Level 2) how a complex LED animation can be decomposed into discrete, independently solvable sub-problems.

**Description:** An interactive p5.js simulation showing a 30-LED strip playing a moving rainbow animation. The canvas is divided into two panels: a left panel showing the full running animation, and a right panel showing a labeled decomposition tree that reveals sub-problems one level at a time.

**Canvas:** 760 × 420 px, responsive (responds to window resize events via `updateCanvasSize()` called first in `setup()`).

**Controls (p5.js built-in):**
- `createButton("Decompose")` — when clicked, animates the right panel to reveal the next level of the decomposition tree (4 levels total, one click per level).
- `createButton("Reset")` — collapses the tree back to the root node only.
- `createCheckbox("Animate", true)` — pauses or resumes the left-panel LED animation.

**Decomposition tree structure (right panel):**
- Root (always visible): "Moving Rainbow Animation" (purple node, #642580)
  - Level 1 (click 1): "Set pixel colors", "Shift by 1 each frame", "Loop forever"
  - Level 2 under "Set pixel colors" (click 2): "Hue = position + offset", "Convert hue → RGB"
  - Level 2 under "Shift by 1 each frame" (click 3): "offset += 1 each frame", "Use % to wrap around"

**Interactions:** Every node in the decomposition tree is clickable. Clicking a node opens a one-sentence tooltip on the canvas explaining what that sub-problem is about. A second click on the same node closes the tooltip.

**Visual design:**
- Left panel: dark (#111) background, glowing HSV-rainbow LED circles (30 circles, radius 10px each, soft glow drawn with decreasing-alpha circles).
- Right panel: light grey (#f0f0f0) background, rounded-rectangle nodes connected by thin dark lines.
- Node colors: root = purple (#642580), Level 1 = teal (#41BAC1), Level 2 = orange (#E8903A).
- White text inside all nodes.

Implementation: p5.js, vanilla JavaScript. HSV-to-RGB conversion defined inline. All controls created with p5.js built-in functions. Canvas parented to `document.querySelector('main')`.
```

## Related Resources

- [Chapter 1: Introduction and Computational Thinking Foundations](../../chapters/01-intro-and-computational-thinking/index.md)
