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

- **`led-strip-two-buttons/`** - Main kit examples with numbered progression (01-blink.py, 02-move.py, etc.)
- **`micropython/`** - MicroPython examples for Raspberry Pi Pico
- **`arduino/`** - Arduino C++ sketches using Adafruit NeoPixel library
- **`pi-500-keyboard/`** - Raspberry Pi 500+ keyboard RGB LED control scripts
- Kit-specific directories (e.g., `katies-busy-board/`, `tiki-bar-sign/`)

### Documentation (`/docs/`)

- **`lessons/`** - Progressive tutorials from basic to advanced
- **`chapters/`** - Structured course chapters
- **`kits/`** - Kit-specific assembly and usage guides
- **`sims/`** - Interactive MicroSims (browser-based simulations)
- **`teachers-guide/`** - Educational methodology and resources

### Key Configuration Pattern

Each kit uses a `config.py` for hardware abstraction:
```python
NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30
BUTTON_PIN_1 = 15
BUTTON_PIN_2 = 14
```

## Platform-Specific Notes

### MicroPython (Raspberry Pi Pico)
- Uses `neopixel` and `machine` libraries
- Files run directly on Pico via Thonny IDE or similar

### Arduino
- Uses Adafruit NeoPixel library
- Standard Arduino IDE workflow

### Pi 500+ Keyboard RGB
- Uses `rpi-keyboard-config` command-line tool and `RPiKeyboardConfig` Python library
- 45 built-in effects (IDs 0-44), 7 preset slots (0-6)
- Key commands: `rpi-keyboard-config effect <id>`, `rpi-keyboard-config preset set <slot> <effect>`

## Educational Design Principles

- **Progressive complexity**: Lessons build incrementally (blink → motion → color → complex patterns)
- **Immediate visual feedback**: Every code change produces visible LED results
- **Low barrier to entry**: ~$13 total hardware cost, minimal wiring (3 wires for LED strip)
- **Transferable concepts**: Loops, conditionals, and functions taught through LED manipulation

When modifying code or documentation, prioritize clarity for beginners over code elegance. Maintain the numbered lesson progression and consistent configuration patterns across kits.