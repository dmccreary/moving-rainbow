---
title: Code Indentation Explorer
description: Students identify which lines of a Python snippet are correctly indented, which have errors, and explain what block each line belongs to.
image: /sims/code-indentation-explorer/code-indentation-explorer.png
og:image: /sims/code-indentation-explorer/code-indentation-explorer.png
twitter:image: /sims/code-indentation-explorer/code-indentation-explorer.png
social:
   cards: false
library: p5.js
status: implemented
---

# Code Indentation Explorer

<iframe src="main.html" width="100%" height="442px" scrolling="no"></iframe>

[Run the Code Indentation Explorer MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

Students identify which lines of a Python snippet are correctly indented, which have errors, and explain what block each line belongs to.

**Learning objective:** Students identify which lines of a Python snippet are correctly indented, which have errors, and explain what block each line belongs to.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/code-indentation-explorer/main.html"
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
Students identify which lines of a Python snippet are correctly indented, which have errors, and explain what block each line belongs to.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 2](../../chapters/02-python-variables-types-operators/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 2: Python Basics — Variables, Data Types, and Operators](../../chapters/02-python-variables-types-operators/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: microsim
**sim-id:** code-indentation-explorer<br/>
**Library:** p5.js<br/>
**Status:** Specified

Bloom Level: Understand (L2)
Bloom Verb: identify, interpret
Learning Objective: Students identify which lines of a Python snippet are correctly indented, which have errors, and explain what block each line belongs to.

Instructional Rationale: Identify/interpret (L2 Understand) calls for a classify-and-explain pattern. The student clicks a line to see its block membership highlighted, then clicks "Check Indentation" to receive color-coded feedback on all lines simultaneously. Immediate feedback on individual lines before the whole-snippet check builds understanding step by step.

Canvas layout:
- Left panel (60%): A Python code snippet displayed in monospace font on a dark background (Thonny-like). Each line is a clickable row. Line numbers shown on the left margin.
- Right panel (40%): Feedback area showing:
  - Block membership for the last clicked line: "This line is at indentation level 1 — inside the `if` block"
  - After "Check Indentation": color-coded verdict for every line

Visual elements:
- Code font: monospace, 14px, white on dark gray background
- Block-level bracket overlays on left: vertical colored lines connecting lines that belong to the same block (level 0 = white, level 1 = blue, level 2 = orange)
- Line highlights: green border = correct indentation, red border = error
- Feedback panel: white background, plain text, 13px

Code examples (cycle with "Next Example" button, 4 examples total):

Example 1 (correct — single if block):
```
is_on = True
if is_on:
    print("LED is on")
    print("Glowing!")
print("Outside the if block")
```

Example 2 (error — missing indentation):
```
brightness = 100
if brightness > 50:
print("Bright!")
```
Error on line 3: should be indented 4 spaces.

Example 3 (correct — nested blocks):
```
for i in range(30):
    if i % 2 == 0:
        print("Even pixel:", i)
    print("Pixel:", i)
```

Example 4 (error — inconsistent indentation):
```
for i in range(5):
    print(i)
      print("extra spaces")
```
Error on line 3: 6 spaces instead of 4.

Interactive features:
- Click any line → highlight that line, show block membership in right panel
- "Check Indentation" button → color all lines green/red and show error explanations for bad lines
- "Show Fix" button → reveal the corrected version side by side with the original
- "Next Example" button → advance to the next code snippet

Responsive design: Panel layout is side-by-side on wide screens, stacks vertically on narrow screens. Font size scales down on narrow screens to keep line content visible.
```

</details>
