---
title: Input Devices, Sensors, and State Machines
description: Wire and read push buttons with debouncing, build mode-cycling programs, read photoresistors with ADC, map sensor values, and implement the state machine pattern.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# Input Devices, Sensors, and State Machines

## Summary

Teaches momentary push button wiring, GPIO input mode, pull-up and pull-down configurations, polling, software debouncing, multiple button handling, mode variables and cycling, photoresistor sensors, ADC voltage reading, sensor value mapping, light threshold detection, and the state machine programming pattern.

## Concepts Covered

This chapter covers the following 33 concepts from the learning graph:

1. Momentary Push Button
2. Button Wiring to GPIO
3. GPIO Input Mode Setup
4. Pin.PULL_UP Configuration
5. Pin.PULL_DOWN Configuration
6. Polling a Button State
7. Button Debouncing
8. Debounce Delay Value
9. Software Debounce Pattern
10. Multiple Button Handling
11. Mode Variable
12. Mode Cycling Logic
13. Mode Switching on Button
14. State Machine Pattern
15. Current Mode Tracking
16. State Transition Logic
17. Event-Driven Programming
18. Photoresistor Sensor
19. ADC Voltage Reading
20. Sensor Value Mapping
21. Light Threshold Setting
22. Automatic Nightlight Trigger
23. Analog Value Smoothing
24. Sensor Calibration Steps
25. Interrupt vs Polling
26. Button Long-Press Logic
27. Two-Button Combination
28. Button LED Test Pattern
29. Real-Time Input Response
30. Input Validation
31. Sensor Data Range Mapping
32. Hysteresis in Sensor Reading
33. Capacitive Touch Concept

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 2: Python Basics: Variables, Data Types, and Operators](../02-python-variables-types-operators/index.md)
- [Chapter 3: Python Functions, Modules, and Programming Best Practices](../03-python-functions-modules-practices/index.md)
- [Chapter 4: Python Control Flow, Loops, and Error Handling](../04-python-control-flow-loops/index.md)
- [Chapter 5: Raspberry Pi Pico Hardware and Development Environment](../05-raspberry-pi-pico-hardware/index.md)
- [Chapter 6: MicroPython APIs, GPIO Control, and Electrical Fundamentals](../06-micropython-apis-and-electronics/index.md)
- [Chapter 15: Electronics Fundamentals: Resistance, Ohm's Law, and Components](../15-electronics-fundamentals/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 18! Your projects have been running on their own until now. In this chapter, you take control — with buttons and sensors that let the physical world change what your LEDs do. This is what turns a light show into an *interactive* light show. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Wire a momentary push button with a pull-up or pull-down resistor
- Poll a button state and detect when it's been pressed
- Implement software debouncing to prevent false triggers
- Build mode-cycling programs that change animation patterns on button press
- Read a photoresistor value with the ADC and map it to a useful range
- Implement the state machine programming pattern
- Explain the difference between polling and interrupt-based input

## What You'll Need

- Raspberry Pi Pico connected to Thonny
- One or two momentary push buttons
- A photoresistor (LDR) and a 10 kΩ resistor
- Breadboard and jumper wires
- NeoPixel strip connected to GP0

---

## Momentary Push Button Wiring

A **momentary push button** closes a circuit only while you hold it down — the moment you release it, the circuit opens again. Unlike a toggle switch, a momentary button has no "on" or "off" state of its own; it just signals *pressed* vs. *released*.

To wire a **button to GPIO**:
1. Connect one leg of the button to a GPIO input pin (GP15 in our examples)
2. Connect the other leg to GND

With this wiring and a pull-up resistor, the GPIO pin reads HIGH (1) when the button is not pressed, and LOW (0) when it is pressed.

### GPIO Input Mode Setup

To read a button, configure the pin as an input with **Pin.PULL_UP Configuration**:

```python
import machine

btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
```

The `PULL_UP` argument activates the internal pull-up resistor. Now `btn.value()` returns `1` (HIGH) when the button is open, and `0` (LOW) when the button is pressed (connecting the pin to GND).

For **Pin.PULL_DOWN Configuration** (less common in this course), the pin connects to GND via an internal resistor, reading LOW when button is open and HIGH when pressed.

### Polling a Button State

**Polling** means checking the button state repeatedly in your main loop. Before reading the code, the pattern is:

1. Read the current button value
2. Compare it to the previous value to detect a change
3. React only when a press (LOW) is detected for the first time (not every frame it stays pressed)

```python
import machine, utime

btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
prev_state = 1   # 1 = not pressed (pull-up default)

while True:
    current_state = btn.value()

    if current_state == 0 and prev_state == 1:
        # Button was just pressed (transition from 1 → 0)
        print("Button pressed!")

    prev_state = current_state
    utime.sleep_ms(10)   # check 100 times per second
```

You should see "Button pressed!" in the Thonny Shell each time you press the button — once per press, not once per loop iteration.

---

## Button Debouncing

When a button is pressed, the metal contacts briefly bounce — making and breaking contact many times in the first few milliseconds. This bouncing causes the pin to read multiple presses in rapid succession, even from a single finger press.

**Button Debouncing** eliminates these false triggers. The simplest approach is the **Software Debounce Pattern**: after detecting a press, wait a short time (the **debounce delay value**, typically 20–50 ms) before accepting another press.

```python
DEBOUNCE_MS = 30    # ignore button bouncing for 30 ms after each press

btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
prev_state = 1
last_press_time = 0

while True:
    current_state = btn.value()
    now = utime.ticks_ms()

    if current_state == 0 and prev_state == 1:
        if utime.ticks_ms() - last_press_time > DEBOUNCE_MS:
            print("Debounced press!")
            last_press_time = now

    prev_state = current_state
    utime.sleep_ms(5)
```

You should see exactly one "Debounced press!" per button press, even if you press and release quickly.

!!! info "Pixel thinks..."
    <img src="../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    Without debouncing, one press can register as 2, 5, or even 10 presses — making your mode cycling jump wildly. Debouncing is one of those things that seems optional until the moment your project starts misbehaving from a light touch. Always include it for buttons.

---

## Mode Variables and Mode Cycling

A **mode variable** stores which animation is currently active. **Mode cycling logic** advances this variable when the button is pressed, cycling through all available patterns.

Before reading the code:
- `mode` is an integer (0, 1, 2, …)
- Each value maps to a different animation
- Pressing the button adds 1 to `mode`; when it reaches the maximum, it wraps back to 0

```python
NUM_MODES = 3
mode = 0         # current animation mode

def run_animation(mode):
    if mode == 0:
        # Mode 0: solid red
        for i in range(config.NUMBER_PIXELS):
            strip[i] = (200, 0, 0)
    elif mode == 1:
        # Mode 1: solid green
        for i in range(config.NUMBER_PIXELS):
            strip[i] = (0, 200, 0)
    else:
        # Mode 2: solid blue
        for i in range(config.NUMBER_PIXELS):
            strip[i] = (0, 0, 200)
    strip.write()

btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
prev_state = 1
last_press = 0

while True:
    state = btn.value()
    if state == 0 and prev_state == 1:
        if utime.ticks_ms() - last_press > 30:
            mode = (mode + 1) % NUM_MODES   # advance and wrap
            last_press = utime.ticks_ms()
    prev_state = state

    run_animation(mode)
    utime.sleep_ms(20)
```

You should see the strip color change between red, green, and blue each time you press the button.

**Mode Switching on Button** is the event-driven mechanism here. The button is an **event**; the mode change is the **response**. **Event-Driven Programming** structures code around events (button presses, timer firings, sensor thresholds) rather than a fixed sequence.

---

## The State Machine Pattern

A **State Machine Pattern** is a way of organizing programs that have multiple modes, where the current mode (state) determines what the program does and what triggers a transition to another state.

Before the diagram, here are the key concepts:
- **Current Mode Tracking** — the `mode` variable stores the current state
- **State Transition Logic** — the rule for when and how `mode` changes
- **State machine states** — each state has a set of behaviors (which animation to run)

#### Diagram: State Machine for a 3-Mode LED Controller

<details markdown="1">
<summary>Interactive state machine diagram: mode transitions on button press</summary>
Type: diagram
**sim-id:** state-machine-diagram
**Library:** Mermaid
**Status:** Specified

A Mermaid state diagram with three states: "Mode 0: Red", "Mode 1: Green", "Mode 2: Blue". Directed arrows between each state labeled "button pressed". Mode 0 → Mode 1 → Mode 2 → Mode 0 (full cycle). Each state node is clickable: clicking opens a tooltip showing what the LED animation does in that mode. The current active state is highlighted in a different color. An "Animate" button cycles through states one step at a time. Arrow labels show the transition condition: "button pressed (debounced)".

Canvas: 700 × 380 px. Responds to window resize.

Learning objective: Understanding — the student can trace a state machine through a sequence of transitions given a series of inputs.
</details>

**Multiple Button Handling** extends this to two buttons — one to advance the mode, one to reverse it. Use the same polling + debounce pattern for each button on a separate GPIO pin.

**Two-Button Combination** — detecting when *both* buttons are pressed simultaneously enables a reset-to-mode-0 function:

```python
btn1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
btn2 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

if btn1.value() == 0 and btn2.value() == 0:
    mode = 0   # reset to default
```

---

## Photoresistor Sensor and ADC Reading

A **photoresistor sensor** (LDR) changes resistance based on light level. Wire it in a voltage divider with a 10 kΩ fixed resistor (LDR between 3.3 V and the midpoint; fixed resistor between midpoint and GND, or vice versa). Connect the midpoint to GP26.

**ADC Voltage Reading** with `machine.ADC(26).read_u16()` returns 0–65535, proportional to the voltage at the ADC pin.

In bright light: LDR resistance drops → more voltage appears at midpoint → ADC reads higher value.
In dark conditions: LDR resistance rises → less voltage → ADC reads lower value.

(The exact behavior depends on which resistor is on top — check your wiring.)

```python
ldr = machine.ADC(26)
reading = ldr.read_u16()
print(reading)   # observe values in bright and dark conditions
```

**Sensor Calibration Steps**: measure the ADC value in your darkest expected condition and in your brightest expected condition. These become your range boundaries for mapping.

### Sensor Value Mapping and Data Range Mapping

**Sensor Value Mapping** converts the raw ADC range (0–65535) to a useful range (e.g., 0–255 for brightness, or 0–360 for hue).

Before the formula, here's the concept: if your LDR reads 20,000 in darkness and 55,000 in bright light, you want 20,000 to map to 0 and 55,000 to map to 255.

**Sensor Data Range Mapping** formula:

```python
def map_value(value, in_min, in_max, out_min, out_max):
    # Clamp to input range first
    value = max(in_min, min(in_max, value))
    # Then map linearly
    return int(out_min + (value - in_min) / (in_max - in_min) * (out_max - out_min))

raw = ldr.read_u16()
brightness = map_value(raw, 20000, 55000, 0, 200)
```

**Analog Value Smoothing**: raw ADC readings can jump around. Averaging several readings reduces noise:

```python
def smooth_read(adc, samples=5):
    total = sum(adc.read_u16() for _ in range(samples))
    return total // samples
```

### Light Threshold and Hysteresis

**Light Threshold Setting** defines the ADC value at which "dark" becomes "bright" or vice versa.

**Hysteresis in Sensor Reading** prevents the output from rapidly switching back and forth when the sensor value hovers near the threshold. Instead of one threshold, you use two:

- Turn on when value drops below `DARK_THRESHOLD = 35000`
- Turn off when value rises above `LIGHT_THRESHOLD = 45000`

```python
DARK_THRESHOLD  = 35000
LIGHT_THRESHOLD = 45000
nightlight_on = False

while True:
    reading = smooth_read(ldr)
    if reading < DARK_THRESHOLD:
        nightlight_on = True    # Automatic Nightlight Trigger
    elif reading > LIGHT_THRESHOLD:
        nightlight_on = False

    # Apply the nightlight state
    color = (200, 200, 200) if nightlight_on else (0, 0, 0)
    for i in range(config.NUMBER_PIXELS):
        strip[i] = color
    strip.write()
    utime.sleep_ms(100)
```

You should see the strip light up white when you cover the photoresistor, and turn off when you uncover it — with no flickering around the threshold.

---

## Interrupt vs. Polling

**Polling** (what we've used) checks the button state in every loop iteration. It's simple and works well for most projects. The cost: the CPU is checking the button even when nothing is happening.

**Interrupt vs. Polling** — an interrupt is a hardware mechanism where a button press automatically interrupts the running program and calls a special function (an interrupt service routine, or ISR). MicroPython supports interrupts via `Pin.irq()`.

For this course, polling is recommended — it's simpler and avoids the timing complexity of interrupts. Interrupts become important when the main program is too slow to reliably catch fast button presses.

**Button Long-Press Logic**: detecting a long press (held for > 1 second) requires tracking how long the button has been held, not just that it was pressed:

```python
press_start = 0
LONG_PRESS_MS = 1000

state = btn.value()
if state == 0 and prev_state == 1:
    press_start = utime.ticks_ms()   # record when press started
if state == 1 and prev_state == 0:
    held_time = utime.ticks_ms() - press_start
    if held_time > LONG_PRESS_MS:
        print("Long press!")
    else:
        print("Short press!")
```

**Input Validation** means checking that input values are in a safe range before using them. For sensor readings: clamp the result with `max(0, min(255, value))` before using it as a brightness parameter.

**Real-Time Input Response** — the goal is to make the system feel responsive. With polling at 20–50 ms intervals, a button press is detected within at most 50 ms — imperceptible to humans.

---

## Capacitive Touch Concept

**Capacitive Touch** is an alternative to mechanical buttons. When a finger touches a conductive pad, it changes the electrical capacitance measurable by the microcontroller. Some Pico-compatible boards include capacitive touch pins. The MicroPython `touch` module supports this on capable boards.

For this course, mechanical buttons are used — but knowing capacitive touch exists helps you understand how touchscreens work and how you might upgrade a future project.

---

## Try It Yourself

1. **Debounce comparison:** Write a version of the button program without debouncing. Press the button quickly several times. How often does it register extra presses?

2. **Three-mode rainbow:** Extend the mode cycling program to three animation modes: solid color, moving rainbow, and twinkle. Press the button to cycle between them.

3. **Light-reactive brightness:** Use the photoresistor reading to control LED brightness. In bright room conditions, LEDs are dim. In a dark room, LEDs are bright. (Map ADC value inversely to brightness.)

4. **Long press reset:** Add long-press detection to the mode cycling program. A short press advances the mode; a long press (1 second) resets to mode 0.

---

## Check Your Understanding

1. What does `Pin.PULL_UP` do to the pin's default voltage when the button is open?
2. Why do buttons need software debouncing?
3. What does the mode variable store, and how does mode cycling work?
4. What is a state machine? Draw a simple three-state diagram.
5. What does `ADC.read_u16()` return and what does the value represent?
6. What is hysteresis and why is it useful for sensor readings?
7. What is the difference between polling and interrupt-based input?

---

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    Your projects can now *respond* to the world! Buttons, debouncing, mode cycling, state machines, sensor reading, and automatic triggers — you've built the foundation of all interactive systems. Every smart device you've ever used is a more complex version of what you built in this chapter. That's a massive insight!

## What's Next

In [Chapter 19](../19-interactive-animations-and-tools/index.md), you'll combine everything — buttons, sensors, and all your animation patterns — into polished multi-mode programs, and master the complete development toolchain including Git, GitHub, and Thonny's advanced features.
