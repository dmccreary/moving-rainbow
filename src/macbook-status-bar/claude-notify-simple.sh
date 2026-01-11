#!/bin/bash
#
# Claude Code Touch Bar Notification Script
# ==========================================
#
# This script writes status text to a temp file that BetterTouchTool
# reads and displays on the MacBook Pro Touch Bar.
#
# Architecture:
#   Claude Code Hook → This Script → Temp File → BTT Widget → Touch Bar
#
# The script is triggered by Claude Code hooks defined in ~/.claude/settings.json.
# BetterTouchTool polls the temp file every second and displays the content
# on the Touch Bar.
#
# Usage:
#   ./claude-notify-simple.sh <status>
#   ./claude-notify-simple.sh <status> --notify  (also shows macOS notification)
#
# Available Statuses:
#   running    - Claude is executing a tool         → ⚙ Running Task...
#   prompt     - Claude awaits next prompt          → 💬 Waiting for Prompt
#   flash      - Task completed successfully        → ✓ Task Complete
#   question   - Claude has a question              → ? Question Waiting
#   permission - Permission needed to proceed       → ⚠ Permission Needed
#   waiting    - Waiting for user input             → ⏳ Waiting for Input
#   context    - Context window almost full         → ⚡ Context Warning
#   off/clear  - Clear the status display           → (empty)
#
# Hook Integration:
#   PreToolUse hook  → calls this script with "running"
#   Stop hook        → calls this script with "prompt"
#
# Example hooks configuration in ~/.claude/settings.json:
#   {
#     "hooks": {
#       "PreToolUse": [{
#         "matcher": "",
#         "hooks": [{"type": "command", "command": "/path/to/claude-notify-simple.sh running"}]
#       }],
#       "Stop": [{
#         "matcher": "",
#         "hooks": [{"type": "command", "command": "/path/to/claude-notify-simple.sh prompt"}]
#       }]
#     }
#   }
#
# Author: Dan McCreary
# License: MIT
#

# ==============================================================================
# Configuration
# ==============================================================================

# Temp file location - BetterTouchTool reads this file every second
# This file acts as the communication channel between Claude Code and BTT
STATUS_FILE="/tmp/claude-code-status.txt"

# ==============================================================================
# Status Handler
# ==============================================================================

# Map the status argument to display text with emoji icon
# Each status writes a single line to the temp file
case "$1" in

    # ---------------------------------------------------------------------------
    # Primary statuses (used by hooks)
    # ---------------------------------------------------------------------------

    running)
        # Triggered by PreToolUse hook
        # Shows while Claude is executing any tool (Bash, Read, Write, etc.)
        echo "⚙ Running Task..." > "$STATUS_FILE"
        ;;

    prompt)
        # Triggered by Stop hook
        # Shows when Claude has finished responding and awaits your next prompt
        echo "💬 Waiting for Prompt" > "$STATUS_FILE"
        ;;

    # ---------------------------------------------------------------------------
    # Secondary statuses (for manual or future hook use)
    # ---------------------------------------------------------------------------

    flash)
        # Manual trigger for explicit task completion notification
        # Useful for scripts or custom workflows
        echo "✓ Task Complete" > "$STATUS_FILE"
        ;;

    question)
        # Claude is asking a clarifying question
        # Could be triggered by a future hook when Claude uses AskUserQuestion tool
        echo "? Question Waiting" > "$STATUS_FILE"
        ;;

    permission)
        # Claude needs permission to proceed with an action
        # Could be triggered when Claude requests elevated permissions
        echo "⚠ Permission Needed" > "$STATUS_FILE"
        ;;

    waiting)
        # Generic waiting state for user input
        # Different from 'prompt' - indicates Claude is blocked waiting for response
        echo "⏳ Waiting for Input" > "$STATUS_FILE"
        ;;

    context)
        # Warning: context window is approaching its limit
        # Could be triggered by a Notification hook with context warning matcher
        echo "⚡ Context Warning" > "$STATUS_FILE"
        ;;

    # ---------------------------------------------------------------------------
    # Clear status
    # ---------------------------------------------------------------------------

    off|clear)
        # Clear the Touch Bar status display
        # Useful when closing Claude Code or resetting state
        echo "" > "$STATUS_FILE"
        ;;

    # ---------------------------------------------------------------------------
    # Invalid argument handler
    # ---------------------------------------------------------------------------

    *)
        # Show usage information for invalid arguments
        echo "Claude Code Touch Bar Notification Script"
        echo ""
        echo "Usage: $0 <status> [--notify]"
        echo ""
        echo "Statuses:"
        echo "  running    - Show 'Running Task...' (used by PreToolUse hook)"
        echo "  prompt     - Show 'Waiting for Prompt' (used by Stop hook)"
        echo "  flash      - Show 'Task Complete'"
        echo "  question   - Show 'Question Waiting'"
        echo "  permission - Show 'Permission Needed'"
        echo "  waiting    - Show 'Waiting for Input'"
        echo "  context    - Show 'Context Warning'"
        echo "  off/clear  - Clear the status"
        echo ""
        echo "Options:"
        echo "  --notify   - Also show a native macOS notification with sound"
        exit 1
        ;;
esac

# ==============================================================================
# Optional: Native macOS Notification
# ==============================================================================

# If --notify flag is passed as second argument, also show a macOS notification
# This provides an additional alert with sound for important status changes
if [ "$2" = "--notify" ]; then
    case "$1" in
        flash)
            # Glass sound for successful completion
            osascript -e 'display notification "Task completed successfully" with title "Claude Code" sound name "Glass"'
            ;;
        running)
            # Pop sound when task starts (usually not needed)
            osascript -e 'display notification "Task is running..." with title "Claude Code" sound name "Pop"'
            ;;
        prompt)
            # Gentle ping when ready for input
            osascript -e 'display notification "Ready for your next prompt" with title "Claude Code" sound name "Ping"'
            ;;
        question)
            # Ping to draw attention to question
            osascript -e 'display notification "Claude has a question for you" with title "Claude Code" sound name "Ping"'
            ;;
        permission)
            # Basso (deeper tone) for permission requests
            osascript -e 'display notification "Permission required to continue" with title "Claude Code" sound name "Basso"'
            ;;
        waiting)
            # Ping for waiting state
            osascript -e 'display notification "Waiting for your input" with title "Claude Code" sound name "Ping"'
            ;;
        context)
            # Sosumi (alert sound) for context warning
            osascript -e 'display notification "Context window is almost full" with title "Claude Code" sound name "Sosumi"'
            ;;
    esac
fi
