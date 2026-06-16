---
title: Claude Code Hooks Workflow
description: Interactive flowchart showing how Claude Code hooks integrate with the MacBook Touch Bar notification system
quality_score: 85
image: /sims/claude-code-hooks-workflow/main.html
---

# Claude Code Hooks Workflow

An interactive flowchart visualizing how Claude Code hooks trigger Touch Bar status updates on your MacBook Pro.

<iframe src="main.html" width="100%" height="500px" style="border:none; overflow:hidden;"></iframe>

[View Fullscreen](main.html){ .md-button }

## Overview

This diagram illustrates the beautiful integration between Claude Code hooks and the MacBook Pro Touch Bar notification system. Watch how your prompt flows through the system, triggering colorful status updates that keep you informed at a glance!

## Workflow Steps

1. **User sends prompt** - You type your request in Claude Code CLI
2. **Claude Code processes request** - Claude analyzes what you need
3. **Tool use needed?** - Decision point: does Claude need to use tools?
4. **Yes path (Blue status)**:
   - **PreToolUse Hook fires** - Hook triggers before tool execution
   - **Script writes JSON with BLUE status** - Touch Bar turns blue
5. **No path (Green status)**:
   - **Claude responds directly** - Text response without tools
   - **Stop Hook fires** - Hook triggers when response completes
   - **Script writes JSON with GREEN status** - Touch Bar turns green
6. **BetterTouchTool reads file** - BTT polls the status file every second
7. **Touch Bar displays status!** - You see the colorful indicator

## Color Semantics

| Color | Meaning | Hook |
|-------|---------|------|
| **Blue** | Claude is working (tool in use) | PreToolUse |
| **Green** | Claude is ready for your next prompt | Stop |

## Key Concepts

- **Claude Code Hooks** - Shell commands that execute on specific events
- **PreToolUse Hook** - Fires before any tool (Bash, Read, Write, etc.) executes
- **Stop Hook** - Fires when Claude finishes responding
- **JSON Status** - Color-coded status written to temp file
- **BetterTouchTool** - macOS app that displays status on Touch Bar

## How Hooks Work

Hooks are configured in `~/.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "",
      "hooks": [{"type": "command", "command": "/path/to/script.sh running"}]
    }],
    "Stop": [{
      "matcher": "",
      "hooks": [{"type": "command", "command": "/path/to/script.sh prompt"}]
    }]
  }
}
```

## Lesson Plan

### Learning Objectives

By studying this workflow, you will understand:

1. How Claude Code hooks provide extensibility points
2. The flow of events when Claude processes a request
3. How file-based IPC enables Touch Bar integration
4. The difference between tool-using and direct responses

### Activities

1. **Trace the Flow**: Follow a prompt through both paths (with and without tools)
2. **Identify Hooks**: List the two hooks used and when they fire
3. **Color Mapping**: Explain why blue indicates "working" and green indicates "ready"

### Assessment Questions

1. What hook fires when Claude starts using the Bash tool?
2. What file does the script write to?
3. How often does BetterTouchTool check for updates?
4. What determines whether the flow takes the "Yes" or "No" path?

## Related Resources

- [MacBook Touch Bar Status Documentation](../../chapters/macbook-touchbar-status/)
- [Claude Code Hooks Documentation](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [BetterTouchTool Documentation](https://docs.folivora.ai/)

## References

- Anthropic. (2025). *Claude Code Hooks*. https://docs.anthropic.com/en/docs/claude-code/hooks
- folivora. (2025). *BetterTouchTool Documentation*. https://docs.folivora.ai/
