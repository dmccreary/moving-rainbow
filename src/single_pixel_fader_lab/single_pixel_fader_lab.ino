#include <Adafruit_NeoPixel.h>

#define PIN 2 // connect the Data In pin
 
// Parameter 1 = number of pixels in strip - I used 12
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_GRB     Pixels are wired for GRB bitstream
//   NEO_KHZ800  800 KHz bitstream (e.g. High Density LED strip)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(1, PIN, NEO_GRB + NEO_KHZ800);

int i=0; // Our fade counter.  Must be between 0 and 255
int minBright = 10; // minimal bright for initial test
int delayVal = 10; // how quickly to ramp up and down each of the 255 brightness levels (milliseconds)

void setup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}
 
void loop() {
  
  // show red for 1 second
  strip.setPixelColor(0, minBright, 0, 0);
  strip.show();
  delay(1000);
  
  // show green for 1 second
  strip.setPixelColor(0, 0, minBright, 0);
  strip.show();
  delay(1000);
  
  // show blue for 1 second
  // we have to triple the value to get a similar brightness
  strip.setPixelColor(0, 0, 0, minBright * 3);
  strip.show();
  delay(1000);
  
  // red fade in
  for (i=0; i<=255; i++) {
    strip.setPixelColor(0, i, 0, 0); // i is red
    strip.show();
    delay(delayVal);
  };
  
  // red fade out
  for (i=255; i>=0; i--) {
    strip.setPixelColor(0, i, 0, 0); // i is red
    strip.show();
    delay(delayVal);
  };
  
  // green fade in
  for (i=0; i<=255; i++) {
    strip.setPixelColor(0, 0, i, 0); // i is green
    strip.show();
    delay(delayVal);
  };
  
  // green fade out
  for (i=255; i>=0; i--) {
    strip.setPixelColor(0, 0, i, 0); // i is green
    strip.show();
    delay(delayVal);
  };
  
  // blue fade in
  for (i=0; i<=255; i++) {
    strip.setPixelColor(0, 0, 0, i); // i is blue
    strip.show();
    delay(delayVal);
  };
  
  // blue fade out
  for (i=255; i>=0; i--) {
    strip.setPixelColor(0, 0, 0, i); // i is blue
    strip.show();
    delay(delayVal);
  };
  
}

