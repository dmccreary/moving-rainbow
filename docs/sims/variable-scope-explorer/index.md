---
title: Variable Scope Explorer
description: Students differentiate local from global variables by clicking variable names in a complete program and seeing which scope zone each variable belongs to, with a plain-English explanation of why.
status: scaffold
library: p5.js
bloom_level: Understand (L2)
---

# Variable Scope Explorer



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 3: Python Functions, Modules, and Programming Best Practices](../../chapters/03-python-functions-modules-practices/index.md).

```text
Type: microsim
**sim-id:** variable-scope-explorer<br/>
**Library:** p5.js<br/>
**Status:** Specified

Bloom Level: Understand (L2)
Bloom Verb: differentiate, classify, identify
Learning Objective: Students differentiate local from global variables by clicking variable names in a complete program and seeing which scope zone each variable belongs to, with a plain-English explanation of why.

Instructional Rationale: Differentiate (L2) is served by a classify-on-click pattern: the student examines a full program, clicks a variable name, and the sim highlights the scope zone that contains it with an explanation. This makes scope concrete and spatial — students build an accurate mental map of what's visible where — rather than abstract.

Canvas layout:
- Left panel (60%): A complete Python program with two functions displayed in monospace font on a dark background. Each variable name occurrence is rendered as a clickable highlighted span.
- Right panel (40%): Scope Inspector showing:
  - Variable name (e.g., `scaled`)
  - Scope type: "LOCAL — lives only inside `fill_color()`"
  - Explanation: "This variable was created inside a function. Python deletes it when the function ends."
  - Visual diagram: A nested rectangle diagram — outer rectangle labeled "Program (global scope)", inner rectangle labeled "fill_color function (local scope)", with the clicked variable highlighted inside its correct box

Code displayed (same for both panels):
```python
NUM_PIXELS = 30          # global
BRIGHTNESS = 0.8         # global

def fill_color(strip, color):
    scaled = scale_color(color, BRIGHTNESS)
    for i in range(NUM_PIXELS):
        strip[i] = scaled
    strip.write()

def scale_color(color, factor):
    r = int(color[0] * factor)
    g = int(color[1] * factor)
    b = int(color[2] * factor)
    return (r, g, b)

fill_color(strip, (255, 0, 0))
```

Clickable variables and their scope labels:
- `NUM_PIXELS` → Global: defined at module level, visible everywhere
- `BRIGHTNESS` → Global: defined at module level, visible everywhere
- `strip` (fill_color param) → Local parameter: created when fill_color is called
- `color` (fill_color param) → Local parameter: created when fill_color is called
- `scaled` → Local variable in fill_color
- `i` → Local loop variable in fill_color's for loop
- `color` (scale_color param) → Local parameter: separate from fill_color's `color`
- `factor` → Local parameter in scale_color
- `r`, `g`, `b` → Local variables in scale_color

Visual elements:
- Program background: dark gray
- fill_color function zone: blue-tinted rounded rectangle
- scale_color function zone: orange-tinted rounded rectangle
- Global variables outside both zones: white text, no tint
- Clicked variable: its zone pulses and its name highlights in yellow everywhere it appears in the code

Controls:
- Click any highlighted variable name → show scope info in right panel
- "Highlight all globals" button → flash all global variables yellow for 1.5 seconds
- "Highlight all locals" button → flash all local variables blue for 1.5 seconds

Responsive design: Panels stack vertically on screens narrower than 580px; font size minimum 12px.
```

## Related Resources

- [Chapter 3: Python Functions, Modules, and Programming Best Practices](../../chapters/03-python-functions-modules-practices/index.md)
