---
title: Example Circuit Connection Diagram for Bike Light Project
description: Applying - the student can trace any signal path from source to destination and identify which pin it uses.
image: /sims/bike-light-circuit-diagram/bike-light-circuit-diagram.png
og:image: /sims/bike-light-circuit-diagram/bike-light-circuit-diagram.png
twitter:image: /sims/bike-light-circuit-diagram/bike-light-circuit-diagram.png
social:
   cards: false
library: p5.js
status: implemented
---

# Example Circuit Connection Diagram for Bike Light Project

<iframe src="main.html" width="100%" height="422px" scrolling="no"></iframe>

[Run the Example Circuit Connection Diagram for Bike Light Project MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A p5.js interactive wiring diagram showing:

**Learning objective:** Applying - the student can trace any signal path from source to destination and identify which pin it uses.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/bike-light-circuit-diagram/main.html"
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
Applying - the student can trace any signal path from source to destination and identify which pin it uses.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 20](../../chapters/20-project-design-and-capstone/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 20: Project Design, Capstone Projects, and Presentation](../../chapters/20-project-design-and-capstone/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: diagram
**sim-id:** bike-light-circuit-diagram
**Library:** p5.js
**Status:** Specified

A p5.js interactive wiring diagram showing:

**Components:**
- Raspberry Pi Pico (center, with all GPIO pins labeled on both sides)
- WS2812B LED strip (right side, 8 pixels shown as a row)
- Momentary button (left side, on breadboard)
- USB power bank (top right, labeled "5V source")

**Connections drawn as colored wires:**
- Red: USB power bank 5V → Pico VBUS pin → LED strip 5V pin
- Black: USB power bank GND → Pico GND → LED strip GND
- Yellow: Pico GP0 → LED strip Data In (with a note: "330Ω resistor in-line recommended")
- Green: Pico GP15 → Button one leg
- Black: Button other leg → GND

Clicking any component opens a tooltip explaining its role. Clicking any wire highlights its full path and shows voltage/signal name.

Canvas: 700 × 420 px. Responds to window resize.

Learning objective: Applying — the student can trace any signal path from source to destination and identify which pin it uses.
```

</details>
