# Keyboard Event Notifications Setup

**Date:** 2026-01-11

## Summary

Set up Claude Code hooks to trigger Raspberry Pi 500+ keyboard LED notifications when Claude needs attention or completes a task.

## Files Created/Modified

### 1. Notification Script
**File:** `/home/dan/ws/moving-rainbow/src/pi-500-keyboard/claude-notify.py`

Python script that controls the F1 key LED with different colors for different events:

| Command | Action | Color |
|---------|--------|-------|
| `claude-notify.py flash` | Task complete | Blue flash (20x) |
| `claude-notify.py question` | Waiting for input | Blue blink (10x) |
| `claude-notify.py permission` | Permission needed | Yellow blink (10x) |
| `claude-notify.py off` | Turn off | Off |

Uses `colorsys` module for RGB to HSV conversion (the `RPiKeyboardConfig` library requires HSV format).

### 2. Claude Code Hooks Configuration
**File:** `~/.claude/settings.json` (user-level settings, requires Claude Code restart)

Added hooks configuration:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/home/dan/ws/moving-rainbow/src/pi-500-keyboard/claude-notify.py flash"
          }
        ]
      }
    ],
    "Notification": [
      {
        "matcher": "idle_prompt",
        "hooks": [
          {
            "type": "command",
            "command": "/home/dan/ws/moving-rainbow/src/pi-500-keyboard/claude-notify.py question"
          }
        ]
      },
      {
        "matcher": "permission_prompt",
        "hooks": [
          {
            "type": "command",
            "command": "/home/dan/ws/moving-rainbow/src/pi-500-keyboard/claude-notify.py permission"
          }
        ]
      }
    ]
  }
}
```

**Important:** The `Stop` hook must NOT have a `matcher` field - only `Notification` hooks use matchers.

## Hook Events

| Hook Event | Matcher | Trigger |
|------------|---------|---------|
| `Stop` | (any) | Claude finishes responding |
| `Notification` | `idle_prompt` | Claude idle 60+ seconds waiting for input |
| `Notification` | `permission_prompt` | Claude needs permission to run a tool |

## Other Work in This Session

### Screenshot Keyboard Shortcuts
**File:** `/home/dan/.config/labwc/rc.xml`

Configured labwc (Wayland compositor) keybindings:

| Key | Action |
|-----|--------|
| Print Screen | Area screenshot with slurp selector |
| F8 | Full screen screenshot |
| F9 | Area screenshot with slurp selector |

Screenshots save to `~/screenshots/ss-YYYYMMDD-HHMMSS.png`

### Gmail Notifier
**File:** `/home/dan/ws/moving-rainbow/src/pi-500-keyboard/gmail-notifier.py`

Script that monitors Gmail via IMAP and blinks F7 red when there are unread emails. Requires:
- Gmail IMAP enabled
- App Password configured
- Credentials in `~/.gmail-notifier.conf` or environment variables

### RGB Color Conversion Best Practice
**File:** `/home/dan/ws/moving-rainbow/skills/pi-keys-generator/SKILL.md`

Updated the pi-keys-generator skill to document using Python's `colorsys` module for RGB to HSV conversion:

```python
import colorsys

def rgb_to_hsv(r, g, b):
    """Convert RGB (0-255) to HSV (0-255 scale for all components)."""
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    return (int(h * 255), int(s * 255), int(v * 255))

# Define colors in familiar RGB format
RED = rgb_to_hsv(255, 0, 0)
GREEN = rgb_to_hsv(0, 255, 0)
BLUE = rgb_to_hsv(0, 0, 255)
```

## Testing

```bash
# Test notification script
/home/dan/ws/moving-rainbow/src/pi-500-keyboard/claude-notify.py flash
/home/dan/ws/moving-rainbow/src/pi-500-keyboard/claude-notify.py question
/home/dan/ws/moving-rainbow/src/pi-500-keyboard/claude-notify.py permission

# Reload labwc config for screenshot shortcuts
killall -SIGHUP labwc
```

## Notes

- Raspberry Pi OS Bookworm uses **labwc** (not wayfire) as the Wayland compositor
- The `scrot` screenshot tool doesn't work on Wayland; use `grim` + `slurp` instead
- `RPiKeyboardConfig` library only accepts HSV colors, not RGB
- F1 key matrix position is `[0, 1]` (row 0, column 1)
- Hooks in `~/.claude/settings.json` require Claude Code restart to take effect
- The `Stop` hook does NOT use a matcher field (unlike `Notification` hooks)
