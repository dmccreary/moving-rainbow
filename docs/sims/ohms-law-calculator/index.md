---
title: Ohm's Law Calculator
description: Applying - the student can solve Ohm's Law problems for any unknown variable.
image: /sims/ohms-law-calculator/ohms-law-calculator.png
og:image: /sims/ohms-law-calculator/ohms-law-calculator.png
twitter:image: /sims/ohms-law-calculator/ohms-law-calculator.png
social:
   cards: false
library: p5.js
status: implemented
---

# Ohm's Law Calculator

<iframe src="main.html" width="100%" height="362px" scrolling="no"></iframe>

[Run the Ohm's Law Calculator MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

An interactive Ohm's Law triangle with three circles labeled V (volts), I (current), R (resistance). Two inputs are active at a time; the third is calculated.

**Learning objective:** Applying - the student can solve Ohm's Law problems for any unknown variable.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/ohms-law-calculator/main.html"
        height="362px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Applying - the student can solve Ohm's Law problems for any unknown variable.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 15](../../chapters/15-electronics-fundamentals/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 15: Electronics Fundamentals — Resistance, Ohm's Law, and Components](../../chapters/15-electronics-fundamentals/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: interactive-infographic
**sim-id:** ohms-law-calculator
**Library:** p5.js
**Status:** Specified

An interactive Ohm's Law triangle with three circles labeled V (volts), I (current), R (resistance). Two inputs are active at a time; the third is calculated. A dropdown lets the user choose which value to solve for. Numeric input fields accept values. Below the triangle, the formula is displayed with the current values substituted: e.g., "I = V ÷ R = 5 ÷ 220 = 0.023 A = 23 mA". A second section shows the power formula: "P = V × I = 5 × 0.023 = 0.115 W". Clicking any circle highlights the formula. Canvas: 700 × 350 px. Responds to window resize.

Learning objective: Applying — the student can solve Ohm's Law problems for any unknown variable.
```

</details>
