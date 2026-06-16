# Programming the Raspberry Pi 500 Keyboard

!!! Note
    Much of these examples were taken from [How To Customize Your Pi 500+ RGB Keyboard | Custom Effects & Python Scripts](https://core-electronics.com.au/guides/how-to-customise-your-pi-500-plus-rgb-keyboard-python-scripts-and-custom-effects/) by Jaryd at Core Electronics in New Zealand. Updated 08 October 2025.

In this guide, we're going to be programming the LEDs on the Pi 500+ keyboard.  We will
start out just using some function keys to turn on different patterns and
we will learn about the seven preset patterns we can program.
Then we will run a few simple shell commands that change the LEDs and preset patterns. 
Lastly we will move to writing small Python scripts to create your own animations, reactive lighting, and even little games or notification systems. By the end, you'll have full control over every LED on your keyboard.  Programming all the keys on your computer will be
your new superpower!  Your friends will be impressed!

## Contents

- [What You Will Need](#what-you-will-need)
- [Installing the Shell Scripts](#installing-the-shell-scripts)
- [Installing the RGB Library](#installing-the-rgb-library)
- [Controlling RGB With Terminal Commands](#controlling-rgb-with-terminal-commands)
- [Binding Function Keys to Programs](#binding-function-keys-to-programs)

## What You Will Need

To follow along with this guide, you will need:

- Raspberry Pi 500+
- USB-C power supply (ideally a 5-watt power supply that supports external USB ports)
- Mouse
- Monitor
- Micro-HDMI to HDMI cable (note, this is a non-standard cable and you may need to special order it)

## Installing the Shell Scripts

All the source code for our samples can be downloaded directly from the
Moving Rainbow GitHub site [here](https://github.com/dmccreary/moving-rainbow/tree/master/src/pi-500-keyboard).

In the documentation below, we often give shell script path that includes the variable `$MOVING_RAINBOW_HOME`.  This refers to where you have checked out the Moving Rainbow
GitHub repository.  You can do this using the github `clone` command.

```sh
cd $HOME/projects
git clone https://github.com/dmccreary/moving-rainbow
set MOVING_RAINBOW_HOME="$HOME/projects/moving-rainbow"
```

Alternatively, you can also simply download the individual shell scripts from GitHub and put them in your local bin `~/.local/bin` if you don't want to download the entire repository.  After you install them
you might need to run the `chmod +x ~/.local/bin/*.sh` program to give the scripts execution permission.

## Installing the RGB Library

To get started, we need to update and upgrade our linux packages:

```sh
sudo apt update && sudo apt upgrade
```

To handle all of our RGB interactions, we are going to be using the official Raspberry Pi keyboard config library. If you are using Raspberry Pi OS `bookworm`, chances are this will come pre-installed. 

You can run the Linux Software Base program with the codename short option (CS) to see what version you are running.

```sh
lsb_release -cs
```

This tutorial was created on the `bookworm` release which came out in 2023 and which the Pi OS is based on.

You can now install the library (and know you have the updated library) with:

```sh
sudo apt install rpi-keyboard-config
```

Then very importantly, ensure your keyboard's firmware is up to date with:

```sh
sudo apt install rpi-keyboard-fw-update
sudo rpi-keyboard-fw-update
```

!!! Note
    The update command is a separate command from the `rpi-keyboard-config` command.
    You can't update the library with the config command.  You MUST use the separate `rpi-keyboard-fw-update` command.  This allows administrators to prevent
    unauthorized updates, which could be a security concern.

## Using the Function Key to Cycle Through the Seven Presets

<iframe width="560" height="415" src="https://www.youtube.com/embed/CY3thrGdL6I?si=Z0JaC9OIb8RPBsbD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

| Preset | Name                  | Description                                                                                                          |
|--------|-----------------------|----------------------------------------------------------------------------------------------------------------------|
| 0      | Off                   | The default preset that only lights the power key, the startup animation, and the Caps Lock indicator.               |
| 1      | Solid Color White    | Solid white backlight.                                                                                               |
| 2      | Solid Color          | Solid color backlight, which you can change using Fn + F3.                                                          |
| 3      | Gradient Left Right   | Fixed rainbow backlight.                                                                                             |
| 4      | Cycle Pinwheel        | Animated rainbow backlight, where the keys cycle through different colors in a rainbow pattern across the keyboard. |
| 5      | Typing Heatmap        | The more you press a key, the closer to red it gets and the more the keys around it light up.                        |
| 6      | Solid Reactive Simple | Reactive keyboard, where the keys light up when you press them. You can choose which color using Fn + F3.           |


## Controlling RGB With Terminal Commands

We are going to start with some basic terminal commands, and keep building up the complexity. It is worthwhile starting basic as most of the commands here will be important in the more advanced sections.

If you hit `FN + F4`, you will cycle through the seven preset colors stored on your keyboard. It's worth noting that by default, the Pi 500+ can hold 7 of these presets.

In the terminal, we can choose which preset we want with:

```sh
rpi-keyboard-config preset index 3
```

This will set the keyboard to preset 3, and we can choose any number from preset 0 to preset 6. This command is essentially the equivalent of pressing `FN + F4`, but just doing it through the terminal.

The default effects you see in these presets are nice, but there are plenty of other effects available to choose from!

A quick distinction here: effects are the RGB patterns/colors/layouts programmed into the keyboard, and presets are slots that can store these effects for convenient access.

Enter the following command to see a list of all the available effects to choose from:

```sh
rpi-keyboard-config list-effects
```

## Built-in Keyboard Effects

Below is a table of the built-in effects for the keyboard LEDs.  There is a video
below that will show these effects.

| ID | Effect Name | Keystroke Trigger | Description |
|----|-------------|-------------------|-------------|
| 0 | OFF | No | All keys turned off. |
| 1 | Direct | No | Direct LED control mode for custom programming via Python scripts. |
| 2 | Solid Color | No | All keys the same color. Use the hue parameter to set the color. |
| 3 | Alphas Mods | No | Letter keys and modifier keys display different colors. |
| 4 | Gradient Up Down | No | Keys on the same row have the same color, creating a vertical gradient. |
| 5 | Gradient Left Right | No | Keys on the same column have the same color, creating a horizontal gradient. |
| 6 | Breathing | No | The brightness of the entire keyboard pulses up and down over a five second interval. |
| 7 | Band Sat | No | A single saturation band moves left to right on a contrasting background color. |
| 8 | Band Val | No | A band of varying brightness moves horizontally across the keyboard. |
| 9 | Band Pinwheel Sat | No | A rotating pinwheel pattern with saturation-based band effect. |
| 10 | Band Pinwheel Val | No | A rotating pinwheel pattern with brightness-based band effect. |
| 11 | Band Spiral Sat | No | A spiral pattern with saturation-based band effect emanating from center. |
| 12 | Band Spiral Val | No | A spiral pattern with brightness-based band effect emanating from center. |
| 13 | Cycle All | No | All keys simultaneously cycle through all hue values together. |
| 14 | Cycle Left Right | No | Rainbow colors cycle horizontally across the keyboard from left to right. |
| 15 | Cycle Up Down | No | Rainbow colors cycle vertically across the keyboard from top to bottom. |
| 16 | Rainbow Moving Chevron | No | Animated multicolor chevron pattern moves across the keyboard. |
| 17 | Cycle Out In | No | Colors cycle from the outer edges toward the center of the keyboard. |
| 18 | Cycle Out In Dual | No | Dual-sided colors cycling from both left and right edges toward center. |
| 19 | Cycle Pinwheel | No | Rainbow pinwheel effect rotating from the center of the keyboard. |
| 20 | Cycle Spiral | No | A spiral rainbow pattern emanates and rotates from the center outward. |
| 21 | Dual Beacon | No | A two-color lighthouse beacon pattern rotates over the keys. |
| 22 | Rainbow Beacon | No | A rainbow lighthouse beacon pattern rotates over the keys. |
| 23 | Rainbow Pinwheels | No | Multiple colored pinwheel patterns move from the center outward. |
| 24 | Raindrops | No | Random keys light up and fade like raindrops falling on the keyboard. |
| 25 | Jellybean Raindrops | No | Colorful random keys light up like multicolored jellybeans falling. |
| 26 | Hue Breathing | No | The entire keyboard's hue slowly shifts while pulsing in brightness. |
| 27 | Hue Pendulum | No | The hue swings back and forth across the color spectrum like a pendulum. |
| 28 | Hue Wave | No | A wave of changing hues moves horizontally across the keyboard. |
| 29 | Typing Heatmap | Yes | Keys change color based on how frequently they are pressed; more presses means redder. |
| 30 | Digital Rain | No | Matrix-style falling green characters cascade down the keyboard. |
| 31 | Solid Reactive Simple | Yes | Keys light up briefly when pressed, then fade out. |
| 32 | Solid Reactive | Yes | Keys light up when pressed with a smooth fade effect. |
| 33 | Solid Reactive Wide | Yes | Pressed keys and nearby keys light up with a wider area glow effect. |
| 34 | Solid Reactive Multiwide | Yes | Multiple wide glows appear simultaneously from multiple key presses. |
| 35 | Solid Reactive Cross | Yes | A cross/plus pattern lights up centered on each pressed key. |
| 36 | Solid Reactive Multicross | Yes | Multiple cross patterns appear from simultaneous key presses. |
| 37 | Solid Reactive Nexus | Yes | A nexus/star pattern radiates outward from each pressed key. |
| 38 | Solid Reactive Multinexus | Yes | Multiple nexus patterns radiate from simultaneous key presses. |
| 39 | Splash | Yes | A colorful splash of rainbow colors radiates outward from pressed keys. |
| 40 | Multisplash | Yes | Multiple rainbow splashes radiate from simultaneous key presses. |
| 41 | Solid Splash | Yes | A solid single-color splash radiates outward from pressed keys. |
| 42 | Solid Multisplash | Yes | Multiple solid-color splashes from simultaneous key presses. |
| 43 | Pixel Rain | No | Individual lit pixels fall down the keyboard like digital rain. |
| 44 | Pixel Fractal | No | Fractal-like pixel patterns spread and grow across the keyboard. |

Note that the third column is set to Yes if the effect is triggered by a keyboard stroke.
When the the third column is No, the effect only changes the keyboard backlight effect and
is not dependant on any key being pressed.

And you can view an effect with:

```sh
rpi-keyboard-config effect 25
```

The command line above views effect number 25, but you should play around and view some more, there are some pretty cool ones available! Some of our favorites are 25, 29, and 40.

Some presets also have inputs that can alter their behavior. You can set the speed, saturation and hue of the effects with the modified command:

```sh
rpi-keyboard-config effect 30 --speed 255 --sat 255 --hue 255
```

The commands will take a number between 0 and 255. You can set all the options like in the command above, or only set two, or one:

```sh
rpi-keyboard-config effect 30 --hue 255
rpi-keyboard-config effect 30 --speed 255 --hue 255
```

Note that there is no delay in the loop.  This shows that the `rpi-keyboard-config` takes about one second to work.

## Cycle Through All Effects

You can cycle through all the effects by running the cycle-effects.sh script. This script uses `figlet` to display ASCII art names for each effect. Install it first:

```sh
sudo apt install figlet
```

### Non-Keystroke Effects

These effects just change the keyboard backdrop color.  They are not triggered by a keystroke.

Then run script the demo with the "-n" option:

```sh
$MOVING_RAINBOW_HOME/src/pi-500-keyboard/cycle-effects.sh -n
```

This will cycle through all the NON-keystroke effects where the Keystroke Trigger in the above table is set to No.

<iframe width="560" height="450" src="https://www.youtube.com/embed/hjW20oUe9d0?si=XVZZMvpBovNXsx3k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Note that on the terminal, if the effect takes parameters, the parameter names are listed in the shell script output under the ASCII art.  So for example the `Solid Color` pattern
shows that the `speed` is 128 and the `sat` is 255 and the effect allows you to set the hue (not fixed) using an `hue` parameter.

Sample output:
```
========================================
Effect 24 of 44
========================================

____       _           _
|  _ \ __ _(_)_ __   __| |_ __ ___  _ __  ___ 
| |_) / _` | | '_ \ / _` | '__/ _ \| '_ \/ __|
|  _ < (_| | | | | | (_| | | | (_) | |_) \__ \
|_| \_\__,_|_|_| |_|\__,_|_|  \___/| .__/|___/
                                |_|        

----------------------------------------

Effect: Raindrops (ID 24)
Press Ctrl+C to exit early at any time.
```

### Keystroke Triggered Effects

The prior video only showed effect that changed the overall backlighting of the keyboard.  The
backlighting did not change as you type on the keyboard.  The next set of effects
are all triggered by a keystroke.

To run this script, use the "-k" (keystroke) option of the `cycle-effects.sh` shell script.

```sh
$MOVING_RAINBOW_HOME/src/pi-500-keyboard/cycle-effects.sh -k
```

<iframe width="560" height="415" src="https://www.youtube.com/embed/Xs5iFZHpCvs?si=oyTRflilRuLBkk2J" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Note that you can also change parameters of the keyboard stroke effects.

## Creating Shell Scripts to Demonstrate Each Effect Parameters

Many of the builtin effect also take parameters.  For example
the solid effect will take the hue of the color you want to use as a `--hue` parameter.

The following shell script will cycle through the hues for the solid color patten.
It will skip 9 out of the 10 colors so that the script will finish in about 25 seconds.

```sh
#!/bin/bash
# Cycle through all hues on the Pi 500+ keyboard
# Uses effect 2 (Solid Color) with varying hue values

for hue in $(seq 0 10 255); do
    rpi-keyboard-config effect 2 --hue $hue
done
```

## Customizing the Seven Presets

Being able to view these commands through the terminal is nice and all, but if you really want to start customizing your keyboard, you can assign an effect to your keyboard's preset slot:

```sh
rpi-keyboard-config preset set 2 25
```

In the command above, we are setting effect number 25 to preset slot 2. You should be able to now use the `FN+F4` keys to cycle through the preset slots and see your effect saved in slot 2!

If you ever want to see what effects are assigned to what slot, you can use the following command:

```sh
rpi-keyboard-config preset get
```

By default, preset slot 0 will be empty. This preset slot is the default that will be loaded when the Pi 500+ is powered on - if you assign your favorite effect to this slot, it will automatically be displayed every time you turn on your Pi.

If you press `FN+F5` and `FN+F6` on your keyboard, you can control the global brightness of your effect. This can also be done in the terminal with:



## Keyboard Configuration Shell Command Examples

The `rpi-keyboard-config` command has a `brightness` parameter can be set with any number between 0 and 255 where 0 is off and 255 is the maximum brightness.

```sh
rpi-keyboard-config brightness 255
```

First we run the clear command to clear all the current LED colors so we can start with a blank canvas:

```sh
rpi-keyboard-config leds clear
```

Let's use a basic command to set all the LEDs on our keyboard a specific color with:

```sh
rpi-keyboard-config leds set --colour "0,255,255"
```

Note that `colour` is not a typo.  This is the British spelling of the command.

The command above uses the HSV format to represent colors. If it is not your cup of tea, you can instead choose to use the RGB format with:

```sh
rpi-keyboard-config leds set --colour "rgb(255,0,0)"
```

Both of these commands achieve the same thing; they just use different ways of representing the color red. Also note that usually the hue value in HSVs range from 0 to 360, in this library it instead only takes a number from 0 to 255. So cyan (which is usually 180), will be scaled down to 128.

Now let's set individual LED colors! It may be wise to run the LEDs clear command to start with a blank canvas again. Then we can use the following command to set the W key to an aqua color with:

```sh
rpi-keyboard-config led set "2,3" --colour "rgb(0,255,255)"
```

This is very similar to the previous command, but this time we have a row and column being used to specify which key to light up.

You can generate a nice visualization of what key has what number row and column with the following command:

```sh
rpi-keyboard-config info --ascii
```

In the image on the right, we went through and assigned some colors with this command. If you have created a custom RGB layout with this and wish to save it, you can do so with the save command:

```sh
rpi-keyboard-config leds save
```

This will save your custom layout as effect 1. Even if you restart your Pi, your layout will still be saved to this effect, and you can also assign it to a keyboard preset slot as usual.

Unfortunately, only one custom layout can be saved at a time - you can only save to effect 1. We will look at how to create unlimited custom layouts with Python scripts later.

Wrapping up, if you ever want to reset all your effects and presets back to the defaults, you can use the following command:

```sh
rpi-keyboard-config reset-presets
```

And just for fun, you can play a game of Flappy Birds with:

```sh
rpi-keyboard-config game
```

## Binding Function Keys to Programs

The Raspberry Pi Desktop use the Wayfire configuration
file to bind a function key to a program.  In the
example below, we have configured the F9 function key to do a screen image
of a region and put it in the ~/screenshots/~ directory.

```ini
# User Wayfire configuration
# This supplements /etc/wayfire/defaults.ini

[command]
# F9: Screenshot selected area (interactive)
binding_screenshot_area = KEY_F9
command_screenshot_area = bash -c 'grim -g "$(slurp)" ~/screenshots/ss-$(date +%Y%m%d-%H%M%S).png'

# This is what the PrtScn screen should do!
# F8: Screenshot entire screen
binding_screenshot_full = KEY_F8
command_screenshot_full = grim ~/screenshot-$(date +%Y%m%d-%H%M%S).png

```

After you change this file you must run the following in the terminal

```sh
killall -SIGUSR1 wayfire
```

## Changing the Default Behavior of Keys

When the user logs in, a program run to initialize the key bindings.
This program reads a sequence of startup **run commands* in ~/~/.config/labwc/rc.xml

This file has a set of `keybind` elements that bind a key to an action.  The action can
be any shell script.  Here are some examples:

```xml
<!-- Print Screen: select area screenshot with timestamp and store the region in the home Screenshots directory -->
<keybind key="Print">
    <action name="Execute">
    <command>sh -c 'grim -g "$(slurp)" ~/Screenshots/ss-$(date +%Y%m%d-%H%M%S).png'</command>
    </action>
</keybind>
<!-- F8: full screenshot with timestamp -->
<keybind key="F8">
    <action name="Execute">
    <command>sh -c 'grim ~/Screenshots/ss-$(date +%Y%m%d-%H%M%S).png'</command>
    </action>
</keybind>
<!-- F9: select area screenshot with timestamp -->
<keybind key="F9">
    <action name="Execute">
    <command>sh -c 'grim -g "$(slurp)" ~/Screenshots/ss-$(date +%Y%m%d-%H%M%S).png'</command>
    </action>
</keybind>
```

```sh
killall -SIGHUP labwc
```

## References

1. [Raspberry Pi Documentation on the Keyboard Computers](https://www.raspberrypi.com/documentation/computers/keyboard-computers.html)
1. [Pi Docs Backlighting Section](https://www.raspberrypi.com/documentation/computers/keyboard-computers.html#backlighting)