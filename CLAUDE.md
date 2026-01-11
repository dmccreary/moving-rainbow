# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Moving Rainbow project - an educational resource for teaching computational thinking and computer science concepts using LED strips and microcontrollers. The project uses both MicroPython (for Raspberry Pi Pico) and Arduino C++ for hands-on learning with addressable LEDs (WS2812B/NeoPixels).

## Build and Documentation Commands

This project uses MkDocs with Material theme for documentation:

```bash
mkdocs serve        # Build and serve locally at http://127.0.0.1:8000
mkdocs build        # Build for production (outputs to /site/)
mkdocs gh-deploy    # Deploy to GitHub Pages
```

## Project Structure

### Source Code (`/src/`)

- **`led-strip-two-buttons/`** - Main kit examples with numbered progression (01-blink.py through 60-pixel-demo.py). This is the canonical reference for lesson code.
- **`arduino/`** - Arduino C++ sketches using Adafruit NeoPixel library (~79 sketch directories)
- **`pi-500-keyboard/`** - Raspberry Pi 500+ keyboard RGB LED control scripts
- Kit-specific directories (e.g., `katies-busy-board/`, `tiki-bar-sign/`, `kits/holiday-hats/`)

### Documentation (`/docs/`)

- **`lessons/`** - Progressive tutorials mapped to numbered source files
- **`sims/`** - Interactive MicroSims (p5.js browser simulations) with `templates/` for creating new sims
- **`kits/`** - Kit-specific assembly and usage guides
- **`prompts/`** - GenAI prompts for content generation

### Key Configuration Pattern

Each kit uses a `config.py` for hardware abstraction that is imported by all lesson files:
```python
# src/led-strip-two-buttons/config.py
NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30
BUTTON_PIN_1 = 15
BUTTON_PIN_2 = 14
```

When creating new MicroPython examples, always import config and use `config.NEOPIXEL_PIN`, `config.NUMBER_PIXELS`, etc.

## Platform-Specific Notes

### MicroPython (Raspberry Pi Pico)
- Uses `neopixel` and `machine` libraries (built into MicroPython)
- Standard pattern: `strip = NeoPixel(Pin(config.NEOPIXEL_PIN), config.NUMBER_PIXELS)`
- Files run directly on Pico via Thonny IDE

### Arduino
- Uses Adafruit NeoPixel library
- Standard Arduino IDE workflow

### Pi 500+ Keyboard RGB
- Uses `rpi-keyboard-config` command-line tool and `RPiKeyboardConfig` Python library
- 45 built-in effects (IDs 0-44), 7 preset slots (0-6)
- Key commands: `rpi-keyboard-config effect <id>`, `rpi-keyboard-config preset set <slot> <effect>`
- Keystroke-triggered effects: 29, 31-42 (react to key presses)
- See `src/pi-500-keyboard/cycle-effects.sh` for effect names

### MicroSims
- Browser-based p5.js simulations in `docs/sims/`
- Each sim has: `index.md` (documentation), `main.html` (entry point), `sketch.js` (p5.js code)
- Use `docs/sims/templates/` as starting point for new sims

## Lesson File Numbering Convention

Files in `src/led-strip-two-buttons/` follow a progression:
- 01-10: Basics (blink, colors, dimmer, movement)
- 11-20: Patterns (bands, comets, rainbow, candle, theater chase)
- 20-30: Advanced (clock, larson scanner, random bounce)
- 30-40: Button integration
- 50+: Complete demos

When adding new lessons, maintain this numbering scheme.

## Educational Design Principles

- **Progressive complexity**: Lessons build incrementally (blink → motion → color → complex patterns)
- **Immediate visual feedback**: Every code change produces visible LED results
- **Low barrier to entry**: ~$13 total hardware cost, minimal wiring (3 wires for LED strip)

When modifying code or documentation, prioritize clarity for beginners over code elegance. Maintain the numbered lesson progression and consistent configuration patterns across kits.

## Claude Code Keyboard Notifications

This project includes a notification system that flashes the F1 key on the Pi 500+ keyboard when Claude Code needs attention.

### Notification Script
**File:** `src/pi-500-keyboard/claude-notify.py`

| Command | Action | Color |
|---------|--------|-------|
| `claude-notify.py flash` | Task complete | Blue flash (20x) |
| `claude-notify.py question` | Waiting for input | Blue blink (10x) |
| `claude-notify.py permission` | Permission needed | Yellow blink (10x) |
| `claude-notify.py off` | Turn off | Off |

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