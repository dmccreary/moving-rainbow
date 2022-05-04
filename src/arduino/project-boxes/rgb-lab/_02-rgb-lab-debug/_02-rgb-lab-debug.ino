#include <Adafruit_NeoPixel.h>

#define RED_POT_PIN A0
#define GREEN_POT_PIN A1 
#define BLUE_POT_PIN A2

#define NUMBER_PIXELS 12
#define LED_DATA_PIN 12
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LED_DATA_PIN, NEO_GRB + NEO_KHZ800);


void setup()
{
  pinMode(RED_POT_PIN, OUTPUT);
  pinMode(GREEN_POT_PIN, OUTPUT);
  pinMode(BLUE_POT_PIN, OUTPUT);
  strip.begin(); // initialize the memory for the LED strip
  Serial.begin(9600);
}

void loop() {
  int redValue2, greenValue2, blueValue2;
  // read the POT values
  int redValue = analogRead(RED_POT_PIN); 
  int greenValue = analogRead(GREEN_POT_PIN);
  int blueValue = analogRead(BLUE_POT_PIN);

    // convert range of 0-1023 to 0-255
  redValue2 = map(redValue, 0, 1024, 0, 255);
  greenValue2 = map(greenValue, 0, 1024, 0, 255);
  blueValue2 = map(blueValue,  0, 1024, 0, 255);
  
  Serial.print("r=");
  Serial.print(redValue, DEC);
  Serial.print(" r=");
  Serial.print(redValue2, DEC);
  
  Serial.print("  g=");
  Serial.print(greenValue, DEC);
  Serial.print(" g=");
  Serial.print(greenValue2, DEC);
  
  Serial.print("  b=");
  Serial.print(blueValue, DEC);
  Serial.print(" b=");
  Serial.println(blueValue2, DEC);


  // update the new values
  for (int i=0; i<=NUMBER_PIXELS; i++)
      strip.setPixelColor(i, redValue2, greenValue2, blueValue2);
   strip.show();
   delay(100); // slow the loop down
}
