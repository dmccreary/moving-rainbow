# List of Moving Rainbow Projects

## Getting Started Labs
The purpose of these labs is to use the minimal hardware to get students started programming LED strips.  Once they have mastered the basic of loops and conditionals we next introduce input sensors.

** LED Blink ** - this is always the first project we start our students with.  It is the simplist project that will demonstrate the round-trip process of writing, uploading and running a small Arduino project.  You can do this with the built-in LED on most Arduinos.  You will need a laptop, a USB cable and a low-cost Arduino Nano.

** LED Blink with Breadboard **  - this is the second lab.  It requires an additional breadboard, a single LED a resistor and some wires.  There are other variations of this lab that use multiple LEDs that move in a pattern.

** RGB LED **  - this third lab requires students to control a red, green and blue LED.  By mixing the colors they can make any color in the rainbow. 

** LED Strip **  - this is the forth lab and the one that opens many doors.  It will require you to purchase learn the parts in the lab above and an LED strip.  We will also learn how to download the Adafruit Neopixel library.  You can use an LED strip of anywhere from 10 to 60 pixels.  We will make a single red LED move down the LED strip using a for loop.

** LED Strip Multiple Colors **  - this lab uses the same LED strip but teaching students how to vary the color of each LED.

** LED Strip Patterns ** - in this lab we will use conditional statements (if/then) to make specific patterns such as alternating colors

# Sensor Input Labs
These labs use one or more input sensors to allow studnets to change what is displayed on the LED strip.

## Button Mode Labs
These labs introduce two input buttons that will allow the user to change the display mode of an LED strip.

** LED Strip Modes ** Here we add two buttons to our breadboard.  By using the built-in pull-up features we don't even need resistors.  We introduce the concept of an interrupt.

** LED Strip Modes with Debounce ** Now we introduce the concept of a debounce process so that we get a clean mode change when a button is pressed.

## LED Strip Potentiometers
These project requrie one to three potentiometers. We often mount them in a clear box so students can see the circuits and LED strip while they change the potentiomenter.

** LED Strip Brightness *** This project changes the brightness of all the pixels on an LED strip

** RGB Potentionter Lab *** This project uses three potentiometers to change the red, green and blue values of an LED strip.  All the LEDs respond together.  We use this box to help younger students learn about color mixing.

## Named Projects

** Simon ** This is the classic "Simon" game that displays a pattern of Red, green, blue yellow flashes and the student must repeat them back using four corrisponding buttons.  The patterns get harder each time.

** Joystick ** This project uses a Joystick to change the color or pattern of an LED array

** Roterery Encoder ** This project uses a rotery encoder "dial" to change what LED is displayed.  It can be combined with buttons to build a selector menu system.

# Advanced Labs
These labs also use a $18 OLED to display the state of the Arduino.  They are useful for teaching the concept of modes, internal state management and menu systems.  They should not be used by beginners because they are more expensive and reuqire more wiring.

** OLED Display ** We add an OLED display to show the internal state of our project.  We use mode buttons and a rotery encoder to change the state value.


