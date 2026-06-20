---
title: Electronics Fundamentals — Resistance, Ohm's Law, and Components
description: Learn resistance, Ohm's Law, breadboard assembly, common components (resistors, potentiometers, photoresistors, transistors), multimeter use, and electrical safety rules.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# Electronics Fundamentals: Resistance, Ohm's Law, and Components

## Summary

Covers resistance, Ohm's Law, complete circuit paths, short and open circuits, pull-up and pull-down resistors, potentiometers, light-dependent resistors, NPN transistors, multimeter operation, capacitors, diodes, voltage dividers, breadboard assembly, circuit diagram reading, and electrical safety rules.

## Concepts Covered

This chapter covers the following 26 concepts from the learning graph:

1. Resistance
2. Ohm's Law
3. Power Formula
4. Complete Circuit Path
5. Short Circuit
6. Open Circuit
7. Breadboard
8. Jumper Wires
9. Current-Limiting Resistor
10. Pull-Up Resistor
11. Pull-Down Resistor
12. Potentiometer
13. Potentiometer Wiper
14. Light-Dependent Resistor
15. Photoresistor Curve
16. NPN Transistor
17. 2N2222 Transistor
18. Transistor Base Terminal
19. Multimeter Overview
20. Milliamp-Hours (mAh)
21. Capacitor for Power Smoothing
22. Diode for Polarity Protection
23. Solderless Circuit Assembly
24. Circuit Diagram Reading
25. Wire Color Conventions
26. Electrical Safety Rules

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 6: MicroPython APIs, GPIO Control, and Electrical Fundamentals](../06-micropython-apis-and-electronics/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 15! We're going deeper into electronics — the physical world that your code controls. Understanding resistance, components, and circuits makes you a more confident hardware builder. No soldering required — everything in this course uses breadboards! Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Explain resistance and apply Ohm's Law to calculate voltage, current, or resistance
- Identify and describe a complete circuit path, short circuit, and open circuit
- Use a breadboard to build circuits without soldering
- Explain and use current-limiting, pull-up, and pull-down resistors
- Describe how potentiometers, photoresistors, and NPN transistors work
- Read a simple circuit diagram
- Apply basic electrical safety rules

## What You'll Need

- A breadboard
- Jumper wires (assorted colors)
- An LED (any color)
- A resistor (220 Ω or 330 Ω)
- Optional: a multimeter, potentiometer, photoresistor

---

## Resistance and Ohm's Law

In Chapter 6, you learned about voltage and current. Now we add **resistance** — the third essential electrical concept.

**Resistance** is how much a component opposes the flow of electrical current. It is measured in **ohms (Ω)**. A high-resistance component lets very little current through. A low-resistance component lets more current flow.

Water analogy: voltage is water pressure, current is flow rate, resistance is how narrow the pipe is.

**Ohm's Law** describes the relationship between these three quantities:

\[ V = I \times R \]

Where:
- V = voltage in volts (V)
- I = current in amps (A) or milliamps (mA)
- R = resistance in ohms (Ω)

You can rearrange this formula to solve for any one of the three:

- \( I = V / R \) — how much current flows given voltage and resistance
- \( R = V / I \) — what resistance is needed to limit current
- \( V = I \times R \) — what voltage drop appears across a resistor

**The Power Formula** tells you how much electrical power a component consumes:

\[ P = V \times I \]

Power is measured in watts (W) or milliwatts (mW). A pixel drawing 20 mA at 5 V uses 0.1 W = 100 mW.

#### Diagram: Ohm's Law Calculator


<iframe src="../../sims/ohms-law-calculator/main.html" width="100%" height="362px" scrolling="no"></iframe>
[Run Ohm's Law Calculator Fullscreen](../../sims/ohms-law-calculator/main.html)

<details markdown="1">
<summary>Interactive calculator: Ohm's Law triangle</summary>
Type: interactive-infographic
**sim-id:** ohms-law-calculator
**Library:** p5.js
**Status:** Specified

An interactive Ohm's Law triangle with three circles labeled V (volts), I (current), R (resistance). Two inputs are active at a time; the third is calculated. A dropdown lets the user choose which value to solve for. Numeric input fields accept values. Below the triangle, the formula is displayed with the current values substituted: e.g., "I = V ÷ R = 5 ÷ 220 = 0.023 A = 23 mA". A second section shows the power formula: "P = V × I = 5 × 0.023 = 0.115 W". Clicking any circle highlights the formula. Canvas: 700 × 350 px. Responds to window resize.

Learning objective: Applying — the student can solve Ohm's Law problems for any unknown variable.
</details>

---

## Complete Circuits, Short Circuits, and Open Circuits

Before building anything, you need to understand three circuit states.

A **complete circuit path** is an uninterrupted path for current from the positive terminal, through components, back to the negative terminal (ground). Current only flows when the path is complete.

An **open circuit** has a gap somewhere in the path — a wire not connected, a switch that's open, or a broken component. No current flows. Your LED won't light.

A **short circuit** is a direct low-resistance path from positive to ground, bypassing the intended components. A short circuit allows dangerously high current to flow, which can overheat wires, damage the power source, or start a fire. The most common cause in our projects: accidentally touching a power wire to a ground pin without a resistor in between.

---

## Breadboard and Solderless Assembly

A **breadboard** is a plastic board with holes that are internally connected in rows and columns. It lets you build circuits without soldering — just push wires and components into the holes.

Before reading the layout description, here's the key structure:

- The **top and bottom rails** (long horizontal strips) are connected all the way across. Use them for power (+) and ground (−). Often marked with red (+) and blue (−) lines.
- The **central rows** (numbered 1–30 or 1–60) are connected in groups of 5, side by side (columns a–e and f–j). The gap in the middle separates the two halves.

**Jumper wires** are short pre-cut wires (or ribbon cables) used to connect breadboard positions to each other or to your Pico. Color conventions help readability:

| Wire Color | Convention |
|---|---|
| Red | Power (+) / Vcc |
| Black | Ground (−) / GND |
| Yellow / Green / Blue | Signal lines |
| White / Orange | Other connections |

**Wire color conventions** are not enforced by physics — any wire works in any position. But following the convention makes your circuit much easier to read and debug.

**Solderless circuit assembly** means plugging components directly into the breadboard without heating any metal. Every circuit in this course uses solderless assembly. You can reuse all components in future projects.

---

## Resistor Types

You'll use three kinds of resistors in this course. Before explaining each, let's define **fixed resistor**: a component with a specific resistance value that doesn't change. The value is printed as a color code on the body.

### Current-Limiting Resistor

A **current-limiting resistor** protects an LED (or other component) from burning out. LEDs have very low resistance — without a limiting resistor, they would draw too much current and immediately fail.

To choose the right resistor value, use Ohm's Law. For a red LED on a 3.3 V output with 20 mA maximum current:

\[ R = \frac{V_{\text{supply}} - V_{\text{LED}}}{I} = \frac{3.3 - 2.0}{0.02} = 65 \, \Omega \]

A 100 Ω or 220 Ω resistor is a safe choice for this course's LEDs.

### Pull-Up and Pull-Down Resistors

These resistors appear in button wiring. Their purpose: ensure a GPIO input pin reads a definite value (not a floating, undefined voltage) when the button is open.

- **Pull-up resistor** — connects the input pin to the supply voltage (3.3 V). When the button is open, the pin reads HIGH (1). When the button closes, it connects to GND, pulling the pin LOW (0). The Pico has built-in pull-up resistors you can enable in code with `Pin.PULL_UP`.
- **Pull-down resistor** — connects the input pin to GND. When the button is open, the pin reads LOW (0). When the button closes, it connects to power, reading HIGH (1).

In MicroPython:

```python
btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
value = btn.value()   # 1 when button open, 0 when button pressed
```

You should see `1` in the console when the button is not pressed, and `0` when you press it.

---

## Potentiometer

A **potentiometer** is a variable resistor — it has a knob or slider you can adjust to change its resistance from 0 Ω to its maximum (often 10 kΩ).

It has three terminals:

- Two **outer terminals** — connected to power (+) and ground
- One **middle terminal** (the **wiper**) — moves between the two ends as you rotate the knob

The **potentiometer wiper** acts as a voltage divider: when the knob is at one end, the wiper output is near GND; at the other end, it's near the supply voltage; in the middle, it's half the supply voltage.

Connect the wiper to an ADC pin on the Pico to read the knob position as a number from 0 to 65535:

```python
pot = machine.ADC(26)    # GP26 = ADC0
reading = pot.read_u16() # 0 when knob at GND end, 65535 when at power end
print(reading)
```

You should see the number change smoothly as you turn the knob.

---

## Light-Dependent Resistor (Photoresistor)

A **Light-Dependent Resistor (LDR)** — also called a photoresistor — changes its resistance based on how much light hits its surface.

The **photoresistor curve** describes this relationship:
- In bright light: resistance is low (1 kΩ or less)
- In dark conditions: resistance is high (100 kΩ or more)

To read a photoresistor, you build a **voltage divider** with a fixed resistor. The ADC reads the voltage at the midpoint, which changes as the LDR resistance changes. This technique is covered in depth in Chapter 18.

---

## NPN Transistor: A Programmable Switch

An **NPN transistor** is a three-terminal device that acts as an electrically controlled switch. The **2N2222** is a common, inexpensive NPN transistor used for switching small loads like LEDs and motors.

The three terminals are:

- **Base** — the control input. When a small current flows into the base, the transistor "turns on."
- **Collector** — connects to the positive side of the load (the LED or motor)
- **Emitter** — connects to GND

The **transistor base terminal** is driven by a GPIO output pin through a resistor. When the GPIO goes HIGH, a small current flows into the base, and the transistor allows a much larger current to flow from collector to emitter — turning on the LED.

This is the "current gain" effect: a small base current (a few mA) controls a much larger load current (up to 600 mA for a 2N2222).

---

## Other Components

### Capacitor for Power Smoothing

A **capacitor** stores a small amount of electrical charge and releases it quickly when needed. In LED circuits, a **100 µF capacitor** placed across the power rails (+ to power rail, − to GND) smooths out rapid current spikes — preventing the Pico from resetting when a large number of LEDs suddenly turn on simultaneously.

### Diode for Polarity Protection

A **diode** allows current to flow in only one direction. A **protection diode** wired in series with the power input means that if you accidentally connect the battery backward, no current flows — protecting your circuit from damage.

### Multimeter Overview

A **multimeter** is a handheld tool that measures voltage, current, and resistance. Key uses:

- **Voltage mode (V)** — touch probes to two points; displays the voltage difference
- **Resistance mode (Ω)** — measures a resistor or checks continuity (beeps if connected)
- **Current mode (A or mA)** — must be wired *in series* with the circuit (more advanced)

For this course, using a multimeter in voltage mode to check that your power rail is actually at 5 V, and in resistance mode to verify component values, covers 90% of your needs.

**Milliamp-hours (mAh)** is a measure of how much energy a battery stores — covered in detail in Chapter 17. One mAh can supply 1 mA for one hour, or 2 mA for half an hour, etc.

---

## Reading Circuit Diagrams

A **circuit diagram** (also called a schematic) uses standardized symbols to represent components. Before wiring any project, practice reading the diagram to know what connects where.

Common symbols:

| Symbol | Component |
|---|---|
| Straight lines | Wires |
| Zigzag | Resistor |
| Two parallel lines (one longer) | Battery/power source |
| Triangle with a line | Diode |
| Circle with rays | LED |
| Three-terminal shape | Transistor |

The rule for reading diagrams: follow the current flow from + to −. Every component in series shares the same current. Every component in parallel shares the same voltage.

---

## Electrical Safety Rules

Working with the Pico and LED strips at 5 V is very safe — the voltages and currents involved cannot harm a healthy person. However, developing good habits now prepares you for working with higher-voltage systems later.

Key rules for this course:

1. **Never work on a live circuit** while adding or removing components. Unplug first.
2. **Always connect GND first**, power second.
3. **Always include a current-limiting resistor** in series with any LED driven directly by a GPIO pin.
4. **Never exceed 500 mA** from a single USB port without a separate power supply.
5. **Keep the Pico dry** — liquid and electronics don't mix.
6. **If something smells hot or smoky**, unplug immediately. Inspect before plugging back in.

!!! warning "Watch out!"
    <img src="../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    Short circuits are the most common wiring mistake. A short circuit connects + to − without any resistance in between. The result: components overheat, batteries drain instantly, and USB ports may shut down to protect themselves. If your USB port stops providing power, unplug and look for a short circuit in your wiring.

---

## Try It Yourself

1. **Ohm's Law practice:** You have a 5 V supply and a 330 Ω resistor. How much current flows? How much power does the resistor dissipate?

2. **Breadboard LED:** Wire an LED in series with a 220 Ω resistor between the 3.3 V output and GND on your Pico. The LED should light up without any code.

3. **Open circuit test:** Remove one wire from your LED circuit. What happens? Put it back. What changed?

4. **Potentiometer reading:** Wire a potentiometer to GP26 and read its value in the REPL with `machine.ADC(26).read_u16()`. Turn the knob and observe the value changing.

---

## Check Your Understanding

1. State Ohm's Law in your own words.
2. What is the difference between an open circuit and a short circuit?
3. Why do LEDs need a current-limiting resistor?
4. What does a pull-up resistor do when a button is open?
5. What are the three terminals of an NPN transistor?
6. How does a potentiometer wiper work?
7. Why do we say the Pico is safe to work with at 5 V?

---

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You're now a real electronics builder! You know Ohm's Law, how to use a breadboard, what pull-up resistors do, how transistors switch, and how to stay safe. These skills let you go from code-only projects to full hardware-software systems. That's a huge step!

## What's Next

In [Chapter 16](../16-circuit-assembly/index.md), you'll put this theory to work — building transistor switch circuits, LED dimmers, voltage dividers, and analog nightlight circuits on your breadboard.
