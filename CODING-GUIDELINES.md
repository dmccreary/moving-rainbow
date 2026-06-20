# Coding Guidelines

This guide should be used when generating sample code within the documentation
or when generating code for the project kits.

## Key Configuration Pattern

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

### Pi 500+ Keyboard RGB
- Uses `rpi-keyboard-config` command-line tool and `RPiKeyboardConfig` Python library
- 45 built-in effects (IDs 0-44), 7 preset slots (0-6)
- Key commands: `rpi-keyboard-config effect <id>`, `rpi-keyboard-config preset set <slot> <effect>`
- Keystroke-triggered effects: 29, 31-42 (react to key presses)
- See `src/pi-500-keyboard/cycle-effects.sh` for effect names

### MicroSims Generation
- Use the /microsim-generator skill
- Follow the guidelines in that skill for all MicroSims
- Place browser-based simulations in `docs/sims/`
- Each MicroSim has: `index.md` (documentation), `main.html` (entry point), `sketch.js` (p5.js code)
- Each MicroSim must be listed in the main mkdocs.yml and the /docs/sims/index.md using the mkdocs-material grid-card format

## Lesson File Numbering Convention

Files in `src/led-strip-two-buttons/` follow a progression:
- 01-10: Basics (blink, colors, dimmer, movement)
- 11-20: Patterns (bands, comets, rainbow, candle, theater chase)
- 20-30: Advanced (clock, larson scanner, random bounce)
- 30-40: Button integration
- 50+: Complete demos
