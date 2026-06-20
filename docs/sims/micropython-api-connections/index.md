---
title: MicroPython API Connections
description: MicroPython API Connections
status: scaffold
library: Mermaid
bloom_level: TBD
---

# MicroPython API Connections



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 6: MicroPython APIs, GPIO Control, and Electrical Fundamentals](../../chapters/06-micropython-apis-and-electronics/index.md).

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

## Related Resources

- [Chapter 6: MicroPython APIs, GPIO Control, and Electrical Fundamentals](../../chapters/06-micropython-apis-and-electronics/index.md)
