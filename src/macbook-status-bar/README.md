# MacBook Pro Touch Bar Status Notifications for Claude Code

Display Claude Code status notifications directly on your MacBook Pro Touch Bar with text descriptions and color-coded indicators.

## Features

| Event | Icon | Text | Color |
|-------|------|------|-------|
| Task Complete | ✓ | Task Complete | Blue |
| Question Waiting | ? | Question Waiting | Blue |
| Permission Needed | ⚠ | Permission Needed | Yellow |
| Waiting for Input | ⏳ | Waiting for Input | Red |
| Context Warning | ⚡ | Context Warning | Orange |

## Requirements

- MacBook Pro with Touch Bar (2016-2020 models)
- macOS 10.12.2 or later
- [BetterTouchTool](https://folivora.ai/) (recommended for Touch Bar customization)

## Quick Setup (Shell Script Method)

This is the simplest approach using a shell script widget in BetterTouchTool.

### 1. Make the script executable

```bash
chmod +x /Users/dan/Documents/ws/moving-rainbow/src/macbook-status-bar/claude-notify-simple.sh
```

### 2. Configure BetterTouchTool

1. Open BetterTouchTool
2. Go to **TouchBar** section
3. Click **+ Widget/Gesture** and select **Shell Script / Task Widget**
4. Configure the widget:
   - **Script**: `cat /tmp/claude-code-status.txt 2>/dev/null || echo ""`
   - **Execute every**: 1 second
   - **Touch Bar Button Width**: 150
   - **Placement**: Left side of Touch Bar

### 3. Configure Claude Code Hooks

Add to your `~/.claude/settings.json`:

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/claude-notify-simple.sh waiting"
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/claude-notify-simple.sh flash"
          }
        ]
      }
    ]
  }
}
```

## Advanced Setup (Python Script Method)

The Python script (`claude-notify.py`) provides more control over animations and BetterTouchTool integration.

### 1. Enable BetterTouchTool Scripting

1. Open BetterTouchTool Preferences
2. Go to **Scripting**
3. Enable **Allow controlling BetterTouchTool from Terminal/Apple Script**

### 2. Import the BTT Preset

1. Download `btt-preset.json`
2. In BetterTouchTool, go to **Presets** > **Import Preset**
3. Select the JSON file

### 3. Test the Script

```bash
python3 claude-notify.py flash      # Shows "✓ Task Complete"
python3 claude-notify.py question   # Shows "? Question Waiting"
python3 claude-notify.py permission # Shows "⚠ Permission Needed"
python3 claude-notify.py waiting    # Shows "⏳ Waiting for Input"
python3 claude-notify.py context    # Shows "⚡ Context Warning"
python3 claude-notify.py off        # Clears the notification
```

## Files in This Directory

| File | Description |
|------|-------------|
| `claude-notify.py` | Full Python script with BTT AppleScript integration |
| `claude-notify-simple.sh` | Simple shell script using temp file approach |
| `btt-preset.json` | BetterTouchTool preset for import |
| `sample-hooks.json` | Example Claude Code hooks configuration |

## How It Works

1. Claude Code triggers a hook event (e.g., task complete, waiting for input)
2. The hook runs the notification script
3. The script either:
   - Writes status to `/tmp/claude-code-status.txt` (simple method)
   - Or triggers a BTT named trigger via AppleScript (advanced method)
4. BetterTouchTool updates the Touch Bar widget
5. You see the status text on the left side of your Touch Bar

## Troubleshooting

### Touch Bar not updating
- Ensure BetterTouchTool is running
- Check that the shell script widget refresh interval is set to 1 second
- Verify the temp file is being written: `cat /tmp/claude-code-status.txt`

### AppleScript not working
- Enable "Allow controlling BetterTouchTool from Terminal" in BTT preferences
- Test with: `osascript -e 'tell application "BetterTouchTool" to trigger_named "ClaudeCodeNotify"'`

### Script permission denied
```bash
chmod +x claude-notify-simple.sh
chmod +x claude-notify.py
```

## Comparison with Pi 500+ Keyboard Version

| Feature | Pi 500+ Keyboard | MacBook Touch Bar |
|---------|------------------|-------------------|
| Visual Indicator | Function key LEDs (F1-F3) | Touch Bar widget |
| Text Display | None (LED colors only) | Full text + emoji |
| Colors | HSV LED colors | Hex colors via BTT |
| API | RPiKeyboardConfig | BetterTouchTool |
| Flashing | LED on/off cycles | Widget show/hide |

## See Also

- [Pi 500+ Keyboard Notifications](../pi-500-keyboard/) - RGB LED notifications for Raspberry Pi keyboard
- [BetterTouchTool Documentation](https://docs.folivora.ai/)
- [Claude Code Hooks Documentation](https://docs.anthropic.com/claude-code/hooks)
