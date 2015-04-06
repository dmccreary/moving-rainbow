#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin(); // initialize the strip
}

void loop() {
  for (int i=0; i<NUMBER_PIEXELS-4; i++) {
    strip.setPixelColor(i,    5, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+1,  50, 0, 0); // turn the i+1 pixel
    strip.setPixelColor(i+2, 2555, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+3,  50, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+4,  5, 0, 0); // turn the "i"th pixel on
    strip.show();
    delay(500); // wait 2/10th of a second
    strip.setPixelColor(i,   0, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+1, 0, 0, 0); // turn the i+1 pixel
    strip.setPixelColor(i+2, 0, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+3, 0, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+4, 0, 0, 0); // turn the "i"th pixel on
    strip.show();
  }
}

