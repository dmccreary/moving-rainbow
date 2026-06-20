---
title: How a for Loop Iterates Over a List
description: Remembering - the student can recall that a for loop assigns each list item to the loop variable in order.
image: /sims/for-loop-list-iteration/for-loop-list-iteration.png
og:image: /sims/for-loop-list-iteration/for-loop-list-iteration.png
twitter:image: /sims/for-loop-list-iteration/for-loop-list-iteration.png
social:
   cards: false
library: p5.js
status: implemented
---

# How a for Loop Iterates Over a List

<iframe src="main.html" width="100%" height="282px" scrolling="no"></iframe>

[Run the How a for Loop Iterates Over a List MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A p5.js MicroSim showing a list of three colored boxes labeled (255,0,0), (0,255,0), (0,0,255). A "loop cursor" arrow moves from box to box as the user clicks a Next Step button.

**Learning objective:** Remembering - the student can recall that a for loop assigns each list item to the loop variable in order.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/for-loop-list-iteration/main.html"
        height="282px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Remembering - the student can recall that a for loop assigns each list item to the loop variable in order.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 4](../../chapters/04-python-control-flow-loops/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 4: Python Control Flow, Loops, and Error Handling](../../chapters/04-python-control-flow-loops/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: interactive-infographic
**sim-id:** for-loop-list-iteration
**Library:** p5.js
**Status:** Specified

A p5.js MicroSim showing a list of three colored boxes labeled `(255,0,0)`, `(0,255,0)`, `(0,0,255)`. A "loop cursor" arrow moves from box to box as the user clicks a **Next Step** button. Each step highlights the current item, shows the value of the loop variable `color`, and displays the iteration number (Iteration 1 of 3, etc.). A **Reset** button returns the arrow to the start. A label below reads: "The for loop gives `color` a new value each time." Canvas: 600 × 280 px. Responds to window resize.

Learning objective: Remembering — the student can recall that a for loop assigns each list item to the loop variable in order.
```

</details>
