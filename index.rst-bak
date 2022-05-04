.. rtd-test documentation master file, created by
   sphinx-quickstart on Sun Sep 30 18:39:18 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
.. This is a comment. It requires two periods at the beginning of a line
.. See the Sphix Cheat Sheet for examples here http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html#restructured-text-rest-and-sphinx-cheatsheet

Welcome to the Moving Rainbow documentation!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

    About Moving Rainbow
    Getting Started
    Programming
    
Learing to program using LED strips version 0.1
###############################################

About Moving Rainbow
====================
Moving Rainbow is a way to learn the basics of programming using LED strips.  We use low-cost components so
you can build an entire costume with 100s of LEDs for under $20

Getting Started
***************

Addressible LED Strips
======================
Addressible LED strips are easy to connect to your project since they only need three wires (Ground, +5V and data).
LED strip can be purchased on sites like ebay.com for under $5/meter of 60 RGB LEDs.

`Moving Rainbow Github Home<https://github.com/dmccreary/moving-rainbow>`_ Use this site to get sample source code and submit your samples via pull requests.
`CoderDojo <http://coderdojo.org/>`_
`CoderDojo Twin Cities <http://coderdojotc.org/>`_
`CodeSavvy <http://codesavvy.org/>`_
Arduino Nanos
=============
Arduino Nanos are the lowest cost member of the Arduino family.  They are small and can be purchased for under $3.

.. image:: images/arduino-nano.png

Breadboards
===========
In our projects we use 1/2 sized breadboard with 400 tie points.

.. image:: images/breadboard.jpg

Mode Buttons
============
A "mode" is a way of having a single Arduino program run multiple patterns on the LED strip.  Each mode has a number associated with it
starting with 0 and continuing to the number of patterns we have in our program.

In this section we will add two mode buttons.  One button will make the pattern mode go to the next mode.  The other button will go to the previous mode.

Programming the LED strip
*************************

Each of our example programs will have at least three sections:
#. The preamble - this constains the library directives and initialization of static unchanging variables
#. The setup() function - this function is run once with the Arduion first starts up
#. The loop function - this function runs continually as long at the Arduino has power

.. code-block::


Sample Blink Program

.. code-block:: c++
    :linenos:

    #include <Adafruit_NeoPixel.h>
    const int LED_STRIP_PIN = 12; // Connect the Data pin of the LED strip here
    const int NUMBER_PIXELS = 60;
    Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LED_STRIP_PIN, NEO_GRB + NEO_KHZ800);
    
    void setup() {
        strip.begin();
    }
    
    void loop() {
        strip.setPixelColor(0, 255, 0, 0);
        strip.show();
        delay(1000);
        strip.setPixelColor(0, 0, 0, 0);
        delay(1000);
    }

Moving Rainbow Pattern
======================

Adding Modes
============

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
