---
title: MicroPython API Connections
description: 
image: /sims/micropython-api-connections/micropython-api-connections.png
og:image: /sims/micropython-api-connections/micropython-api-connections.png
twitter:image: /sims/micropython-api-connections/micropython-api-connections.png
social:
   cards: false
library: Mermaid
status: implemented
---

# MicroPython API Connections

<iframe src="main.html" width="100%" height="682px" scrolling="no"></iframe>

[Run the MicroPython API Connections MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A Mermaid diagram showing a central "Raspberry Pi Pico" box with arrows going to hardware components. Each arrow is labeled with the MicroPython API used:

**Learning objective:** 

## How to Use

Click any box or node in the diagram to read what it does. The explanation appears in the panel just below the diagram. Where an **Animate** button is present, press it to step through the sequence.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/micropython-api-connections/main.html"
        height="682px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective


### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 6](../../chapters/06-micropython-apis-and-electronics/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 6: MicroPython APIs, GPIO Control, and Electrical Fundamentals](../../chapters/06-micropython-apis-and-electronics/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
Type: diagram
**sim-id:** micropython-api-connections
**Library:** Mermaid
**Status:** Specified

A Mermaid diagram showing a central "Raspberry Pi Pico" box with arrows going to hardware components. Each arrow is labeled with the MicroPython API used:
- Pico → LED strip (NeoPixel): "neopixel.NeoPixel via machine.Pin(GP0)"
- Pico → Buzzer or servo: "machine.PWM via machine.Pin"
- Pico → Photoresistor: "machine.ADC via machine.Pin(GP26)"
- Pico → Button: "machine.Pin(GP15, IN)"
- Pico → Built-in LED: "machine.Pin(25, OUT)"
- Pico → Time/Delays: "utime.sleep()"
- Pico → Random effects: "urandom.randint()"

Each node is clickable: clicking opens an overlay explaining what that API does and which chapter covers it in depth. Use a left-to-right flow layout. Color-code: GPIO in blue, PWM in orange, ADC in green, time in purple, random in yellow.
```

</details>
