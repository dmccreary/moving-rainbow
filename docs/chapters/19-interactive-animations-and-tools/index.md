---
title: Interactive Animations and Development Tools
description: Combine buttons, sensors, and animations into polished multi-mode programs, then master the full development toolchain — Thonny, Git, GitHub, config.py, and firmware flashing.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# Interactive Animations and Development Tools

## Summary

Connects input and animation by implementing mode-based, button-triggered, photo-reactive, and sensor-driven animations, then covers the complete development toolchain: Git version control, GitHub repositories, Thonny IDE deep features, firmware flashing workflows, and the config.py hardware abstraction pattern.

## Concepts Covered

This chapter covers the following 40 concepts from the learning graph:

1. Multi-Pattern Program
2. Pattern Switching Logic
3. Animation State Variable
4. Photo-Reactive Animation
5. Button-Triggered Animation
6. Sensor-Driven Animation
7. Mode-Based Animation
8. Animation Restart Logic
9. Interactive Mode Controller
10. Input Abstraction Layer
11. Thonny IDE Overview
12. Thonny REPL Panel
13. Thonny Run Controls
14. Syntax Highlighting
15. Code Autocomplete
16. Serial Console in Thonny
17. REPL Interactive Testing
18. File Upload Workflow
19. Running Script on Pico
20. Git Version Control
21. git clone Command
22. git add Command
23. git commit Command
24. git push Command
25. git pull Command
26. git status Command
27. GitHub Repository
28. Repository Structure
29. README File Creation
30. File Organization in Repo
31. Firmware Flashing Workflow
32. UF2 Drag-and-Drop Process
33. Python Module Paths
34. config.py Module Pattern
35. Hardware Abstraction Layer
36. Cross-Kit Compatibility
37. Thonny Package Manager
38. MicroPython Standard Library
39. Code Backup with GitHub
40. Commit Message Writing

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 2: Python Basics: Variables, Data Types, and Operators](../02-python-variables-types-operators/index.md)
- [Chapter 3: Python Functions, Modules, and Programming Best Practices](../03-python-functions-modules-practices/index.md)
- [Chapter 4: Python Control Flow, Loops, and Error Handling](../04-python-control-flow-loops/index.md)
- [Chapter 5: Raspberry Pi Pico Hardware and Development Environment](../05-raspberry-pi-pico-hardware/index.md)
- [Chapter 6: MicroPython APIs, GPIO Control, and Electrical Fundamentals](../06-micropython-apis-and-electronics/index.md)
- [Chapter 9: NeoPixel Programming: Pixels, Colors, and the NeoPixel Library](../09-neopixel-programming/index.md)
- [Chapter 12: Basic LED Animation Patterns](../12-basic-animation-patterns/index.md)
- [Chapter 13: Intermediate Animation Techniques](../13-intermediate-animations/index.md)
- [Chapter 14: Advanced Animation Patterns: Comet, Scanner, and Candle](../14-advanced-animation-patterns/index.md)
- [Chapter 18: Input Devices, Sensors, and State Machines](../18-input-devices-and-sensors/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to Chapter 19! This is where everything connects. You have animations from Chapters 12–14, and inputs from Chapter 18. Now you'll wire them together into programs people can actually interact with — then learn the pro tools to save, share, and version your work. This is the full-stack maker chapter. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Build a complete multi-mode interactive animation program with button cycling
- Implement photo-reactive and sensor-driven animations
- Use Thonny's REPL, autocomplete, package manager, and console features
- Use the six core Git commands to save and manage your code
- Create and organize a GitHub repository for your projects
- Apply the `config.py` hardware abstraction pattern for cross-kit compatibility
- Flash new firmware onto the Pico using the UF2 drag-and-drop process

## What You'll Need

- Raspberry Pi Pico with NeoPixel strip connected
- Thonny IDE installed and connected
- A momentary push button wired with debouncing (from Chapter 18)
- Optional: photoresistor for sensor-driven animations
- A GitHub account (free at github.com)
- Git installed on your computer

---

## Multi-Pattern Programs

A **multi-pattern program** is one that can run several different animations, switching between them based on user input. Before Chapter 18, your programs ran one animation forever. Now you can build programs where every button press changes the experience.

Before reading the design, here are two key terms:
- **Animation state variable** — an integer that tracks which animation is currently active
- **Pattern switching logic** — the code that reads the current state and calls the right animation function

**Mode-Based Animation** is the design pattern that holds it all together:

1. Each animation gets a unique mode number (0, 1, 2 …)
2. A button press increments the mode (with wrap-around)
3. The main loop calls the animation function for the current mode
4. Each animation function runs for one frame and returns

### Animation Restart Logic

When the mode changes, many animations need to reset their state. Without this, a comet tail animation might start mid-trail when you switch into it — which looks glitchy.

**Animation Restart Logic** resets all animation-specific variables when the mode changes:

```python
import machine, utime, math, neopixel
import config

strip = neopixel.NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)

# ── Button setup ──────────────────────────────────────────────────
btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
prev_btn = 1
last_press = 0
DEBOUNCE_MS = 30
NUM_MODES = 4
mode = 0
prev_mode = -1   # forces a restart on first loop iteration

# ── Per-animation state ───────────────────────────────────────────
offset = 0                      # rainbow offset
scan_pos = 0.0                  # scanner position
scan_dir = 1.0
trail = [0.0] * config.NUMBER_PIXELS  # comet trail
breath_t = 0.0                  # breathing phase

def restart_animation(m):
    global offset, scan_pos, scan_dir, trail, breath_t
    offset = 0
    scan_pos = 0.0
    scan_dir = 1.0
    trail = [0.0] * config.NUMBER_PIXELS
    breath_t = 0.0
```

The `restart_animation` function initializes everything back to a known clean state whenever the mode changes.

### Pattern Switching Logic

Before reading the complete loop, here's how the switching works:

1. Check if `mode != prev_mode` — if so, call `restart_animation()` and record the new `prev_mode`
2. Check the button — if pressed, increment `mode`
3. Run one frame of the current animation function

```python
def frame_rainbow():
    global offset
    for i in range(config.NUMBER_PIXELS):
        hue = int((i * 256 / config.NUMBER_PIXELS + offset) % 256)
        # Simple hue-to-RGB (wheel function from Chapter 10)
        if hue < 85:
            strip[i] = (255 - hue * 3, hue * 3, 0)
        elif hue < 170:
            hue -= 85
            strip[i] = (0, 255 - hue * 3, hue * 3)
        else:
            hue -= 170
            strip[i] = (hue * 3, 0, 255 - hue * 3)
    strip.write()
    offset = (offset + 2) % 256

def frame_scanner():
    global scan_pos, scan_dir
    for i in range(config.NUMBER_PIXELS):
        d = abs(i - scan_pos)
        b = max(0, int((1 - d / 3) * 220)) if d < 3 else 0
        strip[i] = (b, 0, b // 2)
    strip.write()
    scan_pos += scan_dir * 0.6
    if scan_pos >= config.NUMBER_PIXELS - 1 or scan_pos <= 0:
        scan_dir *= -1

def frame_comet():
    global trail
    for i in range(config.NUMBER_PIXELS):
        trail[i] *= 0.82
    pos = int(utime.ticks_ms() / 30) % config.NUMBER_PIXELS
    trail[pos] = 1.0
    for i in range(config.NUMBER_PIXELS):
        b = int(trail[i] * 200)
        strip[i] = (b, int(b * 0.4), 0)
    strip.write()

def frame_breathe():
    global breath_t
    level = (math.sin(breath_t) + 1) / 2
    for i in range(config.NUMBER_PIXELS):
        strip[i] = (int(level * 80), int(level * 30), int(level * 200))
    strip.write()
    breath_t += 0.04

FRAMES = [frame_rainbow, frame_scanner, frame_comet, frame_breathe]

# ── Main loop ─────────────────────────────────────────────────────
while True:
    # Restart on mode change
    if mode != prev_mode:
        restart_animation(mode)
        prev_mode = mode

    # Read button
    state = btn.value()
    if state == 0 and prev_btn == 1:
        if utime.ticks_ms() - last_press > DEBOUNCE_MS:
            mode = (mode + 1) % NUM_MODES
            last_press = utime.ticks_ms()
    prev_btn = state

    # Run one frame
    FRAMES[mode]()
    utime.sleep_ms(20)
```

You should see a moving rainbow, then a scanner, then a comet tail, then breathing color — one button press per switch. Each animation starts cleanly from its initial state when you enter it.

---

## Input Abstraction Layer

An **Input Abstraction Layer** is a helper module that handles all the low-level input details (pin setup, debouncing, state tracking) so the main program can just call `button_pressed()` without thinking about those details.

Before the code, here's the value: if you ever change which GPIO pin your button is on, you update one line in the abstraction layer — not every place in the main program that checks the button.

```python
# input_helpers.py  — save this file to the Pico alongside main.py
import machine, utime

class Button:
    def __init__(self, pin_num, debounce_ms=30):
        self.pin = machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_UP)
        self.debounce_ms = debounce_ms
        self._prev = 1
        self._last_press = 0

    def just_pressed(self):
        state = self.pin.value()
        pressed = (state == 0 and self._prev == 1 and
                   utime.ticks_ms() - self._last_press > self.debounce_ms)
        if pressed:
            self._last_press = utime.ticks_ms()
        self._prev = state
        return pressed
```

With this class, `btn.just_pressed()` returns `True` exactly once per button press. Your main loop becomes clean:

```python
from input_helpers import Button
btn = Button(15)

while True:
    if btn.just_pressed():
        mode = (mode + 1) % NUM_MODES
    FRAMES[mode]()
    utime.sleep_ms(20)
```

---

## Interactive Mode Controller

The **Interactive Mode Controller** is the fully assembled program structure that manages:
- Multiple animation patterns
- Button cycling
- Photo-reactive or sensor-driven override
- Animation restart on mode change

**Photo-Reactive Animation**: the ADC reads the photoresistor and maps it to a brightness parameter that all animations use. In bright room conditions, animations run dimmer; in dark rooms, they run brighter.

```python
ldr = machine.ADC(26)

def get_brightness():
    raw = ldr.read_u16()
    # Map 20000–55000 to 60–220 brightness (inverted: darker = brighter LEDs)
    clamped = max(20000, min(55000, raw))
    return int(220 - (clamped - 20000) / 35000 * 160)
```

**Sensor-Driven Animation**: instead of a fixed color, the animation hue or speed responds to sensor values:

```python
def frame_sensor_rainbow():
    global offset
    speed = int(ldr.read_u16() / 65535 * 6) + 1   # 1–7 pixels per frame
    for i in range(config.NUMBER_PIXELS):
        hue = int((i * 256 / config.NUMBER_PIXELS + offset) % 256)
        # ... wheel function ...
    strip.write()
    offset = (offset + speed) % 256
```

Moving the photoresistor from dark to bright changes the rainbow speed from slow to fast.

**Button-Triggered Animation**: a specific mode that only animates while the button is held, then stops when released. Useful for a "flash" or "strobe" effect:

```python
def frame_hold_to_flash():
    if btn.pin.value() == 0:   # held
        for i in range(config.NUMBER_PIXELS):
            strip[i] = (220, 220, 220)
    else:
        for i in range(config.NUMBER_PIXELS):
            strip[i] = (0, 0, 0)
    strip.write()
```

!!! tip "Pixel says..."
    <img src="../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel points upward with a smile">
    The "frame function returns immediately" rule is what makes all of this work. If an animation used `time.sleep()` inside it, the button wouldn't respond while that sleep ran. Frame-based animation gives both smooth visuals AND fast input response.

---

## Thonny IDE Deep Features

You've been using Thonny since Chapter 5. Now let's explore every feature it provides.

### Thonny REPL Panel

The **Thonny REPL Panel** (also called the Shell) is the interactive Python console at the bottom of the Thonny window. REPL stands for Read–Eval–Print Loop.

**REPL Interactive Testing** means typing Python expressions directly and seeing the result immediately — without writing a full file. This is ideal for hardware debugging:

```python
>>> import machine
>>> machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP).value()
1
```

If you press the button while the cursor is after the parenthesis and press Enter again, you'll see `0` — confirming the button is wired correctly.

The REPL is also useful for testing math formulas, checking color values, and exploring the `neopixel` module without running a full program.

### Thonny Run Controls

The Thonny toolbar has four key run controls:

| Control | What it does |
|---|---|
| Run (F5) | Runs the current file on the connected device |
| Stop (F2) | Stops the running program; returns to REPL prompt |
| Debug | Steps through code line by line |
| Open REPL | Opens a fresh REPL session |

**Serial Console in Thonny**: the Shell panel doubles as a serial console — any `print()` calls in your Pico code appear here in real time. This is your primary debugging tool.

### Syntax Highlighting and Code Autocomplete

**Syntax Highlighting** colors different parts of your code automatically: keywords are one color, strings another, comments another. This makes errors easier to spot — a string that doesn't end will immediately show as a wrong color.

**Code Autocomplete** appears when you press Tab after typing part of an identifier. Type `machine.` and press Tab — a list of all available attributes appears. This speeds up writing and reduces spelling mistakes.

### Thonny Package Manager

The **Thonny Package Manager** installs Python packages to the connected Pico. Open it from the Tools menu → Manage packages.

The **MicroPython Standard Library** is built into MicroPython and does not need to be installed:

- `machine` — hardware control (Pin, ADC, PWM, I2C, SPI)
- `utime` — time functions (sleep, ticks_ms)
- `neopixel` — NeoPixel driver
- `math` — math functions (sin, cos, sqrt, pi)
- `urandom` — random numbers
- `ujson` — JSON encoding/decoding
- `uos` — filesystem operations

Packages NOT included in the standard MicroPython firmware must be installed via the package manager. For example, `umqtt.simple` (for MQTT messaging) must be installed before import.

---

## File Upload Workflow

**File Upload Workflow** describes how a `.py` file moves from your computer to the Pico:

1. Write and test your code in Thonny with the file open locally
2. Use File → Save as → select "Raspberry Pi Pico" as the destination
3. Save as `main.py` (Pico runs this automatically on power-up) or any other name
4. Click Run (F5) to execute it immediately

**Running Script on Pico**: if a script is saved as `main.py` on the Pico, it runs every time the Pico receives power — even without a USB connection. This is how you make a standalone costume project that starts automatically when you plug in the battery.

A typical file organization on the Pico:

```
/ (root of Pico filesystem)
├── main.py          ← runs automatically on power-up
├── config.py        ← hardware settings
└── input_helpers.py ← button abstraction class
```

**Python Module Paths**: MicroPython searches for imported modules in the root of the Pico filesystem. If you `import config`, MicroPython looks for `config.py` in `/`. Place helper files in the root directory alongside `main.py`.

---

## The config.py Module Pattern

The **config.py Module Pattern** is a file named `config.py` that stores hardware-specific settings in one place. Every other file imports from `config` instead of using hard-coded values.

**Hardware Abstraction Layer** — the `config.py` file acts as an abstraction layer between your animation code (which doesn't care which pin is used) and the hardware (which requires a specific pin).

A typical `config.py` for this course:

```python
# config.py — hardware configuration for this kit
NEOPIXEL_PIN = 0          # GP0 → data line to NeoPixel strip
NUMBER_PIXELS = 30        # number of LEDs in the strip
BRIGHTNESS_LIMIT = 0.4    # maximum brightness (0.0–1.0) to save power
BTN_PIN = 15              # GP15 → button input
LDR_PIN = 26              # ADC0 (GP26) → photoresistor
```

Every program file starts with:

```python
import config
strip = neopixel.NeoPixel(machine.Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)
```

**Cross-Kit Compatibility**: when a student borrows a kit with a different number of pixels or a different pin assignment, they only change `config.py`. All programs import from config, so they all adapt automatically.

If you compare this to the alternative — hard-coding `30` as the number of pixels in every program file — the advantage is clear. Changing kits would require editing every file.

---

## Git Version Control

**Git Version Control** is software that tracks changes to your code files over time. Every time you make a meaningful change and "commit" it, Git saves a snapshot. You can compare snapshots, go back to an earlier version, and collaborate with others.

The following six commands cover 90% of everyday Git use.

### git status Command

`git status` shows which files have been changed, added, or are not yet tracked. Always run this first before doing anything else.

```
$ git status
On branch main
Changes not staged for commit:
  modified:   main.py
Untracked files:
  input_helpers.py
```

### git add Command

`git add` stages a file for the next commit. "Staging" means marking it as "include this change in the next snapshot."

```bash
git add main.py input_helpers.py
```

Or to add every changed file at once:

```bash
git add .
```

### git commit Command

`git commit` saves a permanent snapshot of all staged files. The `-m` flag lets you write a **Commit Message** on the same line.

```bash
git commit -m "Add button input abstraction and four-mode animation"
```

**Commit Message Writing**: a good commit message answers "what changed and why in one sentence." Use the imperative mood ("Add", "Fix", "Remove", not "Added", "Fixed", "Removed"). A reader should be able to understand the purpose of the snapshot without reading the code diff.

### git push Command

`git push` uploads your local commits to GitHub. After committing, push to save your work remotely:

```bash
git push
```

If this is the first push on a new branch, you may need:

```bash
git push -u origin main
```

### git pull Command

`git pull` downloads commits that exist on GitHub but not yet on your computer. Run this when you've made changes on another computer (like the school lab) and want them locally:

```bash
git pull
```

### git clone Command

`git clone` downloads an entire repository from GitHub to your computer for the first time:

```bash
git clone https://github.com/your-username/moving-rainbow-projects.git
```

After cloning, Git automatically sets up the link to GitHub, so `push` and `pull` work immediately.

---

## GitHub Repository

A **GitHub Repository** is a cloud-hosted home for a project's code, tracked by Git. GitHub adds a web interface, collaboration tools, and issue tracking on top of Git.

### Repository Structure

Before creating your repository, plan a sensible **file organization** structure. A clear layout helps others (and future-you) understand the project at a glance.

Recommended structure for your Moving Rainbow repository:

```
moving-rainbow-projects/
├── README.md           ← project overview (required!)
├── config.py           ← hardware configuration
├── main.py             ← the main program
├── input_helpers.py    ← button/sensor helpers
├── animations/
│   ├── rainbow.py      ← rainbow animation functions
│   ├── scanner.py      ← scanner animation functions
│   └── comet.py        ← comet animation functions
└── docs/
    └── wiring.md       ← wiring diagram and setup notes
```

### README File Creation

A **README** file (always named `README.md`) appears on the GitHub repository front page. It should explain:
1. What the project does
2. What hardware it needs
3. How to install and run it
4. Any configuration steps

A minimal `README.md`:

```markdown
# Moving Rainbow Project

An interactive NeoPixel LED animation controller using a Raspberry Pi Pico.

## Hardware needed
- Raspberry Pi Pico
- WS2812B LED strip (30 pixels)
- One momentary push button

## Setup
1. Copy `config.py` and `main.py` to the Pico using Thonny
2. Press the button to cycle between animation modes
```

**Code Backup with GitHub**: beyond collaboration, GitHub acts as an automatic off-site backup of your code. If your computer is lost, stolen, or damaged, you can `git clone` your repository to any other machine and continue working within minutes.

#### Diagram: Git Workflow

<details markdown="1">
<summary>Interactive diagram: local ↔ GitHub file flow</summary>
Type: diagram
**sim-id:** git-workflow-diagram
**Library:** Mermaid
**Status:** Specified

A Mermaid flowchart (left-to-right) with three columns:

**Column 1 — Your computer (working files):**
- "Edit code in Thonny" box
- Arrow down to "git add <files>"
- Arrow down to "Staging Area" (dashed box)

**Column 2 — Local Git repository:**
- Arrow from Staging Area labeled "git commit -m '...'"
- "Local commit history" box with three stacked snapshots
- Arrow up from "git pull" (from GitHub to local)

**Column 3 — GitHub (cloud):**
- Arrow from Local labeled "git push"
- "GitHub repository" box
- Arrow down labeled "git clone" to "Another computer" (faded, showing the copy)

Each action box is clickable: clicking it shows a tooltip with the exact command syntax and what it does.

Canvas: 700 × 360 px. Responds to window resize.

Learning objective: Understanding — the student can describe the three locations where Git stores data (working directory, local repo, GitHub) and which command moves data between them.
</details>

---

## Firmware Flashing Workflow

**Firmware flashing** replaces the software that runs permanently inside the Pico's flash memory. You flash new firmware when:
- You want to upgrade to a newer version of MicroPython
- The Pico is stuck and not responding to Thonny
- You want to switch to CircuitPython (a different flavor of Python)

The **UF2 Drag-and-Drop Process** for flashing MicroPython onto a Pico:

1. Download the latest `rp2-pico-*.uf2` file from the MicroPython website
2. Hold the BOOTSEL button on the Pico while plugging in the USB cable
3. Release BOOTSEL after the cable is plugged in — the Pico appears as a USB drive named `RPI-RP2`
4. Drag and drop the `.uf2` file onto the `RPI-RP2` drive
5. The Pico restarts automatically and MicroPython is now running

The entire process takes about 30 seconds. After flashing, reconnect Thonny by selecting the port in the bottom-right corner of the Thonny window.

!!! warning "Watch out!"
    <img src="../../img/mascot/warning.png" class="mascot-admonition-img" alt="Pixel holds up both hands">
    Flashing new firmware erases everything stored on the Pico's filesystem — including `main.py`, `config.py`, and any helper files. Always push your code to GitHub before reflashing, so you can restore it with `git clone` afterward. Losing a half-finished project to an accidental reflash is a real risk.

---

## Try It Yourself

1. **Four-mode controller:** Build the complete four-mode interactive controller from this chapter. Test all four modes and verify that each animation starts from a clean state when you enter it.

2. **Config swap:** Change `config.NUMBER_PIXELS` in `config.py` to half your actual pixel count. Observe how all animations automatically adapt. Then restore the original value.

3. **First Git commit:** Create a GitHub repository called `moving-rainbow`, add your `main.py` and `config.py`, write a README, and make your first commit and push.

4. **Sensor speed control:** Add a photoresistor to your kit and modify the rainbow animation to change speed based on light level. Push the updated code to GitHub with a meaningful commit message.

---

## Check Your Understanding

1. What is an animation state variable and why is it needed?
2. What does animation restart logic do and when does it run?
3. What is the purpose of the Thonny REPL? Give one example of something you would test there.
4. List the six core Git commands in order, and explain what each one does.
5. What is the difference between `git commit` and `git push`?
6. What is the `config.py` pattern and why does it enable cross-kit compatibility?
7. When would you flash new MicroPython firmware onto the Pico?

---

!!! success "Chapter complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing">
    You've graduated from writing single-pattern programs to building complete interactive systems — with Git, GitHub, and the full pro development toolchain to back them up. Every skill you learned in Chapters 1–18 now has a professional workflow wrapped around it. This is how real engineers work. You've earned it!

## What's Next

In [Chapter 20](../20-project-design-and-capstone/index.md), you'll plan and build a complete capstone project from scratch — applying every skill in this book to create something uniquely yours, document it, and present it to an audience.
