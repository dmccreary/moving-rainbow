# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Moving Rainbow project - an educational resource for teaching computational thinking and computer science concepts using LED strips and microcontrollers. The project uses both MicroPython (for Raspberry Pi Pico) and Arduino C++ for hands-on learning with addressable LEDs.

## Build and Documentation Commands

This project uses MkDocs for documentation generation:

```bash
# Build and serve documentation locally
mkdocs serve

# Build documentation for production
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

## Project Structure

### Core Architecture

- **`/src/`** - Source code organized by platform and kit type:
  - **`micropython/`** - MicroPython examples for Raspberry Pi Pico
  - **`arduino/`** - Arduino C++ sketches for various microcontrollers  
  - **`led-strip-two-buttons/`** - Main kit examples with configuration
  - **`pico/`** - Raspberry Pi Pico specific examples
  - Platform-specific directories for different hardware configurations

- **`/docs/`** - MkDocs documentation source:
  - **`lessons/`** - Step-by-step tutorials (01-blink.md through advanced topics)
  - **`getting-started/`** - Setup guides for hardware and software
  - **`teachers-guide/`** - Educational resources and methodology
  - **`kits/`** - Specific kit assembly and usage guides

- **`/site/`** - Generated documentation output (do not edit directly)

### Key Configuration Pattern

Most projects use a `config.py` file for hardware settings:
```python
NEOPIXEL_PIN = 0
NUMBER_PIXELS = 30
BUTTON_PIN_1 = 15
BUTTON_PIN_2 = 14
```

### Code Organization

- Projects follow a progressive learning structure (01-blink.py → 02-move.py → etc.)
- MicroPython examples use the `neopixel` and `machine` libraries
- Arduino examples use the Adafruit NeoPixel library
- Each platform has its own configuration approach but similar learning progression

## Development Workflow

1. **MicroPython Development**: Files are designed to run on Raspberry Pi Pico with NeoPixel strips
2. **Arduino Development**: Use Arduino IDE with appropriate board packages
3. **Documentation**: Edit Markdown files in `/docs/` and use `mkdocs serve` to preview changes
4. **Testing**: Hardware-dependent - requires physical LED strips and microcontrollers

## Educational Focus

This codebase is designed for teaching:
- Sequential programming concepts through LED animations
- Hardware interfacing with microcontrollers
- Color theory and pixel manipulation
- Button input handling and interactive programming
- Progressive complexity from simple blink to complex patterns

When working with this codebase, prioritize educational clarity and maintain the step-by-step learning progression that makes concepts accessible to beginners.