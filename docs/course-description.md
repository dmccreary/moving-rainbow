---
title: Course Description for Moving Rainbow
description: A detailed course description for Moving Rainbow including overview, topics covered and learning objectives in the format of the 2001 Bloom Taxonomy
quality_score: 91
---

# Moving Rainbow: Computational Thinking with LED Programming

## Course Overview

**Course Code:** CS-110
**Target Audience:** High school students (grades 9–12), CoderDojo youth makers, and adult beginners
**Duration:** 10 weeks (1 semester)
**Credit:** 0.5 Credit (Elective — Computer Science / STEM)
**Prerequisites:** None. No prior programming experience required.
**Materials Fee:** ~$13 (students keep their kit)

## Course Description

Moving Rainbow is a hands-on introduction to computer science, computational thinking, and physical computing through the creation of colorful LED animations and wearable electronics. Students learn Python programming by controlling addressable WS2812B NeoPixel LED strips with Raspberry Pi Pico microcontrollers, progressing from simple blinking patterns to complex interactive light displays driven by buttons and sensors.

The course is grounded in the four pillars of computational thinking — decomposition, pattern recognition, abstraction, and algorithm design — and applies them concretely in every lesson. Students gain practical electronics skills including circuit design, battery selection, and power management, alongside software skills in debugging, version control, and project documentation.

The course culminates in a three-week capstone project where students design, build, and present an original LED creation of their choice: a wearable costume, room decoration, interactive art installation, or practical device such as a smart nightlight or clock display.

## Main Topics Covered

### 1. Python Programming Fundamentals
- Variables, data types (integer, float, string, boolean, list, tuple), and type conversion
- Mathematical and comparison operators
- Conditional statements (if/elif/else)
- For loops and while loops (including infinite loops with `while True`)
- Functions — definition, parameters, return values, and reusability
- Imports and standard library modules
- Variable scope (local vs. global)
- List and tuple operations (indexing, iteration, `len()`)
- Built-in functions: `range()`, `len()`, `int()`, `print()`
- Debugging techniques — reading error messages, tracing logic, using print statements

### 2. MicroPython and Raspberry Pi Pico
- Raspberry Pi Pico microcontroller architecture (dual-core ARM Cortex M0+, 264 KB SRAM, 2 MB flash)
- GPIO (General Purpose Input/Output) pins — numbering, modes, and functions
- MicroPython language and its differences from standard Python
- Thonny IDE — writing, uploading, and running programs on the Pico
- REPL (Read-Eval-Print Loop) for interactive exploration
- `machine.Pin` for digital output and input
- PWM (Pulse Width Modulation) — `PWM.freq()` and `PWM.duty_u16()`
- ADC (Analog-to-Digital Converter) — `ADC.read_u16()`
- `utime` module — `sleep()`, `ticks_ms()`, `ticks_us()`, `localtime()`
- `urandom.randint()` for random number generation
- Firmware concepts — UF2 file format, BOOTSEL button, drag-and-drop flashing
- `main.py` execution behavior on boot

### 3. NeoPixel (WS2812B) Addressable LEDs
- WS2812B integrated control circuit and single-wire serial data protocol
- 24-bit color data format (8 bits each for red, green, blue)
- Addressable LEDs — individual pixel control via sequential addressing
- Data propagation and data stripping through the LED chain
- Three-wire connections: power (5V), ground (GND), and data
- NeoPixel class — instantiation, pixel indexing (0-based), `strip.write()`
- RGB tuple format `(r, g, b)` and color value range (0–255)
- Strip power requirements — up to 20 mA per NeoPixel at full brightness
- LED strip form factors — strips, rings, matrices, fairy lights
- Weatherproof ratings — IP20 (bare), IP65 (silicone coated), IP67 (submersible)

