---
title: Transistor Driver and Dimmer Circuit
description: Applying - the student can trace current flow through a transistor driver circuit and predict the LED brightness given a duty cycle.
image: /sims/transistor-circuit-diagrams/transistor-circuit-diagrams.png
og:image: /sims/transistor-circuit-diagrams/transistor-circuit-diagrams.png
twitter:image: /sims/transistor-circuit-diagrams/transistor-circuit-diagrams.png
social:
   cards: false
library: p5.js
status: implemented
---

# Transistor Driver and Dimmer Circuit

<iframe src="main.html" width="100%" height="402px" scrolling="no"></iframe>

[Run the Transistor Driver and Dimmer Circuit MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A p5.js circuit diagram with two side-by-side panels, selectable via tabs:

**Learning objective:** Applying - the student can trace current flow through a transistor driver circuit and predict the LED brightness given a duty cycle.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/transistor-circuit-diagrams/main.html"
        height="402px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Applying - the student can trace current flow through a transistor driver circuit and predict the LED brightness given a duty cycle.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 16](../../chapters/16-circuit-assembly/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 16: Circuit Assembly — Resistors, Transistors, and Circuit Types](../../chapters/16-circuit-assembly/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

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

</details>
