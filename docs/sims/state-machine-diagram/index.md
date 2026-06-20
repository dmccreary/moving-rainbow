---
title: State Machine for a 3-Mode LED Controller
description: Understanding - the student can trace a state machine through a sequence of transitions given a series of inputs.
image: /sims/state-machine-diagram/state-machine-diagram.png
og:image: /sims/state-machine-diagram/state-machine-diagram.png
twitter:image: /sims/state-machine-diagram/state-machine-diagram.png
social:
   cards: false
library: Mermaid
status: implemented
---

# State Machine for a 3-Mode LED Controller

<iframe src="main.html" width="100%" height="442px" scrolling="no"></iframe>

[Run the State Machine for a 3-Mode LED Controller MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A Mermaid state diagram with three states: "Mode 0: Red", "Mode 1: Green", "Mode 2: Blue". Directed arrows between each state labeled "button pressed".

**Learning objective:** Understanding - the student can trace a state machine through a sequence of transitions given a series of inputs.

## How to Use

Click any box or node in the diagram to read what it does. The explanation appears in the panel just below the diagram. Where an **Animate** button is present, press it to step through the sequence.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/state-machine-diagram/main.html"
        height="442px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Understanding - the student can trace a state machine through a sequence of transitions given a series of inputs.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 18](../../chapters/18-input-devices-and-sensors/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 18: Input Devices, Sensors, and State Machines](../../chapters/18-input-devices-and-sensors/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: diagram
**sim-id:** state-machine-diagram
**Library:** Mermaid
**Status:** Specified

A Mermaid state diagram with three states: "Mode 0: Red", "Mode 1: Green", "Mode 2: Blue". Directed arrows between each state labeled "button pressed". Mode 0 → Mode 1 → Mode 2 → Mode 0 (full cycle). Each state node is clickable: clicking opens a tooltip showing what the LED animation does in that mode. The current active state is highlighted in a different color. An "Animate" button cycles through states one step at a time. Arrow labels show the transition condition: "button pressed (debounced)".

Canvas: 700 × 380 px. Responds to window resize.

Learning objective: Understanding — the student can trace a state machine through a sequence of transitions given a series of inputs.
```

</details>
