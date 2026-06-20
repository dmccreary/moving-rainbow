# Programming the Pi 500 Keyboard with Python

## Setting Colors From a Python Script

Although the built-in effects are nice, they are also limited.
If you want to do something simple like turn a function key purple when
you have a new email message, you will need to use Python to program
the keys.

### Environment Setup

Python has about 50,000 libraries and each library can have hundreds of versions
and depend on specific version of other libraries.  To keep your
projects independent, we will use our Python best practice and
create a Python virtual environment using the conda tool.

https://github.com/raspberrypi/rpi-keyboard-config

```sh
conda create -n pi-keyboard python=3.11
conda deactivate
conda activate pi-keyboard
# we must install directly from the GitHub library
pip install git+https://github.com/raspberrypi/rpi-keyboard-config.git
```

```
$ pip install git+https://github.com/raspberrypi/rpi-keyboard-config.git
```

```
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting git+https://github.com/raspberrypi/rpi-keyboard-config.git
  Cloning https://github.com/raspberrypi/rpi-keyboard-config.git to /tmp/pip-req-build-6y43xh6p
  Running command git clone --filter=blob:none --quiet https://github.com/raspberrypi/rpi-keyboard-config.git /tmp/pip-req-build-6y43xh6p
  Resolved https://github.com/raspberrypi/rpi-keyboard-config.git to commit 771a82d63ae500dd1abd19467660e88f6691e609
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: rpi-keyboard-config
  Building wheel for rpi-keyboard-config (pyproject.toml) ... done
  Created wheel for rpi-keyboard-config: filename=rpi_keyboard_config-1.0-py3-none-any.whl size=39284 sha256=963ea6dbcfff58cf33335731caf2dd90a7d9cdf7a90dc4d888ee225a2ff8b09b
  Stored in directory: /tmp/pip-ephem-wheel-cache-bctxfx90/wheels/1c/10/a9/843f799873ad42ee496ad354758ad6a7b893800850cdde8b3e
Successfully built rpi-keyboard-config
Installing collected packages: rpi-keyboard-config
Successfully installed rpi-keyboard-config-1.0
```


Let's now move on to doing what we just looked at, but through Python scripts. Why would we want to do this though? What's wrong with the terminal commands method? Well, the biggest drawback is that it takes about a second to update a key color through the terminal - and we can only update one key color at a time with a command. With 84 keys on our board, that means to randomly assign a color to each key, it would take 84 seconds!

With the Python script method, we can update all the keys at once, and we can do so many times a second! On top of that, it's Python! We can make animations, add integrations, and make interactive layouts!

## Using Thonny



If you haven't done so already, go ahead and download the zip file containing all the Python scripts, and unzip it to a convenient location.

Go ahead and open up `simple_colour.py`. This script is a stripped-back demo of how colors can be controlled. First, it imports the rpi-keyboard-config library, then initializes the keyboard, and sets the LED control mode (telling the keyboard we are about to start sending it RGB commands). These are the important first steps of any script controlling the RGB.

```python
from RPiKeyboardConfig import RPiKeyboardConfig
import time

# Initialize the keyboard
keyboard = RPiKeyboardConfig()

# Set LED direct control mode
keyboard.set_led_direct_effect()
```

Then in a while true loop, we start by setting the color of the W key. Here we set the W key to purple using HSV, and with the same row and column system as the terminal method.

```python
while True:
    # Set LED by matrix position (HSV format: hue, saturation, value)
    keyboard.set_led_by_matrix(matrix=[2, 3], colour=(180, 255, 255))  # Purple
```

But this does not actually set the color of the key yet, it instead queues it up. You can use this command to queue up as many key colors as you want, and could queue up a color change on every single key. To actually push these queued up key colors and update the colors on the board, we use the `send_leds()` command.

```python
while True:
    # Set LED by matrix position (HSV format: hue, saturation, value)
    keyboard.set_led_by_matrix(matrix=[2, 3], colour=(180, 255, 255))  # Purple
    keyboard.send_leds()
```

