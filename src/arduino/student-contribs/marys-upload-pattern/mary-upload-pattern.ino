// Mary wrote this originally to simulate "program loading" status pattern
// Then she added both up and down directions and also added multiple colors

#include <Adafruit_NeoPixel.h>
#define LEDPIN 12
#define NUMBER_PIEXELS 12
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

void setup() { 
    strip.begin();
    Serial.begin(9600);
}

void loop() {
    int color=0;
    
    // turn each pixel on going up the strip
    for (int i=0; i<strip.numPixels(); i++) {
        strip.setPixelColor(i, Wheel(color));
        strip.show();
        delay(50);
        color=color+20;  // add a bit to our current color
   }

   // turn each pixel off going down the strip
   for (int j=strip.numPixels()-1; j>=0; j--) {
       strip.setPixelColor(j, 0, 0, 0);
       strip.show();
       delay(50);
   }
}

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
