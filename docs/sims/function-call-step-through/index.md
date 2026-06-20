---
title: Function Call Step-Through
description: Students trace the execution flow of a function call — from the call site, into the function with its parameters bound, through each line of the body, across the return statement, and back to the caller — using a concrete NeoPixel example.
status: scaffold
library: p5.js
bloom_level: Understand (L2)
---

# Function Call Step-Through



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 3: Python Functions, Modules, and Programming Best Practices](../../chapters/03-python-functions-modules-practices/index.md).

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

## Related Resources

- [Chapter 3: Python Functions, Modules, and Programming Best Practices](../../chapters/03-python-functions-modules-practices/index.md)
