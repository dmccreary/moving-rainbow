---
title: Code Indentation Explorer
description: Students identify which lines of a Python snippet are correctly indented, which have errors, and explain what block each line belongs to.
status: scaffold
library: p5.js
bloom_level: Understand (L2)
---

# Code Indentation Explorer



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 2: Python Basics — Variables, Data Types, and Operators](../../chapters/02-python-variables-types-operators/index.md).

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

## Related Resources

- [Chapter 2: Python Basics — Variables, Data Types, and Operators](../../chapters/02-python-variables-types-operators/index.md)
