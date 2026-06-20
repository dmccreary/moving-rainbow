---
title: MicroPython APIs, GPIO Control, and Electrical Fundamentals
description: Learn the machine.Pin, PWM, ADC, utime, urandom, and neopixel MicroPython APIs, and understand the five electrical concepts you need to wire LED circuits safely.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# MicroPython APIs, GPIO Control, and Electrical Fundamentals

## Summary

Covers the machine.Pin, PWM, ADC, utime, urandom, and neopixel MicroPython APIs for hardware control, alongside five foundational electrical concepts—voltage, current, polarity, ground, and milliamps—needed to safely wire LED circuits.

## Concepts Covered

This chapter covers the following 26 concepts from the learning graph:

1. machine.Pin Class
2. Digital Output Mode
3. Digital Input Mode
4. Pin.high() Method
5. Pin.low() Method
6. Pin.value() Method
7. Pulse Width Modulation
8. PWM Frequency Setting
9. PWM Duty Cycle
10. Analog to Digital Converter
11. 16-Bit ADC Resolution
12. ADC.read_u16() Method
13. utime Module
14. sleep() Function
15. ticks_ms() Function
16. ticks_us() Function
17. localtime() Function
18. urandom Module
19. randint() Function
20. neopixel Module
21. NeoPixel Class
22. Voltage
23. Electrical Current
24. Electrical Polarity
25. Ground (GND)
26. Milliamps (mA)

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 2: Python Basics: Variables, Data Types, and Operators](../02-python-variables-types-operators/index.md)
- [Chapter 3: Python Functions, Modules, and Programming Best Practices](../03-python-functions-modules-practices/index.md)
- [Chapter 4: Python Control Flow, Loops, and Error Handling](../04-python-control-flow-loops/index.md)
- [Chapter 5: Raspberry Pi Pico Hardware and Development Environment](../05-raspberry-pi-pico-hardware/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 6! Your Pico is set up and ready. Now you're going to learn the tools MicroPython gives you to talk to hardware — and the electrical basics that keep everything safe. This is where code meets the real world. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Use `machine.Pin` to set GPIO pins high or low and read their state
- Explain what PWM is and set its frequency and duty cycle
- Read analog sensor values with the ADC
- Use `utime` to create delays and measure elapsed time
- Generate random numbers with `urandom`
- Create and control a NeoPixel strip with the `neopixel` module
- Describe voltage, current, polarity, ground, and milliamps in plain terms

## What You'll Need

- Raspberry Pi Pico connected via USB with MicroPython installed
- Thonny IDE open and connected
- NeoPixel LED strip connected to GP0 (data) and power

---

## Five Electrical Concepts You Must Know

Before we look at MicroPython code, you need five electrical building blocks. Every wiring decision you make for the rest of this course depends on these ideas.

### Voltage

**Voltage** is the "pressure" that pushes electrical charge through a circuit. It's measured in **volts (V)**. Think of voltage like the pressure of water in a hose — higher pressure pushes more water through. Your USB port provides 5 V. The Pico's GPIO pins output 3.3 V.

### Electrical Current

**Electrical current** is the flow of charge through a wire. It's measured in **amps (A)** or for small circuits in **milliamps (mA)**. One milliamp is one-thousandth of an amp. A typical NeoPixel LED draws up to 20 mA at full brightness. Your USB port can supply up to 500 mA — enough for about 25 pixels at full white.

### Milliamps (mA)

**Milliamps (mA)** is the unit you'll use most often in this course. Remember: **20 mA per NeoPixel pixel at full white**. Multiply the number of pixels by 20 to estimate peak current draw. A 30-pixel strip at full white needs 600 mA — more than a single USB port can safely supply.

### Electrical Polarity

**Electrical polarity** means that electricity flows in one direction. Every power source has a positive terminal (+) and a negative terminal (−). Connect them the right way and everything works. Connect them backward and you can damage components. On LED strips, the wires are color-coded: red is positive (+5 V), black or white is negative (GND).

### Ground (GND)

**Ground (GND)** is the common reference point for all voltages in your circuit. It is always 0 V. Every component in a circuit must connect back to ground to complete the electrical path. On the Pico, any pin labeled GND works. The GND pin on the Pico and the GND wire on the LED strip must connect together — always.

The table below summarizes these five concepts:

| Concept | Symbol | Unit | What It Means |
|---|---|---|---|
| Voltage | V | Volts (V) | Electrical "pressure" — how hard charge is pushed |
| Current | I | Amps (A) or milliamps (mA) | How much charge flows per second |
| Milliamps | mA | mA | 1/1000 of an amp — used for small circuits |
| Polarity | +/− | None | Direction — connect + to + and − to − |
| Ground | GND | 0 V | Common reference; must connect to all components |

!!! warning "Watch out!"
    <img src="../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    Always connect GND first. If you connect power before ground, some components can get a voltage spike and break. Build the habit now: ground first, power second.

---

## The machine Module: Controlling GPIO Pins

MicroPython's `machine` module gives you control over the Pico's hardware. Before exploring each API, import the module:

```python
import machine
```

### machine.Pin Class

The **`machine.Pin` class** represents a single GPIO pin. The two most common modes are **digital output** (the Pico drives a signal) and **digital input** (the Pico reads a signal).

To create a Pin object, you pass the GP number and the mode:

```python
led = machine.Pin(25, machine.Pin.OUT)   # GP25 as digital output
btn = machine.Pin(15, machine.Pin.IN)    # GP15 as digital input
```

**Digital Output Methods:**

- **`Pin.high()`** — sets the pin to 3.3 V (logic "1")
- **`Pin.low()`** — sets the pin to 0 V (logic "0")
- **`Pin.value(1)`** — equivalent to `high()`; **`Pin.value(0)`** equivalent to `low()`

**Digital Input:**

- **`Pin.value()`** with no argument — reads the pin; returns `1` (high) or `0` (low)

Here's a blink example using the built-in LED:

```python
import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.high()         # turn on
    utime.sleep(0.5)   # wait half a second
    led.low()          # turn off
    utime.sleep(0.5)
```

You should see the small green LED on the Pico board blink at one blink per second.

### Pulse Width Modulation (PWM)

**Pulse Width Modulation (PWM)** is a technique for controlling brightness or motor speed by switching a pin on and off very fast. Instead of a constant 3.3 V, the pin switches between 3.3 V and 0 V hundreds or thousands of times per second. The proportion of time it spends "on" is called the **duty cycle**.

Before writing PWM code, here are the key terms:
- **PWM Frequency** — how many on/off cycles per second, in Hertz (Hz). For LEDs, 1000 Hz works well (1000 cycles per second — too fast for the eye to see flicker).
- **PWM Duty Cycle** — the percentage of each cycle that the pin is "on". 0 = always off, 65535 = always on (MicroPython uses a 16-bit value, 0–65535).

```python
import machine

pwm = machine.PWM(machine.Pin(25))   # attach PWM to the built-in LED pin
pwm.freq(1000)                        # set frequency to 1000 Hz
pwm.duty_u16(32768)                   # 50% duty cycle — half brightness
```

You should see the built-in LED glow at roughly half brightness. Change `32768` to `0` for off and `65535` for full brightness.

### Analog to Digital Converter (ADC)

The **Analog to Digital Converter (ADC)** reads an analog voltage (anything from 0 to 3.3 V) and converts it to a number your program can use. The Pico's ADC has **16-bit resolution**, meaning it produces values from 0 to 65535.

Before reading the code, here's what the numbers mean: 0 represents 0 V (no signal), and 65535 represents 3.3 V (maximum signal). Values in between are proportional.

The **`ADC.read_u16()` method** takes a reading and returns a value from 0 to 65535:

```python
import machine

sensor = machine.ADC(26)         # create ADC on pin GP26 (ADC0)
reading = sensor.read_u16()      # take a reading (0–65535)
print(reading)                   # print to the Thonny console
```

You should see a number appear in the Thonny Shell. If nothing is connected to GP26, you'll see a small noisy value (that's normal — unconnected analog pins pick up electrical noise).

