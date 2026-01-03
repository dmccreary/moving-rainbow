# Generating Pi Keyboard Python Programs

In this chapter we will cover the steps used
th generate python programs that manipulate the
Raspberry Pi 500 keyboard LEDs.  We assume that
you have already installed the Python library from the
previous chapter.  If not, you will need to use
the following command:

```sh
pip install git+https://github.com/raspberrypi/rpi-keyboard-config.git
```


## Installing the Skill

```sh
$MOVING_RAINBOW_HOME/scripts/install-skills.sh
```

!!! prompt
    Use the pi-key-generator skill to create a new python program that will blink the f1 key red on and off with a delay of .5 second 

The skill will generate the following code:

```python
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
```

```sh
python3 $MOVING_RAINBOW_HOME/src/pi-500-keyboard/blink-f1-red.py
```