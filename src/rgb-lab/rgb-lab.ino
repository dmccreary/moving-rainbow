#include <Adafruit_NeoPixel.h>

#define LEDPIN 12 // connect the Data In pin
#define NUMBER_PIXELS 12// connect the Data In pin
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

const int analog_red_pin   = 0; // Analog input pin number for reading Red value
const int analog_green_pin = 1; // Analog input pin number for reading Green value
const int analog_blue_pin  = 2; // Analog input pin number for reading Blue value
// the value is the number from 0 to 1023 from the POT
// the brightness is the brightness of the color from 0 to 255
// The offset is the minimum value of the POT
int red_value, red_brightness, red_offset = 23;
int green_value, green_brightness, green_offset = 70;
int blue_value, blue_brightness, blue_offset = 25;

void setup() {
  strip.begin(); // initialize memory for the LED strip
  for (int i = 0; i < NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, 255, 0, 0);
  }
  strip.show();
  delay(200);
  for (int i = 0; i < NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, 0, 255, 0);
  }
  strip.show();
  delay(200);
  for (int i = 0; i < NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, 0, 0, 255);
  }
  strip.show();
  delay(200);
  Serial.begin(9600); // Enable the serial port
  Serial.println("Start");
}

void loop() {
  // the third number is the max value of the pot 
  red_value   = analogRead(analog_red_pin);
  red_brightness = map(red_value, red_offset, 950, 0, 255);
  red_brightness = constrain(red_brightness, 0, 255);
  
  green_value = analogRead(analog_green_pin);
  green_brightness = map(green_value, green_offset, 990, 0, 255);
  green_brightness = constrain(green_brightness, 0, 255);
  
  blue_value  = analogRead(analog_blue_pin);
  blue_brightness = map(blue_value, blue_offset, 910, 0, 255);
  blue_brightness = constrain(blue_brightness, 0, 255);
  
  // convert the values to 1/4 of the inverse
  
  for (int i = 0; i < NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, red_brightness, green_brightness , blue_brightness);
  }
  strip.show();
 
  Serial.print("red=");
  Serial.print(red_value);
  Serial.print(",");
  Serial.print(red_brightness);
  Serial.print(" green=");
  Serial.print(green_value);
  Serial.print(",");
  Serial.print(green_brightness);
  Serial.print(" blue=");
  Serial.print(blue_value);
  Serial.print(",");
  Serial.print(blue_brightness);
  Serial.println("");
}
