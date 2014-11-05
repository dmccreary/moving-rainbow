#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int delayTime = 20;

void setup() {
  strip.begin(); // initialize the strip
}

void loop() {
  for (int i=0; i<=11; i++) {
    strip.setPixelColor(i,   150, 0, 0);
    strip.show();
    delay(delayTime);
    strip.setPixelColor(i,   175, 0, 0);
    strip.show();
    delay(delayTime);
    strip.setPixelColor(i,   200, 0, 0);
    strip.show();
    delay(delayTime);
    strip.setPixelColor(i,   175, 0, 0);
    strip.show();
    delay(delayTime);
    strip.setPixelColor(i,   150, 0, 0);
    strip.show();
    delay(delayTime);
    strip.setPixelColor(i, 0, 0, 0);
  }
}

