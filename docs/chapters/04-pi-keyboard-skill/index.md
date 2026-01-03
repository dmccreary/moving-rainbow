# Generating Pi Keyboard Python Programs with Skills

In this chapter we will cover the steps used
th generate python programs that manipulate the
Raspberry Pi 500 keyboard LEDs using Skills.  We assume that
you have already installed the Python library from the
previous chapter.  If not, you will need to use
the following command:

```sh
pip install git+https://github.com/raspberrypi/rpi-keyboard-config.git
```


## Installing the Skill

This skill can be used to generate both shell scripts and Python programs that
manipulate your keyboard LEDs for both backlighting and for keystroke-based
patterns.  The skill is packaged in a standard skill format with
a directory, a main SKILL.md file and the appropriate templates and script
files.  You can view the skills on our GitHub repo [here](https://github.com/dmccreary/moving-rainbow/tree/master/skills/pi-keys-generator).

We provide a handy UNIX shell script that will create a symbolic link
for you that will install the skills so that Claude Code can use them.

After you run the git clone command, you can just run the following command:

```sh
$MOVING_RAINBOW_HOME/scripts/install-skills.sh
```

Here  `$MOVING_RAINBOW_HOME` is where you checked out the repository.

Now a very short single-line prompt will create an entire
Python program that you can run in a command line or
open is the [Thonny](../../glossary.md#thonny) editor.

!!! prompt
    Use the pi-key-generator skill to create a new python program that will blink the f1 key red on and off with a delay of .5 second 

The prompt above will generate the following code:

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

You can run the command from our source code here:

```sh
python3 $MOVING_RAINBOW_HOME/src/pi-500-keyboard/blink-f1-red.py
```

Note that this script does extensive "cleanup" to make sure
that when the program stops, all the blinking will be cleaned
up and the state of the keyboard will be restored to how
it was before the program was executed.