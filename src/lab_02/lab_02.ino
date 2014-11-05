#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

void setup() {
  strip.begin(); // initialize all the variables
  strip.setPixelColor(0, 255, 0, 0); // set the first pixel to be red
  strip.setPixelColor(1, 0, 255, 0); // set second pixel green
  strip.setPixelColor(2, 0, 0, 255); // set the third pixel to be blue
  strip.setPixelColor(3, 128, 128, 0); // set fourth pixel to be olive?
  strip.setPixelColor(4, 255, 165, 0); // set fifth pixel to be orange
  strip.setPixelColor(5, 255, 255, 0); // set sixth pixel to be yellow
  strip.setPixelColor(6, 255, 0, 255); // set seventh pixel to be Fuchsia/Magenta
  strip.setPixelColor(7, 0, 255, 255); // set eighth pixel to be Aqua/Cyan
  strip.setPixelColor(8, 255, 105, 180); // set ninth pixel to be hot pink
  strip.setPixelColor(9, 255, 255, 255); // set tenth pixel to be white
  strip.setPixelColor(10, 10, 10, 10); // set eleventh pixel to be light gray
  strip.setPixelColor(11, 1, 1, 1); // set twelfth and last pixel to be almost off
  strip.show(); // Send to the strip}
}

void loop() {
  
}

