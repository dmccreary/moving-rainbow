# Arduino Blink
=====
Here is one of simplest programs.  It is our version of "Hello World!.  This program will
initialize the LED strip and then turn the first pixel on and off.
Note that the first pixel must be addressed with the index number "0".  So this is the first
parameter of the setPixelColor method.

```c
#include <Adafruit_NeoPixel.h>
#define NUMBER_PIEXEL 12
#define LEDPIN    12

// Our version of "Hello World!".  Blink the first pixel (0) on and off every second

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXEL, LEDPIN, NEO_GRB + NEO_KHZ800);
 
void setup() {
  strip.begin();
}
 
void loop() {
  strip.setPixelColor(0, 255, 0, 0); // set pixel 0 to be bright red
  strip.show(); // send data to the strip
  delay(1000); // wait one second
  strip.setPixelColor(0, 0, 0, 0); // set pixel 0 to be off
  strip.show(); // send data to the strip
  delay(1000); // wait one second
}
```