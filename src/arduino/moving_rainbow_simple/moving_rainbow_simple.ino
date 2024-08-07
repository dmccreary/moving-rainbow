#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int delayTime = 100; // 100 milliseconds or 1/10 of a second is a good speed for a 12 pixel strip

void setup() {
  strip.begin(); // initialize the strip
}

void loop() {
  for (int i=0; i<strip.numPixels()-1; i++) {
    rainbow7(i, delayTime); // starting at i, draw the 7 color rainbow
  }
}

// draw a seven-segment rainbow on the LED strip with red on the highest pixel
// i is the index of where to start, wait is the delay time
// strip is the LED strip global
void rainbow7(uint16_t i, uint16_t wait) {
    int np = strip.numPixels();  // we use the modulo function with this
    strip.setPixelColor(    i  % np, 0, 0, 0); // turn off the traling edge
    strip.setPixelColor( (i+1) % np, 25, 0, 25); // violet
    strip.setPixelColor( (i+2) % np, 255, 0, 255); // indigo
    strip.setPixelColor( (i+3) % np, 0, 0, 150); // blue
    strip.setPixelColor( (i+4) % np, 0, 150, 0); // green
    strip.setPixelColor( (i+5) % np, 255, 255, 0); // yellow
    strip.setPixelColor( (i+6) % np, 110, 70, 0); // orange
    strip.setPixelColor( (i+7) % np, 150, 0, 0); // red
    strip.show();
    delay(wait);
}
