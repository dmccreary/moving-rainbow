---
title: Python Operator Playground
description: Students apply Python's mathematical, comparison, and logical operators to LED-themed problems and observe the result of each expression.
status: scaffold
library: p5.js
bloom_level: Apply (L3)
---

# Python Operator Playground



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 2: Python Basics — Variables, Data Types, and Operators](../../chapters/02-python-variables-types-operators/index.md).

```text
Type: microsim
**sim-id:** python-operator-playground<br/>
**Library:** p5.js<br/>
**Status:** Specified

Bloom Level: Apply (L3)
Bloom Verb: calculate, use, demonstrate
Learning Objective: Students apply Python's mathematical, comparison, and logical operators to LED-themed problems and observe the result of each expression.

Instructional Rationale: Apply (L3) calls for a parameter-exploration or interactive calculator pattern. Students select an operator, enter operands, and see the Python result alongside a plain-English LED interpretation. Prediction challenges are included so students commit to an answer before seeing the result — strengthening Apply-level encoding over purely passive observation.

Canvas layout:
- Top row: Three category tabs — Math | Comparison | Logic — active tab highlighted in blue
- Center panel: Left operand input, operator display (large, centered), right operand input
- Result panel: Shows the Python expression and its result (e.g., `47 % 30 = 17`)
- LED Interpretation panel: Explains what this result means in an LED context
- Challenge panel: A pre-loaded challenge problem for the student to solve before revealing the answer

Visual elements:
- Three tabs: styled as segmented control at top; active tab has solid blue background
- Operand inputs: Large text fields (100px wide), border highlights on focus
- Operator display: Large centered symbol (font-size 36px) in a rounded box between the operands
- Result value: Large (font-size 48px), color-coded: blue for numbers, green for True, red for False
- LED interpretation: Small text panel below result — e.g., "If your strip has 30 LEDs and a pixel is at position 47, it wraps to position 17"

Available operators:
- Math tab (dropdown): +, -, *, /, //, %, **
- Comparison tab (dropdown): ==, !=, <, >, <=, >=
- Logic tab: operands become True/False dropdowns; operator dropdown has: and, or, not (not uses only left operand)

Data Visibility Requirements:
Stage 1: Student selects a tab and operator
Stage 2: Student enters operand values (or selects True/False for Logic)
Stage 3: Result updates live as student types: show full expression `100 % 30 = 10`
Stage 4: LED interpretation panel updates with a real NeoPixel context for this exact calculation

Challenge problems (pre-loaded, student must enter answer before "Reveal" button):
- Math: "A strip has 30 LEDs. A pixel is at position 47. Where does it appear? Enter: 47 % 30"
- Comparison: "Red channel = 128, Blue channel = 255. Is red brighter? Enter: 128 > 255"
- Logic: "Button A is pressed (True). Button B is not pressed (False). Are BOTH pressed? Select: True and False"

Responsive design: Canvas fills container width; operator display and inputs scale with canvas width; tabs reflow to vertical on very narrow screens.
```

## Related Resources

- [Chapter 2: Python Basics — Variables, Data Types, and Operators](../../chapters/02-python-variables-types-operators/index.md)
