#!/usr/bin/env python3
"""
Blink the F1 key red on and off with a 0.5 second delay.
"""
from RPiKeyboardConfig import RPiKeyboardConfig
import time

# F1 key matrix position
F1_KEY = [0, 1]

# Red color in HSV (hue=0, saturation=255, value=255)
RED = (0, 255, 255)
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

        print("Blinking F1 key red. Press Ctrl+C to stop.")

        while True:
            # Turn F1 red
            keyboard.set_led_by_matrix(matrix=F1_KEY, colour=RED)
            keyboard.send_leds()
            time.sleep(DELAY)

            # Turn F1 off
            keyboard.set_led_by_matrix(matrix=F1_KEY, colour=OFF)
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