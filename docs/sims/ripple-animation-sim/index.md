---
title: Ripple Animation Mechanics
description: Analyzing - the student can explain how phase and distance combine to produce the ripple pattern.
image: /sims/ripple-animation-sim/ripple-animation-sim.png
og:image: /sims/ripple-animation-sim/ripple-animation-sim.png
twitter:image: /sims/ripple-animation-sim/ripple-animation-sim.png
social:
   cards: false
library: p5.js
status: implemented
---

# Ripple Animation Mechanics

<iframe src="main.html" width="100%" height="312px" scrolling="no"></iframe>

[Run the Ripple Animation Mechanics MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A p5.js MicroSim showing a horizontal row of 20 pixel circles. A center pixel is marked with a small dot.

**Learning objective:** Analyzing - the student can explain how phase and distance combine to produce the ripple pattern.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/ripple-animation-sim/main.html"
        height="312px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Analyzing - the student can explain how phase and distance combine to produce the ripple pattern.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 13](../../chapters/13-intermediate-animations/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 13: Intermediate Animation Techniques](../../chapters/13-intermediate-animations/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: interactive-infographic
**sim-id:** ripple-animation-sim
**Library:** p5.js
**Status:** Specified

A p5.js MicroSim showing a horizontal row of 20 pixel circles. A center pixel is marked with a small dot. A **Pulse** button triggers a ripple — a brightness wave that expands from the center outward. As the wave passes each pixel, that pixel brightens then dims. The wave reaches the strip edges and disappears. Controls: a **Decay** slider (0.2–0.9) showing how quickly the ripple fades with distance; a **Speed** slider (slow/fast); a **Loop** checkbox for continuous pulsing. A live formula display shows the current brightness for the highlighted pixel based on `cos((distance - phase) * decay_rate)`. Canvas: 700 × 280 px. Responds to window resize.

Learning objective: Analyzing — the student can explain how phase and distance combine to produce the ripple pattern.
```

</details>
