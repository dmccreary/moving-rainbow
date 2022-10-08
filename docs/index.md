
# Welcome to the MicroPython Moving Rainbow documentation!

![](img/moving-rainbow-logo.png)

Learning to program using LED strips version 2

''' Note!
    We are no longer accepting pull request for Arduino C code.  Due to the fact that we can get Raspberry Pi Pico processors for $4 that run Python we have moved
    all our Moving Rainbow code over to Python.

## About Moving Rainbow

Moving Rainbow is a way to learn the basics of programming using LED strips.  We use low-cost components so you can build an entire costume with 100s of LEDs for under $20

## Getting Started

## Addressable LED Strips
Addressable LED strips are easy to connect to your project since they only need three wires (Ground, +5V and data).
LED strip can be purchased on sites like ebay.com for under $5/meter of 60 RGB LEDs.

## References
[CoderDoj](<http://coderdojo.org)
[CoderDojo Twin Cities](http://coderdojotc.org)
[CodeSavvy](http://codesavvy.org)

## Raspberry Pi Pico

The Raspberry Pi Pico cost only $4 and runs Python.  All our labs use this processor.


## Breadboards

In our projects we use 1/2 sized breadboard with 400 tie points.

![](img/breadboard.jpg)

## Mode Buttons
A "mode" is a way of having a single Arduino program run multiple patterns on the LED strip.  Each mode has a number associated with it
starting with 0 and continuing to the number of patterns we have in our program.

In this section we will add two mode buttons.  One button will make the pattern mode go to the next mode.  The other button will go to the previous mode.

## Programming the LED strip


Each of our example programs will have at least three sections:

1. The preamble - this constains the library directives and initialization of static unchanging variables
2. The setup() function - this function is run once with the Arduion first starts up
3. The loop function - this function runs continually as long at the Arduino has power

Sample Blink Program

```python

```
