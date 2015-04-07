// fade in and out

#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int waitTime = 10;

void setup() {
  strip.begin();
}

void loop() {
  fadeInAndOut(255, 0, 0, waitTime); // Red
  fadeInAndOut(0, 255, 0, waitTime); // Green
  fadeInAndOut(0, 0, 255, waitTime); // Blue
}

void fadeInAndOut(uint8_t red, uint8_t green, uint8_t blue, uint8_t wait) {
  
  for(uint8_t b=0; b <255; b++) {
     for(uint8_t i=0; i < strip.numPixels(); i++) {
        strip.setPixelColor(i, red*b/255, green*b/255, blue*b/255);
     }
     strip.show();
     delay(wait);
  };
  
  for(uint8_t b=255; b > 0; b--) {
     for(uint8_t i=0; i < strip.numPixels(); i++) {
        strip.setPixelColor(i, red*b/255, green*b/255, blue*b/255);
     }
     strip.show();
     delay(wait);
  };
  
 
  
}
