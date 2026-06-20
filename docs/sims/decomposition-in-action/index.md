---
title: Decomposition in Action
description: Students will understand (Bloom's Level 2) how a complex LED animation can be decomposed into discrete, independently solvable sub-problems.
image: /sims/decomposition-in-action/decomposition-in-action.png
og:image: /sims/decomposition-in-action/decomposition-in-action.png
twitter:image: /sims/decomposition-in-action/decomposition-in-action.png
social:
   cards: false
library: p5.js
status: implemented
---

# Decomposition in Action

<iframe src="main.html" width="100%" height="422px" scrolling="no"></iframe>

[Run the Decomposition in Action MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

An interactive p5.js simulation showing a 30-LED strip playing a moving rainbow animation. The canvas is divided into two panels: a left panel showing the full running animation, and a right panel showing a labeled decomposition tree that reveals sub-problems one level at a time.

**Learning objective:** Students will understand (Bloom's Level 2) how a complex LED animation can be decomposed into discrete, independently solvable sub-problems.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/decomposition-in-action/main.html"
        height="422px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Students will understand (Bloom's Level 2) how a complex LED animation can be decomposed into discrete, independently solvable sub-problems.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 1](../../chapters/01-intro-and-computational-thinking/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 1: Introduction and Computational Thinking Foundations](../../chapters/01-intro-and-computational-thinking/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

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

</details>
