---
name: pi-keys-generator
description: This skill generates Python scripts and shell scripts to control RGB LEDs on the Raspberry Pi 500+ keyboard. Use this skill when the user asks to create keyboard lighting effects, animations, color patterns, notification systems, or any program that controls the Pi 500+ keyboard LEDs. This skill should be used for requests like "turn F1-F12 keys blue", "create a typing speed indicator", or "make an email notification effect".
---

# Pi Keys Generator

## Overview

This skill generates Python and shell scripts for controlling RGB LEDs on the Raspberry Pi 500+ keyboard using the `RPiKeyboardConfig` Python library and `rpi-keyboard-config` command-line tool.

## When to Use This Skill

- Creating scripts to set specific keys to specific colors
- Building keyboard LED animations (rainbow, breathing, waves)
- Developing notification systems (flash keys for alerts)
- Making typing-reactive effects
- Setting up preset configurations
- Any task involving Pi 500+ keyboard LED control

## Output Locations

Save generated files to these locations if the directories exist:

- **Python scripts**: `$MOVING_RAINBOW_HOME/src/pi-500-keyboard/examples/`
- **Shell scripts**: `$MOVING_RAINBOW_HOME/src/pi-500-keyboard/scripts/`

If the directories do not exist, save to the user's current working directory.

## Script Generation Guidelines

### Python Script Template

All Python scripts controlling the keyboard follow this structure:

```python
#!/usr/bin/env python3
"""
Script description here.
"""
from RPiKeyboardConfig import RPiKeyboardConfig
import colorsys
import time

def rgb_to_hsv(r, g, b):
    """Convert RGB (0-255) to HSV (0-255 scale for all components)."""
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    return (int(h * 255), int(s * 255), int(v * 255))

# Define colors in RGB format
RED = rgb_to_hsv(255, 0, 0)
GREEN = rgb_to_hsv(0, 255, 0)
BLUE = rgb_to_hsv(0, 0, 255)
OFF = (0, 0, 0)

def main():
    keyboard = RPiKeyboardConfig()

    try:
        # Save current preset to restore later
        current_preset = keyboard.get_current_preset_index()

        # Enable direct LED control
        keyboard.set_led_direct_effect()

        # === Main logic here ===

    except KeyboardInterrupt:
        print("\nInterrupted by user")
    finally:
        # Cleanup: restore previous state
        keyboard.rgb_clear()
        keyboard.send_leds()
        keyboard.set_current_preset_index(current_preset, save_index=False)
        keyboard.close()

if __name__ == "__main__":
    main()
```

### Shell Script Template

Shell scripts use the `rpi-keyboard-config` command:

```bash
#!/bin/bash
# Script description here

# Set an effect
rpi-keyboard-config effect <effect_id> [--speed 255] [--hue 128] [--sat 255]

# Set a preset
rpi-keyboard-config preset index <0-6>

# Set all LEDs to a color (HSV format: "hue,sat,val")
rpi-keyboard-config leds set --colour "128,255,255"

# Set all LEDs to a color (RGB format)
rpi-keyboard-config leds set --colour "rgb(255,0,0)"

# Clear all LEDs
rpi-keyboard-config leds clear

# Set brightness (0-255)
rpi-keyboard-config brightness 255
```

## Color Reference (HSV)

Colors use HSV format with values 0-255:

| Color | Hue Value |
|-------|-----------|
| Red | 0 |
| Orange | 21 |
| Yellow | 43 |
| Green | 85 |
| Cyan | 128 |
| Blue | 170 |
| Purple | 213 |

Saturation: 255 = full color, 0 = white
Value: 255 = full brightness, 0 = off

## Using RGB Colors (Recommended)

While the `RPiKeyboardConfig` library requires HSV colors, you can define colors in the more familiar RGB format and convert them using Python's built-in `colorsys` module.

### RGB to HSV Conversion Helper

Add this helper function to your scripts:

```python
import colorsys

def rgb_to_hsv(r, g, b):
    """Convert RGB (0-255) to HSV (0-255 scale for all components)."""
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    return (int(h * 255), int(s * 255), int(v * 255))
```

### Defining Colors in RGB

```python
# Define colors in familiar RGB format
RED = rgb_to_hsv(255, 0, 0)
GREEN = rgb_to_hsv(0, 255, 0)
BLUE = rgb_to_hsv(0, 0, 255)
YELLOW = rgb_to_hsv(255, 255, 0)
CYAN = rgb_to_hsv(0, 255, 255)
MAGENTA = rgb_to_hsv(255, 0, 255)
ORANGE = rgb_to_hsv(255, 165, 0)
WHITE = rgb_to_hsv(255, 255, 255)
OFF = (0, 0, 0)

# Use with the keyboard API
keyboard.set_led_by_matrix(matrix=[0, 1], colour=RED)
```

