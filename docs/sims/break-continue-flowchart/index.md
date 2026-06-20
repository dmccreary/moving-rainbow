---
title: break vs. continue Flow
description: 
image: /sims/break-continue-flowchart/break-continue-flowchart.png
og:image: /sims/break-continue-flowchart/break-continue-flowchart.png
twitter:image: /sims/break-continue-flowchart/break-continue-flowchart.png
social:
   cards: false
library: Mermaid
status: implemented
---

# break vs. continue Flow

<iframe src="main.html" width="100%" height="1012px" scrolling="no"></iframe>

[Run the break vs. continue Flow MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A Mermaid flowchart showing a for loop cycle. Nodes: "Start Loop" to "i in range?" to yes to "Check condition" to "break?" to yes to "Exit loop"; no to "continue?" to yes to "Back to top" (arrow goes back to "i in range?" node); no to "Run loop body" to "Back to top".

**Learning objective:** 

## How to Use

Click any box or node in the diagram to read what it does. The explanation appears in the panel just below the diagram. Where an **Animate** button is present, press it to step through the sequence.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/break-continue-flowchart/main.html"
        height="1012px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective


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
Type: diagram
**sim-id:** break-continue-flowchart
**Library:** Mermaid
**Status:** Specified

A Mermaid flowchart showing a `for` loop cycle. Nodes: "Start Loop" → "i in range?" → yes → "Check condition" → "break?" → yes → "Exit loop"; no → "continue?" → yes → "Back to top" (arrow goes back to "i in range?" node); no → "Run loop body" → "Back to top". Each node is clickable: clicking "break?" shows a tooltip "break exits the loop entirely"; clicking "continue?" shows "continue skips to the next iteration"; clicking "Run loop body" shows "This is where your animation code goes." Color-code: break path in red, continue path in orange, normal path in green.
```

</details>
