#include <Adafruit_NeoPixel.h>
#define NUMBER_PIXEL 12
#define STRIP_PIN    12
#define TOUCH_PIN     4

// Our version of "Hello World".  Blink the first pixel (0) on and off every second

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXEL, STRIP_PIN, NEO_GRB + NEO_KHZ800);

int touchValue = LOW;

void setup() {
  strip.begin();
  pinMode(TOUCH_PIN, INPUT);
}
 
void loop() {
  strip.setPixelColor(0, 255, 0, 0); // set pixel 0 to be bright red
  touchValue = digitalRead(TOUCH_PIN);
  strip.setPixelColor(0, touchValue*100, 0, 0); // set pixel 0 to be off
  strip.show(); // send data to the strip
  delay(50);
}
