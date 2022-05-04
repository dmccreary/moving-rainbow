
#include <Encoder.h>
#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIXELS 24 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

// Change these pin numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder myEnc(2, 3);
long oldPosition  = -999;
long clicks  = -999;

void setup() {
  Serial.begin(9600);
  Serial.println("Encoder Test:");
  clicks = 0;
}




void loop() {
  long newPosition = myEnc.read();
  
  if (newPosition != oldPosition) {
    oldPosition = newPosition;
    // Serial.println(newPosition);
    clicks = newPosition / 4;
    Serial.println(clicks);
  }
}
