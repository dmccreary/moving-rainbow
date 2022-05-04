# Color Wheel

Wouldn't it be nice if we could have each of our pixels change their color as though they were walking around
a color wheel?

Here is a program that does this.

The key is a function called Wheel, that is provided with our NeoPixel library.  The Wheel function is quite clever.
It uses a set of if/then else functions that splits the colors up into three ranges.  It does slightly different things if the input is:

1. less then 88
2. less then 170
3. over 170

```
#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int wait = 10; // how long we wait on each color (milliseconds)

void setup() {
  strip.begin();
}

void loop() {
  
    for (int color=0; color<255; color++) {
      for (int i=0; i<strip.numPixels(); i++) {
        strip.setPixelColor(i, Wheel(color));
       }
    strip.show();
    delay(wait);
  }
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
   return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else if(WheelPos < 170) {
    WheelPos -= 85;
   return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  } else {
   WheelPos -= 170;
   return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  }
}
```
## More to Explore
Look at the intensity of the colors.  You will find that although there are some darker colors, most of them tend to skew toward the white colors.  This is because on the average, there are at least two colors that are over half on.  We usually only get a deep color if two colors are almost off and the third one is on.  How can you change the program so that we get a more full spectrum of colors?