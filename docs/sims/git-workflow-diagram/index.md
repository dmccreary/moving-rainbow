---
title: Git Workflow
description: Understanding — the student can describe the three locations where Git stores data (working directory, local repo, GitHub) and which command moves data between them.
status: scaffold
library: Mermaid
bloom_level: TBD
---

# Git Workflow



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 19: Interactive Animations and Development Tools](../../chapters/19-interactive-animations-and-tools/index.md).

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

## Related Resources

- [Chapter 19: Interactive Animations and Development Tools](../../chapters/19-interactive-animations-and-tools/index.md)
