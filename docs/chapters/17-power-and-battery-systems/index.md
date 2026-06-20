---
title: Power Systems, Batteries, and Energy Management
description: Compare all battery types, learn series and parallel configurations, charging circuits, LiPo safety, power consumption calculations, and LED series resistor design.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# Power Systems, Batteries, and Energy Management

## Summary

Covers all battery types (coin cell, AA, AAA, 9V, USB power bank, LiPo, 18650), series and parallel battery configurations, charging circuits, LiPo and USB power safety, power consumption and battery life calculations, over-charge and over-discharge protection, and LED series resistor calculations.

## Concepts Covered

This chapter covers the following 22 concepts from the learning graph:

1. Coin Cell Battery
2. AA Alkaline Battery
3. AAA Alkaline Battery
4. 9-Volt Battery
5. USB Power Bank
6. LiPo Battery
7. 18650 Lithium Cell
8. Series Battery Configuration
9. Parallel Battery Configuration
10. Battery Charging Circuit
11. TC4056 Charger IC
12. Overcharge Protection
13. Over-Discharge Protection
14. Charging Current Setting
15. Total System Current Draw
16. Power Consumption Calculation
17. LED Forward Voltage
18. LED Series Resistor Calculation
19. LiPo Battery Safe Handling
20. USB Power Safety Limits
21. Ohm's Law Arithmetic
22. Battery Life Calculation

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 6: MicroPython APIs, GPIO Control, and Electrical Fundamentals](../06-micropython-apis-and-electronics/index.md)
- [Chapter 15: Electronics Fundamentals: Resistance, Ohm's Law, and Components](../15-electronics-fundamentals/index.md)
- [Chapter 16: Circuit Assembly: Resistors, Transistors, and Circuit Types](../16-circuit-assembly/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 17! Power is what makes your projects go. Choose the wrong battery and your costume dies halfway through the party. Choose the right one and you're glowing all night. Let's learn how to pick batteries like a pro. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Compare common battery types by voltage, capacity, size, and best use case
- Explain series and parallel battery configurations and what each does to voltage and capacity
- Calculate total system current draw and expected battery life
- Describe how LiPo charging circuits work and how to use them safely
- Calculate the correct LED series resistor using LED forward voltage and Ohm's Law
- Apply USB power safety limits to your project designs

## What You'll Need

- Pencil and paper for calculations
- Optional: multimeter to measure actual battery voltage
- Your project power budget (number of pixels, estimated brightness)

---

## Battery Types for LED Projects

Before comparing batteries, let's define two key terms:

- **Battery capacity** — measured in milliamp-hours (mAh). Tells you how much total charge a battery holds.
- **Nominal voltage** — the typical voltage the battery delivers during discharge.

Now let's look at each type, from simplest to most capable.

### Coin Cell Battery (CR2032)

The **Coin Cell Battery** (CR2032) is a flat, round lithium battery 20 mm in diameter and 3.2 mm thick. It provides **3 V** and about **200–250 mAh** capacity.

Coin cells are great for very small, low-power projects — a single LED with a microcontroller. They cannot supply the current needed for NeoPixel strips (even a single NeoPixel at full white can briefly draw 60 mA — more than a coin cell can sustain).

Use case: indicator LEDs, tiny keychain projects, small blinking badges.

### AA Alkaline Battery

The **AA Alkaline Battery** provides **1.5 V** and about **2,000–3,000 mAh** capacity. They're widely available, inexpensive, and safe.

Two AA batteries in series = 3 V (usable for some Pico projects). Four AA batteries in series = 6 V, which works well with a voltage regulator to step down to 5 V.

Use case: projects where the student needs batteries they can buy at a convenience store and swap easily.

### AAA Alkaline Battery

The **AAA Alkaline Battery** is smaller than AA — same 1.5 V but about half the capacity (1,200 mAh). Useful when space is tight.

### 9-Volt Battery

The **9-Volt Battery** provides 9 V and about **400–600 mAh** capacity. Enough voltage to power a 5 V system with a voltage regulator, but low capacity — a 30-pixel strip at moderate brightness would drain it in under an hour.

Use case: quick-test power supply when you don't have USB nearby. Not ideal for costumes.

### USB Power Bank

The **USB Power Bank** is the most practical power source for wearable NeoPixel projects. It provides a regulated **5 V** output at up to **2,000–5,000 mA** and capacities ranging from 2,000 to 20,000+ mAh.

Benefits:
- Directly powers the NeoPixel strip at the correct 5 V
- Charges via USB
- Available in very small sizes (3,000–5,000 mAh fits in a pocket)
- Has built-in overcharge and discharge protection

Use case: costumes, portable art installations, wearable projects — the recommended choice for this course.

**USB Power Safety Limits**: a standard USB 2.0 port provides 500 mA. A USB 3.0 port provides 900 mA. USB-C Power Delivery ports can supply 1.5–5 A. Check your power bank's output rating before connecting many pixels.

### LiPo Battery

A **LiPo Battery** (Lithium Polymer) is a rechargeable flat-pack cell commonly used in RC cars, drones, and wearables. Voltage is **3.7 V nominal** (fully charged: 4.2 V, fully discharged: 3.0 V). Capacities range from 100 mAh to 10,000+ mAh.

LiPo batteries are lightweight and flexible, making them ideal for sewn-in or compact wearable designs.

**LiPo Battery Safe Handling** — follow these rules without exception:

- Never puncture, crush, or bend a LiPo battery
- Never charge beyond 4.2 V — use a proper LiPo charger IC
- Never discharge below 3.0 V — this permanently damages the cell
- Store at 3.7–3.85 V (approximately 50% charge) for long-term storage
- If a LiPo battery swells (puffs up), stop using it immediately — it is damaged

### 18650 Lithium Cell

The **18650 Lithium Cell** is a cylindrical rechargeable cell 18 mm in diameter and 65 mm long (hence "18650"). It provides **3.7 V nominal** and **2,000–3,500 mAh** per cell. The same chemistry as LiPo, but in a rigid metal housing that's more durable.

18650 cells are popular for projects that need more capacity than a LiPo pouch but where the cylindrical shape fits (flashlight-style holders, belt packs).

The comparison table below summarizes all battery types:

| Battery | Voltage | Capacity (mAh) | Best Use |
|---|---|---|---|
| CR2032 (coin cell) | 3.0 V | 200–250 | Tiny badges, single LEDs |
| AA alkaline | 1.5 V | 2,000–3,000 | General projects, easy to replace |
| AAA alkaline | 1.5 V | 1,000–1,200 | Compact projects |
| 9-volt | 9 V | 400–600 | Quick testing with regulator |
| USB power bank | 5 V | 2,000–20,000+ | Costumes — recommended |
| LiPo pouch | 3.7 V | 100–10,000 | Lightweight wearables |
| 18650 cell | 3.7 V | 2,000–3,500 | Higher-capacity portable |

---

## Series and Parallel Battery Configurations

Two ways to connect multiple cells:

**Series Battery Configuration** — batteries connected positive-to-negative in a chain. Voltage adds up; capacity stays the same.

Example: Two AA cells (1.5 V each) in series = 3.0 V at 2,500 mAh.

**Parallel Battery Configuration** — batteries connected positive-to-positive and negative-to-negative. Voltage stays the same; capacity adds up.

Example: Two 2,500 mAh AA cells in parallel = 1.5 V at 5,000 mAh.

The rule of thumb: use series to increase voltage for your circuit. Use parallel to increase runtime without changing voltage.

---

## Power Consumption Calculation

To design a battery system, you need the **total system current draw** — the sum of all current consumers:

\[ I_{\text{total}} = I_{\text{Pico}} + I_{\text{LEDs}} + I_{\text{sensors}} \]

Typical values:
- Raspberry Pi Pico: ~25 mA
- Each NeoPixel at full white: 20 mA
- Each NeoPixel at 30% brightness: ~6 mA
- Photoresistor + resistor divider: ~0.3 mA (negligible)

A 30-pixel strip at 30% brightness plus the Pico:

\[ I_{\text{total}} = 25 + (30 \times 6) = 25 + 180 = 205 \text{ mA} \]

**Battery Life Calculation**:

\[ \text{Hours} = \frac{\text{capacity (mAh)}}{I_{\text{total}} \text{ (mA)}} \]

For a 5,000 mAh USB power bank:

\[ \text{Hours} = \frac{5000}{205} \approx 24 \text{ hours} \]

More than enough for any costume event.

#### Diagram: Battery Life Calculator

<details markdown="1">
<summary>Interactive calculator: battery life for LED projects</summary>
Type: interactive-infographic
**sim-id:** battery-life-calculator
**Library:** p5.js
**Status:** Specified

A clean p5.js form with interactive inputs:
- Battery type selector: (coin cell / AA / USB power bank / LiPo 500mAh / LiPo 2000mAh / 18650)
- Number of pixels slider: 1–60
- Brightness level slider: 10%–100%
- "Include Pico power" checkbox (adds 25 mA when checked)

Outputs displayed dynamically:
- Total current draw: X mA
- Battery capacity: Y mAh
- Estimated battery life: Z hours Z minutes
- Warning indicator if total current exceeds safe USB limit (500 mA)

A bar chart shows the proportion of power used by Pico vs. LEDs. Canvas: 700 × 420 px. Responds to window resize.

Learning objective: Applying — the student can calculate battery life for any project configuration.
</details>

---

## LiPo Charging Circuits and the TC4056

To recharge a LiPo battery safely, you need a charger IC that controls the charging voltage and current precisely.

The **TC4056** (also called the TP4056) is a popular, inexpensive LiPo charger IC available on small breakout modules. Here's what it does:

1. **Constant-current phase**: charges at the set current (up to 1000 mA) until the battery voltage approaches 4.2 V
2. **Constant-voltage phase**: holds at exactly 4.2 V and lets the current taper down
3. **Termination**: when current drops below about 10% of the set current, charging stops

**Charging Current Setting**: a single resistor on the TC4056 module sets the maximum charging current. A 1.2 kΩ resistor sets 1000 mA. A 10 kΩ resistor sets 130 mA. Most ready-made modules use 1 kΩ for 1000 mA charging.

**Overcharge Protection**: the TC4056 stops charging when the battery reaches 4.2 V — preventing the dangerous condition of a LiPo charged above its maximum voltage.

**Over-Discharge Protection**: the TC4056 itself doesn't include this, but most complete LiPo modules include a DW01 protection IC that cuts off the battery if voltage drops below 2.5–3.0 V, preventing irreversible cell damage.

!!! warning "Watch out!"
    <img src="../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    Never charge a LiPo battery that is visibly swollen, has been punctured, or has been discharged below 3.0 V without first consulting an expert. A damaged LiPo can catch fire. The small extra cost of a protected LiPo module is always worth it for a student project.

---

## LED Forward Voltage and Series Resistor Calculation

Non-addressable LEDs (ordinary LEDs, not NeoPixels) require a specific voltage called the **LED Forward Voltage** to operate. This is typically:

- Red: 1.8–2.2 V
- Green: 1.9–2.4 V
- Blue/White: 3.0–3.4 V

When you power an LED from a 5 V supply, the resistor must drop the excess voltage. The **LED Series Resistor Calculation** uses Ohm's Law:

\[ R = \frac{V_{\text{supply}} - V_{\text{forward}}}{I_{\text{LED}}} \]

For a red LED (V_forward = 2.0 V) at 20 mA from a 5 V supply:

\[ R = \frac{5.0 - 2.0}{0.020} = \frac{3.0}{0.020} = 150 \, \Omega \]

Choose the nearest standard resistor value (150 Ω or 220 Ω). A higher value is safer (dimmer LED, less current) than a lower value.

**Ohm's Law Arithmetic** reminder — the calculation above assumes all quantities are in the same units. If supply is in volts and current in amps, resistance comes out in ohms.

---

## Try It Yourself

1. **Battery comparison:** You need a project to run for 8 hours at 100 mA total current. Which battery type from the table would work? Which is the lightest option?

2. **Series config:** Two 18650 cells each at 3.7 V connected in series. What is the total voltage? What is the capacity?

3. **Current budget:** Your project has 40 pixels at 30% brightness and a Pico. Calculate total current draw. How long will a 3000 mAh USB power bank last?

4. **Resistor calculation:** You want to drive a blue LED (V_forward = 3.2 V) at 15 mA from a 3.3 V Pico GPIO pin. What resistor do you need? (Hint: 3.3 V − 3.2 V = 0.1 V. Calculate R. What does that tell you?)

---

## Check Your Understanding

1. What does mAh measure?
2. What is the difference between series and parallel battery configurations?
3. What voltage does a fully charged LiPo cell reach?
4. What does the TC4056 charger IC protect against?
5. Why is a USB power bank the recommended choice for wearable NeoPixel projects?
6. What is LED forward voltage and why does it matter for resistor calculations?
7. Your 18650 cell reads 2.8 V on a multimeter. Should you use it? Why or why not?

---

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You're a power systems engineer now! You can compare battery types intelligently, calculate how long a project will run, choose the right charging circuit, and protect LiPo batteries correctly. These skills will serve you in every portable electronics project you build for the rest of your life. Huge win!

## What's Next

In [Chapter 18](../18-input-devices-and-sensors/index.md), you'll connect buttons and sensors to your Pico — writing code that responds to the physical world with button presses, debouncing, mode cycling, and photoresistor light sensing.
