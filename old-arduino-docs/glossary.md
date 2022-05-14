# Glossary

## Arduino
A popular and set of hardware and software used for teaching physical computing.  Also the name of a company that popularized the devices and supports the standards.  Note that many of the low-cost devices we use in these kits are technically not true Arduino devices.  They are classified as Arduino clones.  Many of the clones are 1/10 the cost of the original devices.
* [Wikipedia Definition](http://en.wikipedia.org/wiki/Arduino)

## Arduino Integrated Development Environment (IDE)
A software program to edit, compile, debug and download Arduino programs.  It runs on both Windows and Mac.
* [Download Page](http://arduino.cc/en/Main/Software)

## Arduino Nano
The original Arduino devices have a defect in that they are not compatible with standardized solderless breadboards.  We use a lower-cost version that can plug in directly to a solderless breadboard.
* [Hardware Web Page](http://arduino.cc/en/Main/ArduinoBoardNano)
* [Guide to the Arduino Nano](http://arduino.cc/en/Guide/ArduinoNano)

## CH340
The name of the low-cost USB interface chip that is use instead of the more expensive FTDI USB interface chip.
Although the chip is low cost, the driver is not usually included with the Arduino IDE and 
the driver is not digitally
sigined for the Mac.
See the [CH340 drivers here](http://www.wch.cn/download/CH341SER_ZIP.html)
See [Arduino Nano CH340 Instructable](http://www.instructables.com/id/Arduino-Nano-CH340/) for a good description of how to make the CH340 work on the Mac.

## Light Emitting Diode (LED)
A solid-state device that emits light when a voltage is applied.  LEDs come in various colors such as red, green and blue.
* [Wikipedia Definition](http://en.wikipedia.org/wiki/Light-emitting_diode)

## Moving Rainbow Kits
These are kits that combine three important aspects of learning: Color, Motion and Social Constructionism.  
Students are interested in sensing and changing the world around them.  
The use of low-cost LEDs and DC-motors can make these kits not only fun, 
but inexpensive enough that students can purchase them and take them home to share with friends.  A typical
cost is around $15USD.

## Light Emitting Diode (LED)
A device that converts DC current into light.  In our project each Pixel element has a red, green and blue LED in it.

## Red-Green-Blue LED (RGB LED)
A single device that has three colors of LEDs.  One for red, one for blue and one for green.  By combining various intensities of each of these three colors we can create many additional colors.

## NeoPixel
This is the name coined by Adafruit for an individually addressable LED.  
Adafruit also provides a high-quality open source library on github to drive these LEDs.
* [NeoPixel on Adafruit Web Site](http://www.adafruit.com/category/168)

## NeoPixel Library
The Arduino library used in these guides.  
We picked this library because of its popularity and the many on-line
tutorials about how to use them.
* [NeoPixel Library Guide on the Adafruit Web Site]https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library
* [NeoPixel Library on GitHub](https://github.com/adafruit/Adafruit_NeoPixel)

## Physical Computing
Hardware and software that can sense and respond to changes in the world around us.
* [Wikipedia Definition](http://en.wikipedia.org/wiki/Physical_computing)

## Social Constructionism
Getting students to build things together in teams.  This style of teaching has many benefits over the standard lecture-style learning.
* [Wikipedia Definition](http://en.wikipedia.org/wiki/Social_constructionism)
* [Berkeley Web Site on Social Constructionism in Education](http://gsi.berkeley.edu/gsi-guide-contents/learning-theory-research/social-constructivism/)

## WS2812B
A standard for addressable RGB LEDs
* [Data sheet from Adafruit](http://www.adafruit.com/datasheets/WS2812B.pdf)