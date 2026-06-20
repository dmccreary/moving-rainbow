---
title: Python Data Type Explorer
description: Students classify Python values by data type - given a displayed value, they select its type from six options and receive feedback that connects the type t
image: /sims/python-data-type-explorer/python-data-type-explorer.png
og:image: /sims/python-data-type-explorer/python-data-type-explorer.png
twitter:image: /sims/python-data-type-explorer/python-data-type-explorer.png
social:
   cards: false
library: p5.js
status: implemented
---

# Python Data Type Explorer

<iframe src="main.html" width="100%" height="422px" scrolling="no"></iframe>

[Run the Python Data Type Explorer MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

Students classify Python values by data type - given a displayed value, they select its type from six options and receive feedback that connects the type to an LED programming context.

**Learning objective:** Students classify Python values by data type - given a displayed value, they select its type from six options and receive feedback that connects the type to an LED programming context.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/python-data-type-explorer/main.html"
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
Students classify Python values by data type - given a displayed value, they select its type from six options and receive feedback that connects the type to an LED programming context.

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
**sim-id:** python-data-type-explorer<br/>
**Library:** p5.js<br/>
**Status:** Specified

Bloom Level: Understand (L2)
Bloom Verb: classify, identify
Learning Objective: Students classify Python values by data type — given a displayed value, they select its type from six options and receive feedback that connects the type to an LED programming context.

Instructional Rationale: The classify objective (L2 Understand) calls for a prediction-then-reveal pattern, not animation. Students see a value, commit to a type selection, then receive confirmation with an explanation. Prediction before reveal is the key retrieval-practice mechanism for retention at this level.

Canvas layout:
- Top area: A large "value card" showing a Python value in monospace font on a dark background (e.g., `42`, `"hello"`, `True`, `3.14`, `[1,2,3]`, `(255,0,0)`, `None`)
- Center area: Seven labeled type buttons — Integer, Float, String, Boolean, List, Tuple, None — arranged in a row or two rows on narrow screens
- Bottom area: Feedback panel showing correct/incorrect result with an explanation and an LED code example
- Progress bar: "Question X of 15" shown below the value card

Visual elements:
- Value card: Large rounded rectangle, dark background, white monospace text, border color matches type (blue=int, cyan=float, green=string, yellow=bool, orange=list, purple=tuple, gray=none) — border only shown AFTER student answers
- Type buttons: Pill-shaped, highlight on hover, turn green (correct) or amber (incorrect) after selection
- Feedback panel: Warm green background (correct) or amber (not quite) with two lines of text: (1) why this value is that type, (2) an LED example using this value

Data Visibility Requirements:
Stage 1: Show value card with value visible, border color hidden
Stage 2: Student clicks a type button
Stage 3: Reveal correct type, color the border, show feedback:
- Why: e.g., "255 is an integer — it's a whole number with no decimal point"
- LED example: e.g., "In NeoPixel code: `strip[0] = (255, 0, 0)` — 255 is the red channel value"
Stage 4: "Next" button advances to a new value

Values to cycle through (15 total):
- `42` → Integer
- `3.14` → Float
- `"hello"` → String
- `True` → Boolean
- `[255, 0, 0]` → List
- `(128, 0, 200)` → Tuple
- `None` → None
- `0` → Integer
- `0.5` → Float
- `"Moving Rainbow"` → String
- `False` → Boolean
- `[1, 2, 3, 4, 5]` → List
- `(255, 255, 255)` → Tuple
- `255` → Integer
- `""` → String (empty string)

Controls:
- Seven type buttons (one per type)
- "Next Value" button — shown after student answers, advances to next card
- "Shuffle" button — randomizes card order for replay

Responsive design: Canvas width fills container; font sizes and button layout scale with canvas width; buttons reflow to two rows on narrow screens.
```

</details>
