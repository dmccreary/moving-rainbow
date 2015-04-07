# The Larson Scanner

The Larson Scanner is one of the most famous patterns in special effects.  It was named after Glen A. Larson
who used the pattern in the intelligent car in Knight Rider and as the eyes in Cylons in Battlestar Galactica.

Here is out it works.
1. We start the loop by drawing five intensities of light.  Dim at the ends and bright in the center.
2. We offset each of these by a position.
3. Each time we go through the loop we move the position up until we reach the end.  When we reach the end
of the strip we flip the direction (dir = -dir)

Here is some sample code to do the Larson Scanner.
```
#include <Adafruit_NeoPixel.h>
 
#define NUMBER_PIEXEL 12
#define LEDPIN    12
 
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXEL, LEDPIN, NEO_GRB + NEO_KHZ800);
 
void setup() {
  strip.begin();
}
 
int pos = 0, dir = 1; // Position, direction of "eye"
 
void loop() {
  int j;
 
  // Draw 5 pixels centered on pos.  setPixelColor() will clip any
  // pixels off the ends of the strip, we don't need to watch for that.
  strip.setPixelColor(pos - 2, 0x100000); // Dark red
  strip.setPixelColor(pos - 1, 0x800000); // Medium red
  strip.setPixelColor(pos    , 0xFF3000); // Center pixel is brightest
  strip.setPixelColor(pos + 1, 0x800000); // Medium red
  strip.setPixelColor(pos + 2, 0x100000); // Dark red
 
  strip.show();
  delay(50);
 
  // Rather than being sneaky and erasing just the tail pixel,
  // it's easier to erase it all and draw a new one next time.
  for(j=-2; j<= 2; j++) strip.setPixelColor(pos+j, 0);
 
  // Bounce off ends of strip
  pos += dir;
  if(pos < 0) {
    pos = 1;
    dir = -dir;
  } else if(pos >= strip.numPixels()) {
    pos = strip.numPixels() - 2;
    dir = -dir;
  }
}
```