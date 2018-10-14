#include <Adafruit_NeoPixel.h>

#define LED_PIN 12

#define NUM_PIXELS 60

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUM_PIXELS, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  pixels.begin(); // This initializes the NeoPixel library.
}

void loop() {
  for(int i=0;i<NUMPIXELS;i++){
    pixels.setPixelColor(i, 255, 0, 255);  // R,G,B for purple
    pixels.show();
    delay(100); // 1/10 sec
    pixels.setPixelColor(i, 0, 0, 0);  // erase
  }
}
