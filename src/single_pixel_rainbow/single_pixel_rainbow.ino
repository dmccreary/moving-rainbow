#include <Adafruit_NeoPixel.h>
 
// Sample code for using a breadboard Arduino to drive WS2812B LED strip with Adafruit NeoPixel library
// I got mine on e-bay:
// http://www.ebay.com/itm/181268207260?ssPageName=STRK:MEWNX:IT&_trksid=p3984.m1439.l2649
// Note - colors for data and ground vary
// I used a 16MHZ Crystal Oscilator
#define PIN 2 // connect the Data In pin
 
// Parameter 1 = number of pixels in strip - I used 12
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_GRB     Pixels are wired for GRB bitstream
//   NEO_KHZ800  800 KHz bitstream (e.g. High Density LED strip)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(1, PIN, NEO_GRB + NEO_KHZ800);

int delayVal = 100; // how quickly to stay on each of the 255 colors (milliseconds)

void setup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}

void loop() {
  // i is an unsigned 8 bit integer or a byte
  for (int i=0; i<255; i++) {
    strip.setPixelColor(0, Wheel(i));
    strip.show();
    delay(delayVal);
  };
  
  // turn off for 1/2 second
  strip.setPixelColor(0, 0, 0, 0);
  strip.show();
  delay(1000);
}

// a color wheel function.
// Input a value 0 to 255 to get a color value.
// The colors transition from red, orange, yellow, green, blue, purple, then back to red
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
   return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else if(WheelPos < 170) {
    WheelPos -= 85;
   return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  } else {
   WheelPos -= 170;
   return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  }
}
