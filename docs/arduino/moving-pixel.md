# Moving Pixel

This example program turn on a single pixel for 1/10th of a second and then turn it off.  It will repeat this pattern for each of the pixels in the LED strip.

To do this we will begin with using a for loop.  Here is the ovreall structure of the for loop:

```
  for (int i=0; i < NUMBER_PIEXELS; i++) {
  }
```

This loop has three parts within the parenthesis.

1. The initialization of the loop (int i=0)
2. The test for exiting the loop (i<NUMBER_PIEXELS)
3. The function that should be run at the end of each loop (i++) which increments the counter by 1.

```
#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin(); // initialize the strip
}

void loop() {
  for (int i=0; i<NUMBER_PIEXELS; i++) {
    strip.setPixelColor(i, 255, 0, 0); // turn the "i"th pixel on
    strip.show();
    delay(100); // wait 1/10th of a second
    strip.setPixelColor(i, 0, 0, 0); // // turn the "i"th pixel off
  }
}
```