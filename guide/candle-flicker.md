Candle Flicker
==============

Here we combine some random functions with the intensity of a yellow and orange colors.

```
#include <Adafruit_NeoPixel.h>
#define PIN 12 // connect the Data In pin
Adafruit_NeoPixel strip = Adafruit_NeoPixel(18, PIN, NEO_GRB + NEO_KHZ800);
 
void setup() {
  strip.begin();
}

void loop() {
  candle();
}

void candle() {
   uint8_t green; // brightness of the green 
   uint8_t red;  // add a bit for red
   for(uint8_t i=0; i<100; i++) {
     green = 50 + random(155);
     red = green + random(50);
     strip.setPixelColor(random(strip.numPixels() - 1), red, green, 0);
     strip.show();
     delay(5);
  }
}
```