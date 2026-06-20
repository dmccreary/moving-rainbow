---
title: NeoPixel Wiring Diagram
description: Applying - the student can wire a NeoPixel strip from a diagram.
image: /sims/neopixel-wiring-diagram/neopixel-wiring-diagram.png
og:image: /sims/neopixel-wiring-diagram/neopixel-wiring-diagram.png
twitter:image: /sims/neopixel-wiring-diagram/neopixel-wiring-diagram.png
social:
   cards: false
library: p5.js
status: implemented
---

# NeoPixel Wiring Diagram

<iframe src="main.html" width="100%" height="402px" scrolling="no"></iframe>

[Run the NeoPixel Wiring Diagram MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

An interactive wiring diagram showing a Raspberry Pi Pico on the left and a 10-pixel NeoPixel strip on the right. Three colored wires connect them:

**Learning objective:** Applying - the student can wire a NeoPixel strip from a diagram.

## How to Use

Use the on-screen controls - buttons, sliders, dropdowns, and clickable regions - to explore the idea. Every change updates the canvas immediately, so you can predict an outcome and then check it.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/neopixel-wiring-diagram/main.html"
        height="402px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Applying - the student can wire a NeoPixel strip from a diagram.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 8](../../chapters/08-neopixel-led-hardware/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 8: NeoPixel LED Hardware — WS2812B, Wiring, and Form Factors](../../chapters/08-neopixel-led-hardware/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: interactive-infographic
**sim-id:** neopixel-wiring-diagram
**Library:** p5.js
**Status:** Specified

An interactive wiring diagram showing a Raspberry Pi Pico on the left and a 10-pixel NeoPixel strip on the right. Three colored wires connect them:
- Red wire from VSYS (Pico) to +5V (strip)
- Black wire from GND (Pico) to GND (strip)
- Green wire from GP0 (Pico) to DIN/DATA (strip)

Each wire is clickable: clicking opens a tooltip explaining "What this wire does" and "What happens if you forget this wire." An arrow on the strip shows the data direction. A small inset shows the WS2812B chip inside one pixel with labels: "RGB LEDs", "Control IC", "DIN", "DOUT". Hovering over a pixel on the strip shows its index number (0, 1, 2...). Canvas: 700 × 400 px. Responds to window resize.

Learning objective: Applying — the student can wire a NeoPixel strip from a diagram.
```

</details>