### 4. Color Theory and RGB Color Model
- RGB additive color model — red, green, and blue as primary light colors
- Additive vs. subtractive (pigment) color mixing
- Color values (0–255 per channel, 16.7 million possible colors)
- Named colors as RGB tuples — red `(255,0,0)`, white `(255,255,255)`, black `(0,0,0)`
- Color wheel and spectral progression (red → orange → yellow → green → blue → indigo → violet)
- Smooth color transitions by incrementing/decrementing RGB channels
- HSV color model and its relationship to RGB
- Gamma correction — non-linear brightness adjustment to match human visual perception
- Gamma value (typically 2.2) and the gamma correction function
- Perceived brightness vs. actual (physical) LED brightness
- Normalized color values (0.0 to 1.0 range) used in gamma calculations

### 5. LED Animation Patterns and Techniques
- **Blink** — turning the entire strip on and off at timed intervals
- **Fade in and out** — smoothly increasing and decreasing overall brightness
- **Heartbeat** — simulating a pulse with a double-beat delay pattern
- **Color wipe** — filling the strip pixel by pixel with a single color
- **Moving pixel** — a single illuminated pixel traveling along the strip
- **Up and down** — a pixel bouncing back and forth between strip ends
- **Moving bands** — blocks of color advancing across the strip
- **Rainbow** — a static spectrum spread across all pixels simultaneously
- **Moving rainbow** — the rainbow spectrum continuously scrolling
- **Rainbow cycle** — each pixel cycles through the full spectrum independently
- **Comet tail** — a bright head pixel with a brightness-fading trail
- **Larson scanner** — a bouncing hot-spot with variable-brightness surround (inspired by Knight Rider)
- **Theater chase** — alternating pixel groups marching forward (classic marquee effect)
- **Ripple** — expanding brightness waves from a center point
- **Twinkle** — random pixels briefly lighting at random colors
- **Candle flicker** — simulating flame using random orange/yellow brightness variation
- **Random colors** — random pixel positions with random color selection

**Animation Techniques:**
- Frame-based animation with controlled delays
- Position variables and directional motion
- Bounce logic (reversing direction at strip ends)
- Modulo arithmetic (`%`) for circular/wrapping motion
- Brightness scaling (multiplying RGB tuples by a factor 0.0–1.0)
- Erasing trailing pixels to create clean motion
- Offset-based pattern shifting

### 6. Electronics, Circuits, and Power Systems
**Electrical Fundamentals:**
- Voltage (electrical potential, measured in volts)
- Current (electrical flow, measured in milliamps/amps)
- Resistance (opposition to flow, measured in ohms)
- Ohm's Law (V = IR) and power formula (P = V × I)
- Polarity — positive and negative terminals
- Ground (GND) as the common reference point
- Complete circuit path requirement

**Components:**
- Current-limiting resistors and pull-up/pull-down resistors
- Potentiometers (variable resistors) — outer terminals and wiper
- Light-dependent resistors (LDRs / photoresistors) — resistance vs. light intensity
- NPN transistors (2N2222) — base, collector, emitter; transistor current gain (beta)
- Voltage dividers — two-resistor circuits for sensor reading and analog signal scaling
- Breadboards — prototyping without soldering
- Jumper wires and connector types

**Power and Battery Systems:**
- Battery capacity (milliamp-hours, mAh)
- Battery life formula: battery life (hours) = mAh ÷ mA current draw
- Battery types and characteristics:
  - Coin cell (CR2032): 200–250 mAh, 3 V
  - AA alkaline: 2,000–3,000 mAh, 1.5 V
  - 9-volt: 400–600 mAh, 9 V
  - USB power bank: 2,000–20,000+ mAh, 5 V output
  - LiPo pouch cells: 500–2,000 mAh, 3.7 V
  - 18650 cylindrical cells: 2,000–3,500 mAh, 3.7 V
- Series vs. parallel battery configurations (voltage adds in series; capacity adds in parallel)
- Overcharge and over-discharge protection circuits
- LiPo charger ICs (TC4056, IP2312) and charging current
- Power consumption at scale — 20 mA per NeoPixel × number of pixels

