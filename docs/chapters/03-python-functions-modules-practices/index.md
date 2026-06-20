---
title: Python Functions, Modules, and Programming Best Practices
description: Learn to define and call functions, understand variable scope, and apply clean-code principles that make LED programs easier to read, reuse, and extend.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:30:03
version: 0.09
---

# Python Functions, Modules, and Programming Best Practices

## Summary

Teaches function definition, parameters, return values, variable scope, the DRY principle, and applied computational thinking concepts including code readability, abstraction, modular design, and code reuse strategies.

## Concepts Covered

This chapter covers the following 25 concepts from the learning graph:

1. len() Function
2. int() Function
3. float() Function
4. print() Function
5. Function Definition
6. Function Parameters
7. Function Return Value
8. Function Call
9. Variable Scope
10. Local Variable
11. Global Variable
12. Code Readability
13. DRY Principle
14. Hiding Implementation Details
15. Documentation as Communication
16. Separation of Concerns
17. Generalizing a Solution
18. Template-Based Solving
19. Code Commenting Strategy
20. Readable Variable Names
21. Meaningful Function Names
22. Modular Program Design
23. Code Reuse via Functions
24. Identifying Repeated Code
25. Boundary Conditions

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 2: Python Basics: Variables, Data Types, and Operators](../02-python-variables-types-operators/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 3! In Chapter 2 you learned how to store and compute with data. Now you'll learn how to organize that code so it's easy to reuse, easy to read, and easy to build on. Functions are one of the most powerful tools in programming. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Use Python's built-in functions like `len()`, `int()`, `float()`, and `print()`
- Define your own functions with parameters and return values
- Explain the difference between local and global variables
- Apply the DRY principle to remove repeated code from your programs
- Write code that is organized, readable, and easy to build on

## What You'll Need

For this chapter, you need Thonny and your Raspberry Pi Pico connected via USB. The short examples in the first two sections run in the Python Shell (REPL). The LED examples near the end need your NeoPixel strip connected.

## Built-in Functions Python Already Knows

In Chapter 2, you used `print()` to show values on the screen. `print()` is a **function** — a named block of code that does a specific job. You run it by writing its name followed by parentheses.

Before looking at more built-in functions, let's define two terms. An **argument** is a value you hand to a function so it can work with that value. A **return value** is the result the function sends back to you when it finishes.

Python comes loaded with many useful built-in functions. Here are the ones you'll use most in this course. Study this table, then we'll try each one:

| Function | What It Does | Example | Result |
|----------|-------------|---------|--------|
| `print()` | Shows a value in Thonny's Shell | `print("hello")` | Displays `hello` |
| `len()` | Returns the count of items | `len([1, 2, 3])` | `3` |
| `int()` | Converts to an integer | `int("200")` | `200` |
| `float()` | Converts to a float | `float("1.5")` | `1.5` |
| `str()` | Converts to a string | `str(255)` | `"255"` |
| `range()` | Creates a number sequence | `range(5)` | `0, 1, 2, 3, 4` |

Let's see `len()` in a real NeoPixel context. `len()` counts the items in any list or collection. Here it counts the pixels in our strip:

```python
import config
import neopixel

strip = neopixel.NeoPixel(config.NEOPIXEL_PIN, config.NUMBER_PIXELS)
print(len(strip))   # Prints the number of LEDs in the strip, e.g. 30
```

Run this in Thonny and you should see your pixel count appear in the Shell.

`range()` is one you'll use inside almost every `for` loop. It generates a sequence of integers starting from 0. `range(30)` generates 0, 1, 2, ... 29 — perfect for stepping through a 30-LED strip one pixel at a time.

## Why Write Your Own Functions?

Imagine you want to turn all your pixels red, then all green, then all blue. Without a custom function, you'd repeat almost identical code three times:

```python
import config
import neopixel
import utime

strip = neopixel.NeoPixel(config.NEOPIXEL_PIN, config.NUMBER_PIXELS)

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

All three blocks do the same job. The only thing that changes is the color value. This is called **identifying repeated code** — and it's the first step toward writing better programs.

The **DRY Principle** stands for "Don't Repeat Yourself." When you find yourself writing the same structure more than once, that's a signal to create a function. Repeated code creates problems: if you discover a bug in that structure, you must fix it in three places instead of one.

**Code reuse via functions** is the solution. You write the code once, give it a name, and call that name whenever you need it.

!!! tip "Pixel's tip"
    <img src="../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel points upward with a sparkle">
    How do you spot repeated code? Look for copy-paste patterns — blocks that look nearly identical except for one or two values. Those changing values (like the color) are exactly what become function parameters. The shared code becomes the function body.

## Defining a Function

A **function definition** tells Python: "here is a block of code, and here is its name." You use the `def` keyword (short for "define"):

```python
def function_name(parameter1, parameter2):
    # Code that runs when the function is called
    return result
```

The `def` line must end with a colon (`:`). Everything indented below it belongs to the function.

Let's replace the three repeated blocks from above with one function. The function needs to accept a color, fill every pixel, send the update, and pause briefly:

```python
import config
import neopixel
import utime

strip = neopixel.NeoPixel(config.NEOPIXEL_PIN, config.NUMBER_PIXELS)

def fill_color(strip, color):
    for i in range(len(strip)):
        strip[i] = color
    strip.write()
    utime.sleep(0.5)

# Now the three-color sequence is just three short lines
fill_color(strip, (255, 0, 0))   # Red
fill_color(strip, (0, 255, 0))   # Green
fill_color(strip, (0, 0, 255))   # Blue
```

The same visual result — red, green, blue flashes — now takes three lines instead of fifteen. If you find a bug in how `fill_color` works, you fix it in one place.

!!! info "Pixel thinks..."
    <img src="../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinks with a glowing ring">
    Think of a function like a recipe. The recipe's name is `fill_color`. The ingredients are `strip` and `color` (the parameters). The steps are the lines inside the function. You "cook" the recipe by writing its name and handing it the ingredients. Every time you need that dish, you just call the same recipe — you don't rewrite it from scratch.

### Function Parameters

**Function parameters** are the inputs a function needs to do its job. You list them inside the parentheses in the `def` line, separated by commas.

In `def fill_color(strip, color):`, there are two parameters:

- `strip` — the NeoPixel strip object to fill
- `color` — the RGB tuple to use as the fill color

When you call the function, you pass the actual values in the same order. Python matches the first argument to the first parameter, the second to the second, and so on:

```python
fill_color(strip, (255, 0, 0))
#          ^       ^
#          |       color = (255, 0, 0)
#          strip = our NeoPixel object
```

A function can have as many parameters as it needs. A function with no parameters is also valid — just leave the parentheses empty:

```python
def clear_strip():
    for i in range(len(strip)):
        strip[i] = (0, 0, 0)
    strip.write()
```

### Function Return Values

A **function return value** is the result a function sends back to the caller. You use the `return` keyword followed by the value to send back.

Not every function needs to return a value. `fill_color` does its work and that's it. But some functions calculate something you want to use later:

```python
def scale_color(color, factor):
    r = int(color[0] * factor)   # Scale the red channel
    g = int(color[1] * factor)   # Scale the green channel
    b = int(color[2] * factor)   # Scale the blue channel
    return (r, g, b)             # Send the new color back to the caller
```

When a function returns a value, you capture it in a variable:

```python
dim_red = scale_color((255, 0, 0), 0.5)
print(dim_red)   # Prints: (127, 0, 0) — half as bright
```

The `return` statement immediately exits the function and hands the value back to wherever the function was called.

### Function Calls

A **function call** runs a function. It's the function name followed by parentheses holding any arguments:

```python
fill_color(strip, (255, 0, 0))            # Call with two arguments
dim = scale_color((255, 0, 0), 0.5)       # Call that captures the return value
print(len(strip))                          # A built-in function call
```

Every function call follows three steps: Python jumps to the function's code, runs it with your arguments, then jumps back to where you called it (bringing the return value, if any).

Let's see this step by step in the next interactive simulation:

#### Diagram: Function Call Step-Through

<iframe src="../../sims/function-call-step-through/main.html" width="100%" height="540px" scrolling="no"></iframe>

<details markdown="1">
<summary>Function Call Step-Through</summary>
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
</details>

## Variable Scope: Where Variables Live

**Variable scope** describes where in a program a variable can be seen and used. Not every variable is visible from everywhere.

Before seeing code, let's define the two main types clearly. A **local variable** is created inside a function and only exists while that function is running. Once the function ends, the local variable disappears. A **global variable** is created outside all functions and can be seen from anywhere in the program.

Here's a side-by-side example showing both types at work:

```python
NUM_PIXELS = 30        # Global variable — visible everywhere in the program
BRIGHTNESS = 0.8       # Global variable — visible everywhere

def fill_color(strip, color):
    pixel_index = 0    # Local variable — only exists inside fill_color
    for i in range(NUM_PIXELS):   # i is also local — loop variable
        strip[i] = color
    strip.write()
    # pixel_index and i disappear when fill_color ends

fill_color(strip, (255, 0, 0))
print(NUM_PIXELS)       # Works — NUM_PIXELS is global
# print(pixel_index)    # Would raise NameError — pixel_index is local and gone
```

Local variables are created when a function starts and deleted when it ends. You can't access them from outside the function. This is intentional — it means each function manages its own data cleanly, and functions can't accidentally change each other's variables.

!!! warning "Watch out!"
    <img src="../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up hands gently">
    It's tempting to put every variable at the top of your program as a global so you can access it anywhere. Resist that! Too many global variables make bugs hard to find — when a value changes unexpectedly, you have to search your entire program to find where it changed. Keep variables as local as possible, and pass values through function parameters instead.

Let's see scope visually — click on any variable in the explorer below to see exactly where it lives:

#### Diagram: Variable Scope Explorer

<iframe src="../../sims/variable-scope-explorer/main.html" width="100%" height="520px" scrolling="no"></iframe>

<details markdown="1">
<summary>Variable Scope Explorer</summary>
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
</details>

## Writing Clean, Readable Code

A program that works is good. A program that works AND that any teammate can read and understand is great. The practices in this section help you reach that higher standard.

### Code Readability and Naming

**Code readability** measures how easily another person — or your future self — can read and understand your code.

Two of the most powerful readability tools are the simplest ones: choosing good names.

**Readable variable names** describe exactly what they store. Compare these two programs:

```python
# Hard to read — what do x, y, and z mean?
x = 30
y = 0.75
z = (255, 0, 0)

# Easy to read — names tell the whole story
num_pixels = 30
brightness_factor = 0.75
red_color = (255, 0, 0)
```

**Meaningful function names** describe exactly what a function does. A function named `f()` tells you nothing. A function named `fill_strip_with_color()` tells you everything:

```python
# Unclear name
def f(s, c):
    ...

# Clear name — reads like a sentence
def fill_strip_with_color(strip, color):
    ...
```

When your main program reads like plain English, you know you have great names:

```python
fill_strip_with_color(strip, RED)
fade_to_black(strip, RED)
play_rainbow_cycle(strip)
```

### Code Commenting Strategy and Documentation

A **code commenting strategy** means deciding what to comment and what to leave uncommented.

Good comments explain **why** you made a choice — not **what** the code does. The code already shows what it does. Comments fill in the reasoning:

```python
# Section labels — mark where a new topic begins
# ---- Color Constants ----
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Why comments — explain a non-obvious choice
brightness = 0.5     # Half brightness saves battery on wearable costumes

# Parameter labels — name a mystery number
utime.sleep(0.033)   # 33 ms pause gives approximately 30 frames per second
```

**Documentation as communication** is the bigger idea behind all of this. Your code is a message. Every name, every comment, and every structure you choose is part of that message. Clear code is clear communication — it tells the next reader (which might be you in six months) exactly what you were thinking.

### Separation of Concerns and Hiding Implementation Details

**Separation of concerns** means organizing your code so each function does exactly one job. A function called `fill_color` should only fill colors. It should not also print debug messages, handle timing, or check for button presses. Each concern gets its own function.

**Hiding implementation details** (also called **abstraction**) means that the code calling a function doesn't need to know how the function works inside. When you call `fill_color(strip, (255, 0, 0))`, you don't need to think about the `for` loop or `strip.write()` inside. That complexity is hidden. You just see a simple call that fills the strip.

```python
# Caller sees one clear line — complexity is hidden inside the function
fill_color(strip, RED)
```

This is one of the four pillars of computational thinking: abstraction. You hide the complexity so you can think about the problem at a higher level.

### Generalizing Solutions and Template-Based Solving

**Generalizing a solution** means taking code that works for one specific case and turning it into code that works for any case.

Our `fill_color` function is a generalized solution. Instead of being locked to one color, it works with any color you pass in. Instead of assuming 30 pixels, it uses `len(strip)` to work with any strip length.

**Template-based solving** is closely related. You recognize that a new problem matches a pattern — a template — you've already solved. You adapt the template rather than starting from scratch.

Here is the general "moving position" template for LED animations:

```python
def move_position(position, step, max_pos):
    position = (position + step) % max_pos   # Wrap using modulo
    return position
```

Once you know this template, you can adapt it for a bouncing pixel (change the step direction), a fast pixel (larger step), or a wrapping comet (same template, different drawing code). The template stays the same; only the parameters and drawing code change.

Before reading the summary table below, review each practice in your mind. The table summarizes what you've just read — it doesn't introduce new ideas:

| Practice | What It Means | LED Code Example |
|----------|---------------|-----------------|
| DRY Principle | No repeated code — use a function | `fill_color(strip, RED)` instead of copying the loop |
| Readable variable names | Names describe what's stored | `brightness_factor` not `bf` |
| Meaningful function names | Names describe what the function does | `scale_color()` not `sc()` |
| Separation of concerns | Each function does exactly one job | `fill_color()` fills; `scale_color()` scales |
| Hiding details | Callers don't see the inner workings | `fill_color(strip, RED)` — no visible loop |
| Generalizing a solution | Works for any input, not one hardcoded case | `color` parameter instead of `(255,0,0)` hardcoded |
| Template-based solving | Adapt a known pattern to a new situation | Moving-position template → bouncing, wrapping, etc. |
| Code commenting strategy | Comment WHY, not WHAT | `# Half brightness saves battery` |
| Documentation as communication | Code is a message to future readers | Clear names + comments = readable message |

Now let's see the DRY Principle in action — before and after refactoring:

#### Diagram: DRY Principle Before and After

<iframe src="../../sims/dry-principle-before-after/main.html" width="100%" height="560px" scrolling="no"></iframe>

<details markdown="1">
<summary>DRY Principle Before and After</summary>
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
</details>

## Modular Program Design

**Modular program design** means building a program as a collection of small, focused functions. Each function (module) does one job well. You build bigger programs by combining these small pieces.

This approach has three big benefits:

- Each function is easy to test on its own
- You can reuse functions across different programs
- When something breaks, you know which function to look in

Here's a short but complete modular LED program. Notice how the main section at the bottom reads almost like plain English:

```python
import config
import neopixel
import utime

strip = neopixel.NeoPixel(config.NEOPIXEL_PIN, config.NUMBER_PIXELS)

def scale_color(color, factor):
    r = int(color[0] * factor)
    g = int(color[1] * factor)
    b = int(color[2] * factor)
    return (r, g, b)

def fill_color(strip, color):
    for i in range(len(strip)):
        strip[i] = color
    strip.write()

def fade_to_black(strip, color, steps=10):
    for step in range(steps, 0, -1):
        factor = step / steps          # 1.0, 0.9, 0.8 ... 0.1
        dim = scale_color(color, factor)
        fill_color(strip, dim)
        utime.sleep(0.05)

# Main program — reads like a plan, not a puzzle
fill_color(strip, (255, 0, 0))         # Flash red
utime.sleep(0.5)
fade_to_black(strip, (255, 0, 0))      # Slowly fade to off
fill_color(strip, (0, 255, 0))         # Flash green
utime.sleep(0.5)
fade_to_black(strip, (0, 255, 0))      # Slowly fade to off
```

The main section is short and readable because all the complexity is hidden inside the three functions above. If you want to change how fading works, you only change `fade_to_black`. Nothing else needs to touch.

## Boundary Conditions

**Boundary conditions** are the edge cases that happen at the very limits of your code — the first value, the last value, an empty input, or an unexpected number. Bugs hide most often at boundaries.

Before looking at LED examples, picture any "between X and Y" rule. The boundary conditions are exactly at X and at Y — not somewhere safe in the middle.

Common boundary conditions in LED programming:

- Pixel index `0` (the very first pixel)
- Pixel index `len(strip) - 1` (the very last pixel)
- Color channel value `0` (completely off)
- Color channel value `255` (maximum brightness)
- A position counter that reaches exactly the strip length during a wrap-around animation

Here's a function that handles a boundary condition safely:

```python
def safe_set_pixel(strip, index, color):
    # Boundary condition check — index must be a valid position
    if index < 0 or index >= len(strip):
        return   # Exit quietly instead of crashing
    strip[index] = color
```

Without the check, passing an out-of-range index raises an `IndexError` and stops your program. With the check, the function exits gracefully and your animation keeps running.

!!! success "You've got this!"
    <img src="../../img/mascot/encouraging.png" class="mascot-admonition-img" alt="Pixel gives a big thumbs-up">
    Boundary conditions feel like a lot to think about — and they are! Good programmers develop a habit: whenever you write a loop or use an index, ask three quick questions: "What happens at the very first value? At the very last value? What if the list is empty?" Asking those three questions catches most boundary bugs before they bite. Every bug is just a puzzle in disguise!

## Try It Yourself

**Challenge 1 — Your First Function:** Write a function called `set_single_pixel` that takes three parameters: `strip`, `index`, and `color`. It should set the pixel at `index` to `color` and call `strip.write()`. Test it by calling the function three times to light pixels 0, 1, and 2 in three different colors.

**Challenge 2 — DRY Cleanup:** Here is some repeated code. Identify what's repeated, write a function to replace it, then rewrite the code using three function calls.

```python
import config
import neopixel
import utime

strip = neopixel.NeoPixel(config.NEOPIXEL_PIN, config.NUMBER_PIXELS)

# Flash red 3 times
for _ in range(3):
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (255, 0, 0)
    strip.write()
    utime.sleep(0.2)
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()
    utime.sleep(0.2)

# Flash green 3 times
for _ in range(3):
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 255, 0)
    strip.write()
    utime.sleep(0.2)
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)
    strip.write()
    utime.sleep(0.2)
```

Hint: What is the only thing that changes between "flash red" and "flash green"? That's your parameter.

## Check Your Understanding

Think through each answer first, then check below.

1. What does the DRY Principle stand for, and why does it matter if your strip changes from 30 to 60 pixels?

2. What is the difference between a **local variable** and a **global variable**? Give one example of each from the code in this chapter.

3. A function called `go()` takes no parameters and returns nothing. Another function is `calculate_dim_color(color, factor)`. Which follows the principle of **meaningful function names**? What might you rename `go()` to?

4. What is a **boundary condition**? Give one specific example from LED strip programming.

5. A classmate shows you this function. Find two problems with it and explain how you'd fix each one.

```python
def turn_on(strip):
    for i in range(30):          # 30 is hardcoded
        strip[i] = (255, 0, 0)  # Color is hardcoded
    strip.write()
```

??? question "Show answers"
    1. DRY stands for "Don't Repeat Yourself." If you hardcode `30` in five places and the strip grows to 60 pixels, you'd need to change five lines. With DRY, you read the strip length from `config.NUMBER_PIXELS` (or `len(strip)`) in one place, and the rest of your code updates automatically.

    2. A **local variable** is created inside a function and disappears when the function ends. Example: `r`, `g`, `b` inside `scale_color()`. A **global variable** is created outside all functions and is visible everywhere. Example: `NUM_PIXELS = 30` at the top of the program.

    3. `calculate_dim_color(color, factor)` has a meaningful name — it tells you what it does, what it needs, and what it returns (a dimmed color). `go()` tells you nothing. You might rename it `start_animation()`, `run_color_fade()`, or whatever it actually does.

    4. A **boundary condition** is a value at the edge of what your code can handle. Example: pixel index `0` (the first pixel) and `len(strip) - 1` (the last pixel) are boundary conditions for any loop or index operation on the strip. Accessing an index outside these bounds causes an `IndexError`.

    5. Two problems: (1) `range(30)` hardcodes the strip length — if the strip has a different number of pixels, this loop goes past the end or stops short. Fix: `range(len(strip))`. (2) `(255, 0, 0)` hardcodes the color — the function can only ever fill red. Fix: add a `color` parameter and use it: `def turn_on(strip, color)` and `strip[i] = color`.

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with a full rainbow blazing">
    You've mastered functions! You know how to define them, call them, pass data in with parameters, and get results back with return values. You understand scope, and you know the best practices that separate a good programmer from a great one. Your LED code is about to get a whole lot cleaner — and cleaner code is easier to build on, easier to share, and way more fun to work with!

## What's Next

In [Chapter 4](../04-python-control-flow-loops/index.md), you'll add decision-making and repetition to your toolkit — `if` statements, `for` loops, and `while` loops — the control structures that make your LED animations actually come alive.