Then after a short delay, we repeat the same process but this time with orange. The end result of this code is that it will flash the W key orange and purple.

```python
    # Set individual LED by index
    keyboard.set_led_by_idx(idx=33, colour=(20, 255, 255))      # Orange
    # Send LED updates to keyboard (required after setting colors)
    keyboard.send_leds()
    time.sleep(0.5)
```

There is one slight difference in this line. Here we are setting the W key through its ID rather than with rows and columns. This ID system is just another way of representing the keys. Start on the top row of your keyboard and count the keys from left to right (but do not count the power button). Once you reach the right side of the keyboard, move down a row and continue counting from left to right. If you do this once more, you should land on W and have counted to 33 - so W has an ID of 33.

There is one final helpful command being used in this script as well:

```python
    print(keyboard.get_leds())
```

The command will return the current color of every single LED on the keyboard. This is an incredibly helpful tool if you are doing anything animation-related, as you can get the current state of the board and animate from that point.

The lines in this demo script are the basic building blocks that you can use to go out and make nearly any custom effects! For example, if you open up and run `game_of_life.py`, you will have a game of life simulation run on your keyboard in a random color. This script uses the same fundamental building blocks as the simple demo; it just has extra code deciding which LEDs to light up.

Another example is `fire.py`. This is a very basic fire simulation that spawns embers and simulates them rising up and changing color. Again, it uses the same building blocks, and most of the code is dedicated to calculating which keys to light up and what color.

Now, creating animations like this is a lot of work and can sometimes require a fair amount of math. A great option might be to try and use an LLM like ChatGPT or Claude. If you copy and paste to them any of these demo scripts, they will likely be able to help you generate code for other custom effects.

For example, we were able to take this fire demo script and get it to add something called interpolation. If you run `fire_interpolated.py`, you will see that this makes animations far smoother, and if you are going to the effort of asking an LLM to help you write code, it is probably worthwhile asking them to add interpolation as well.

At this point, we were wondering how much of a toll this is having on our Pi, and how fast can we update our RGB? To test this, we wrote `speed_test.py`, which flashes every key a random color as fast as possible.

Running this, we found that the keyboard was able to update at over 30 fps! This is substantially faster than the roughly 1 key a second through the terminal method.

We also opened up a resource manager with the following command:

```sh
htop
```

While running this code, we found that it used about 5% to 10% of the Pi's CPU - not a huge amount, but not a negligible amount. This usage will of course be more or less depending on how complex your effect is and how fast you are updating it.

## A Simple Notification System

Much of the things we did in the terminal can also be done through the library - including setting a preset. In the project folder you will find `flash_demo.py`. This short script creates a small "flash" effect on the Pi 500+ keyboard that triggers at random intervals — showing how you can temporarily override your normal RGB preset, display an animation, and then bring it straight back. Let's break it down step by step.

We start by importing the required packages and setting up our keyboard object:

```python
import random
import time
from RPiKeyboardConfig import RPiKeyboardConfig
keyboard = RPiKeyboardConfig()
```

Here, `random` and `time` are standard Python libraries, and `RPiKeyboardConfig` is the official library that talks directly to the keyboard's lighting system. The final line initializes that library so we can start sending it commands.

Now we jump into our main loop:

```python
while True:
    # Generate a random number between 1 and 5
    random_number = random.randint(1, 5)
    print(f"Random number: {random_number}")
```

This loop keeps the script running continuously. Each pass it rolls a new random number between 1 and 5. This is how we decide when to do our "flash" effect — only when the number comes up 3.

Inside that condition, the magic happens:

```python
    if random_number == 3:
        # 1) Save the preset slot index
        current_idx = keyboard.get_current_preset_index()
        # 2) Switch to direct LED mode
        keyboard.set_led_direct_effect()
```

The first line remembers which preset you're currently using so it can be restored later. Then we switch the keyboard to direct LED mode, which basically gives us raw control over every LED on the board.

Next we fill the keyboard with random colors:

