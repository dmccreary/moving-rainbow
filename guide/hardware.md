Moving Rainbow Hardware
==============

Arduino Moving Rainbow Kits

![Arduino IDE to LED Strip](guide/images/arduino-ide.png/)

The Moving Rainbow Kit is based on a strip of 12 "addressable" Red, Green and Blue (RGB) Light Emitting Diodes (LEDs).  We only need a single data signal (and power and ground) to connect the entire strip.


Green, red and blue LEDs in a segment of the strip
on the tape.  You can cut the tape between any LEDs.

We will use a software library provided by Adafruit called the "NeoPixel" library to turn lights on and off.  Our LED strip has 12 pixels.  However we start numbering at "0" to show how computer science people are usually off-by-one digit when they access memory locations!

![Pixel Numbering](guide/images/pixel-numbering.png/)
The first pixel has an address of "0", the second an address called "1" etc.
