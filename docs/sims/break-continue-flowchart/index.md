---
title: break vs. continue Flow
description: break vs. continue Flow
status: scaffold
library: Mermaid
bloom_level: TBD
---

# break vs. continue Flow



<iframe src="main.html" width="100%" height="600"></iframe>

[Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }

## Specification

The full specification below is extracted from
[Chapter 4: Python Control Flow, Loops, and Error Handling](../../chapters/04-python-control-flow-loops/index.md).

```text
Type: diagram
**sim-id:** break-continue-flowchart
**Library:** Mermaid
**Status:** Specified

A Mermaid flowchart showing a `for` loop cycle. Nodes: "Start Loop" → "i in range?" → yes → "Check condition" → "break?" → yes → "Exit loop"; no → "continue?" → yes → "Back to top" (arrow goes back to "i in range?" node); no → "Run loop body" → "Back to top". Each node is clickable: clicking "break?" shows a tooltip "break exits the loop entirely"; clicking "continue?" shows "continue skips to the next iteration"; clicking "Run loop body" shows "This is where your animation code goes." Color-code: break path in red, continue path in orange, normal path in green.
```

## Related Resources

- [Chapter 4: Python Control Flow, Loops, and Error Handling](../../chapters/04-python-control-flow-loops/index.md)