```python
        # 3) Fill with random colors
        all_leds = keyboard.get_leds()
        for led in all_leds:
            h = random.randint(0, 255)
            s = 255
            v = 255
            keyboard.set_led_by_idx(idx=led.idx, colour=(h, s, v))
        keyboard.send_leds()
```

We grab a list of all LEDs on the board, generate random color values for each (using full saturation and brightness), then send those colors to the keyboard. This is the "flash" moment.

After holding that flash for a second, we clear everything and bring back the normal preset:

```python
        # 4) Hold the flash
        time.sleep(1)
        # 5) Clear LEDs
        keyboard.rgb_clear()
        keyboard.send_leds()
        # 6) Restore preset
        if current_idx is not None:
            keyboard.set_current_preset_index(current_idx, save_index=False)
            print(f"Restored preset index {current_idx}")
```

This brief pause keeps the flash visible, then the script wipes the LEDs and reloads your saved preset so it looks exactly how it did before.

Finally, we wait a second before running the next loop.

```python
    # Wait 1 second before next iteration
    time.sleep(1)
```

Now, this might seem like a bit of a strange thing to do, but what we've actually built here is a simple notification or heads-up system. You could have your favorite lighting preset running, and then - say the doorbell rings - a Python integration could flash your keyboard to alert you. Or maybe you connect it to Home Assistant to display information on your desk; it's almost like having a low-resolution screen built into your keyboard. You could even set up built-in timers, like a Pomodoro tracker or system reminders. There are countless creative ways to use this approach, and by reading and loading presets, you can make all sorts of interactive lighting effects that suit your setup.

## Creating Interactive Effects

We can pre-program fancy LED colors and animations, but we are using Python here - we can do more complex things like reacting to keyboard inputs.

The keyboard library we have been using does natively support detecting key presses, but it also includes a security feature that requires you to press enter and escape to unlock the keyboard before it can detect them - this must be done every time the Pi is restarted.

This is not a major issue, but we are looking at having these Python scripts automatically start on boot up, and this extra manual step is a slight hassle. As a result, we will be using Pynput, which does the same task. You can install it with the following command:

```sh
pip install pynput --break-system-packages
```

In the script `snake.py`, you will find (as the name suggests) a game of snake that uses pynput for controls. Follow the instructions in the shell of Thonny to get going with it!

Let's put everything together and make something really cool - a sort of screensaver for the keyboard. Go ahead and open up the `screensaver.py` script, and you'll see exactly what's going on.

There's quite a bit happening under the hood, but in simple terms, the script watches for keyboard activity, and if it doesn't register any input for five seconds, it springs into action. It saves the current preset you're using, gradually fades out the keyboard's brightness (using the same global brightness command we used earlier in the terminal), and then starts displaying a soft "firefly" animation. As soon as you press a key again, it restores your original preset and brightness — a neat little screensaver, but for your keyboard.

## Automatically Running Scripts on Boot

We have this all running out of Thonny just fine, but this is not very practical in day-to-day use. There is a way to make this Python script run automatically on launch so it just does its thing in the background. First of all, we need to have the script in a readily available place, or somewhere we know the path to. If you want to follow along with the exact locations in these commands, copy your Python script to `/home/pi` (the folder that opens by default when you open the folder browser).

Once it is in there, we will need to use chmod to make it executable with:

```sh
chmod +x /home/pi/fire.py
```

Our script is called `fire.py`, so you should change this to whatever your script is called. Then, open a new terminal window and edit the crontab file with:

```sh
crontab -e
```

The first time you do this, you may need to select an editor to use. Enter in 1 to use the nano editor. Once you are in the file, use the arrow keys to navigate to the bottom of the file, and in a new line, enter the following:

```sh
@reboot sleep 10 && /usr/bin/python3 /home/pi/fire.py &
```

You will likely need to alter this line. The user name of our device is "pi", so we have `/home/pi/fire.py`, but you will need to replace pi with whatever your username is. Again, our script is called `fire.py`, so you also need to change it to what you have named yours.

Once you have entered this line correctly, hit `Ctrl + X`, then `Y` and then `Enter` to save it. The next time you reboot your Pi, this should automatically start!

