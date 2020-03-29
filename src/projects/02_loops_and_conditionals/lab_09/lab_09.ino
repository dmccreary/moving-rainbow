#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int delayTime = 100; // 1/10 of a second

void setup() {
  strip.begin(); // initialize the strip
}

void loop() {
  for (int i=0; i<strip.numPixels()-1; i++) {
    rainbow7(i, delayTime); // starting at i, draw the 7 color rainbow
  }
}

// a seven segment rainbow with red on the highest pixel
void rainbow7(uint16_t i, uint16_t wait) {
    int np = strip.numPixels();  // we use the modulo function with this
    strip.setPixelColor(i     % np, 25, 0, 25); // violet
    strip.setPixelColor((i+1) % np, 255, 0, 255); // indigo
    strip.setPixelColor((i+2) % np, 0, 0, 150); // blue
    strip.setPixelColor((i+3) % np, 0, 150, 0); // green
    strip.setPixelColor((i+4) % np, 255, 255, 0); // yellow
    strip.setPixelColor((i+5) % np, 110, 70, 0); // orange
    strip.setPixelColor((i+6) % np, 150, 0, 0); // red
    // we don't need to touch 7, 8 and 9
    strip.setPixelColor((i+10) % np, 0, 0, 0); // turn the second to the last one off
    strip.setPixelColor((i+11) % np, 0, 0, 0); // turn the last one off
    strip.show();
    delay(wait);
}
