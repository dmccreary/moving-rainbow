---
title: Python Control Flow, Loops, and Error Handling
description: Learn conditional statements, for and while loops, loop control, list iteration, and how to read common Python error messages.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# Python Control Flow, Loops, and Error Handling

## Summary

Covers conditional statements (if/elif/else), for and while loops, loop control statements (break/continue), infinite loops, list iteration, common Python error types, and off-by-one error prevention.

## Concepts Covered

This chapter covers the following 19 concepts from the learning graph:

1. Boolean Expressions
2. if Statement
3. elif Clause
4. else Clause
5. Nested Conditionals
6. for Loop
7. while Loop
8. Infinite Loop
9. break Statement
10. continue Statement
11. Loop Counter Variable
12. range() Function
13. List Iteration
14. SyntaxError
15. NameError
16. IndentationError
17. TypeError
18. IndexError
19. Off-by-One Error

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 2: Python Basics: Variables, Data Types, and Operators](../02-python-variables-types-operators/index.md)
- [Chapter 3: Python Functions, Modules, and Programming Best Practices](../03-python-functions-modules-practices/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 4! You know how to store data and write functions. Now your code gets to *make decisions* and *repeat actions*. That's how animations work — your program checks what's happening and runs the right code, over and over. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Write `if`, `elif`, and `else` statements to make your code choose a path
- Use `for` loops to repeat code a set number of times
- Use `while` loops to repeat code until a condition changes
- Control loops with `break` and `continue`
- Use `range()` to produce number sequences
- Iterate over lists to process every item
- Read five common Python error messages and fix them
- Avoid the off-by-one error

## What You'll Need

- Thonny IDE open on your computer
- Your Raspberry Pi Pico connected via USB (helpful for testing, not strictly required)

---

## Making Decisions: Boolean Expressions and if Statements

Every decision in Python starts with a question that has a yes-or-no answer. That kind of question is called a **boolean expression** — a piece of code that evaluates to either `True` or `False`.

You already know comparison operators from Chapter 2. Here they are again, because you'll use them constantly:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 10` | `True` |
| `>` | Greater than | `10 > 3` | `True` |
| `<=` | Less than or equal to | `5 <= 5` | `True` |
| `>=` | Greater than or equal to | `4 >= 7` | `False` |

You can combine boolean expressions using `and`, `or`, and `not`:

- `True and True` → `True` (both must be true)
- `True or False` → `True` (at least one must be true)
- `not True` → `False` (flips the value)

### The if Statement

An **if statement** tells Python: "Run this block of code *only if* this condition is true." The block must be indented with four spaces (or one tab).

Here's the basic form:

```python
if condition:
    # code here runs only when condition is True
```

Here's a real example. This code checks whether a brightness level is too high:

```python
brightness = 200  # brightness goes from 0 to 255

if brightness > 200:
    print("That's very bright!")
```

When you run this, nothing prints — because 200 is not greater than 200. Change `brightness` to `250` and you'll see `That's very bright!` in the console.

### The elif and else Clauses

An **elif clause** (short for "else if") checks a second condition when the first one is false. An **else clause** runs when none of the above conditions are true.

Before reading the code below, here's what each keyword does:

- `if` → checks the first condition
- `elif` → checks the next condition (only if `if` was false)
- `else` → runs when everything above was false

```python
brightness = 128

if brightness > 200:
    print("Very bright!")
elif brightness > 100:
    print("Medium brightness")
else:
    print("Dim")
```

You should see `Medium brightness` because 128 is greater than 100 but not greater than 200.

!!! info "Pixel thinks..."
    <img src="../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    Python checks `if`, then `elif`, then `else` — in order, top to bottom. The moment one condition is `True`, Python runs that block and skips all the rest. It never checks two conditions at once.

### Nested Conditionals

A **nested conditional** is an `if` statement inside another `if` statement. Use this when you need to check a second thing *only after* the first thing is true.

```python
red = 200
green = 50

if red > 100:
    if green < 100:
        print("High red, low green — looks orange!")
```

You should see `High red, low green — looks orange!` Nesting too deeply can make code hard to read, so keep it to two levels at most.

---

## Repeating Code: The for Loop

A **for loop** runs a block of code a set number of times, once for each item in a sequence. The variable after `for` takes the value of each item, one at a time.

### Using range()

The **`range()` function** produces a sequence of integers. It's the most common tool for controlling how many times a `for` loop runs.

Here are the three ways to call `range()`:

| Call | Produces | Example values |
|---|---|---|
| `range(n)` | 0 up to but not including n | `range(5)` → 0, 1, 2, 3, 4 |
| `range(start, stop)` | start up to but not including stop | `range(2, 6)` → 2, 3, 4, 5 |
| `range(start, stop, step)` | counting by step | `range(0, 10, 2)` → 0, 2, 4, 6, 8 |

This loop prints the numbers 0 through 4:

```python
for i in range(5):
    print(i)
```

The variable `i` is the **loop counter variable**. Its value increases by 1 each time the loop runs. You should see the numbers 0, 1, 2, 3, 4 printed on separate lines.

Here's how you'd use this to set every LED on a 30-pixel strip:

```python
import neopixel
import machine
import config

strip = neopixel.NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

for i in range(config.NUMBER_PIXELS):
    strip[i] = (0, 100, 200)   # set pixel i to a blue-green color

strip.write()   # send the data to the LEDs
```

You should see your entire LED strip glow blue-green. The loop visits pixel 0, then pixel 1, all the way to the last pixel.

### List Iteration

A `for` loop can also go through a **list** — visiting each item in order. This is called **list iteration**.

```python
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # red, green, blue

for color in colors:
    print(color)
```

You should see `(255, 0, 0)`, `(0, 255, 0)`, and `(0, 0, 255)` on separate lines. The variable `color` takes each tuple from the list, one at a time.

#### Diagram: How a for Loop Iterates Over a List


<iframe src="../../sims/for-loop-list-iteration/main.html" width="100%" height="282px" scrolling="no"></iframe>
[Run How a for Loop Iterates Over a List Fullscreen](../../sims/for-loop-list-iteration/main.html)

<details markdown="1">
<summary>Interactive diagram: for loop stepping through a list</summary>
Type: interactive-infographic
**sim-id:** for-loop-list-iteration
**Library:** p5.js
**Status:** Specified

A p5.js MicroSim showing a list of three colored boxes labeled `(255,0,0)`, `(0,255,0)`, `(0,0,255)`. A "loop cursor" arrow moves from box to box as the user clicks a **Next Step** button. Each step highlights the current item, shows the value of the loop variable `color`, and displays the iteration number (Iteration 1 of 3, etc.). A **Reset** button returns the arrow to the start. A label below reads: "The for loop gives `color` a new value each time." Canvas: 600 × 280 px. Responds to window resize.

Learning objective: Remembering — the student can recall that a for loop assigns each list item to the loop variable in order.
</details>

!!! tip "Pixel's tip"
    <img src="../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel points upward">
    When you want to both know *which pixel* you're on AND set its color, use `for i in range(config.NUMBER_PIXELS)` and index with `strip[i]`. When you just need each item from a list, use `for item in my_list`. Choose the form that fits your task.

---

## while Loops: Repeat Until Something Changes

A **while loop** keeps running as long as its condition stays `True`. Use it when you don't know ahead of time how many times the loop should run.

```python
brightness = 0

while brightness < 256:
    print(brightness)
    brightness = brightness + 10
```

This loop prints 0, 10, 20, ... up to 250. When `brightness` reaches 260, the condition `brightness < 256` is `False` and the loop stops.

### Infinite Loops

An **infinite loop** runs forever — on purpose. Almost every LED animation program uses one. The loop keeps updating LEDs until you unplug the device or press Ctrl+C in Thonny.

```python
import utime

while True:
    print("LEDs are running!")
    utime.sleep(1)   # wait 1 second before the next print
```

You'll see `LEDs are running!` print once per second until you stop the program. In LED programs, you replace `print` with code that updates the strip.

!!! warning "Watch out!"
    <img src="../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    A `while True` loop that never updates the LEDs will look like nothing is happening — but your Pico is actually running full speed. Always include `strip.write()` and a short `utime.sleep()` inside animation loops. Without the sleep, the strip may flicker or not update correctly.

---

## Controlling Loops: break and continue

Sometimes you need to exit a loop early or skip one iteration. Two keywords handle this.

### The break Statement

The **`break` statement** stops the loop immediately and jumps past it, even if the condition is still true.

```python
for i in range(10):
    if i == 5:
        break         # exit the loop when i reaches 5
    print(i)
```

You'll see 0, 1, 2, 3, 4 — then the loop stops. The number 5 is never printed because `break` fires before the `print`.

### The continue Statement

The **`continue` statement** skips the rest of the current iteration and jumps back to the top of the loop to check the condition again.

```python
for i in range(6):
    if i == 3:
        continue      # skip the print when i is 3
    print(i)
```

You'll see 0, 1, 2, 4, 5 — the number 3 is missing because `continue` skipped it.

Here's a practical use: skip pixel 0 (the first pixel) and color the rest:

```python
for i in range(config.NUMBER_PIXELS):
    if i == 0:
        continue          # leave pixel 0 black
    strip[i] = (0, 150, 255)

strip.write()
```

You should see all LEDs blue-cyan except the very first one, which stays off.

#### Diagram: break vs. continue Flow


<iframe src="../../sims/break-continue-flowchart/main.html" width="100%" height="1012px" scrolling="no"></iframe>
[Run break vs. continue Flow Fullscreen](../../sims/break-continue-flowchart/main.html)

<details markdown="1">
<summary>Interactive flowchart: break and continue in a for loop</summary>
Type: diagram
**sim-id:** break-continue-flowchart
**Library:** Mermaid
**Status:** Specified

A Mermaid flowchart showing a `for` loop cycle. Nodes: "Start Loop" → "i in range?" → yes → "Check condition" → "break?" → yes → "Exit loop"; no → "continue?" → yes → "Back to top" (arrow goes back to "i in range?" node); no → "Run loop body" → "Back to top". Each node is clickable: clicking "break?" shows a tooltip "break exits the loop entirely"; clicking "continue?" shows "continue skips to the next iteration"; clicking "Run loop body" shows "This is where your animation code goes." Color-code: break path in red, continue path in orange, normal path in green.
</details>

---

## Reading Python Error Messages

When something goes wrong, Python prints an error message. Learning to read these messages is a superpower. Here are the five errors you'll see most often.

Before we look at each one, here's the key rule: **always read the last line of the error first**. That line tells you what went wrong. The lines above it tell you where.

### SyntaxError

A **SyntaxError** means Python can't understand your code. You typed something that isn't valid Python.

```
  File "main.py", line 3
    if brightness > 200
                       ^
SyntaxError: expected ':'
```

The `^` points at the problem. Here, the `if` statement is missing its colon. Add `:` at the end of line 3 and it will work.

### IndentationError

An **IndentationError** means the spaces at the start of a line are wrong. Python uses indentation to understand where blocks start and end.

```
  File "main.py", line 4
    print("hello")
    ^
IndentationError: unexpected indent
```

Check that every line inside a block uses exactly four spaces (not a mix of tabs and spaces).

### NameError

A **NameError** means you used a variable or function name that Python doesn't recognize.

```
NameError: name 'brigthness' is not defined
```

Look carefully — this is often a typo. `brigthness` should be `brightness`. Check your spelling.

### TypeError

A **TypeError** means you tried to use a value in a way that doesn't match its type.

```
TypeError: can only concatenate str (not "int") to str
```

This happens if you write `"Value: " + 42`. Python can't join a string and an integer directly. Use an f-string instead: `f"Value: {42}"`.

### IndexError

An **IndexError** means you tried to access a list position that doesn't exist.

```
IndexError: list index out of range
```

If your list has 3 items (indexes 0, 1, 2) and you try `my_list[3]`, Python raises this error. There is no index 3 — the last index is always `len(my_list) - 1`.

### Off-by-One Errors

An **off-by-one error** is a logic mistake, not a Python error. Your code runs without crashing, but it does the wrong thing by exactly one step.

The most common cause: forgetting that Python counts from 0, not 1.

```python
colors = ["red", "green", "blue"]  # 3 items: indexes 0, 1, 2
print(colors[3])                   # IndexError! Index 3 does not exist.
```

The fix: remember the last valid index is `len(colors) - 1`, which is 2. Use `range(len(colors))` to safely loop over all items.

In LED programs, off-by-one errors look like: lighting one more pixel than intended, or an animation that ends one step early. When results are "almost right but off by one," check your `range()` call and your loop condition.

!!! success "You've got this!"
    <img src="../../img/mascot/encouraging.png" class="mascot-admonition-img" alt="Pixel gives a thumbs-up">
    Error messages feel scary at first. But each one is Python's way of pointing right at the problem. Read the last line, find the file and line number, and you've already done half the detective work. Every bug is just a puzzle in disguise!

---

## Putting It Together: Fading an LED Strip

Here's a program that uses a `while` loop, an `if` statement, and `range()` together. It fades the strip from dark to bright, then from bright back to dark — forever.

Before reading the code, here's the plan:
- `brightness` starts at 0 and counts up to 255, then back down
- `direction` tracks whether we're going up (`1`) or down (`-1`)
- Inside the loop, we set every pixel to a blue color scaled by brightness

```python
import neopixel
import machine
import utime
import config

strip = neopixel.NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

brightness = 0     # starts dark
direction = 1      # 1 = going brighter, -1 = going darker

while True:
    for i in range(config.NUMBER_PIXELS):
        r = 0
        g = int(100 * brightness / 255)   # scale green with brightness
        b = int(255 * brightness / 255)   # scale blue with brightness
        strip[i] = (r, g, b)

    strip.write()
    utime.sleep(0.01)   # 10 ms delay between steps

    brightness = brightness + direction

    if brightness >= 255:   # reached the top — start going down
        direction = -1
    elif brightness <= 0:   # reached the bottom — start going up
        direction = 1
```

You should see the strip gently pulse between dark and a blue-green color, repeating smoothly. The `if/elif` at the bottom reverses the direction each time `brightness` hits an edge.

---

## Try It Yourself

1. **Color selector:** Write an `if/elif/else` block that prints a different message for each of these brightness values: below 85 prints "Dim", 85–170 prints "Medium", above 170 prints "Bright".

2. **Countdown:** Use a `for` loop with `range()` to print the numbers 10 down to 1 (hint: use `range(10, 0, -1)`), then print "Blast off!".

3. **Skip the middle:** Write a `for` loop over `range(10)` that uses `continue` to skip the numbers 4, 5, and 6.

4. **Fade out:** Modify the fade program above so it starts at full brightness (255) and fades to 0, then stops completely instead of bouncing back.

---

## Check Your Understanding

1. What are the two possible values of a boolean expression?
2. What is the difference between `elif` and `else`?
3. What does `range(3, 10, 2)` produce?
4. What does `break` do inside a loop? What does `continue` do?
5. You have a list with 5 items. What is the valid range of indexes you can use?
6. What type of error do you get when your code has a typo in a variable name?
7. Why is an infinite `while True` loop useful for LED animations?

---

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You did it! You can now make your code decide things with `if/elif/else`, repeat things with `for` and `while`, and control those repetitions with `break` and `continue`. You can also read error messages instead of panicking when they appear. That's real programmer thinking right there!

## What's Next

In [Chapter 5](../05-raspberry-pi-pico-hardware/index.md), you'll meet the Raspberry Pi Pico — the tiny computer that runs your LED animations — and set up the Thonny IDE so you can put your Python skills to work on real hardware.
