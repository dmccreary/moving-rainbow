---
title: Raspberry Pi Pico Hardware Overview
description: Remembering — identify key parts of the Pico board by name.
status: scaffold
library: p5.js
bloom_level: TBD
---

# Raspberry Pi Pico Hardware Overview



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 5: Raspberry Pi Pico Hardware and Development Environment](../../chapters/05-raspberry-pi-pico-hardware/index.md).

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

## Related Resources

- [Chapter 5: Raspberry Pi Pico Hardware and Development Environment](../../chapters/05-raspberry-pi-pico-hardware/index.md)
