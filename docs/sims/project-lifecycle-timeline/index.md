---
title: Full Project Lifecycle
description: Analyzing - the student can identify which phase of the project lifecycle is most at risk given a project's current state.
image: /sims/project-lifecycle-timeline/project-lifecycle-timeline.png
og:image: /sims/project-lifecycle-timeline/project-lifecycle-timeline.png
twitter:image: /sims/project-lifecycle-timeline/project-lifecycle-timeline.png
social:
   cards: false
library: Mermaid
status: implemented
---

# Full Project Lifecycle

<iframe src="main.html" width="100%" height="562px" scrolling="no"></iframe>

[Run the Full Project Lifecycle MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A Mermaid Gantt-style diagram showing the six-week project timeline:

**Learning objective:** Analyzing - the student can identify which phase of the project lifecycle is most at risk given a project's current state.

## How to Use

Click any box or node in the diagram to read what it does. The explanation appears in the panel just below the diagram. Where an **Animate** button is present, press it to step through the sequence.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/project-lifecycle-timeline/main.html"
        height="562px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Analyzing - the student can identify which phase of the project lifecycle is most at risk given a project's current state.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 20](../../chapters/20-project-design-and-capstone/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 20: Project Design, Capstone Projects, and Presentation](../../chapters/20-project-design-and-capstone/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
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
```

</details>
