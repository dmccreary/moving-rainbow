---
title: Example Circuit Connection Diagram for Bike Light Project
description: Applying — the student can trace any signal path from source to destination and identify which pin it uses.
status: scaffold
library: p5.js
bloom_level: TBD
---

# Example Circuit Connection Diagram for Bike Light Project



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 20: Project Design, Capstone Projects, and Presentation](../../chapters/20-project-design-and-capstone/index.md).

```text
Type: diagram
**sim-id:** bike-light-circuit-diagram
**Library:** p5.js
**Status:** Specified

A p5.js interactive wiring diagram showing:

**Components:**
- Raspberry Pi Pico (center, with all GPIO pins labeled on both sides)
- WS2812B LED strip (right side, 8 pixels shown as a row)
- Momentary button (left side, on breadboard)
- USB power bank (top right, labeled "5V source")

**Connections drawn as colored wires:**
- Red: USB power bank 5V → Pico VBUS pin → LED strip 5V pin
- Black: USB power bank GND → Pico GND → LED strip GND
- Yellow: Pico GP0 → LED strip Data In (with a note: "330Ω resistor in-line recommended")
- Green: Pico GP15 → Button one leg
- Black: Button other leg → GND

Clicking any component opens a tooltip explaining its role. Clicking any wire highlights its full path and shows voltage/signal name.

Canvas: 700 × 420 px. Responds to window resize.

Learning objective: Applying — the student can trace any signal path from source to destination and identify which pin it uses.
```

## Related Resources

- [Chapter 20: Project Design, Capstone Projects, and Presentation](../../chapters/20-project-design-and-capstone/index.md)
