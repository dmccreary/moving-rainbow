---
title: Function Call Step-Through
description: Students trace the execution flow of a function call - from the call site, into the function with its parameters bound, through each line of the body, acro
image: /sims/function-call-step-through/function-call-step-through.png
og:image: /sims/function-call-step-through/function-call-step-through.png
twitter:image: /sims/function-call-step-through/function-call-step-through.png
social:
   cards: false
library: p5.js
status: implemented
---

# Function Call Step-Through

<iframe src="main.html" width="100%" height="412px" scrolling="no"></iframe>

[Run the Function Call Step-Through MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

Students trace the execution flow of a function call - from the call site, into the function with its parameters bound, through each line of the body, across the return statement, and back to the caller - using a concrete NeoPixel example.

**Learning objective:** Students trace the execution flow of a function call - from the call site, into the function with its parameters bound, through each line of the body, across the return statement, and back to the caller - using a concrete NeoPixel example.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/function-call-step-through/main.html"
        height="412px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Students trace the execution flow of a function call - from the call site, into the function with its parameters bound, through each line of the body, across the return statement, and back to the caller - using a concrete NeoPixel example.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 3](../../chapters/03-python-functions-modules-practices/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 3: Python Functions, Modules, and Programming Best Practices](../../chapters/03-python-functions-modules-practices/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: microsim
**sim-id:** function-call-step-through<br/>
**Library:** p5.js<br/>
**Status:** Specified

Bloom Level: Understand (L2)
Bloom Verb: explain, interpret, trace
Learning Objective: Students trace the execution flow of a function call — from the call site, into the function with its parameters bound, through each line of the body, across the return statement, and back to the caller — using a concrete NeoPixel example.

Instructional Rationale: Trace/explain (L2 Understand) requires seeing data values at each step, not abstract animation. The step-through pattern (Next/Previous buttons) lets students pause at each phase and predict what happens before revealing the next state. This is superior to auto-play animation, which removes the prediction step essential for encoding at the Understand level.

Canvas layout:
- Left panel (55%): Two code areas stacked vertically:
  - Top: "Caller code" — the main program lines that include the function call, with an animated red arrow pointing at the active line
  - Bottom: "Function body" — the `def fill_color(...)` block, with an animated red arrow pointing at the active line
- Right panel (45%): "State Inspector" showing:
  - Current step label: "Step 3 of 7: Loop body — strip[0] gets color"
  - Parameter table: variable names and current values at this step
  - Return value: blank until the return statement is active, then shows the value
  - Plain-English explanation of what is happening this step

Code used in the simulation:
```python
# Caller code (top panel)
dim = scale_color((255, 0, 0), 0.5)
print(dim)

# Function body (bottom panel)
def scale_color(color, factor):
    r = int(color[0] * factor)
    g = int(color[1] * factor)
    b = int(color[2] * factor)
    return (r, g, b)
```

Execution steps (7 total):
Step 1: Caller — "Python reads `scale_color((255,0,0), 0.5)` and prepares to jump"
Step 2: Function — "Parameters are bound: color=(255,0,0), factor=0.5"
Step 3: Function — "r = int(255 * 0.5) = 127"
Step 4: Function — "g = int(0 * 0.5) = 0"
Step 5: Function — "b = int(0 * 0.5) = 0"
Step 6: Function — "return (127, 0, 0) — function exits and sends this tuple back"
Step 7: Caller — "dim = (127, 0, 0); print(dim) shows (127, 0, 0)"

Data Visibility Requirements:
At each step the State Inspector shows:
- Which panel is active (caller vs. function) — highlighted with a blue tint
- All current parameter and local variable values with concrete numbers
- Whether we're "inside" or "outside" the function
- Return value column (blank until step 6, then shows `(127, 0, 0)`)

Controls:
- "Next Step" button — advance to next step
- "Previous Step" button — go back one step
- "Restart" button — reset to step 1
- Step counter display: "Step X of 7"

Visual elements:
- Code font: monospace, 13px, syntax-highlighted (keywords in blue, strings in green, numbers in orange)
- Active line: yellow background highlight
- Active arrow: red arrow pointing at the active line in the relevant panel
- "Inside function" indicator: blue tinted background behind the function panel when execution is there
- State Inspector: white background, 12px sans-serif, colored variable names

Responsive design: Panels stack vertically on screens narrower than 600px. Font size reduces to 11px when stacked.
```

</details>
