---
title: Project Design, Capstone Projects, and Presentation
description: Plan, build, document, and present a complete capstone LED project using the full engineering design cycle — from ideation and requirements through peer review and final demo.
generated_by: claude skill chapter-content-generator
date: 2026-06-20 07:47:04
version: 0.09
---

# Project Design, Capstone Projects, and Presentation

## Summary

Covers the complete project lifecycle from ideation and requirements specification through circuit design, algorithm pseudocode, milestone planning, iterative development, peer code review, and technical presentation, including all capstone project categories (wearable, room décor, interactive art, practical devices) and wearable safety standards.

## Concepts Covered

This chapter covers the following 36 concepts from the learning graph:

1. Project Ideation
2. Requirements Specification
3. Circuit Connection Diagram
4. Algorithm Pseudocode Plan
5. Milestone Planning
6. Timeline Creation
7. Iterative Development Cycle
8. Build-Test-Revise Cycle
9. Peer Code Review
10. Code Review Criteria
11. Inline Code Comments
12. Project Documentation
13. Technical Presentation Skills
14. Project Reflection
15. Wearable Electronics Design
16. LED Costume Project
17. Room Decoration Project
18. Interactive Art Installation
19. Practical Device Project
20. Solar-Powered LED System
21. LED Clock Project
22. LED Nightlight Project
23. Bike Safety Light Project
24. Project Proposal Document
25. Component Parts List
26. Project Testing Protocol
27. User Experience Design
28. Project Iteration
29. Final Project Demo
30. Capstone Presentation
31. Project Peer Feedback
32. Design Constraint Analysis
33. Project Complexity Estimate
34. Feature Prioritization
35. Minimum Viable Project
36. Wearable Safety Standards

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction and Computational Thinking Foundations](../01-intro-and-computational-thinking/index.md)
- [Chapter 2: Python Basics: Variables, Data Types, and Operators](../02-python-variables-types-operators/index.md)
- [Chapter 3: Python Functions, Modules, and Programming Best Practices](../03-python-functions-modules-practices/index.md)
- [Chapter 4: Python Control Flow, Loops, and Error Handling](../04-python-control-flow-loops/index.md)
- [Chapter 5: Raspberry Pi Pico Hardware and Development Environment](../05-raspberry-pi-pico-hardware/index.md)
- [Chapter 6: MicroPython APIs, GPIO Control, and Electrical Fundamentals](../06-micropython-apis-and-electronics/index.md)
- [Chapter 7: Color Theory: The RGB Color Model and Color Mixing](../07-rgb-color-theory/index.md)
- [Chapter 8: NeoPixel LED Hardware: WS2812B, Wiring, and Form Factors](../08-neopixel-led-hardware/index.md)
- [Chapter 9: NeoPixel Programming: Pixels, Colors, and the NeoPixel Library](../09-neopixel-programming/index.md)
- [Chapter 10: Advanced Color Theory: HSV, Gamma Correction, and Color Palettes](../10-advanced-color-theory/index.md)
- [Chapter 11: Mathematics for LED Programming](../11-math-for-led-programming/index.md)
- [Chapter 12: Basic LED Animation Patterns](../12-basic-animation-patterns/index.md)
- [Chapter 13: Intermediate Animation Techniques](../13-intermediate-animations/index.md)
- [Chapter 14: Advanced Animation Patterns: Comet, Scanner, and Candle](../14-advanced-animation-patterns/index.md)
- [Chapter 15: Electronics Fundamentals: Resistance, Ohm's Law, and Components](../15-electronics-fundamentals/index.md)
- [Chapter 16: Circuit Assembly: Resistors, Transistors, and Circuit Types](../16-circuit-assembly/index.md)
- [Chapter 17: Power Systems, Batteries, and Energy Management](../17-power-and-battery-systems/index.md)
- [Chapter 18: Input Devices, Sensors, and State Machines](../18-input-devices-and-sensors/index.md)
- [Chapter 19: Interactive Animations and Development Tools](../19-interactive-animations-and-tools/index.md)

---

!!! tip "Pixel says..."
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="Pixel waves hello">
    Welcome to the final chapter! Everything you've learned — code, circuits, color, animation, sensors, power, Git — comes together here. Chapter 20 isn't just about building a project. It's about learning to *think* like an engineer: define the problem, design before you build, test with purpose, and communicate what you made. This is where the book becomes *yours*. Let's light this up!

## What You'll Learn

By the end of this chapter, you'll be able to:

- Generate and evaluate project ideas using ideation techniques
- Write a requirements specification and project proposal document
- Create a circuit connection diagram and a components parts list
- Write algorithm pseudocode before coding
- Plan project milestones and timelines
- Apply the minimum viable project and feature prioritization approach
- Use the build-test-revise cycle for iterative development
- Perform and receive peer code reviews
- Design a wearable project that meets safety standards
- Deliver a technical presentation and capstone demo

## What You'll Need

- All previous kit materials (Pico, LED strip, breadboard, wires, button, LDR)
- Optional: additional LEDs, additional buttons, a LiPo battery system, mounting materials
- Access to GitHub for code backup
- Paper or a document editor for planning documents
- Your 19 previous chapters as a reference library

---

## Project Ideation

**Project Ideation** is the creative phase where you generate as many project ideas as possible before committing to one. Good ideation rules:

- Write down every idea, no matter how impossible it seems — ideas evolve
- Think across all four project categories: wearable, décor, interactive art, practical device
- Ask: "Who will use this? Where? When? What problem does it solve or experience does it create?"

Techniques that help:

**Brainstorming**: set a timer for 10 minutes and write every idea without judging them. Aim for quantity over quality.

**Constraint brainstorming**: deliberately limit yourself. "What if I could only use 10 pixels?" or "What if the project had to run on batteries for 8 hours?" Constraints often produce the most creative ideas.

**Problem-first thinking**: identify a problem first, then ask how LEDs and a Pico might help. "My backpack isn't visible at night." → Bike safety light or bag LED accent. "My room is boring." → Room decoration project.

After ideation, narrow to 2–3 ideas and evaluate them against your constraints.

---

## Design Constraint Analysis and Complexity Estimate

Before choosing a project, analyze what each one actually requires. **Design Constraint Analysis** identifies limitations that will affect your design:

The following table shows common constraint categories:

| Constraint Type | Questions to ask |
|---|---|
| Budget | How many components does it need? Can you afford them? |
| Time | How many class periods or hours do you have? |
| Skill | Does it need techniques you haven't learned? |
| Physical | What size does it need to be? How does it attach? |
| Power | How long does it need to run without charging? |

**Project Complexity Estimate**: after listing the constraints, estimate complexity on a simple scale:

- **Basic** — 1 animation, no input, USB power
- **Intermediate** — 2–4 animations, one button, USB or power bank
- **Advanced** — mode cycling, sensor input, battery-powered, wearable form factor

For a capstone project in one course, target intermediate complexity. Advanced is achievable with extra time; basic is a starting point but aim to extend it.

---

## Minimum Viable Project and Feature Prioritization

A **Minimum Viable Project** (MVP) is the smallest version of your project that demonstrates its core function. For a bike safety light, the MVP is: LEDs on, attached to the bike, visible at night. Everything else (patterns, button cycling, battery level indicator) is an enhancement.

**Feature Prioritization** ranks features into three tiers:

1. **Must-have** — the MVP. These must work for the project to exist.
2. **Should-have** — strong improvements that add value if time allows.
3. **Could-have** — nice extras for if the core is done early.

Example for an LED costume jacket:

| Feature | Priority |
|---|---|
| LEDs sewn to jacket, solid color | Must-have |
| Moving rainbow animation | Must-have |
| Button to change animation | Should-have |
| LiPo battery (no USB cable dangling) | Should-have |
| Auto-brightness via photoresistor | Could-have |
| Heartbeat sync to music tempo | Could-have |

Build the must-haves first. Only start should-haves after the MVPs are tested and working.

---

## Requirements Specification and Project Proposal

A **Requirements Specification** is a written document that defines exactly what your project will do. It prevents scope creep (the endless addition of features) and gives you a concrete target to test against.

Before the template, here are two key terms:
- **Functional requirement** — what the project does (e.g., "LEDs display a moving rainbow when powered on")
- **Non-functional requirement** — quality of how it does it (e.g., "Battery life must exceed 4 hours at full brightness")

A minimal requirements specification:

```
Project: LED Bike Safety Light
Creator: [Your Name]

PURPOSE
Help cyclists be visible at night.

FUNCTIONAL REQUIREMENTS
1. LEDs illuminate red when powered on (default mode)
2. Button cycles between: solid red, flashing red, white forward light
3. Automatic mode switch at startup (manual override via button)

NON-FUNCTIONAL REQUIREMENTS
1. Battery life: minimum 4 hours in flashing mode
2. Weatherproof: waterproof enclosure for Pico and battery
3. Attachment: secures to bike frame without permanent mounting

OUT OF SCOPE (not in this version)
- Bluetooth connectivity
- Charging from bike dynamo
```

The **Project Proposal Document** packages the requirements specification with:
- Project title and creator
- Project category (wearable / décor / art / practical)
- Component parts list
- Rough circuit diagram sketch
- Timeline and milestones

### Component Parts List

A **Component Parts List** (also called a Bill of Materials) lists every physical item your project needs. Before ordering parts or signing out kit components, knowing exactly what you need avoids mid-project surprises.

Example parts list for a bike safety light:

| Component | Quantity | Notes |
|---|---|---|
| Raspberry Pi Pico | 1 | From kit |
| WS2812B LED strip, 30 pixels | 1 | Weatherproof variant |
| 5V LiPo battery, 2000 mAh | 1 | With USB output |
| Momentary push button | 1 | Waterproof rated |
| 3D-printed enclosure | 1 | STL file from GitHub |
| Jumper wires | 6 | 10 cm |
| Zip ties | 4 | For mounting |

---

## Circuit Connection Diagram

A **Circuit Connection Diagram** shows how every component connects to the Pico. Before wiring anything, draw this diagram by hand or with a tool like Fritzing.

The diagram should show:
- Pico with labeled GPIO pins
- Each component connected to the correct pin with wire color notation
- Power rails (5V, 3.3V, GND) clearly marked
- Any resistors or capacitors in the circuit

Before wiring your actual project, walk through the diagram with a partner and check: "Is there a path from every component to GND? Is there a current-limiting resistor on every directly-driven LED? Is there a pull-up or pull-down on every input pin?"

A diagram reviewed in advance takes 5 minutes. A short circuit discovered at power-on can take 30 minutes to diagnose.

#### Diagram: Example Circuit Connection Diagram for Bike Light Project


<iframe src="../../sims/bike-light-circuit-diagram/main.html" width="100%" height="422px" scrolling="no"></iframe>
[Run Example Circuit Connection Diagram for Bike Light Project Fullscreen](../../sims/bike-light-circuit-diagram/main.html)

<details markdown="1">
<summary>Interactive wiring diagram: Pico + LED strip + button for bike light</summary>
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
</details>

---

## Algorithm Pseudocode Plan

**Algorithm Pseudocode** is a plain-language description of your program's logic written before you write actual code. Pseudocode uses everyday words to describe what the computer should do, step by step.

Why write pseudocode first? It's much faster to catch logic errors in plain text than in working code. A missing step in pseudocode costs a sentence to fix. A missing step found after coding costs reworking the entire program.

Pseudocode example for the bike safety light:

```
SET UP:
  Initialize LED strip (30 pixels, GP0)
  Initialize button (GP15, pull-up)
  Set mode = 0 (solid red)

MAIN LOOP:
  If button just pressed:
    mode = (mode + 1) modulo 3

  If mode = 0:
    Set all pixels red, full brightness
    Write to strip

  If mode = 1:
    If frame counter is even: set all pixels red
    If frame counter is odd:  set all pixels off
    Write to strip
    Advance frame counter

  If mode = 2:
    Set first 10 pixels white (forward light)
    Set remaining 20 pixels off
    Write to strip

  Wait 50ms
  Go back to top of loop
```

After writing pseudocode, review it with a partner. Can they follow every step? Does each step map to code you already know how to write?

---

## Milestone Planning and Timeline Creation

**Milestone Planning** breaks a project into named, dateable checkpoints. Each milestone is something you can demonstrate — a working subset of the final project.

**Timeline Creation** assigns dates to each milestone. Work backward from the final demo date:

| Milestone | Target Date | Success Criteria |
|---|---|---|
| Proposal approved | Week 1 | Proposal document reviewed by teacher |
| MVP working | Week 2 | Solid LED color powered by USB |
| Core features done | Week 3 | All must-have features functional |
| Should-haves added | Week 4 | Button cycling, battery-powered |
| Testing complete | Week 5 | Project testing protocol run, issues fixed |
| Peer review done | Week 5 | Code review received and addressed |
| Presentation ready | Week 6 | Demo rehearsed, slide or poster prepared |

Plan for milestones to slip by one day each. If every milestone arrives exactly on time, you're either planning conservatively (fine) or getting very lucky.

---

## The Build-Test-Revise Cycle

The **Iterative Development Cycle** — also called the **Build-Test-Revise Cycle** — is how real engineers build anything non-trivial. Instead of building the entire project and testing at the end (where everything might be broken), you:

1. **Build** — implement the smallest next piece (one mode, one animation, one input)
2. **Test** — verify it works before adding more
3. **Revise** — fix what doesn't work, then go back to step 1

**Project Iteration** is each pass through this cycle. A typical intermediate project goes through 8–15 iterations before the final demo.

The most important rule: **test small, test early, test often**. If you wire 30 pixels, write 200 lines of code, and test for the first time — and it doesn't work — you have 230 potential failure points. If you test after every 15 lines of code, you have at most 15 places to look.

### Project Testing Protocol

A **Project Testing Protocol** is a written checklist of tests that the project must pass. Writing it before building ensures you test what matters:

Example testing protocol for the bike light:

```
FUNCTIONAL TESTS (must pass):
[ ] Solid red mode: all 30 pixels display red on power-up
[ ] Button press: mode advances from 0 → 1 → 2 → 0
[ ] Flashing mode: LEDs blink at ~2 Hz, visible at arm's length in daylight
[ ] White mode: forward 10 pixels white, no flicker
[ ] Battery runtime: runs 4 hours in flashing mode without dimming

NON-FUNCTIONAL TESTS (must pass):
[ ] Drop test: enclosure survives a drop from handlebar height onto pavement
[ ] Moisture test: survives 30 seconds of water spray from a garden hose
[ ] Vibration test: mounted on bike and ridden 1 km on rough pavement, no loose connections

EDGE CASES (should handle):
[ ] Button held: no continuous mode cycling (debounce working)
[ ] Low battery: brightness should reduce gracefully, not crash
```

Run every test before the final presentation. Document the results: which tests passed, which needed revision, and what was changed to fix failures.

---

## Capstone Project Categories

Four categories of projects are supported by this course's hardware. The description of each category below also identifies which chapters provide the key skills.

### Wearable Electronics Design — LED Costume Project

**Wearable Electronics Design** combines programming and physical construction to create garments or accessories that light up. The **LED Costume Project** is the classic example: LEDs sewn or attached to a jacket, hat, bag, or costume.

Key design considerations specific to wearables:
- **Weight and bulk** — LiPo batteries add weight; route wires so they don't pull on fabric
- **Flexibility** — LED strips must bend with the garment; use silicone-sheathed strips
- **Reachability** — the Pico and battery must be accessible for charging without disassembly
- **Washability** — the project is likely not washable; design for it to be removable

Key chapters for wearables: 7 (color theory), 12–14 (animations), 17 (battery systems), 18 (buttons for mode switching).

### Room Decoration Project

The **Room Decoration Project** creates permanent LED installations in a personal space: under-shelf accent lighting, backlit picture frames, desk ambient lighting, or holiday decorations.

Because room decoration projects stay plugged into USB power, power budget constraints are much looser. This frees you to use higher brightness and more complex animations.

Key chapters: 7, 9, 12–14 (color and animation), 19 (config.py for customization).

### Interactive Art Installation

The **Interactive Art Installation** creates an experience that responds to the viewer's presence or actions. Examples: a wall panel that changes color when touched, a mobile that sways and triggers pixel ripples, a shadow box where a photoresistor detects ambient light.

Key skills: sensor-driven animation (Chapter 18), state machines (Chapter 18), mode cycling (Chapter 19).

### Practical Device Projects

**Practical Device Projects** solve a real problem. Four specific examples:

**Bike Safety Light Project**: red rear light with multiple flashing modes, waterproofed, battery-powered, attaches to bike seat post. Safety-critical — the testing protocol must include a visibility test.

**LED Nightlight Project**: photoresistor automatically activates warm-white LEDs when the room gets dark. Plugs into USB. Optional: button cycles through colors.

**LED Clock Project**: uses `utime.localtime()` to map hours, minutes, and seconds to pixel positions or colors. Requires the Pico to have its clock set (via Thonny or NTP with a wireless-capable variant).

**Solar-Powered LED System**: a small solar panel charges a LiPo via a MPPT solar charge controller, powering outdoor LEDs at night. Advanced project — requires the LiPo safety knowledge from Chapter 17 and a suitable weatherproof enclosure.

!!! tip "Pixel says..."
    <img src="../../img/mascot/tip.png" class="mascot-admonition-img" alt="Pixel points upward with a smile">
    Not sure which category to choose? Ask yourself: will this project be used, displayed, or experienced? "Used" often points to a practical device. "Displayed" points to décor. "Experienced" points to interactive art. "Worn" points to a costume. That one question often settles it.

---

## Wearable Safety Standards

**Wearable Safety Standards** are design rules that prevent wearable electronics from causing discomfort or harm. Before wearing any electronic project on the body:

1. **Enclose all bare conductors.** Exposed solder joints, bare component legs, or bare wire ends can scratch skin or short-circuit against metal buttons. Cover with heat-shrink tubing, electrical tape, or a 3D-printed case.

2. **Secure the battery.** A LiPo battery that falls out of a pocket and gets stepped on can rupture. Use a battery pocket with a snap or zipper, not just friction.

3. **Keep heat away from skin.** Resistors and voltage regulators can run warm under load. Route them away from direct skin contact, especially in costume pieces worn under fabric.

4. **Never bypass the LiPo protection circuit.** Some bare LiPo cells are sold without protection ICs — they may be slightly lighter but can go into thermal runaway if over-discharged. Always use protected cells or add an external protection module.

5. **Test before wearing in public.** Run the full project at maximum brightness for 30 minutes before wearing it. If any component becomes noticeably warm, investigate before putting it on your body.

6. **Add a power switch or accessible disconnect.** If an LED gets stuck at maximum brightness and starts heating up, you should be able to disconnect power immediately without tools.

---

## Peer Code Review

**Peer Code Review** is the practice of having another student read, understand, and comment on your code before it's finalized. Code review catches bugs, spots confusing variable names, and often results in better designs — because a reviewer asks "why?" at exactly the places where the code is fragile.

### Code Review Criteria

Before the review, the reviewer reads the code with these questions in mind:

**Correctness:**
- Does the code do what the comments and function names promise?
- Are there edge cases that would cause the code to fail?

**Readability:**
- Are variable names descriptive? (`brightness` vs. `b`)
- Are functions small and focused on one task?

**Safety:**
- Are sensor values validated before being used as array indices?
- Is there a way to exit the main loop if something goes wrong?

**Inline Code Comments**: comments should appear where the WHY is not obvious. A comment explaining that a delay exists because the strip needs 300 µs to latch the signal is valuable. A comment that says `# add 1 to offset` above `offset += 1` adds no information.

Good inline comment example:
```python
utime.sleep_us(300)   # WS2812B protocol requires 300µs latch gap after write
```

### Project Documentation

**Project Documentation** is everything a new person would need to understand and use your project: the README, the wiring diagram, the config.py settings, and the testing protocol.

Minimum documentation for the capstone:

1. **README.md** on GitHub with: project description, hardware required, wiring overview, how to install and run
2. **Circuit diagram** (drawn or exported from Fritzing/KiCad)
3. **config.py** with comments explaining every setting

---

## User Experience Design

**User Experience Design** (UX) is thinking about your project from the perspective of the person who will use it — not the programmer who built it.

Questions to ask about your UX:

- How does the user know the project is on? (Indicator LED, startup animation?)
- How does the user know which mode they're in? (A label, a specific color, a pattern?)
- What happens if the user presses the button too quickly? (Debouncing handles this, but test it)
- What happens when the battery is nearly dead? (Does it crash, dim, or show a warning?)

The best UX improvements are often tiny details: a brief flash of white at startup, a distinctive color for each mode, or a slow red blink when battery voltage is low.

---

## Technical Presentation Skills and Capstone Presentation

The **Capstone Presentation** is your opportunity to explain what you built, how it works, and what you learned. A strong technical presentation has three parts:

**1. Live Demo (3–5 minutes)**
- Power on the project in front of the audience
- Demonstrate every must-have feature
- Show one should-have if time allows
- If something breaks during the demo, narrate what's happening and stay calm — this happens to professional engineers, too

**2. Technical Explanation (2–3 minutes)**
- Describe the circuit: "The Pico's GP0 connects to the data line of the LED strip. GP15 reads a button with a pull-up resistor."
- Describe the software: "The main loop checks the button state, updates a mode variable, and calls the animation function for the current mode."
- Show the key code structure — you don't need to read every line, just the structure

**3. Reflection (1–2 minutes)**
- What worked well?
- What would you do differently?
- What would you add if you had more time?

**Final Project Demo** tip: practice the demo twice before the presentation day. Know the exact sequence of button presses that shows all modes. Have a backup plan if the USB cable disconnects.

### Project Reflection

**Project Reflection** is the honest assessment of your own work after the project is complete. Good reflection goes beyond "it worked" or "it didn't work":

- What was the hardest part? Why?
- What skill from earlier chapters did you use most?
- Which early decision turned out to be a mistake, and how did you recover?
- What would the "version 2" of this project look like?

Writing a brief reflection also helps the next student who might build a similar project — your lessons learned become their head start.

### Project Peer Feedback

**Project Peer Feedback** is structured comments from classmates after the presentation. Useful peer feedback is specific and constructive:

- Specific: "The scanner mode felt slow compared to the other modes — was that intentional?"
- Constructive: "The wiring inside the enclosure was hard to follow — color-coding the wires would make it easier to service."

Avoid vague feedback like "good job" or "it was cool" — that doesn't help the builder improve.

---

#### Diagram: Full Project Lifecycle


<iframe src="../../sims/project-lifecycle-timeline/main.html" width="100%" height="562px" scrolling="no"></iframe>
[Run Full Project Lifecycle Fullscreen](../../sims/project-lifecycle-timeline/main.html)

<details markdown="1">
<summary>Interactive timeline diagram: from ideation to presentation</summary>
Type: diagram
**sim-id:** project-lifecycle-timeline
**Library:** Mermaid
**Status:** Specified

A Mermaid Gantt-style diagram showing the six-week project timeline:

**Week 1 — Plan:**
- Project ideation
- Constraint analysis
- Proposal document

**Week 2 — Build MVP:**
- Circuit wiring
- Config.py setup
- Basic animation working

**Week 3 — Core features:**
- Button cycling
- All must-have modes
- Git commit at each milestone

**Week 4 — Enhancements:**
- Should-have features
- Battery power integration
- UX polish

**Week 5 — Verify:**
- Full testing protocol
- Peer code review
- Fix issues found

**Week 6 — Present:**
- Demo rehearsal
- Capstone presentation
- Peer feedback session

Each bar is clickable: clicking a phase opens a tooltip with the success criteria for that phase.

Canvas: 700 × 340 px. Responds to window resize.

Learning objective: Analyzing — the student can identify which phase of the project lifecycle is most at risk given a project's current state.
</details>

---

## Try It Yourself

1. **Ideation sprint:** Set a 10-minute timer. Generate at least 15 project ideas across all four categories. Then score each one: Easy / Medium / Hard, and Fun / Interesting / Useful. Circle your top three.

2. **MVP definition:** Choose your favorite idea from the sprint. Write the three must-have features that define the MVP. Write two should-haves and one could-have.

3. **Pseudocode first:** Write pseudocode for the main loop of your project. Get a partner to read it. Ask: "Is every step clear? Is anything missing?"

4. **Peer review practice:** Swap `main.py` files with a partner. Review their code using the four criteria: correctness, readability, safety, and inline comments. Provide at least three specific comments.

---

## Check Your Understanding

1. What is the difference between a functional requirement and a non-functional requirement?
2. What is a Minimum Viable Project and why should you build it first?
3. What is the purpose of the build-test-revise cycle?
4. Name three wearable safety standards for battery-powered projects.
5. What makes peer feedback "constructive"? Give an example of vague vs. specific feedback on the same issue.
6. What three parts make up a strong capstone presentation?
7. What is project reflection and why is it valuable beyond just "it worked"?

---

!!! success "Course complete!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="Pixel leaps with rainbow blazing, all colors streaming behind them">
    You made it! From "what is a variable" to "here is my capstone project" — that is one of the longest journeys in any technical field, and you completed it. You now know how to write Python, control real hardware, design circuits, choose power systems, handle sensor input, and build something that lights up a room — literally. Every professional engineer, every maker, every product designer you admire built on exactly these foundations. Where you go next is up to you. But you now have the tools to go anywhere. Pixel couldn't be prouder.

## What's Next

You've completed the Moving Rainbow course. Here are some directions to continue:

- **Explore MicroPython further**: wireless networking with the Pico W (`network` module), I2C sensors, servo motors, and audio output
- **Try CircuitPython**: a variant of MicroPython with different hardware support and a large Adafruit library ecosystem
- **Share your project**: post it on GitHub, submit it to a maker fair, or teach a younger student how to do it
- **Extend your capstone**: implement the should-haves and could-haves from your feature prioritization list
- **Learn more electronics**: explore PCB design with KiCad, 3D printing enclosures, and surface-mount soldering

The skills you built here — breaking problems into parts, testing incrementally, reading documentation, debugging systematically, and communicating your work — are transferable to every technical field. Use them well.
