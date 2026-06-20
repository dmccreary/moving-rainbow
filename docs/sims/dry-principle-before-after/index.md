---
title: DRY Principle Before and After
description: Students compare repeated code ("Before DRY") with a refactored version that uses a function ("After DRY"), identifying which lines were duplicated, what the function parameter replaced, and why the refactored version is better.
status: scaffold
library: p5.js
bloom_level: Analyze (L4)
---

# DRY Principle Before and After



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 3: Python Functions, Modules, and Programming Best Practices](../../chapters/03-python-functions-modules-practices/index.md).

```text
Type: microsim
**sim-id:** dry-principle-before-after<br/>
**Library:** p5.js<br/>
**Status:** Specified

Bloom Level: Analyze (L4)
Bloom Verb: differentiate, compare, examine
Learning Objective: Students compare repeated code ("Before DRY") with a refactored version that uses a function ("After DRY"), identifying which lines were duplicated, what the function parameter replaced, and why the refactored version is better.

Instructional Rationale: Compare/differentiate (L4 Analyze) is served by a side-by-side comparison with interactive highlighting. The student clicks a repeated block on the left to see it matched to its corresponding function call on the right. A "Find the Bug" challenge makes the DRY benefit concrete: a bug inserted in only two of three copies illustrates how DRY reduces a three-fix problem to a one-fix problem.

Canvas layout:
- Two code panels side by side (47% each, 6% gap):
  - Left panel: "Before DRY" — three repeated fill-strip blocks
  - Right panel: "After DRY" — one function definition, three short calls
- Below panels: "What changed" explanation panel
- Line count badges: "Before: 15 lines" and "After: 9 lines" shown above each panel

Before DRY code (left panel):
```python
# Turn all pixels red
for i in range(config.NUMBER_PIXELS):
    strip[i] = (255, 0, 0)
strip.write()
utime.sleep(0.5)

# Turn all pixels green
for i in range(config.NUMBER_PIXELS):
    strip[i] = (0, 255, 0)
strip.write()
utime.sleep(0.5)

# Turn all pixels blue
for i in range(config.NUMBER_PIXELS):
    strip[i] = (0, 0, 255)
strip.write()
utime.sleep(0.5)
```

After DRY code (right panel):
```python
def fill_color(strip, color):
    for i in range(len(strip)):
        strip[i] = color
    strip.write()
    utime.sleep(0.5)

fill_color(strip, (255, 0, 0))   # Red
fill_color(strip, (0, 255, 0))   # Green
fill_color(strip, (0, 0, 255))   # Blue
```

Interactive features:
- Click any 5-line block on the left → that block highlights orange, and the matching `fill_color(...)` call on the right highlights orange
- Click the function body on the right → all three blocks on the left highlight simultaneously
- "Count lines" toggle → shows/hides "15 lines" and "9 lines" badges
- "What's different?" button → reveals the explanation panel: "The three blocks are identical except for the color value. Moving the shared code into a function and making color a parameter reduces 15 lines to 9. If a bug exists in the loop, you only fix it once instead of three times."
- "Find the Bug" challenge: A typo — `strip.write` (missing parentheses `()`) — is pre-inserted in two of the three left-panel blocks but not the third. The student must click all instances of the bug to "fix" them. Counter shows "0 / 2 fixed". After fixing: "With DRY, this bug would only exist in one place — the function body."

Responsive design: Panels stack vertically on screens narrower than 600px (left on top of right). Font size 12px minimum.
```

## Related Resources

- [Chapter 3: Python Functions, Modules, and Programming Best Practices](../../chapters/03-python-functions-modules-practices/index.md)
