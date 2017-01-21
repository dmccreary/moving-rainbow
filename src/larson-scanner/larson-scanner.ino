#include <Adafruit_NeoPixel.h>
#define NUMBER_PIEXEL 12
#define LEDPIN    12

// Our equivenlt to "Hello World".  Blink the first pixes (0) on and off every second

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXEL, LEDPIN, NEO_GRB + NEO_KHZ800);
 
void setup() {
  strip.begin();
}
 
void loop() {
  strip.setPixelColor(0, 255, 0, 0); // set pixel 0 to be bright red
  strip.show(); // send data to the strip
  delay(1000); // wait one second
  strip.setPixelColor(0, 0, 0, 0); // set pixel 0 to be off
  strip.show(); // send data to the strip
  delay(1000); // wait one second
}
