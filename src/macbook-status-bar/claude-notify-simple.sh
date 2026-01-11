#!/bin/bash
#
# Claude Code Touch Bar Notification Script
# ==========================================
#
# This script writes JSON status to a temp file that BetterTouchTool
# reads and displays on the MacBook Pro Touch Bar with color formatting.
#
# Architecture:
#   Claude Code Hook → This Script → Temp File (JSON) → BTT Widget → Touch Bar
#
# The script is triggered by Claude Code hooks defined in ~/.claude/settings.json.
# BetterTouchTool polls the temp file every second and displays the content
# on the Touch Bar with the specified colors.
#
# JSON Format for BetterTouchTool:
#   {
#     "text": "Display Text",
#     "background_color": "R,G,B,A",   (0-255 for each)
#     "font_color": "R,G,B,A",          (0-255 for each)
#     "font_size": 12
#   }
#
# Usage:
#   ./claude-notify-simple.sh <status>
#   ./claude-notify-simple.sh <status> --notify  (also shows macOS notification)
#
# Available Statuses:
#   running    - Claude is executing a tool         → ⚙ Running Task...   (blue)
#   prompt     - Claude awaits next prompt          → 💬 Waiting for Prompt (green)
#   flash      - Task completed successfully        → ✓ Task Complete      (green)
#   question   - Claude has a question              → ? Question Waiting   (blue)
#   permission - Permission needed to proceed       → ⚠ Permission Needed  (yellow)
#   waiting    - Waiting for user input             → ⏳ Waiting for Input  (red)
#   context    - Context window almost full         → ⚡ Context Warning    (orange)
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

# Font size for Touch Bar display
FONT_SIZE=12

# ==============================================================================
# Color Definitions (RGBA format: Red,Green,Blue,Alpha - values 0-255)
# ==============================================================================

# White text for most backgrounds
WHITE="255,255,255,255"
# Black text for light backgrounds (yellow)
BLACK="0,0,0,255"

# Background colors
GREEN_BG="34,139,34,255"       # Forest green - for prompt/ready states
BRIGHT_GREEN_BG="0,180,0,255"  # Bright green - for task complete
BLUE_BG="30,144,255,255"       # Dodger blue - for running/working states
ROYAL_BLUE_BG="65,105,225,255" # Royal blue - for questions
YELLOW_BG="255,200,0,255"      # Gold - for permission needed
RED_BG="220,20,60,255"         # Crimson - for waiting/blocked states
ORANGE_BG="255,140,0,255"      # Dark orange - for warnings
GRAY_BG="80,80,80,255"         # Dark gray - for cleared/off state

# ==============================================================================
# Status Handler
# ==============================================================================

# Map the status argument to JSON with text and colors
# Each status writes a JSON object to the temp file
case "$1" in

    # ---------------------------------------------------------------------------
    # Primary statuses (used by hooks)
    # ---------------------------------------------------------------------------

    running)
        # Triggered by PreToolUse hook
        # Shows while Claude is executing any tool (Bash, Read, Write, etc.)
        # Blue background indicates active work
        cat > "$STATUS_FILE" << EOF
{"text":"⚙ Running Task...","background_color":"${BLUE_BG}","font_color":"${WHITE}","font_size":${FONT_SIZE}}
EOF
        ;;

    prompt)
        # Triggered by Stop hook
        # Shows when Claude has finished responding and awaits your next prompt
        # Green background indicates ready/go state
        cat > "$STATUS_FILE" << EOF
{"text":"💬 Waiting for Prompt","background_color":"${GREEN_BG}","font_color":"${WHITE}","font_size":${FONT_SIZE}}
EOF
        ;;

    # ---------------------------------------------------------------------------
    # Secondary statuses (for manual or future hook use)
    # ---------------------------------------------------------------------------

    flash)
        # Manual trigger for explicit task completion notification
        # Bright green background for success
        cat > "$STATUS_FILE" << EOF
{"text":"✓ Task Complete","background_color":"${BRIGHT_GREEN_BG}","font_color":"${WHITE}","font_size":${FONT_SIZE}}
EOF
        ;;

    question)
        # Claude is asking a clarifying question
        # Royal blue background to draw attention
        cat > "$STATUS_FILE" << EOF
{"text":"? Question Waiting","background_color":"${ROYAL_BLUE_BG}","font_color":"${WHITE}","font_size":${FONT_SIZE}}
EOF
        ;;

    permission)
        # Claude needs permission to proceed with an action
        # Yellow background with black text for high visibility warning
        cat > "$STATUS_FILE" << EOF
{"text":"⚠ Permission Needed","background_color":"${YELLOW_BG}","font_color":"${BLACK}","font_size":${FONT_SIZE}}
EOF
        ;;

    waiting)
        # Generic waiting state for user input
        # Red background indicates blocked/urgent state
        cat > "$STATUS_FILE" << EOF
{"text":"⏳ Waiting for Input","background_color":"${RED_BG}","font_color":"${WHITE}","font_size":${FONT_SIZE}}
EOF
        ;;

    context)
        # Warning: context window is approaching its limit
        # Orange background for warning state
        cat > "$STATUS_FILE" << EOF
{"text":"⚡ Context Warning","background_color":"${ORANGE_BG}","font_color":"${WHITE}","font_size":${FONT_SIZE}}
EOF
        ;;

    # ---------------------------------------------------------------------------
    # Clear status
    # ---------------------------------------------------------------------------

    off|clear)
        # Clear the Touch Bar status display
        # Gray background with minimal text
        cat > "$STATUS_FILE" << EOF
{"text":"","background_color":"${GRAY_BG}","font_color":"${WHITE}","font_size":${FONT_SIZE}}
EOF
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
        echo "Statuses (with colors):"
        echo "  running    - '⚙ Running Task...'    Blue background"
        echo "  prompt     - '💬 Waiting for Prompt' Green background"
        echo "  flash      - '✓ Task Complete'      Bright green background"
        echo "  question   - '? Question Waiting'   Royal blue background"
        echo "  permission - '⚠ Permission Needed'  Yellow background"
        echo "  waiting    - '⏳ Waiting for Input'  Red background"
        echo "  context    - '⚡ Context Warning'    Orange background"
        echo "  off/clear  - Clear the status       Gray background"
        echo ""
        echo "Options:"
        echo "  --notify   - Also show a native macOS notification with sound"
        echo ""
        echo "Output format: JSON for BetterTouchTool widget"
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
