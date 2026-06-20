---
title: Raspberry Pi Pico Hardware and Development Environment
description: Meet the RP2040 microcontroller, learn GPIO pins, flash MicroPython firmware, and set up the Thonny IDE for writing and uploading programs to your Pico.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# Raspberry Pi Pico Hardware and Development Environment

## Summary

Introduces the RP2040 microcontroller, GPIO pins, MicroPython firmware, Thonny IDE, REPL, the Pico file system, firmware flashing, and debugging methodology, along with alternative platforms including the RP2040-Zero and Raspberry Pi 500 keyboard.

## Concepts Covered

This chapter covers the following 29 concepts from the learning graph:

1. MicroPython
2. Raspberry Pi Pico
3. Raspberry Pi Pico W
4. RP2040 Microcontroller
5. ARM Cortex M0+ Processor
6. Dual-Core Processing
7. 264 KB SRAM
8. 2 MB Flash Storage
9. GPIO Pins
10. Pin Numbering System
11. Firmware
12. UF2 File Format
13. BOOTSEL Button
14. Drag-and-Drop Flashing
15. REPL
16. main.py Auto-Run
17. Pico File System
18. Serial Console
19. USB Connectivity
20. Thonny IDE
21. Thonny File Manager
22. Uploading Files to Pico
23. Running Scripts on Pico
24. Serial Console Debugging
25. Raspberry Pi 500 Keyboard
26. Pi Keyboard RGB Effects
27. RP2040-Zero Form Factor
28. Debugging Methodology
29. Systematic Troubleshooting

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 2: Python Basics: Variables, Data Types, and Operators](../02-python-variables-types-operators/index.md)
- [Chapter 3: Python Functions, Modules, and Programming Best Practices](../03-python-functions-modules-practices/index.md)
- [Chapter 4: Python Control Flow, Loops, and Error Handling](../04-python-control-flow-loops/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 5! So far you've been writing Python on a laptop. Now you're going to put your code onto a tiny computer that fits in your palm — the Raspberry Pi Pico. Get ready to go from software to hardware. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Describe what the Raspberry Pi Pico is and what the RP2040 chip does
- Identify the GPIO pins and their numbering system
- Flash MicroPython firmware onto the Pico
- Use the Thonny IDE to write, upload, and run Python programs on the Pico
- Use the REPL to test code interactively
- Explain what happens when the Pico boots and finds `main.py`
- Apply a systematic debugging method when something doesn't work

## What You'll Need

- A Raspberry Pi Pico or Pico W
- A USB cable (micro-USB to USB-A)
- A computer with Thonny IDE installed (download at thonny.org)

---

## Meet the Raspberry Pi Pico

The **Raspberry Pi Pico** is a small green circuit board about the size of a stick of gum. It costs around four dollars and can run Python programs that control LEDs, read sensors, and drive motors. Unlike a full computer, it has no screen, no keyboard, and no operating system — just a chip, some memory, and a row of pins.

The Pico's brain is the **RP2040 microcontroller** — a chip designed by Raspberry Pi specifically for this board. A **microcontroller** is a small computer-on-a-chip that contains a processor, memory, and input/output controls all in one package.

Inside the RP2040 are two **ARM Cortex M0+ processors** running at up to 133 MHz. Having two processors is called **dual-core processing**. For our LED projects, one core does all the work, but knowing two exist helps you understand why the Pico is fast enough for smooth animations.

The Pico has two types of memory:

- **264 KB SRAM** (Static RAM) — the working memory where your running program and its variables live. It's fast but temporary — everything in SRAM disappears when you unplug the Pico.
- **2 MB Flash Storage** — permanent storage that keeps your files (including `main.py`) even when power is off. 2 MB is enough for thousands of lines of code.

The **Raspberry Pi Pico W** is the same board with a Wi-Fi chip added. For this course, you can use either the Pico or Pico W — the LED programming is identical on both.

#### Diagram: Raspberry Pi Pico Hardware Overview

<details markdown="1">
<summary>Interactive diagram: Pico board with labeled parts</summary>
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
</details>

---

## GPIO Pins: The Pico's Hands

The Pico has 40 pins along its edges. Many of them are **GPIO pins** — **General Purpose Input/Output** pins. A GPIO pin can:

- Output a high voltage (3.3 V, meaning "on") or low voltage (0 V, meaning "off") to drive an LED or signal a device
- Read whether an external signal is high or low (for reading a button press, for example)

The **pin numbering system** uses two kinds of labels:

- **Physical pin numbers** — the actual position on the board (1–40, counting around the chip)
- **GP numbers** — the GPIO function name printed on most diagrams (GP0, GP1, GP2, …, GP28)

In MicroPython code, you always use the GP number, not the physical position. For example, the NeoPixel data line in this course connects to GP0, and in code you write `machine.Pin(0)`.

The following pins have special roles you'll use in this course:

| Pin Name | Function | Use in this course |
|---|---|---|
| GP0 | GPIO (digital) | NeoPixel data line |
| GP25 | Built-in LED | Quick test: blink without extra hardware |
| ADC0 (GP26) | Analog input | Read photoresistor (light sensor) |
| ADC1 (GP27) | Analog input | Second analog sensor |
| GND | Ground | Required for every circuit |
| VSYS | Power in | Battery or USB power input |
| 3V3 OUT | 3.3 V out | Power for small sensors |

!!! tip "Pixel's tip"
    <img src="../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel points upward">
    Every Pico diagram you'll ever find online uses GP numbers. When a tutorial says "connect to GP0", that's the number you use in your Python code. The physical pin number (the position around the edge) is mainly for physical wiring — not for code.

---

## What Is Firmware and MicroPython?

Your Pico needs to know what *language* to speak before it can run your programs. That knowledge is called **firmware** — software stored permanently in flash memory that controls basic hardware behavior.

Out of the box, the Pico ships with its own firmware. To run Python programs, you need to replace that firmware with **MicroPython** — a version of Python 3 designed to run on tiny microcontrollers. MicroPython fits in less than 1 MB and includes just the Python features you need for hardware control.

### Flashing MicroPython with a UF2 File

Replacing firmware is called **flashing**. The process uses a special file format called **UF2** (USB Flashing Format). Here's how it works:

1. Hold down the **BOOTSEL button** (the small white button near the USB connector)
2. While holding BOOTSEL, plug the USB cable into your computer
3. A new drive called **RPI-RP2** appears on your computer — like a USB flash drive
4. Download the MicroPython UF2 file from the official MicroPython site for Raspberry Pi Pico
5. Drag and drop the UF2 file onto the **RPI-RP2** drive
6. The Pico automatically restarts with MicroPython installed

This is called **drag-and-drop flashing**. The Pico erases its old firmware and writes the new UF2 in seconds. After the restart, the RPI-RP2 drive disappears — that means it worked.

---

## Setting Up Thonny IDE

**Thonny** is a Python code editor designed for learners. It has a built-in connection to the Pico that makes writing, uploading, and running programs easy.

Download Thonny from thonny.org if you haven't already. After installing and opening it:

1. Click **Tools → Options → Interpreter**
2. Choose **MicroPython (Raspberry Pi Pico)** from the dropdown
3. Choose the correct USB port (on Windows it looks like `COM3`, on Mac like `/dev/tty.usbmodem1`)
4. Click **OK**

You should see `MicroPython vX.X.X; Raspberry Pi Pico` in the Shell panel at the bottom. That means Thonny is connected.

### The Thonny Layout

Thonny has three main areas:

- **Editor panel** (top) — where you write your Python code
- **Shell / REPL panel** (bottom) — where you see output and can type commands interactively
- **File Manager** (optional panel on the left) — shows files on both your computer and the Pico

### Uploading Files to the Pico

To run a program on the Pico, you need to upload it to the Pico's file system. Here's how:

1. Write your code in the editor
2. Click **File → Save As**
3. When asked where to save, choose **Raspberry Pi Pico**
4. Name the file (e.g., `my_program.py`)
5. Click **Save**

The file is now stored in the Pico's **flash storage**. You can see it in the File Manager under the Pico section.

To run the file you just uploaded, click the green **Run** button (▶) in Thonny.

### The main.py Auto-Run Behavior

The Pico has a special rule: when it boots (powers up or restarts), it automatically runs a file called **`main.py`** if one exists. This is how your project runs without a computer attached.

When you're developing, you usually save files with descriptive names like `fade.py` and run them from Thonny. When you want the project to run standalone (battery powered, no computer), rename the file to `main.py` or save it as `main.py` directly.

!!! warning "Watch out!"
    <img src="../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    If you have a `main.py` on your Pico that crashes immediately, you might not be able to connect to Thonny — because the Pico keeps restarting. Hold Ctrl+C in the Thonny Shell right after plugging in to interrupt the program before it crashes again. Then you can fix and re-upload `main.py`.

---

## Using the REPL for Interactive Testing

The **REPL** stands for **Read-Eval-Print Loop**. It's the interactive console in Thonny's Shell panel. You type a line of Python, press Enter, and the Pico runs it immediately and shows the result.

Try typing these in the REPL after connecting your Pico:

```python
>>> print("Hello from the Pico!")
Hello from the Pico!
>>> 2 + 3
5
>>> import machine
>>> led = machine.Pin(25, machine.Pin.OUT)
>>> led.on()
```

After `led.on()`, the small green LED on the Pico board should light up. Type `led.off()` to turn it off. This is how you test ideas without writing a full program.

The **Serial Console** is the same channel the REPL uses. When your running program calls `print()`, the output appears in the Thonny Shell. This makes `print()` a powerful debugging tool — you can print variable values while your program runs.

### Pico File System

The Pico's **file system** stores your Python files permanently in flash memory. You can:

- Upload files from your computer using Thonny's File Manager or Save As dialog
- Download files from the Pico back to your computer the same way
- Delete files you no longer need (right-click in the File Manager)

Typical files you'll have on your Pico:

| File | Purpose |
|---|---|
| `main.py` | Runs automatically on boot |
| `config.py` | Hardware settings (pin numbers, strip length) |
| `animation.py` | A library file with animation functions |

---

## Alternative Platforms

This course focuses on the standard Pico, but two other RP2040-based boards are worth knowing about.

### RP2040-Zero

The **RP2040-Zero** is a tiny version of the Pico — about half the size — made by Waveshare. It uses the same RP2040 chip and runs MicroPython identically. It's popular for wearable projects where every millimeter counts. The GPIO pinout is slightly different, so always check the diagram for whichever board you're using.

### Raspberry Pi 500 Keyboard

The **Raspberry Pi 500** is a full keyboard with a Raspberry Pi 5 computer built into it. Some versions include RGB LED keys, making it a fun platform for writing **Pi Keyboard RGB Effects** — lighting effects that run directly on the keyboard hardware. The underlying programming concepts are identical to what you're learning here.

---

## Debugging Methodology: A Systematic Approach

When your program doesn't work, resist the urge to change things randomly. **Debugging methodology** means following a logical process to find the root cause.

**Systematic troubleshooting** follows these steps:

1. **Identify the symptom** — what exactly is wrong? ("The LEDs don't light up" is more useful than "it's broken.")
2. **Form a hypothesis** — what could cause that symptom? ("Maybe the wrong pin number is in config.py")
3. **Test one thing at a time** — change only one variable and observe what happens
4. **Use print() liberally** — print variable values at key points to verify assumptions
5. **Check the simple things first** — power, connections, and file name before digging into logic

Here's a quick checklist for the most common Pico + LED problems:

- Is the USB cable plugged in fully?
- Does Thonny show "MicroPython" in the Shell (not a connection error)?
- Is `config.py` on the Pico with the correct `NEOPIXEL_PIN` and `NUMBER_PIXELS`?
- Is the LED strip's data wire connected to the correct GPIO pin?
- Did you call `strip.write()` after setting pixel colors?

!!! success "You've got this!"
    <img src="../../img/mascot/encouraging.png" class="mascot-admonition-img" alt="Pixel gives a thumbs-up">
    Setting up new hardware always takes a few tries. If something doesn't connect right away, run through the checklist above. Almost every first-time setup issue is a cable, a pin number, or a missing `strip.write()`. You're closer than you think!

---

## Try It Yourself

1. **Blink the built-in LED:** Open Thonny, connect to your Pico, and type these lines in the REPL one at a time:
   ```python
   import machine, utime
   led = machine.Pin(25, machine.Pin.OUT)
   led.on()
   utime.sleep(1)
   led.off()
   ```
   You should see the small green LED blink once.

2. **REPL math:** In the REPL, type `2 ** 8` and press Enter. What do you get? (Hint: `**` is "to the power of".)

3. **Upload a file:** Write a program that prints `"Pico is alive!"` every second in an infinite loop. Save it as `test.py` on the Pico and run it from Thonny. Press Ctrl+C to stop it.

---

## Check Your Understanding

1. What does RP2040 stand for, and what is a microcontroller?
2. What is the difference between SRAM and flash storage on the Pico?
3. What does BOOTSEL stand for, and when do you press it?
4. What is the difference between a GP number and a physical pin number?
5. What happens when the Pico finds a file called `main.py` on boot?
6. What is the REPL and what can you do with it?
7. List the first three steps of the debugging methodology.

---

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You've met your hardware partner! You know what the RP2040 chip is, how to flash MicroPython, how to use Thonny to upload and run code, and how to debug problems systematically. You're ready to start writing programs that control real LEDs. That's huge!

## What's Next

In [Chapter 6](../06-micropython-apis-and-electronics/index.md), you'll learn the MicroPython APIs that control GPIO pins, generate PWM signals, read analog sensors, and drive NeoPixels — plus the basic electrical concepts you need to wire everything safely.
