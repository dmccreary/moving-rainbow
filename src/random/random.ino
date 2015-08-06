#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int index, red, green, blue;

void setup() {
  strip.begin(); // initialize the strip
}

void loop() {
  index = random(12);
  red = random(255);
  green = random(255);
  blue = random(255);
  strip.setPixelColor(index, strip.Color(red, green, blue));
  strip.show();
  delay(100);
}

