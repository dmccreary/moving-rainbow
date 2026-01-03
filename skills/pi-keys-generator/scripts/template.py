#!/usr/bin/env python3
"""
Pi 500+ Keyboard LED Control Template

This template provides a starting point for creating custom keyboard LED scripts.
Copy this file and modify the main logic section for your specific use case.

Usage:
    python3 template.py

Requirements:
    pip install RPiKeyboardConfig
"""
from RPiKeyboardConfig import RPiKeyboardConfig
import time


# HSV Color Constants (hue, saturation, value)
RED = (0, 255, 255)
ORANGE = (21, 255, 255)
YELLOW = (43, 255, 255)
GREEN = (85, 255, 255)
CYAN = (128, 255, 255)
BLUE = (170, 255, 255)
PURPLE = (213, 255, 255)
WHITE = (0, 0, 255)
OFF = (0, 0, 0)


def flash_all_keys(keyboard, color, times=3, on_time=0.2, off_time=0.2):
    """Flash all keyboard LEDs a specific color."""
    for _ in range(times):
        for led in keyboard.get_leds():
            keyboard.set_led_by_idx(idx=led.idx, colour=color)
        keyboard.send_leds()
        time.sleep(on_time)
        keyboard.rgb_clear()
        keyboard.send_leds()
        time.sleep(off_time)


def set_key_group(keyboard, positions, color):
    """Set a group of keys to a specific color.

    Args:
        keyboard: RPiKeyboardConfig instance
        positions: List of [row, col] positions
        color: HSV tuple (hue, sat, val)
    """
    for pos in positions:
        keyboard.set_led_by_matrix(matrix=pos, colour=color)
    keyboard.send_leds()


def main():
    keyboard = RPiKeyboardConfig()
    current_preset = None

    try:
        # Save current preset to restore later
        current_preset = keyboard.get_current_preset_index()

        # Enable direct LED control
        keyboard.set_led_direct_effect()

        # ========================================
        # === YOUR MAIN LOGIC HERE ===
        # ========================================

        # Example: Set F1-F4 keys to blue
        f_keys = [[0, 1], [0, 2], [0, 3], [0, 4]]
        set_key_group(keyboard, f_keys, BLUE)

        # Example: Flash entire keyboard green
        # flash_all_keys(keyboard, GREEN, times=3)

        # Example: Rainbow animation
        # for hue in range(0, 256, 5):
        #     for led in keyboard.get_leds():
        #         keyboard.set_led_by_idx(idx=led.idx, colour=(hue, 255, 255))
        #     keyboard.send_leds()
        #     time.sleep(0.05)

        # Keep the effect visible
        print("Press Ctrl+C to exit...")
        while True:
            time.sleep(1)

        # ========================================

    except KeyboardInterrupt:
        print("\nInterrupted by user")
    finally:
        # Cleanup: restore previous state
        keyboard.rgb_clear()
        keyboard.send_leds()
        if current_preset is not None:
            keyboard.set_current_preset_index(current_preset, save_index=False)
        keyboard.close()
        print("Keyboard restored to previous state")


if __name__ == "__main__":
    main()
