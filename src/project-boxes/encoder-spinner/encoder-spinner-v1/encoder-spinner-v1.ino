#include <Adafruit_NeoPixel.h>
#include <Encoder.h> // http://www.pjrc.com/teensy/td_libs_Encoder.html
#define ENCODER_PIN_A 2 // Digital input with an interrupt
#define ENCODER_PIN_B 3 // Digital input with an interrupt

#define LEDPIN 12 // connect the Data In pin
#define NUMBER_PIXELS 24// connect the Data In pin
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);
Encoder myEnc(ENCODER_PIN_A, ENCODER_PIN_B);
// where we start to draw
int stripIndex = 0;
long newPosition;
long oldPosition  = -999;

void setup()
{
  strip.begin(); // sets up the memory for the LED strip
  pinMode(13, OUTPUT);     // Pin 13 is usually on an onboard LED
  pinMode(ENCODER_PIN_A, INPUT_PULLUP);
  pinMode(ENCODER_PIN_B, INPUT_PULLUP);
  Serial.begin (9600);
  Serial.println("Start");
  dot(stripIndex);
}

void loop()
{
  newPosition = myEnc.read();
  // Serial.println(newPosition);
  // only update the display if we have a new position 
  if (newPosition != oldPosition) {
    oldPosition = newPosition;
    stripIndex = newPosition/4 % strip.numPixels();
    if (stripIndex < 0) 
       stripIndex = strip.numPixels() - 1;
    Serial.print("pos:");
    Serial.print(newPosition);
    Serial.print(" strip index=");
    Serial.println(stripIndex);
    dot(stripIndex); // draw the rainbow starting at this index
  };
  delay(100);
}

void dot(int startIndex) {
    strip.setPixelColor(startIndex - 2 ,  0, 0, 0);
    strip.setPixelColor(startIndex - 1 ,  0, 0, 0);
    strip.setPixelColor(startIndex,     255, 0, 255); // purple
    strip.setPixelColor(startIndex + 1 ,  0, 0, 0);
    strip.setPixelColor(startIndex + 2 ,  0, 0, 0);
    strip.show();
}

void rainbow7(int startIndex) {
    for (int i=startIndex; i<startIndex+strip.numPixels()-1; i++) {
      int np = strip.numPixels();  // we use the modulo function with this
      strip.setPixelColor(i     % np, 25, 0, 25); // violet
      strip.setPixelColor((i+1) % np, 255, 0, 255); // indigo
      strip.setPixelColor((i+2) % np, 0, 0, 150); // blue
      strip.setPixelColor((i+3) % np, 0, 150, 0); // green
      strip.setPixelColor((i+4) % np, 255, 255, 0); // yellow
      strip.setPixelColor((i+5) % np, 110, 70, 0); // orange
      strip.setPixelColor((i+6) % np, 150, 0, 0); // red
      // we don't need to touch 7, 8 and 9
      strip.setPixelColor((i+7) % np, 0, 0, 0); // turn the second to the last one off
      strip.setPixelColor((i+8) % np, 0, 0, 0); // turn the second to the last one off
      strip.setPixelColor((i+9) % np, 0, 0, 0); // turn the second to the last one off
      strip.setPixelColor((i+10) % np, 0, 0, 0); // turn the second to the last one off
      strip.setPixelColor((i+11) % np, 0, 0, 0); // turn the last one off
      strip.show();
    }
}
