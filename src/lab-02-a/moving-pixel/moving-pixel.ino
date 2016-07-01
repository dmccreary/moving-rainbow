#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin(); // initialize all the variables
}

void loop() {
  for (int i=0; i<strip.numPixels(); i++) {
    strip.setPixelColor(i, 255, 165, 0); // set pixel i to be yellow
    strip.show();
    delay(100);
    strip.setPixelColor(i, 0, 0, 0); // turn pixel i off
    strip.show();
    delay(100);
  }
}

