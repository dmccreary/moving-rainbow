#!/usr/bin/env python3
"""
Claude Code notification - flash keyboard LEDs when Claude needs attention.

Events:
  flash      - Task complete (blue flash on F1)
  question   - Question waiting (blue blink on F1)
  permission - Permission needed (yellow blink on F1)
  waiting    - Waiting for user input (red flash on F2)
  context    - Context window almost full (orange flash on F3)
  off        - Turn off notification
"""
from RPiKeyboardConfig import RPiKeyboardConfig
import colorsys
import sys
import time

def rgb_to_hsv(r, g, b):
    """Convert RGB (0-255) to HSV (0-255 scale for all components)."""
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    return (int(h * 255), int(s * 255), int(v * 255))

# Key positions (row, column)
F1_KEY = [0, 1]  # Task complete, questions, permissions
F2_KEY = [0, 2]  # Waiting for input
F3_KEY = [0, 3]  # Context window warning

# Colors
GREEN = rgb_to_hsv(0, 255, 0)
BLUE = rgb_to_hsv(0, 100, 255)
YELLOW = rgb_to_hsv(255, 255, 0)
RED = rgb_to_hsv(255, 0, 0)
ORANGE = rgb_to_hsv(255, 69, 0)  # Red-orange for better visibility
OFF = (0, 0, 0)

def flash_key(keyboard, key, color, times=3, delay=0.2):
    """Flash a key a specific color."""
    for _ in range(times):
        keyboard.set_led_by_matrix(matrix=key, colour=color)
        keyboard.send_leds()
        time.sleep(delay)
        keyboard.set_led_by_matrix(matrix=key, colour=OFF)
        keyboard.send_leds()
        time.sleep(delay)

def blink_key(keyboard, key, color, times=5, delay=0.3):
    """Blink a key for a limited time."""
    for _ in range(times):
        keyboard.set_led_by_matrix(matrix=key, colour=color)
        keyboard.send_leds()
        time.sleep(delay)
        keyboard.set_led_by_matrix(matrix=key, colour=OFF)
        keyboard.send_leds()
        time.sleep(delay)

def main():
    if len(sys.argv) < 2:
        print("Usage: claude-notify.py [flash|question|permission|waiting|context|off]")
        sys.exit(1)

    action = sys.argv[1].lower()

    keyboard = RPiKeyboardConfig()

    try:
        current_preset = keyboard.get_current_preset_index()
        keyboard.set_led_direct_effect()

        if action == 'flash':
            # Task complete - flash blue on F1
            flash_key(keyboard, F1_KEY, BLUE, times=20)
        elif action == 'question':
            # Question waiting - blink blue on F1
            blink_key(keyboard, F1_KEY, BLUE, times=10, delay=0.4)
        elif action == 'permission':
            # Permission needed - blink yellow on F1
            blink_key(keyboard, F1_KEY, YELLOW, times=10, delay=0.3)
        elif action == 'waiting':
            # Waiting for user input - flash red on F2
            flash_key(keyboard, F2_KEY, RED, times=15, delay=0.3)
        elif action == 'context':
            # Context window almost full - flash orange on F3
            flash_key(keyboard, F3_KEY, ORANGE, times=10, delay=0.3)
        elif action == 'off':
            # Turn off all notification keys
            for key in [F1_KEY, F2_KEY, F3_KEY]:
                keyboard.set_led_by_matrix(matrix=key, colour=OFF)
            keyboard.send_leds()
        else:
            print(f"Unknown action: {action}")

    except KeyboardInterrupt:
        pass
    finally:
        keyboard.rgb_clear()
        keyboard.send_leds()
        keyboard.set_current_preset_index(current_preset, save_index=False)
        keyboard.close()

if __name__ == "__main__":
    main()
