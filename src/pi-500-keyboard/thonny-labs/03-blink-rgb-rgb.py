#!/usr/bin/env python3
"""
Blink the F1, F2, and F3 keys in red, green, and blue sequence.
"""
from RPiKeyboardConfig import RPiKeyboardConfig
import colorsys
import time

def rgb_to_hsv(r, g, b):
    """Convert RGB (0-255) to HSV (0-255 scale for all components)."""
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    return (int(h * 255), int(s * 255), int(v * 255))

# F1 key matrix position
F1_KEY = [0, 1]
F2_KEY = [0, 2]
F3_KEY = [0, 3]

# Colors in RGB format (red, green, blue) - converted to HSV for the library
RED = rgb_to_hsv(255, 0, 0)
GREEN = rgb_to_hsv(0, 255, 0)
BLUE = rgb_to_hsv(0, 0, 255)
OFF = (0, 0, 0)

# Blink delay in seconds
DELAY = 0.5

def main():
    keyboard = RPiKeyboardConfig()

    try:
        # Save current preset to restore later
        current_preset = keyboard.get_current_preset_index()

        # Enable direct LED control
        keyboard.set_led_direct_effect()

        print("Blinking F1-F3 keys RGB. Press Ctrl+C to stop.")

        while True:
            # Turn F1 red
            keyboard.set_led_by_matrix(matrix=F1_KEY, colour=RED)
            keyboard.send_leds()
            time.sleep(DELAY)

            # Turn F1 off
            keyboard.set_led_by_matrix(matrix=F1_KEY, colour=OFF)
            keyboard.send_leds()
            time.sleep(DELAY)

            # Turn F2 green
            keyboard.set_led_by_matrix(matrix=F2_KEY, colour=GREEN)
            keyboard.send_leds()
            time.sleep(DELAY)

            # Turn F2 off
            keyboard.set_led_by_matrix(matrix=F2_KEY, colour=OFF)
            keyboard.send_leds()
            time.sleep(DELAY)

            # Turn F3 blue
            keyboard.set_led_by_matrix(matrix=F3_KEY, colour=BLUE)
            keyboard.send_leds()
            time.sleep(DELAY)

            # Turn F3 off
            keyboard.set_led_by_matrix(matrix=F3_KEY, colour=OFF)
            keyboard.send_leds()
            time.sleep(DELAY)

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
