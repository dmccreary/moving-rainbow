---
title: Git Workflow
description: Understanding - the student can describe the three locations where Git stores data (working directory, local repo, GitHub) and which command moves data bet
image: /sims/git-workflow-diagram/git-workflow-diagram.png
og:image: /sims/git-workflow-diagram/git-workflow-diagram.png
twitter:image: /sims/git-workflow-diagram/git-workflow-diagram.png
social:
   cards: false
library: Mermaid
status: implemented
---

# Git Workflow

<iframe src="main.html" width="100%" height="432px" scrolling="no"></iframe>

[Run the Git Workflow MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This MicroSim

A Mermaid flowchart (left-to-right) with three columns:

**Learning objective:** Understanding - the student can describe the three locations where Git stores data (working directory, local repo, GitHub) and which command moves data between them.

## How to Use

Click any box or node in the diagram to read what it does. The explanation appears in the panel just below the diagram. Where an **Animate** button is present, press it to step through the sequence.

## Iframe Embed Code

You can place this MicroSim on any web page by adding the following HTML:

```html
<iframe src="https://dmccreary.github.io/moving-rainbow/sims/git-workflow-diagram/main.html"
        height="432px"
        width="100%"
        scrolling="no"></iframe>
```

## Lesson Plan

### Grade Level
Grades 6-12

### Duration
10-15 minutes

### Learning Objective
Understanding - the student can describe the three locations where Git stores data (working directory, local repo, GitHub) and which command moves data between them.

### Activities

1. **Explore (5 min):** Open the MicroSim and try every control. Notice what changes on screen.
2. **Predict (5 min):** Before each change, predict what will happen, then test your prediction.
3. **Discuss (5 min):** Explain the idea in your own words and connect it to the LED code in [Chapter 19](../../chapters/19-interactive-animations-and-tools/index.md).

### Assessment
Ask students to describe, in one or two sentences, the relationship the MicroSim demonstrates and how it shows up when programming the LED strip.

## References

1. [Chapter 19: Interactive Animations and Development Tools](../../chapters/19-interactive-animations-and-tools/index.md) - the chapter where this MicroSim is used.
2. [Moving Rainbow Intelligent Textbook](https://dmccreary.github.io/moving-rainbow/) - the full course this MicroSim belongs to.
3. [MicroSims Reference](https://dmccreary.github.io/microsims/) - the standards behind these interactive simulations.

## Original Specification

<details markdown="1">
<summary>Full specification used to generate this MicroSim</summary>

```text
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
```

</details>
