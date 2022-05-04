
#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIXELS 8 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int delayTime = 15; // 20 milliseconds

void setup() {
  strip.begin(); // initialize the strip
}

void loop() {
  for (int i=10; i<=150; i++) {
    all_Blue(i); // starting at zero, increase brightness
    delay(delayTime);
  }

  for (int i=150; i>=10; i--) {
    all_Blue(i); // starting at full brightness, go to zero
    delay(delayTime);
  }
}

// a draw all pixels the same color blue with brightness b
void all_Blue(int  b) {
    for (int i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, 0, 0, b);
    }
    
    strip.show();
    
}
