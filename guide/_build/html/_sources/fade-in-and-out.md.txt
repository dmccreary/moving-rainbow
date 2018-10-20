# Fade In and Out


```
fadeInAndOut(uint32_t color, uint8_t wait) {

};
```

This says that the colorWipe function has two inputs:
1. The first parameter (color), is an unsigned 32-bit integer
2. The second input is wait, which is an unsigned 8 bit integer.

It is somewhat complicate to write hex numbers.  So to make this easy we will use a function that takes
three integers (red, green and blue) and converts them to a single hex number.  This is called the strip.Color() function.

Here is the full program that will turn our LED strip, red, then green, then blue.
```
// fade in and out

#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int waitTime = 10;

void setup() {
  strip.begin();
}

void loop() {
  fadeInAndOut(255, 0, 0, waitTime); // Red
  fadeInAndOut(0, 255, 0, waitTime); // Green
  fadeInAndOut(0, 0, 255, waitTime); // Blue
}

void fadeInAndOut(uint8_t red, uint8_t green, uint8_t blue, uint8_t wait) {
  
  for(uint8_t b=0; b <255; b++) {
     for(uint8_t i=0; i < strip.numPixels(); i++) {
        strip.setPixelColor(i, red*b/255, green*b/255, blue*b/255);
     }
     strip.show();
     delay(wait);
  };
  
  for(uint8_t b=255; b > 0; b--) {
     for(uint8_t i=0; i < strip.numPixels(); i++) {
        strip.setPixelColor(i, red*b/255, green*b/255, blue*b/255);
     }
     strip.show();
     delay(wait);
  };
};
```

## More to explore
What happens if you change the second parameter from 150 milliseconds to 50 milliseconds?  What about 5 milliseconds?  Can you still see the motion when the delay is very small?