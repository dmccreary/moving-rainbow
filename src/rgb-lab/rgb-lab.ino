#include <Adafruit_NeoPixel.h>

#define LEDPIN 12 // connect the Data In pin
#define NUMBER_PIEXELS 10// connect the Data In pin
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

const int analog_red_pin   = 0; // Analog input pin number for reading Red value
const int analog_green_pin = 1; // Analog input pin number for reading Green value
const int analog_blue_pin  = 2; // Analog input pin number for reading Blue value
int red_value;
int green_value;
int blue_value;

void setup() {
  strip.begin(); // initialize memory for the LED strip
  for (int i = 0; i < NUMBER_PIEXELS; i++) {
    strip.setPixelColor(i, 255, 0, 0);
  }
  strip.show();
  delay(500);
  for (int i = 0; i < NUMBER_PIEXELS; i++) {
    strip.setPixelColor(i, 0, 255, 0);
  }
  strip.show();
  delay(500);
  for (int i = 0; i < NUMBER_PIEXELS; i++) {
    strip.setPixelColor(i, 0, 0, 255);
  }
  strip.show();
  delay(500);
  Serial.begin(9600); // Enable the serial port
  Serial.println("Start");
}

void loop() {
  red_value   = analogRead(analog_red_pin);
  green_value = analogRead(analog_green_pin);
  blue_value  = analogRead(analog_blue_pin);
  
  // convert the values to 1/4 of the inverse
  
  for (int i = 0; i < NUMBER_PIEXELS; i++) {
    strip.setPixelColor(i, red_value / 4, green_value / 4, blue_value / 4);
  }
  strip.show();
 
  Serial.print("red=");
  Serial.print(red_value);
  Serial.print(" green=");
  Serial.print(green_value);
  Serial.print(" blue=");
  Serial.print(blue_value);
  Serial.println("");
}
