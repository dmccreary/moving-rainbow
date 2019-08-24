//Ice and Snow
// blue ice goes up as white snow comes down
#include <Adafruit_NeoPixel.h>

#define BRIGHTNESS_POT_PIN A0
#define SPEED_POT_PIN A1

// Output pin
#define LED_PIN 12 // connect the Data In pin
#define NUMBER_PIXELS 144 // connect the Data In pin
#define MODE_COUNT 28
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LED_PIN, NEO_GRB + NEO_KHZ800);

// these variables updated with each loop
int brightness = 50; // The brightness from the pot is from 0 to 1023 but to the LEDs are 1 to 254
int speed_level = 50; // The brightness from the pot is from 0 to 1023 but to the LEDs are 1 to 254

int myIndex = 0; // the index of where we are drawing to the LED strip - cycles from 0 to NUMBER_PIXELS

void setup() {
  strip.begin(); // sets up the memory for the LED strip
  pinMode(LED_PIN, OUTPUT);     // Pin 13 is output to which an LED is connected
  pinMode(BRIGHTNESS_POT_PIN, INPUT);
  pinMode(SPEED_POT_PIN, INPUT);

  Serial.begin(9600);
  Serial.println("Start Function Finished");
}

void loop() {
    brightness = analogRead(BRIGHTNESS_POT_PIN);
    speed_level = analogRead(SPEED_POT_PIN);
    display_ice_and_snow(brightness);
    myIndex++;
    if (myIndex > strip.numPixels()) 
      myIndex = 0;
    delay(speed_level);
}

// ice moves up and snow comes down
void display_ice_and_snow(int brightness) {
  int step_distance = 15;
  int offset, offset_top, base;
  int np = strip.numPixels();
  int num_pix_draws = np / step_distance;
  for (int i=0; i < num_pix_draws + 2; i++) {
      offset = i * step_distance;
      offset_top = offset - (myIndex % step_distance) -1;
      // blue goes up from 0 to step_distance
      base = offset + myIndex;
      strip.setPixelColor(base % np, 0, 0, 0);
      strip.setPixelColor((base + 1) % np, 0, 0, brightness);

      // white goes down
      strip.setPixelColor(offset_top % np, 0, 0, 0);
      strip.setPixelColor((offset_top - 1)  % np, brightness, brightness, brightness);
      
    }
  strip.show();
}
