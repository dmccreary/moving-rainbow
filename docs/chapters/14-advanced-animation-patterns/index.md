---
title: Advanced Animation Patterns — Comet, Scanner, and Heartbeat
description: Implement heartbeat, Larson scanner, comet tail, dual-direction scan, expanding ripple, and time-mapped LED clock using brightness envelopes, scanner widths, and sine-based breathing.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# Advanced Animation Patterns: Comet, Scanner, and Candle

## Summary

Teaches the most complex animation effects—heartbeat, Larson scanner, comet tail, dual-direction scanning, candle flicker, photo-reactive animations, sensor-driven displays, and clock with localtime()—using brightness envelopes, scanner width parameters, and comet trail length control.

## Concepts Covered

This chapter covers the following 17 concepts from the learning graph:

1. Heartbeat Pattern
2. Comet Tail Animation
3. Larson Scanner Pattern
4. Comet Trail Length
5. Scanner Width Parameter
6. Pattern Composition
7. Brightness Envelope
8. Clock with localtime()
9. Seconds and Minutes Display
10. Color Mapping to Time
11. LED as Clock Hands
12. Single-Color Scan
13. Dual-Direction Scan
14. Alternating Pixel Groups
15. Expanding Ripple Rings
16. Brightness Formula
17. Sine-Based Breathing Effect

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 2: Python Basics: Variables, Data Types, and Operators](../02-python-variables-types-operators/index.md)
- [Chapter 3: Python Functions, Modules, and Programming Best Practices](../03-python-functions-modules-practices/index.md)
- [Chapter 4: Python Control Flow, Loops, and Error Handling](../04-python-control-flow-loops/index.md)
- [Chapter 6: MicroPython APIs, GPIO Control, and Electrical Fundamentals](../06-micropython-apis-and-electronics/index.md)
- [Chapter 9: NeoPixel Programming: Pixels, Colors, and the NeoPixel Library](../09-neopixel-programming/index.md)
- [Chapter 11: Mathematics for LED Programming](../11-math-for-led-programming/index.md)
- [Chapter 12: Basic LED Animation Patterns](../12-basic-animation-patterns/index.md)
- [Chapter 13: Intermediate Animation Techniques](../13-intermediate-animations/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 14! These are the advanced patterns — the ones people remember. A Larson scanner on a costume gets noticed. A comet tail on a hat gets questions. A heartbeat on a glowing sign gets feelings. Let's build the effects that make people look twice. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Implement the heartbeat pattern using a brightness envelope
- Build a comet tail animation with controllable trail length
- Create the Larson scanner (Knight Rider effect) with scanner width control
- Implement dual-direction scanning with two independent scan points
- Use `localtime()` to map time to colors and pixel positions
- Compose multiple simple patterns into more complex visual effects

## What You'll Need

- Raspberry Pi Pico with NeoPixel strip connected
- Thonny IDE connected
- `import math` (available in MicroPython)

---

## The Brightness Envelope Concept

Before building the advanced patterns, let's define **brightness envelope** — the concept underlying all of them.

A brightness envelope is a function that maps time (or position, or distance) to a brightness value. Instead of pixels being simply "on" or "off," each pixel has a brightness determined by where it falls in a mathematical envelope.

The table below summarizes the envelopes used in this chapter:

| Pattern | Envelope Shape | Key Variable |
|---|---|---|
| Heartbeat | Double pulse then long pause | Phase counter |
| Comet tail | Exponential decay behind head | Trail length |
| Larson scanner | Gaussian peak at scan position | Scanner width |
| Sine breathing | Smooth sine wave | Time step |

Understanding the envelope is 80% of understanding the pattern. The code is just implementing the envelope mathematically.

---

## Pattern: Heartbeat

The **Heartbeat Pattern** simulates a pulse: two quick bright flashes (the "lub-dub" of a heartbeat) followed by a longer dark pause.

Before the code, here's the brightness envelope:
- Phase 0: ramp up fast (bright flash 1)
- Phase 1: ramp down fast
- Phase 2: ramp up fast (bright flash 2, slightly smaller)
- Phase 3: ramp down fast
- Phase 4: long pause at darkness

```python
import math, utime

def heartbeat_value(phase, total_phases):
    # Returns brightness 0-255 for a given phase position
    if phase < total_phases * 0.1:
        return int(phase / (total_phases * 0.1) * 255)   # ramp up fast
    elif phase < total_phases * 0.2:
        return int((1 - (phase - total_phases*0.1) / (total_phases*0.1)) * 255)  # ramp down
    elif phase < total_phases * 0.3:
        return int((phase - total_phases*0.2) / (total_phases*0.1) * 180)   # smaller pulse
    elif phase < total_phases * 0.4:
        return int((1 - (phase - total_phases*0.3) / (total_phases*0.1)) * 180)  # ramp down
    else:
        return 0   # long pause

TOTAL = 60   # total phases per heartbeat cycle

while True:
    for phase in range(TOTAL):
        brightness = heartbeat_value(phase, TOTAL)
        for i in range(config.NUMBER_PIXELS):
            strip[i] = (brightness, 0, 0)   # red heartbeat
        strip.write()
        utime.sleep_ms(20)
```

You should see the strip pulse red in a double-beat heartbeat rhythm — two quick flashes, then a pause, then repeat.

---

## Pattern: Comet Tail Animation

The **Comet Tail Animation** features a bright head pixel moving across the strip with a decaying brightness trail behind it. The **comet trail length** controls how many pixels the trail spans.

Before the code:
- `trail` — a list of brightness values for each pixel
- `DECAY` — how quickly trail brightness fades (0.8 = drops to 80% each frame)
- `TRAIL_LENGTH` controls apparent tail length — higher DECAY = longer tail

```python
trail = [0.0] * config.NUMBER_PIXELS
DECAY = 0.8
pos = 0

while True:
    # Decay all brightness
    for i in range(config.NUMBER_PIXELS):
        trail[i] *= DECAY

    # Set head to maximum
    trail[pos] = 1.0

    # Render the trail
    for i in range(config.NUMBER_PIXELS):
        b = int(trail[i] * 200)
        g = int(trail[i] * 80)
        strip[i] = (b, g, 0)   # orange-yellow comet

    strip.write()
    pos = (pos + 1) % config.NUMBER_PIXELS
    utime.sleep_ms(30)
```

You should see a bright orange-yellow comet head racing around the strip, leaving a fading warm trail.

To control trail length: change `DECAY`. At 0.95, the trail persists much longer. At 0.5, it disappears almost instantly after the head passes.

!!! info "Pixel thinks..."
    <img src="../../img/mascot/thinking.png" class="mascot-admonition-img" alt="Pixel thinking">
    The trail length is not a direct setting — it's an emergent property of the decay rate and animation speed. Want a longer trail? Slow down the animation OR increase the DECAY value. Want a shorter, crisper trail? Speed up or decrease DECAY. Two knobs, one effect.

---

## Pattern: Larson Scanner (Single-Color Scan)

The **Larson Scanner** (inspired by the KITT car from Knight Rider) is a bright hot-spot that bounces back and forth, with neighboring pixels lit proportionally dimmer based on their distance from the scan center.

Before the code, the **brightness formula** for each pixel:
- Distance from scan center → 0 = full brightness, higher distance = dimmer
- The **scanner width parameter** controls how wide the bright spot appears

```python
import math

scan_pos = 0.0    # position (float for smooth motion)
direction = 1.0
SPEED = 0.5       # pixels per frame
WIDTH = 3         # half-width of scanner glow

while True:
    for i in range(config.NUMBER_PIXELS):
        distance = abs(i - scan_pos)
        if distance < WIDTH:
            brightness = int((1 - distance / WIDTH) * 255)
        else:
            brightness = 0
        strip[i] = (brightness, 0, 0)   # red scanner

    strip.write()
    scan_pos += direction * SPEED

    if scan_pos >= config.NUMBER_PIXELS - 1:
        direction = -1
    elif scan_pos <= 0:
        direction = 1

    utime.sleep_ms(20)
```

You should see a red glow that sweeps back and forth, with pixels on either side of the center glowing proportionally dimmer.

Increase `WIDTH` for a wider, softer glow. Decrease it to 1 for a tight, intense spot.

### Dual-Direction Scan

The **Dual-Direction Scan** extends the scanner to two independent scan heads moving in opposite directions. The brightness is the maximum of the two scanners at each pixel.

```python
pos1, pos2 = 0.0, float(config.NUMBER_PIXELS - 1)
dir1, dir2 = 1.0, -1.0
WIDTH = 3

while True:
    for i in range(config.NUMBER_PIXELS):
        d1 = abs(i - pos1)
        d2 = abs(i - pos2)
        b1 = max(0, int((1 - d1 / WIDTH) * 200)) if d1 < WIDTH else 0
        b2 = max(0, int((1 - d2 / WIDTH) * 200)) if d2 < WIDTH else 0
        brightness = max(b1, b2)   # take the brighter of the two
        strip[i] = (0, 0, brightness)   # blue dual scanner

    strip.write()
    pos1 += dir1 * 0.5
    pos2 += dir2 * 0.5
    if pos1 >= config.NUMBER_PIXELS - 1 or pos1 <= 0: dir1 *= -1
    if pos2 >= config.NUMBER_PIXELS - 1 or pos2 <= 0: dir2 *= -1
    utime.sleep_ms(20)
```

You should see two blue glowing spots racing toward each other, bouncing off the ends and crossing paths in the middle.

---

## Sine-Based Breathing Effect

The **Sine-Based Breathing Effect** uses a sine wave to smoothly oscillate all pixel brightness. You learned the math in Chapter 11 — here's the full implementation:

```python
import math, utime

t = 0.0
SPEED = 0.05   # how fast the breath cycles

while True:
    # Sine gives -1 to 1; shift and scale to 0 to 1
    level = (math.sin(t) + 1) / 2

    for i in range(config.NUMBER_PIXELS):
        r = int(level * 100)
        g = int(level * 50)
        b = int(level * 200)
        strip[i] = (r, g, b)   # blue-purple breathing

    strip.write()
    t += SPEED
    utime.sleep_ms(20)
```

You should see the strip smoothly pulse between dark and a soft blue-purple color.

#### Diagram: Brightness Envelopes for Advanced Patterns

<details markdown="1">
<summary>Interactive chart: compare heartbeat, comet, scanner, and sine envelopes</summary>
Type: chart
**sim-id:** brightness-envelope-comparison
**Library:** Chart.js
**Status:** Specified

A tab-panel with four tabs, each showing the brightness envelope for one pattern:

1. **Heartbeat tab**: X axis = time steps (0–60), Y axis = brightness (0–255). Two narrow peaks (at t=6 and t=18) followed by a long flat zero section. Animates a moving dot.
2. **Comet Tail tab**: X axis = pixel index (0–29), Y axis = brightness. Exponential decay from a peak at position 20, falling toward zero to the left. A "head position" slider moves the peak.
3. **Larson Scanner tab**: X axis = pixel index, Y axis = brightness. A triangular peak centered at scan position. A "width" slider changes the peak width.
4. **Sine Breathing tab**: X axis = time, Y axis = brightness. Smooth sine curve, labeled with key points (peak, trough, half-way).

Each tab plays a live animation of the strip simulated below the chart. Canvas: 700 × 400 px. Responds to window resize.

Learning objective: Analyzing — the student can match a brightness envelope shape to the visual effect it produces.
</details>

---

## Expanding Ripple Rings

The **Expanding Ripple Rings** effect sends concentric brightness waves outward from a center point on each pulse trigger. This builds on the Chapter 13 ripple with improved pulse logic.

Before the code:
- `rings` — a list of (position, brightness) tuples, one per active ring
- Each frame, ring brightness decays and position expands
- New rings appear on a timer

```python
rings = []   # list of (center_offset, brightness)
pulse_timer = 0
CENTER = config.NUMBER_PIXELS // 2

while True:
    # Decay and expand existing rings
    new_rings = []
    for offset, brightness in rings:
        if brightness > 5:
            new_rings.append((offset + 1, int(brightness * 0.9)))
    rings = new_rings

    # Add a new ring pulse periodically
    pulse_timer += 1
    if pulse_timer > 20:
        rings.append((0, 200))   # new ring at center, full brightness
        pulse_timer = 0

    # Render
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (0, 0, 0)

    for offset, brightness in rings:
        left  = CENTER - offset
        right = CENTER + offset
        if 0 <= left  < config.NUMBER_PIXELS: strip[left]  = (0, 0, brightness)
        if 0 <= right < config.NUMBER_PIXELS: strip[right] = (0, 0, brightness)

    strip.write()
    utime.sleep_ms(40)
```

You should see blue rings appearing at the center and expanding outward, fading as they travel.

---

## Pattern Composition

**Pattern composition** means combining two or more simpler animations into one complex effect. The key technique: compute the output from each sub-pattern and blend the results.

Here's an example: a scanner pattern overlaid with a slow breathing effect.

```python
import math, utime

scan_pos = 0.0
scan_dir = 0.5
breath_t = 0.0

while True:
    breath_level = (math.sin(breath_t) + 1) / 2

    for i in range(config.NUMBER_PIXELS):
        # Scanner component
        distance = abs(i - scan_pos)
        scan_b = max(0, int((1 - distance / 3) * 200)) if distance < 3 else 0

        # Breathing background
        bg_r = int(breath_level * 30)
        bg_b = int(breath_level * 60)

        strip[i] = (bg_r + scan_b, 0, bg_b)

    strip.write()
    scan_pos += scan_dir
    if scan_pos >= config.NUMBER_PIXELS - 1 or scan_pos <= 0:
        scan_dir *= -1
    breath_t += 0.03
    utime.sleep_ms(20)
```

You should see a warm scanner gliding over a slow blue-breathing background — two patterns, one program.

---

## Try It Yourself

1. **Color heartbeat:** Modify the heartbeat to pulse through the color sequence red → orange → yellow across three consecutive heartbeats.

2. **Long comet:** Set DECAY to 0.97 in the comet tail. How far back does the tail reach? Count the pixels that are visibly lit.

3. **Wide scanner:** Increase the scanner WIDTH to 8. Compare with WIDTH = 2. Which looks more like a "laser sweep"?

4. **Composed effect:** Combine the comet tail and twinkle effects. The comet runs normally, but random pixels briefly spark with a different color as the comet passes nearby.

---

## Check Your Understanding

1. What is a "brightness envelope"? Give one example.
2. In the comet tail, what does the DECAY value control?
3. What two parameters control the appearance of the Larson scanner?
4. How does dual-direction scanning differ from the single-color scan?
5. What does `(math.sin(t) + 1) / 2` produce, and why is it useful?
6. What is "pattern composition"?
7. How does the expanding ripple rings effect track each ring's position over time?

---

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You've built the showstoppers! The Larson scanner, comet tail, heartbeat, and dual scanner are the effects that get noticed at Halloween, maker fairs, and costume contests. You also learned how to compose patterns together — which means from now on, "pattern + pattern = new pattern" is always an option. Level up!

## What's Next

In [Chapter 15](../15-electronics-fundamentals/index.md), you'll step back from code and go deeper into electronics — resistance, Ohm's Law, breadboard wiring, potentiometers, transistors, and the components you'll use in your capstone circuits.