---

## The utime Module: Timing and Delays

The **`utime` module** provides time-related functions for MicroPython programs.

| Function | What It Does | Example |
|---|---|---|
| `sleep(seconds)` | Pause for this many seconds | `utime.sleep(1)` — pause 1 second |
| `sleep_ms(ms)` | Pause for this many milliseconds | `utime.sleep_ms(500)` — pause 0.5 s |
| `ticks_ms()` | Milliseconds since boot | Used to measure elapsed time |
| `ticks_us()` | Microseconds since boot | For very precise timing |
| `localtime()` | Current time as a tuple | Used in clock displays |

The `sleep()` function is the one you'll use most often to control animation speed. The `ticks_ms()` function is useful when you want something to happen after a certain amount of time *without stopping the whole program*:

```python
import utime

start = utime.ticks_ms()           # record the current time

# ... do other things here ...

elapsed = utime.ticks_ms() - start
if elapsed > 1000:                 # if more than 1000 ms have passed
    print("One second has passed!")
```

The **`localtime()` function** returns the current date and time as a tuple `(year, month, day, weekday, hour, minute, second, microsecond)`. You'll use this in the clock display animation in a later chapter.

---

## The urandom Module: Random Numbers

The **`urandom` module** generates random numbers. The most useful function is `randint()`.

