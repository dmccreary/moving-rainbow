#!/usr/bin/env python3
"""
Claude Code notification for MacBook Pro Touch Bar.

This script displays status notifications on the MacBook Pro Touch Bar
when Claude Code events occur (via hooks).

Events:
    flash      - Task complete (blue indicator + "Task Complete" text)
    question   - Question waiting (blue indicator + "Question Waiting" text)
    permission - Permission needed (yellow indicator + "Permission Needed" text)
    waiting    - Waiting for user input (red indicator + "Waiting for Input" text)
    context    - Context window almost full (orange indicator + "Context Warning" text)
    off        - Clear notification from Touch Bar

Requirements:
    - macOS 10.12.2+ with Touch Bar
    - BetterTouchTool installed and running (https://folivora.ai/)
    - BetterTouchTool scripting server enabled

Setup:
    1. Install BetterTouchTool from https://folivora.ai/
    2. Enable "Allow controlling BetterTouchTool from Terminal/Apple Script"
       (Preferences > Scripting > Enable Apple Script)
    3. Add this script to your Claude Code hooks in ~/.claude/settings.json

Usage:
    python3 claude-notify.py flash
    python3 claude-notify.py question
    python3 claude-notify.py permission
    python3 claude-notify.py waiting
    python3 claude-notify.py context
    python3 claude-notify.py off
"""

import subprocess
import sys
import time
import json
from typing import Tuple, Optional

# Status configurations: (color_hex, text_label, icon_emoji)
STATUSES = {
    'flash': ('#0064FF', 'Task Complete', '✓'),
    'question': ('#0064FF', 'Question Waiting', '?'),
    'permission': ('#FFFF00', 'Permission Needed', '⚠'),
    'waiting': ('#FF0000', 'Waiting for Input', '⏳'),
    'context': ('#FF4500', 'Context Warning', '⚡'),
    'off': (None, None, None),
}

# Widget UUID for BetterTouchTool (consistent ID for updates)
WIDGET_UUID = "claude-code-status-widget"


def run_applescript(script: str) -> Tuple[bool, str]:
    """Execute AppleScript and return success status and output."""
    try:
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0, result.stdout.strip()
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except Exception as e:
        return False, str(e)


def check_bettertouchtool() -> bool:
    """Check if BetterTouchTool is running."""
    script = '''
    tell application "System Events"
        return (name of processes) contains "BetterTouchTool"
    end tell
    '''
    success, _ = run_applescript(script)
    return success


def send_btt_notification(action: str) -> bool:
    """Send notification to BetterTouchTool Touch Bar widget."""
    if action not in STATUSES:
        print(f"Unknown action: {action}")
        return False

    color, text, icon = STATUSES[action]

    if action == 'off':
        # Hide/clear the widget
        script = f'''
        tell application "BetterTouchTool"
            trigger_named "ClaudeCodeClear"
        end tell
        '''
        run_applescript(script)
        return True

    # Create Touch Bar widget with text and color
    display_text = f"{icon} {text}"

    # Use BetterTouchTool's JSON-based widget update
    widget_config = {
        "BTTWidgetName": display_text,
        "BTTTouchBarButtonColor": color,
        "BTTTouchBarFreeSpaceAfterButton": 5,
        "BTTTouchBarItemIconWidth": 22,
        "BTTTouchBarItemPlacement": 0,  # 0 = left side
    }

    config_json = json.dumps(widget_config).replace('"', '\\"')

    script = f'''
    tell application "BetterTouchTool"
        trigger_named "ClaudeCodeNotify" with parameter "{display_text}"
    end tell
    '''

    success, output = run_applescript(script)
    return success


def show_native_notification(action: str) -> bool:
    """Fallback: Show native macOS notification if BTT not available."""
    if action not in STATUSES or action == 'off':
        return True

    _, text, icon = STATUSES[action]
    display_text = f"{icon} Claude Code: {text}"

    script = f'''
    display notification "{text}" with title "Claude Code" subtitle "{icon}"
    '''

    success, _ = run_applescript(script)
    return success


def flash_touchbar(action: str, times: int = 3, delay: float = 0.3) -> None:
    """Flash the Touch Bar notification for attention."""
    for _ in range(times):
        send_btt_notification(action)
        time.sleep(delay)
        send_btt_notification('off')
        time.sleep(delay)
    # Leave the notification on after flashing
    send_btt_notification(action)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nUsage: claude-notify.py [flash|question|permission|waiting|context|off]")
        sys.exit(1)

    action = sys.argv[1].lower()

    if action not in STATUSES:
        print(f"Unknown action: {action}")
        print("Valid actions: flash, question, permission, waiting, context, off")
        sys.exit(1)

    # Check for optional flash count argument
    flash_count = 3
    if len(sys.argv) >= 3:
        try:
            flash_count = int(sys.argv[2])
        except ValueError:
            pass

    # Try BetterTouchTool first
    if check_bettertouchtool():
        if action in ['flash', 'question', 'permission', 'waiting', 'context']:
            flash_touchbar(action, times=flash_count)
        else:
            send_btt_notification(action)
        print(f"Touch Bar notification: {action}")
    else:
        # Fallback to native notification
        print("BetterTouchTool not running, using native notification")
        show_native_notification(action)


if __name__ == "__main__":
    main()
