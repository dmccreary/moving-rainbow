# RPiKeyboardConfig Python Library Reference

This reference documents the RPiKeyboardConfig Python library for controlling RGB LEDs on the Raspberry Pi 500+ keyboard.

## Installation

```bash
pip install RPiKeyboardConfig
```

## Classes

### LED

Represents a single LED on the keyboard.

**Attributes:**
- `idx` (int): LED index (0-83 for 84 keys)
- `matrix` (List[int]): [row, column] position on keyboard
- `flags` (int): LED flags
- `x` (int): X coordinate
- `y` (int): Y coordinate
- `colour` (Tuple[int, int, int]): HSV color tuple (hue, saturation, value)

### Preset

Represents a keyboard preset configuration.

**Constructor:**
```python
Preset(
    effect: int,           # Effect ID (0-44)
    flags=LED_FLAG_ALL,    # Which LEDs to affect
    speed=255,             # Animation speed (0-255)
    fixed_hue=False,       # Lock hue value
    startup_animation=..., # Startup animation config
    hue=255,               # Hue value (0-255)
    sat=255                # Saturation value (0-255)
)
```

### RPiKeyboardConfig

Main class for keyboard control.

## Core Methods

### Initialization

```python
from RPiKeyboardConfig import RPiKeyboardConfig

keyboard = RPiKeyboardConfig()  # Auto-detect keyboard
keyboard = RPiKeyboardConfig(path="/dev/hidraw0")  # Specific device
```

### Cleanup

```python
keyboard.close()  # Close HID connection when done
```

## LED Control Methods

### Direct LED Control Mode

Before setting individual LED colors, enable direct control:

```python
keyboard.set_led_direct_effect()  # Required before setting LED colors
```

### Setting LED Colors

Colors use HSV format: (hue, saturation, value) where each is 0-255.

```python
# By matrix position [row, column]
keyboard.set_led_by_matrix(matrix=[2, 3], colour=(180, 255, 255))  # W key purple

# By LED index (0-83)
keyboard.set_led_by_idx(idx=33, colour=(20, 255, 255))  # Orange
```

### Sending LED Updates

LED colors are queued until sent:

```python
# Queue multiple LED changes
keyboard.set_led_by_matrix(matrix=[0, 0], colour=(0, 255, 255))
keyboard.set_led_by_matrix(matrix=[0, 1], colour=(85, 255, 255))
keyboard.set_led_by_matrix(matrix=[0, 2], colour=(170, 255, 255))

# Send all queued changes at once
keyboard.send_leds()
```

### Getting LED Information

```python
# Get all LEDs
leds = keyboard.get_leds()  # Returns List[LED]

# Get specific LED info
led = keyboard.get_led_info(idx=33)

# Get current LED colors
current_leds = keyboard.get_current_direct_leds()

# Get number of LEDs
num_leds = keyboard.get_number_leds()  # Returns 84
```

### Clearing LEDs

```python
keyboard.rgb_clear()  # Turn off all LEDs
keyboard.send_leds()  # Apply the clear
```

### Converting Matrix to Index

```python
idx = keyboard.led_matrix_to_idx(matrix=(2, 3))  # Returns LED index for [2,3]
```

## Brightness and Hue

### Global Brightness

```python
brightness = keyboard.get_brightness()  # Get current (0-255)
keyboard.set_brightness(255)  # Set max brightness
```

### Global Hue

```python
hue = keyboard.get_hue()  # Get current (0-255)
keyboard.set_hue(128)  # Set to cyan
```

## Preset Management

### Current Preset

```python
# Get current preset index (0-6)
idx = keyboard.get_current_preset_index()

# Set current preset
keyboard.set_current_preset_index(3, save_index=True)

# Revert to saved preset
keyboard.revert_to_saved_preset()
```

### Preset Configuration

```python
from RPiKeyboardConfig import Preset

# Get a preset
preset = keyboard.get_preset(preset_index=2)

# Create and set a preset
new_preset = Preset(effect=25, speed=200, hue=128, sat=255)
keyboard.set_preset(preset_index=2, new_preset)
```

## Effects

### Available Effects

```python
effects = keyboard.get_supported_effects()  # Returns List[str]
```

### Temporary Effects

```python
# Get current effect
effect = keyboard.get_current_effect()

# Set temporary effect (doesn't save)
keyboard.set_temp_effect(preset=Preset(effect=30, speed=255))
```

## Saving and Loading

### Direct LED Colors

```python
keyboard.save_direct_leds()  # Save to EEPROM (effect slot 1)
keyboard.load_direct_leds()  # Load from EEPROM
```

### Reset to Defaults

```python
keyboard.reset_presets_and_direct_leds()  # Reset all RGB settings
keyboard.reset_keymap()  # Reset key mappings
```

## Keyboard State

### Key Press Detection

