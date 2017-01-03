# The Wipe Function

In this section we will learn how put a logical grouping of code together in a bundle and give it a name.
We call these functions.  Just like we have a setup() and loop() function that all Arduino programs have,
we will next learn to write our own functions.

Creating functions is one of the greatest features of programming.  Once they are written we
can reuse them over and over.  They keep our programs smaller and easier to read.

You might wonder why setup and loop have those parens after them.  That is the place that
you can put inputs to a function.  However neither setup() or loop() have inputs.

Our first function will be called wipe.  It will wipe our LED strip with a new color.  It will take two input parameters - things that control what happens inside
the function.  The first parameter will be the color expressed as a hex number.  The second will
be the amount of delay (in milliseconds).

Here is what the function will look like:

colorWipe(uint32_t color, uint8_t wait) {
   // our code here...
};

This says that the colorWipe function has two inputs:
1. The first parameter (color), is an unsigned 32-bit integer
2. The second input is wait, which is an unsigned 8 bit integer.

It is somewhat complicate to write hex numbers.  So to make this easy we will use a function that takes
three integers (red, green and blue) and converts them to a single hex number.  This is called the strip.Color() function.

Here is the full program that will turn our LED strip, red, then green, then blue.
```
#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();
}

void loop() {
  colorWipe(strip.Color(255, 0, 0), 150); // Red
  colorWipe(strip.Color(0, 255, 0), 150); // Green
  colorWipe(strip.Color(0, 0, 255), 150); // Blue
}

void colorWipe(uint32_t color, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, color);
      strip.show();
      delay(wait);
  }
}
```

## More to explore
What happens if you change the second parameter from 150 milliseconds to 50 milliseconds?  What about 5 milliseconds?  Can you still see the motion when the delay is very small?