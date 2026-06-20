---
title: Raspberry Pi Pico Hardware Overview
description: Remembering - identify key parts of the Pico board by name.
image: /sims/pico-hardware-overview/pico-hardware-overview.png
og:image: /sims/pico-hardware-overview/pico-hardware-overview.png
twitter:image: /sims/pico-hardware-overview/pico-hardware-overview.png
social:
   cards: false
library: p5.js
status: implemented
---

# Raspberry Pi Pico Hardware Overview

<iframe src="main.html" width="100%" height="432px" scrolling="no"></iframe>

[Run the Raspberry Pi Pico Hardware Overview MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A top-down illustration of the Raspberry Pi Pico board. Labeled regions with click-to-expand info boxes:

**Learning objective:** Remembering - identify key parts of the Pico board by name.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/pico-hardware-overview/main.html"
        height="432px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Remembering - identify key parts of the Pico board by name.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 5](../../chapters/05-raspberry-pi-pico-hardware/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 5: Raspberry Pi Pico Hardware and Development Environment](../../chapters/05-raspberry-pi-pico-hardware/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: interactive-infographic
**sim-id:** pico-hardware-overview
**Library:** p5.js
**Status:** Specified

A top-down illustration of the Raspberry Pi Pico board. Labeled regions with click-to-expand info boxes:
- RP2040 chip (center): "The RP2040 microcontroller — dual ARM Cortex M0+ cores at up to 133 MHz"
- USB connector (top): "Micro-USB port — connects to your computer for power and programming"
- BOOTSEL button (top-left): "Hold this while plugging in USB to enter firmware-flash mode"
- LED (near USB): "Built-in green LED connected to GPIO 25"
- Left GPIO bank: "Pins GP0–GP14 — general-purpose input/output"
- Right GPIO bank: "Pins GP15–GP28 — more GPIO, plus ADC inputs"
- GND pins: "Ground — the common reference for all circuits"
- 3.3V OUT pin: "Regulated 3.3 V output for sensors and small components"
- VSYS pin: "Raw supply voltage from USB or battery (4.5–5.5 V)"

Canvas: 700 × 420 px. Clicking any labeled region opens an overlay card with name, description, and a relevant fact. Responds to window resize.

Learning objective: Remembering — identify key parts of the Pico board by name.
```

</details>
