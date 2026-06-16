#!/usr/bin/env python3
"""
Test script to light up F1 (blue), F2 (red), and F3 (orange) simultaneously.
Press Ctrl+C to exit and restore keyboard preset.
"""
from RPiKeyboardConfig import RPiKeyboardConfig
import colorsys
import time

def rgb_to_hsv(r, g, b):
    """Convert RGB (0-255) to HSV (0-255 scale for all components)."""
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    return (int(h * 255), int(s * 255), int(v * 255))

# Key positions (row, column)
F1_KEY = [0, 1]
F2_KEY = [0, 2]
F3_KEY = [0, 3]

# Colors
BLUE = rgb_to_hsv(0, 100, 255)
RED = rgb_to_hsv(255, 0, 0)
ORANGE = rgb_to_hsv(255, 69, 0)

def main():
    keyboard = RPiKeyboardConfig()

    try:
        current_preset = keyboard.get_current_preset_index()
        keyboard.set_led_direct_effect()

        # Set all three keys
        keyboard.set_led_by_matrix(matrix=F1_KEY, colour=BLUE)
        keyboard.set_led_by_matrix(matrix=F2_KEY, colour=RED)
        keyboard.set_led_by_matrix(matrix=F3_KEY, colour=ORANGE)
        keyboard.send_leds()

        print("F1=Blue, F2=Red, F3=Orange")
        print("Press Ctrl+C to exit...")

        # Keep running until interrupted
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        keyboard.rgb_clear()
        keyboard.send_leds()
        keyboard.set_current_preset_index(current_preset, save_index=False)
        keyboard.close()

if __name__ == "__main__":
    main()
