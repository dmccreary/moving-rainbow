#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 16 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);
int n = strip.numPixels();
int color_step = (int) 255/n; // 1/16 of the way around the 255 element color wheel

void setup() {
  strip.begin();
  draw_color_menu();
}

void loop() {
}

// draw each pixel in the ring with a different color on the color wheel
void draw_color_menu() {
   for (int i=0; i<strip.numPixels(); i++) {
        strip.setPixelColor(i, Wheel(color_step * i));
  }
  strip.show();
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
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
