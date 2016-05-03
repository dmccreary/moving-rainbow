#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int delayTime = 500; // 1/2 of a second

void setup() {
  strip.begin(); // initialize the strip
}

void loop() {
  for (int i=0; i<strip.numPixels(); i++) {
    rainbow7(i, delayTime); // starting at i, draw the 7 color rainbow
  }
}

// a seven segment rainbow with red on the highest pixel
void rainbow7(int  i,int  wait) {
    int np = strip.numPixels();  // we use the modulo function with this
    strip.setPixelColor(i %np, 255, 255, 0);
    strip.show();
    delay(wait);
}