**Circuit Types:**
- Static LED circuits (resistor + LED + battery)
- Transistor switch circuits (digital control of high-current loads)
- Voltage divider circuits for photoresistor sensing
- LED dimmer circuits (transistor-controlled brightness)
- Nightlight circuits (photoresistor-triggered switching)
- LED noodle projects (non-addressable LED strips with simple driver circuits)
- Solar-powered circuits with LiPo charging

### 7. Computational Thinking
- **Decomposition** — breaking a complex animation or project into smaller, solvable sub-problems
- **Pattern recognition** — identifying repeated structures in code and in physical LED behavior
- **Abstraction** — isolating the essential parameters of a problem (hiding unnecessary detail)
- **Algorithm design** — expressing step-by-step solutions in pseudocode and then in code
- DRY principle (Don't Repeat Yourself) and code reuse through functions
- Template-based problem solving — adapting a known pattern to a new context
- Generalizing specific solutions — moving from a hardcoded example to a parameterized function
- Explainability — describing why code behaves a particular way to others
- Identifying and eliminating bias in automated or procedural systems
- Events as computational triggers — connecting physical inputs to program state changes

### 8. Interactive Systems — Buttons, Sensors, and State
- Momentary push buttons and digital GPIO input
- `machine.Pin.IN` with `Pin.PULL_UP` or `Pin.PULL_DOWN`
- Reading button state with `pin.value()`
- Button debouncing — software delays and state-tracking to prevent false triggers
- Multiple-button programs and simultaneous input handling
- Mode variables — tracking which animation is active
- Mode cycling — advancing through modes 0, 1, 2, … on button press
- State-machine program structure — current state determines behavior on each input
- Photoresistors as analog light sensors
- Reading analog values with `ADC.read_u16()` (0–65535 range)
- Mapping ADC values to output parameters (brightness, color, speed)
- Light threshold detection for automatic nightlight activation

### 9. Development Tools and Workflow
- Thonny Python IDE — editor, file manager, REPL panel, run controls
- Uploading files to the Pico filesystem
- `main.py` auto-run behavior vs. explicit run in Thonny
- Serial console output with `print()` for runtime debugging
- Git version control — clone, add, commit, push, pull, status
- GitHub repositories — creating, cloning, and contributing
- Repository structure and file organization conventions
- Firmware flashing workflow — hold BOOTSEL, connect USB, drop UF2 file

### 10. Project Design and Capstone
- Project ideation — brainstorming LED project concepts
- Requirements specification — defining what the project must do
- Algorithm design and pseudocode before coding
- Circuit design — selecting components and drawing connection diagrams
- Milestone planning and timeline creation
- Iterative development — build, test, revise cycles
- Peer code review — reading and giving feedback on classmate code
- Documentation — inline code comments, README files, project reports
- Technical presentation — explaining design choices and demonstrating the project
- Reflection on the development process and what would be improved next time

**Capstone project categories:**
- Wearable electronics (light-up jacket, costume, hat, sneakers)
- Home and room decoration (ambient lighting, clock display, art installation)
- Interactive art (sound-reactive visualizer, touch-sensitive color mixer, LED sign)
- Practical devices (solar nightlight, bike safety lights, study timer)

---

## Topics NOT Covered in This Course

To keep the course focused and accessible to beginners, the following topics are intentionally out of scope:

- Object-oriented programming (classes, inheritance, polymorphism) — covered in follow-on courses
- Web development (HTML, CSS, JavaScript, APIs)
- Networking and internet protocols (TCP/IP, HTTP, MQTT) — even though the Pico W supports Wi-Fi
- Advanced data structures (trees, graphs, hash tables, queues)
- Machine learning or artificial intelligence
- 3D printing, laser cutting, or other digital fabrication
- PCB (printed circuit board) design and manufacturing
- Advanced soldering — all connections in this course use breadboards or pre-crimped connectors
- Mobile app development
- Server-side or database programming
- Computer architecture beyond what is needed to understand the Pico
- Advanced signal processing (FFT, filtering) — used in some MicroSim visualizations but not coded by students

---

## Learning Outcomes

After completing this course, students will be able to demonstrate competencies at each level of the 2001 Bloom's Taxonomy:

### Remember
Students will be able to recall and recognize foundational facts and vocabulary:

1. **List** the three color channels in the RGB color model and their value ranges (0–255)
2. **Name** the four pillars of computational thinking: decomposition, pattern recognition, abstraction, and algorithm design
3. **Identify** the key pins on a Raspberry Pi Pico: GPIO pins, USB connector, GND, 3.3V out, and VSYS
4. **Recall** the MicroPython libraries used in this course: `neopixel`, `machine`, `utime`, and `urandom`
5. **Define** key terms: addressable LED, NeoPixel, WS2812B, GPIO, PWM, ADC, REPL, firmware, debouncing, gamma correction
6. **Name** at least ten LED animation patterns covered: blink, fade, heartbeat, comet tail, rainbow, moving rainbow, theater chase, twinkle, candle flicker, Larson scanner
7. **State** the power draw of a WS2812B NeoPixel at full white brightness (approximately 20 mA per pixel at 5V)
8. **Recall** the battery life formula: battery life (hours) = capacity (mAh) ÷ current draw (mA)
9. **List** the Python data types used: integer, float, string, boolean, list, and tuple

### Understand
Students will be able to explain and interpret course concepts in their own words:

1. **Explain** how WS2812B NeoPixels receive color data using a single-wire serial protocol, including how 24-bit data is structured and how sequential pixels strip off their own data
2. **Describe** how additive color mixing (light) produces colors differently than subtractive/pigment mixing
3. **Summarize** how a microcontroller's fetch-decode-execute cycle runs a program instruction by instruction
4. **Explain** the relationship between voltage, current, resistance, and power using Ohm's Law and P = V × I
5. **Describe** why gamma correction is needed and how it adjusts LED brightness to match human perception of lightness
6. **Interpret** a simple circuit diagram and trace the path of current from the power source through components to ground
7. **Explain** the difference between static LED circuits (simple on/off) and dynamic circuits (microcontroller-controlled)
8. **Describe** how battery capacity (mAh), LED current draw, and number of pixels interact to determine how long a project can run on battery power
9. **Summarize** what debouncing is and why it is necessary when reading physical push buttons in code

### Apply
Students will be able to use course skills in new but familiar situations:

1. **Write** Python programs using variables, loops, conditionals, and functions to control NeoPixel LEDs on a Raspberry Pi Pico
2. **Use** the `neopixel`, `machine`, `utime`, and `urandom` MicroPython libraries to implement original lighting programs
3. **Apply** RGB color values to produce target colors, smooth fades, and full-spectrum rainbow effects
4. **Implement** at least ten named animation patterns from scratch, given only the pattern name and a description
5. **Use** button inputs and GPIO pin sensing to build interactive, mode-switching LED programs with debounce logic
6. **Calculate** the expected battery life of a given LED project using the mAh ÷ mA formula
7. **Apply** the Thonny IDE workflow to write, upload, and run MicroPython programs, using the REPL for debugging
8. **Use** Git and GitHub commands (clone, add, commit, push) to version-control and share project code
9. **Apply** modulo arithmetic and brightness-scaling techniques to produce wrapping motion and fade effects

### Analyze
Students will be able to break material into parts and examine relationships:

1. **Deconstruct** a complex animation algorithm into its sub-components: position tracking, color calculation, timing delays, and pixel update
2. **Compare** the power consumption of different LED animation modes and identify which patterns are most battery-efficient
3. **Differentiate** between hardware faults (incorrect wiring, power issues) and software bugs (logic errors, wrong index) when diagnosing a non-working project
4. **Analyze** how adjusting loop delay values changes animation speed, smoothness, and the visual perception of motion
5. **Compare** five battery types (coin cell, AA, LiPo, 18650, USB power bank) by voltage, capacity, size, and best-use scenario for LED projects
6. **Break down** a multi-mode interactive program into its state-machine components: states, transitions, trigger conditions, and per-state behaviors
7. **Examine** a gamma correction curve and explain how it redistributes brightness values to compensate for human non-linear light perception

### Evaluate
Students will be able to make judgments based on criteria and standards:

1. **Justify** the selection of a specific battery type and capacity for a portable wearable project based on weight, runtime, and rechargeability requirements
2. **Assess** a peer's code for readability and maintainability using defined criteria: meaningful variable names, function decomposition, comments, and consistent style
3. **Prioritize** feature additions for a capstone project given a fixed time budget, distinguishing must-have from nice-to-have requirements
4. **Critique** an animation design for visual quality — timing, color harmony, motion smoothness — and propose specific improvements with justification
5. **Evaluate** tradeoffs between animation complexity and processor load on the Raspberry Pi Pico, and recommend when simplification is warranted
6. **Judge** whether a proposed wearable circuit design meets safety and durability requirements, citing specific risks and mitigations

### Create
Students will be able to synthesize new work from course concepts:

1. **Design** an original LED animation algorithm — express it first as pseudocode, then implement it as working, commented MicroPython code
2. **Construct** a complete hardware-software system integrating a Raspberry Pi Pico, NeoPixel strip, and at least one input device (button or photoresistor)
3. **Build** a multi-mode LED controller that cycles through three or more original animation patterns using button inputs, with clean mode-transition logic
4. **Compose** well-organized, documented Python code that a peer can read, understand, and modify without assistance from the author
5. **Design and execute** a capstone project from initial concept through planning, circuit design, algorithm design, implementation, testing, and presentation
6. **Produce** a technical presentation that explains design decisions, demonstrates the finished project, and reflects on what worked and what the student would improve

---

## Course Structure

### Weeks 1–2: Foundations
Setup of hardware (Raspberry Pi Pico, Thonny IDE, NeoPixel strip) and introduction to Python fundamentals through LED control. First programs: blink, named colors, simple fade. Introduction to computational thinking.

### Weeks 3–4: Motion and Color
Loops and iteration for motion effects. Moving pixel, color wipe, color wheel, and rainbow patterns. RGB color model and the relationship between code values and perceived color.

### Weeks 5–6: Interactivity
Button input, GPIO sensing, debouncing, conditional logic, mode variables. Building multi-mode programs with three or more patterns switchable by buttons.

### Week 7: Advanced Animations
Complex patterns — comet tail, theater chase, Larson scanner, twinkle, candle flicker. Functions and code organization. Brightness scaling and gamma correction. Random number generation.

### Weeks 8–10: Capstone Project
Students design and build an original LED project demonstrating mastery of course concepts.
- **Week 8:** Project proposal, circuit design, algorithm pseudocode, milestone planning
- **Week 9:** Implementation, debugging, peer code review, iteration
- **Week 10:** Final demonstration, technical presentation, reflection and peer feedback

---

## Why This Course Matters

Computing is now embedded in almost every physical object — lights, clothing, furniture, art, toys, and tools. This course teaches students to be creators, not just consumers, of that technology. By working with real hardware (a $4 microcontroller and a $6 LED strip), students get immediate visual feedback for every line of code they write, making abstract programming concepts concrete and memorable.

The skills developed here — Python programming, physical computing, electronics reasoning, and computational thinking — transfer directly to robotics, IoT product development, game development, wearable technology, and virtually every branch of engineering. More importantly, the creative confidence students build by designing and presenting original projects is a foundation for any technical career.

**This course welcomes complete beginners.** No prior programming or electronics experience is required. Every student leaves with a working project they built themselves — and the knowledge to keep building.

## Career Connections

Concepts from this course apply directly to:
- Embedded systems and firmware engineering
- IoT (Internet of Things) product development
- Robotics and automation
- Wearable technology and smart textiles
- Entertainment technology (stage lighting, interactive exhibits)
- Electrical engineering
- User experience design for physical products
- Game development (hardware-accelerated feedback)
- Product design and prototyping
