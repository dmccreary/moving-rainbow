# Claude Code Keyboard Notifications

Some classrooms use Claude Code and the Raspberry Pi 500 that has LEDs on the keyboard.
For these classrooms, we can update the key LEDs when Claude is working with the teachers or students.

This project includes a notification system that flashes function keys (F1-F3) on the Pi 500+ keyboard when Claude Code needs attention.

### Notification Script
**File:** `src/pi-500-keyboard/claude-notify.py`

| Command | Key | Action | Color |
|---------|-----|--------|-------|
| `claude-notify.py flash` | F1 | Task complete | Blue flash (20x) |
| `claude-notify.py question` | F1 | Question asked | Blue blink (10x) |
| `claude-notify.py permission` | F1 | Permission needed | Yellow blink (10x) |
| `claude-notify.py waiting` | F2 | Waiting for user input | Red flash (15x) |
| `claude-notify.py context` | F3 | Context window almost full | Orange flash (10x) |
| `claude-notify.py off` | All | Turn off | Off |

### Hooks Configuration
**File:** `~/.claude/settings.json` (user-level, requires Claude Code restart to take effect)

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
            "command": "/home/dan/ws/moving-rainbow/src/pi-500-keyboard/claude-notify.py waiting"
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
    ],
    "PreCompact": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/home/dan/ws/moving-rainbow/src/pi-500-keyboard/claude-notify.py context"
          }
        ]
      }
    ]
  }
}
```

**Important:** The `Stop` and `PreCompact` hooks must NOT have a `matcher` field - only `Notification` hooks use matchers.