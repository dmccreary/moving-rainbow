---
title: Animation Pattern Comparison
description: Analyzing - the student can visually match a running LED pattern to its name and algorithm.
image: /sims/animation-pattern-comparison/animation-pattern-comparison.png
og:image: /sims/animation-pattern-comparison/animation-pattern-comparison.png
twitter:image: /sims/animation-pattern-comparison/animation-pattern-comparison.png
social:
   cards: false
library: p5.js
status: implemented
---

# Animation Pattern Comparison

<iframe src="main.html" width="100%" height="502px" scrolling="no"></iframe>

[Run the Animation Pattern Comparison MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

Six rows of small LED strip simulations (10 pixels each), each labeled with its pattern name:

**Learning objective:** Analyzing - the student can visually match a running LED pattern to its name and algorithm.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/animation-pattern-comparison/main.html"
        height="502px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Analyzing - the student can visually match a running LED pattern to its name and algorithm.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 12](../../chapters/12-basic-animation-patterns/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 12: Basic LED Animation Patterns](../../chapters/12-basic-animation-patterns/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

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

</details>