**`randint(a, b)`** returns a random integer between `a` and `b`, inclusive. Both endpoints are included.

```python
import urandom

color = urandom.randint(0, 255)    # random number from 0 to 255
print(color)
```

You should see a different number every time you run this. Random numbers power effects like twinkle (random pixels light up) and candle flicker (random brightness variation).

!!! tip "Pixel's tip"
    <img src="../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel points upward">
    `urandom.randint(0, 255)` is your best friend for LED effects. Use it to pick a random pixel index, a random color value, or a random delay time. The combinations are endless!

---

## The neopixel Module: Controlling LED Strips

The **`neopixel` module** is the MicroPython library specifically designed for WS2812B addressable LEDs. It handles all the complex timing needed to send color data to the strip.

### NeoPixel Class

The **`NeoPixel` class** represents your entire LED strip. To create one, you need two things: the pin the data wire is connected to, and how many pixels are on your strip. In this course, we always get these from `config.py`:

```python
import neopixel
import machine
import config

strip = neopixel.NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
```

After creating `strip`, you set pixel colors by indexing it like a list. Each pixel takes an RGB tuple `(red, green, blue)` with values from 0 to 255. Then you call `strip.write()` to actually send the data:

```python
strip[0] = (255, 0, 0)    # pixel 0 = red
strip[1] = (0, 255, 0)    # pixel 1 = green
strip[2] = (0, 0, 255)    # pixel 2 = blue
strip.write()              # send all the data at once
```

You should see the first three LEDs light up red, green, and blue.

#### Diagram: MicroPython API Connections


<iframe src="../../sims/micropython-api-connections/main.html" width="100%" height="682px" scrolling="no"></iframe>
[Run MicroPython API Connections Fullscreen](../../sims/micropython-api-connections/main.html)

<details markdown="1">
<summary>Interactive diagram: MicroPython APIs and hardware connections</summary>
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
</details>

---

## Putting It Together: A First NeoPixel Program

Here's a complete program that uses many of the APIs from this chapter. Read the comments — they explain each step.

Before reading the code, here are the key parameters:
- `config.NEOPIXEL_PIN` — the GP number your data wire connects to
- `config.NUMBER_PIXELS` — how many LEDs are on your strip
- `utime.sleep_ms(50)` — 50 milliseconds per frame = roughly 20 frames per second

```python
import neopixel
import machine
import utime
import urandom
import config

# Create the strip object
strip = neopixel.NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

while True:
    # Pick a random pixel and a random color
    pixel = urandom.randint(0, config.NUMBER_PIXELS - 1)
    r = urandom.randint(0, 255)
    g = urandom.randint(0, 255)
    b = urandom.randint(0, 255)

    strip[pixel] = (r, g, b)   # set that pixel
    strip.write()               # send to the strip
    utime.sleep_ms(50)          # wait 50 ms before the next update
```

You should see random pixels flashing random colors — a quick preview of the twinkle effect you'll build properly in Chapter 12.

---

## Try It Yourself

1. **Blink faster:** Modify the LED blink example to blink 5 times per second instead of 1.

2. **Read ADC:** Connect a wire from 3V3 to GP26 and run the ADC example. What value do you get? Then connect the wire from GND to GP26. What value do you get?

3. **Random colors:** Modify the final program so it only changes the color of pixel 0 — not a random pixel. Use `urandom.randint` just for the colors.

4. **Timed blink:** Use `ticks_ms()` to make an LED blink once per second without using `sleep()`. (Hint: record the start time, then check `ticks_ms() - start > 1000`.)

---

## Check Your Understanding

1. What is the difference between voltage and current?
2. Why is it important that every component connects back to GND?
3. What does `Pin.high()` do to the voltage on that pin?
4. What values does `ADC.read_u16()` return, and what do the extremes represent?
5. What does PWM duty cycle mean? What value means "always on"?
6. What two arguments do you pass to `NeoPixel()` to create a strip?
7. Why do you need to call `strip.write()` after setting pixel colors?

---

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You've got the full toolkit now! You can drive GPIO pins, dim LEDs with PWM, read sensors with the ADC, control timing with utime, add randomness with urandom, and talk to NeoPixel strips directly. Plus you understand the electrical basics that keep everything safe. Let's build some animations!

## What's Next

In [Chapter 7](../07-rgb-color-theory/index.md), you'll explore the RGB color model in depth — how light mixes differently than paint, how the color wheel works, and why some color combinations look amazing together.
