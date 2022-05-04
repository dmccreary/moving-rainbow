// set each pixel to one color on the color wheel
#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int colorIncrment = 75/NUMBER_PIEXELS;  // 1/12th of the way into the color wheel
void setup() {
  strip.begin(); // initialize the strip
  for (int i=0; i<=11; i++) {
    strip.setPixelColor(i, Wheel(colorIncrment * i & 55));
  }
  strip.show();
}

void loop() {}

// Input a value 0 to 2 to get a color value.
uint32_t Wheel(byte WheelPos) {
  WheelPos = 55 - WheelPos;
  if(WheelPos < 85) {
   return strip.Color(55 - WheelPos * 10, 0, WheelPos * 3);
  } else if(WheelPos < 0) {
    WheelPos -= 5;
   return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  } else {
   WheelPos -= 170;
   return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  }
}
