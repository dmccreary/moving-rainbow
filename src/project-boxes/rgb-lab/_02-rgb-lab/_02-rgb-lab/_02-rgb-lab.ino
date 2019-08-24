#include <Adafruit_NeoPixel.h>

#define RED_POT_PIN A0
#define GREEN_POT_PIN A1 
#define BLUE_POT_PIN A0 

#define NUMBER_PIXELS 12
#define LED_DATA_PIN 12
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LED_DATA_PIN, NEO_GRB + NEO_KHZ800);
int redValue, greenValue, blueValue;

void setup()
{
  pinMode(RED_POT_PIN, OUTPUT);
  pinMode(GREEN_POT_PIN, OUTPUT);
  pinMode(BLUE_POT_PIN, OUTPUT);
  strip.begin(); // initialize the memory for the LED strip
}

void loop() {
  // read the POT values
  redValue = analogRead(RED_POT_PIN); 
  greenValue = analogRead(GREEN_POT_PIN);
  blueValue = analogRead(BLUE_POT_PIN);

  // convert range of 0-1023 to 0-255
  redValue = map(redValue,   0, 1024, 0, 255);
  greenValue = map(greenValue, 0, 1024, 0, 255);
  blueValue = map(blueValue,  0, 1024, 0, 255);

  // update the new values
  for (int i=0; i<=NUMBER_PIXELS; i++)
      strip.setPixelColor(i, redValue, greenValue, blueValue);
   strip.show();
   delay(50); // slow the loop down
}
