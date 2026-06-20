---
title: Problem-Solving Steps Flowchart
description: Students will understand (Bloom's Level 2) the five-step problem-solving framework and be able to sequence the steps correctly.
image: /sims/problem-solving-steps/problem-solving-steps.png
og:image: /sims/problem-solving-steps/problem-solving-steps.png
twitter:image: /sims/problem-solving-steps/problem-solving-steps.png
social:
   cards: false
library: Mermaid
status: implemented
---

# Problem-Solving Steps Flowchart

<iframe src="main.html" width="100%" height="782px" scrolling="no"></iframe>

[Run the Problem-Solving Steps Flowchart MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A vertical Mermaid flowchart (top-down direction) showing five problem-solving steps used by programmers. Every node has a click directive that calls a JavaScript function to update a <div id="step-info"> element below the diagram with a one-sentence definition and a one-sentence LED-specific example.

**Learning objective:** Students will understand (Bloom's Level 2) the five-step problem-solving framework and be able to sequence the steps correctly.

## How to Use

Click any box or node in the diagram to read what it does. The explanation appears in the panel just below the diagram. Where an **Animate** button is present, press it to step through the sequence.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/problem-solving-steps/main.html"
        height="782px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Students will understand (Bloom's Level 2) the five-step problem-solving framework and be able to sequence the steps correctly.

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
Type: Diagram
**sim-id:** problem-solving-steps<br/>
**Library:** Mermaid<br/>
**Status:** Specified

**Learning Objective:** Students will *understand* (Bloom's Level 2) the five-step problem-solving framework and be able to sequence the steps correctly.

**Description:** A vertical Mermaid flowchart (top-down direction) showing five problem-solving steps used by programmers. Every node has a `click` directive that calls a JavaScript function to update a `<div id="step-info">` element below the diagram with a one-sentence definition and a one-sentence LED-specific example. Default div text: "Click any step to learn more."

**Nodes and click content:**

- **step1** — "Understand the Problem" (stadium shape)
  Click: "Restate the problem in your own words before touching code. *LED example: 'I need 30 LEDs to display a rainbow that scrolls right, one pixel per frame.'*"

- **step2** — "Plan Your Solution" (rectangle)
  Click: "Write pseudocode or draw a flowchart before opening your editor. *LED example: Pseudocode listing how to calculate each pixel's color from its position.*"

- **step3** — "Write the Code" (rectangle)
  Click: "Translate your plan into Python one small, testable piece at a time. *LED example: Write just the loop that assigns a hue to each pixel index.*"

- **step4** — "Test and Debug" (diamond shape, question text: "Does it work?")
  Click: "Run the program and compare actual output to expected output. *LED example: The rainbow scrolls backward — trace the offset increment sign.*"

- **step5** — "Reflect and Improve" (stadium shape)
  Click: "Ask: is the code readable? Can it be reused? What would you change? *LED example: Extract the hue formula into a named function for Chapter 9.*"

**Arrows:**
- step1 → step2 → step3 → step4 (main flow)
- step4 → step3 (labeled "bug found", loops back)
- step4 → step5 (labeled "it works!")
- step5 → step1 (labeled "new challenge")

**Info box:** A `<div id="step-info">` below the Mermaid `<div>`, styled with a light-purple background, rounded corners, and 1em padding. Updated by `showStepInfo(id)` JavaScript function triggered by Mermaid `click` directives.

**Visual style:** Node fill: purple (#642580), white text. Arrow labels styled in teal (#41BAC1). Direction: `flowchart TD`.

Implementation: Mermaid 10.x `<div class="mermaid">` block. Companion `<script>` block defines `window.showStepInfo(id)` as a global function mapping node ids to content strings, and sets the innerHTML of `#step-info`. The Mermaid `click` directive uses: `click step1 showStepInfo "step1"`.
```

</details>
