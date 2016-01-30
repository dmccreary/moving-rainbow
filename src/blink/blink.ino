#include <Adafruit_NeoPixel.h>
#define NUMBER_PIXEL 10
#define STRIP_PIN    0

// Our version of "Hello World".  Blink the first pixel (0) on and off every second

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXEL, STRIP_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin();
}
 
void loop() {
  strip.setPixelColor(0, 255, 0, 0); // set pixel 0 to be bright red
  strip.show(); // send data to the strip
  delay(1000); // wait 1 second
  strip.setPixelColor(0, 0, 0, 0); // set pixel 0 to be off
  delay(1000);  // wait 1 second
  strip.show(); // send data to the strip
}
