---
title: State Machine for a 3-Mode LED Controller
description: Understanding — the student can trace a state machine through a sequence of transitions given a series of inputs.
status: scaffold
library: Mermaid
bloom_level: TBD
---

# State Machine for a 3-Mode LED Controller



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 18: Input Devices, Sensors, and State Machines](../../chapters/18-input-devices-and-sensors/index.md).

```text
Type: diagram
**sim-id:** state-machine-diagram
**Library:** Mermaid
**Status:** Specified

A Mermaid state diagram with three states: "Mode 0: Red", "Mode 1: Green", "Mode 2: Blue". Directed arrows between each state labeled "button pressed". Mode 0 → Mode 1 → Mode 2 → Mode 0 (full cycle). Each state node is clickable: clicking opens a tooltip showing what the LED animation does in that mode. The current active state is highlighted in a different color. An "Animate" button cycles through states one step at a time. Arrow labels show the transition condition: "button pressed (debounced)".

Canvas: 700 × 380 px. Responds to window resize.

Learning objective: Understanding — the student can trace a state machine through a sequence of transitions given a series of inputs.
```

## Related Resources

- [Chapter 18: Input Devices, Sensors, and State Machines](../../chapters/18-input-devices-and-sensors/index.md)
