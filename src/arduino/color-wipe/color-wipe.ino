
#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int waitTime = 100;

void setup() {
  strip.begin();
}

void loop() {
  colorWipe(strip.Color(255, 0, 0), waitTime); // Red
  colorWipe(strip.Color(0, 255, 0), waitTime); // Green
  colorWipe(strip.Color(0, 0, 255), waitTime); // Blue
}

void colorWipe(uint32_t color, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, color);
      strip.show();
      delay(wait);
  }
}