This approach is preferred because:
- RGB values are more intuitive and widely understood
- Easy to use web color pickers to find RGB values
- No need to memorize HSV hue values

## Key Matrix Reference

Common key positions (row, column):

| Key | Matrix Position |
|-----|-----------------|
| ESC | [0, 0] |
| F1-F12 | [0, 1] through [0, 12] |
| W | [2, 2] |
| A | [3, 1] |
| S | [3, 2] |
| D | [3, 3] |
| Space | [5, 6] |
| Arrow Up | [4, 15] |
| Arrow Left | [5, 14] |
| Arrow Down | [5, 15] |
| Arrow Right | [5, 16] |

For the complete matrix layout, use: `rpi-keyboard-config info --ascii`

## Common Patterns

### Set Specific Keys to a Color

```python
# Set function keys F1-F4 to blue (using RGB conversion)
BLUE = rgb_to_hsv(0, 0, 255)
f_keys = [[0, 1], [0, 2], [0, 3], [0, 4]]
for pos in f_keys:
    keyboard.set_led_by_matrix(matrix=pos, colour=BLUE)
keyboard.send_leds()
```

### Flash Effect for Notifications

```python
def flash_keyboard(keyboard, color, times=3, delay=0.2):
    """Flash entire keyboard a color."""
    for _ in range(times):
        for led in keyboard.get_leds():
            keyboard.set_led_by_idx(idx=led.idx, colour=color)
        keyboard.send_leds()
        time.sleep(delay)
        keyboard.rgb_clear()
        keyboard.send_leds()
        time.sleep(delay)
```

### Rainbow Animation

```python
def rainbow_wave(keyboard, duration=10):
    """Animate rainbow across keyboard."""
    start = time.time()
    while time.time() - start < duration:
        for led in keyboard.get_leds():
            hue = (led.x * 3 + int(time.time() * 50)) % 256
            keyboard.set_led_by_idx(idx=led.idx, colour=(hue, 255, 255))
        keyboard.send_leds()
        time.sleep(0.03)
```

### Integration with External Events

```python
# Example: Check for condition and flash
def check_and_notify(keyboard, check_function, color):
    """Flash keyboard when condition is true."""
    if check_function():
        flash_keyboard(keyboard, color)
        return True
    return False
```

## Effect IDs Quick Reference

| ID | Effect | Reactive |
|----|--------|----------|
| 0 | OFF | No |
| 2 | Solid Color | No |
| 6 | Breathing | No |
| 19 | Cycle Pinwheel | No |
| 24 | Raindrops | No |
| 25 | Jellybean Raindrops | No |
| 29 | Typing Heatmap | Yes |
| 30 | Digital Rain | No |
| 31 | Solid Reactive Simple | Yes |
| 39 | Splash | Yes |
| 40 | Multisplash | Yes |

## API Reference

For detailed API documentation including all methods and parameters, consult `references/api_reference.md`.

Key methods:
- `keyboard.set_led_by_matrix(matrix=[row, col], colour=(h, s, v))` - Set LED by position
- `keyboard.set_led_by_idx(idx=n, colour=(h, s, v))` - Set LED by index
- `keyboard.send_leds()` - Apply queued LED changes
- `keyboard.rgb_clear()` - Turn off all LEDs
- `keyboard.set_led_direct_effect()` - Enable direct LED control
- `keyboard.get_leds()` - Get list of all LEDs
- `keyboard.set_brightness(n)` - Set global brightness (0-255)
- `keyboard.close()` - Close connection (always call in finally block)

## Example Prompts and Responses

**Prompt:** "Create a script that turns the F1-F12 keys blue"

Generate a Python script that:
1. Initializes keyboard connection
2. Enables direct LED mode
3. Sets keys at matrix positions [0,1] through [0,12] to blue (hue=170)
4. Includes proper cleanup

**Prompt:** "Make a typing speed indicator that changes key colors"

Generate a Python script that:
1. Uses pynput to track keystrokes
2. Calculates typing speed (WPM)
3. Maps speed to hue (slow=blue, fast=red)
4. Updates all key colors based on current speed

**Prompt:** "Create a notification effect when I get an email"

Generate a Python script that:
1. Monitors for a trigger (file, IMAP, or webhook)
2. Saves current preset
3. Flashes keyboard purple 3 times
4. Restores previous preset
