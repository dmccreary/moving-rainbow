#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin(); // initialize the strip
}

void loop() {
  for (int i=0; i<=11; i++) {
    strip.setPixelColor(i,   10, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+1, 200, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+2, 10, 0, 0); // turn the "i"th pixel on
    strip.show();
    delay(100); // wait 1/10th of a second
    strip.setPixelColor(i, 0, 0, 0);
    strip.setPixelColor(i+1, 0, 0, 0);
    strip.setPixelColor(i+2, 0, 0, 0);
  }
}