```python
# Get currently pressed keys (requires unlock)
matrix_state = keyboard.get_switch_matrix_state()  # Returns List[List[bool]]
```

### Unlock for Key Detection

```python
keyboard.unlock(restricted_commands=False)  # Unlock with visual prompt
# User must press ESC then ENTER
keyboard.lock()  # Lock again when done
```

### System Information

```python
firmware = keyboard.get_firmware_version()  # Returns (major, minor, patch)
uptime = keyboard.get_uptime()  # Returns milliseconds since boot
```

## HSV Color Reference

Hue values (0-255) map to colors:

| Hue | Color |
|-----|-------|
| 0 | Red |
| 21 | Orange |
| 43 | Yellow |
| 85 | Green |
| 128 | Cyan |
| 170 | Blue |
| 213 | Purple/Magenta |
| 255 | Red (wraps) |

Saturation: 0 = white, 255 = full color
Value: 0 = off, 255 = full brightness

## Keyboard Matrix Layout

Use `keyboard.get_ascii_keycode_map()` to see the full layout, or use `rpi-keyboard-config info --ascii` from terminal.

Key rows and approximate columns:
- Row 0: ESC, F1-F12, Print/Scroll/Pause
- Row 1: `/~, 1-0, -=, Backspace, Ins/Home/PgUp
- Row 2: Tab, Q-P, []\, Del/End/PgDn
- Row 3: Caps, A-L, ;'Enter
- Row 4: LShift, Z-M, ,./RShift, Up
- Row 5: Ctrl, Super, Alt, Space, Alt, Fn, Ctrl, Left/Down/Right

## Effect IDs Reference

| ID | Effect Name | Keystroke Triggered |
|----|-------------|---------------------|
| 0 | OFF | No |
| 1 | Direct | No |
| 2 | Solid Color | No |
| 3 | Alphas Mods | No |
| 4 | Gradient Up Down | No |
| 5 | Gradient Left Right | No |
| 6 | Breathing | No |
| 7 | Band Sat | No |
| 8 | Band Val | No |
| 9 | Band Pinwheel Sat | No |
| 10 | Band Pinwheel Val | No |
| 11 | Band Spiral Sat | No |
| 12 | Band Spiral Val | No |
| 13 | Cycle All | No |
| 14 | Cycle Left Right | No |
| 15 | Cycle Up Down | No |
| 16 | Rainbow Moving Chevron | No |
| 17 | Cycle Out In | No |
| 18 | Cycle Out In Dual | No |
| 19 | Cycle Pinwheel | No |
| 20 | Cycle Spiral | No |
| 21 | Dual Beacon | No |
| 22 | Rainbow Beacon | No |
| 23 | Rainbow Pinwheels | No |
| 24 | Raindrops | No |
| 25 | Jellybean Raindrops | No |
| 26 | Hue Breathing | No |
| 27 | Hue Pendulum | No |
| 28 | Hue Wave | No |
| 29 | Typing Heatmap | Yes |
| 30 | Digital Rain | No |
| 31 | Solid Reactive Simple | Yes |
| 32 | Solid Reactive | Yes |
| 33 | Solid Reactive Wide | Yes |
| 34 | Solid Reactive Multiwide | Yes |
| 35 | Solid Reactive Cross | Yes |
| 36 | Solid Reactive Multicross | Yes |
| 37 | Solid Reactive Nexus | Yes |
| 38 | Solid Reactive Multinexus | Yes |
| 39 | Splash | Yes |
| 40 | Multisplash | Yes |
| 41 | Solid Splash | Yes |
| 42 | Solid Multisplash | Yes |
| 43 | Pixel Rain | No |
| 44 | Pixel Fractal | No |

## Common Patterns

### Flash All Keys Then Restore

```python
from RPiKeyboardConfig import RPiKeyboardConfig
import time

keyboard = RPiKeyboardConfig()
current_idx = keyboard.get_current_preset_index()
keyboard.set_led_direct_effect()

# Flash red
for led in keyboard.get_leds():
    keyboard.set_led_by_idx(idx=led.idx, colour=(0, 255, 255))
keyboard.send_leds()
time.sleep(0.5)

# Restore
keyboard.rgb_clear()
keyboard.send_leds()
keyboard.set_current_preset_index(current_idx, save_index=False)
keyboard.close()
```

### Animate Through Hues

```python
import time
for hue in range(0, 256, 5):
    for led in keyboard.get_leds():
        keyboard.set_led_by_idx(idx=led.idx, colour=(hue, 255, 255))
    keyboard.send_leds()
    time.sleep(0.05)
```

### Set Specific Key Group

```python
# Set WASD keys to green
wasd_positions = [[2, 1], [3, 0], [3, 1], [3, 2]]  # W, A, S, D
for pos in wasd_positions:
    keyboard.set_led_by_matrix(matrix=pos, colour=(85, 255, 255))
keyboard.send_leds()
```
