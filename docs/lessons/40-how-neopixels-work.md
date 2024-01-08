# How NeoPixels Work

NeoPixels, such as the WS2812B, are a type of addressable LED commonly used in various lighting projects. Here's an explanation of how they function:

## Integrated Control Circuit
Each NeoPixel contains a control circuit and an RGB LED. This design makes each LED independently addressable within a strip.

## Data Transmission
NeoPixels are controlled by a digital data signal sent from a microcontroller. This signal is a sequence of binary data.

## Signal Processing
The data signal is sent through a single data line to the strip. Each LED reads its part of the data (usually 24 bits: 8 bits each for Red, Green, and Blue) and uses this information to set its color.

## Color Control
The color of each LED is determined by the 24 bits of data it receives. These bits represent the intensity levels for each of the red, green, and blue components of the LED. The combination of these intensities produces the final color.

## Data Propagation
After an LED reads its data, it removes (or 'strips') this data from the stream and passes the remaining data to the next LED. The next LED then reads its respective data, and this process continues down the strip.

## Sequential Addressing
The first LED in the strip reads the first set of data, the second LED reads the next set, and so on. This sequential processing allows for individual control of each LED in the strip.

## Refresh Rate
The entire process of data reading and color setting happens very quickly, allowing dynamic effects like color changes to appear smooth.

## Electrical Connection
Only three connections are required for a NeoPixel strip: power (5V), ground, and data input. This simplicity makes them popular for various lighting projects.

## Conclusion
NeoPixels offer a combination of simplicity in wiring and complexity in control, allowing for a wide range of creative lighting applications.

This document provides an overview of the basic operation of NeoPixels without delving into the specific technicalities of signal timing and electrical characteristics.
