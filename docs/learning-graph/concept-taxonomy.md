# Concept Taxonomy for Moving Rainbow

12 categories covering the full scope of the Moving Rainbow course.

## Taxonomy Table

| Category Name | TaxonomyID | Count | % | Description |
|---------------|-----------|-------|---|-------------|
| Python Programming | PYTH | 55 | 11.3% | Python language syntax, data types, control flow, functions, modules, and debugging |
| MicroPython and Pico | UPICO | 45 | 9.3% | Raspberry Pi Pico hardware, MicroPython-specific libraries, GPIO, PWM, ADC, firmware, and the Thonny IDE |
| NeoPixel Hardware | NEO | 40 | 8.2% | WS2812B/NeoPixel LED hardware, data protocols, wiring, pixel addressing, and NeoPixel class usage |
| Color Theory | COLOR | 40 | 8.2% | RGB color model, additive mixing, color wheel, HSV, gamma correction, and color perception |
| Animation Patterns | ANIM | 65 | 13.4% | Named animation effects, motion techniques, timing, brightness, and multi-pattern programming |
| Electronics and Circuits | ELEC | 70 | 14.4% | Electrical fundamentals, circuit components, battery systems, power management, and circuit types |
| Computational Thinking | CT | 30 | 6.2% | Decomposition, pattern recognition, abstraction, algorithm design, debugging methodology, and code organization |
| Input and Interactivity | INPUT | 35 | 7.2% | Push buttons, GPIO input, debouncing, mode switching, sensors, state machines, and event-driven programming |
| Dev Tools and Workflow | TOOLS | 30 | 6.2% | Thonny IDE, REPL, file upload, Git, GitHub, firmware flashing, and configuration patterns |
| Project Design | PROJ | 35 | 7.2% | Project planning, documentation, capstone projects, presentations, and iterative development |
| Mathematics | MATH | 30 | 6.2% | Modulo arithmetic, interpolation, normalization, range mapping, random numbers, and LED math |
| Hardware Platforms | HW | 10 | 2.1% | Alternative hardware form factors (RP2040-Zero, matrices, Pi keyboard) and electrical safety |

## Category Descriptions

### PYTH — Python Programming
Core Python language concepts taught in the course: variable assignment, data types (int, float, string, boolean, list, tuple), control flow (if/elif/else, for, while), functions (definition, parameters, return values), module imports, and error types. These are the foundational software building blocks used throughout every lesson.

### UPICO — MicroPython and Pico
Hardware-specific programming: the Raspberry Pi Pico microcontroller, its RP2040 processor, GPIO pins, MicroPython language, key libraries (`machine`, `utime`, `urandom`, `neopixel`), PWM, ADC, firmware flashing, REPL, and the Thonny development environment.

### NEO — NeoPixel Hardware
Everything about WS2812B/NeoPixel addressable LEDs: how they work (single-wire serial protocol, 24-bit data), how to connect them (three-wire connection, polarity), and how to control them with the `NeoPixel` class (pixel indexing, RGB tuples, `strip.write()`).

### COLOR — Color Theory
The science and art of color in LED programming: the RGB additive color model, the color wheel and spectral sequence, HSV color space, smooth color transitions, gamma correction for perceptual accuracy, and color psychology.

### ANIM — Animation Patterns
The complete library of LED animation effects: 17 named patterns (blink, fade, heartbeat, color wipe, moving pixel, bounce, bands, rainbow, moving rainbow, rainbow cycle, comet tail, Larson scanner, theater chase, ripple, twinkle, candle flicker, random colors) plus the underlying techniques for building new patterns (position tracking, modulo wrapping, brightness scaling, multi-pattern programs).

### ELEC — Electronics and Circuits
Electrical fundamentals (voltage, current, resistance, Ohm's Law, power), circuit components (resistors, transistors, potentiometers, photoresistors, breadboards), battery types and battery life calculations, circuit configurations (static, dynamic, dimmer, nightlight), and power management (LiPo charging, USB power).

### CT — Computational Thinking
The four pillars of CT (decomposition, pattern recognition, abstraction, algorithm design) and their application to LED programming. Includes pseudocode writing, iterative development, debugging methodology, test cases, edge cases, and code organization principles (DRY, separation of concerns, modular design).

### INPUT — Input and Interactivity
Making LED projects respond to the physical world: push buttons (wiring, polling, debouncing, long-press), mode variables and state machines, photoresistors as light sensors, ADC voltage reading, sensor value mapping, and event-driven programming patterns.

### TOOLS — Dev Tools and Workflow
The development environment and practices: Thonny IDE features (REPL, file manager, run controls, syntax highlighting), the file upload workflow to the Pico, Git version control commands, GitHub repositories, firmware flashing, and the `config.py` hardware abstraction pattern.

### PROJ — Project Design
The complete project lifecycle: ideation, requirements specification, circuit and algorithm planning, milestone timelines, iterative build-test-revise cycles, peer code review, documentation, capstone project types (wearables, décor, interactive art, practical devices), and technical presentations.

### MATH — Mathematics
Mathematical concepts applied to LED programming: modulo arithmetic for wrapping, linear interpolation for smooth transitions, normalization and range mapping, random number generation, sine waves for breathing effects, exponential decay for fade trails, and the arithmetic behind Ohm's Law, battery life, and gamma correction.

### HW — Hardware Platforms
Alternative and extended hardware covered in the course: RP2040-Zero form factor, 8×8 and 16×16 NeoPixel matrices, the Raspberry Pi 500 keyboard RGB system, and electrical safety rules (short circuit prevention, LiPo handling, wearable safety, USB power limits).
