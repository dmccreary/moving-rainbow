// single pattern test
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

// 10 color array
int colors[30] =
   {255,  64,  64,
    255,   0,   0,
    255, 128,   0,
    255, 255,   0,
    0,   255,   0,
    0,   255, 255,
    0,     0, 255,
    128,   0, 255,
    255,   0, 255,
    128,  50, 128
   };
    

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
    brightness = map(brightness, 0, 1023, 1, 255);
    speed_level = analogRead(SPEED_POT_PIN);
    speed_level = map(speed_level, 0, 1023, 30, 1000);  // anything faster than 30 is a blur


    display_theater_chase_rainbow(brightness);
    myIndex++;
    if (myIndex > strip.numPixels()) 
      myIndex = 0;
    delay(speed_level);
}


// Theatre-style crawling lights - 10 colors 6 pixels apart
void display_theater_chase_rainbow(int brightness) {
  int step, red, green, blue, offset;
  int np = strip.numPixels();
  int num_pix_draws = np / 6;
  for (int i=0; i < num_pix_draws; i++) {
      int color = i % 10;
      red = map(colors[color], 0, 255, 0, brightness);
      green = map(colors[color+1], 0, 255, 0, brightness);
      blue = map(colors[color+2], 0, 255, 0, brightness);
      offset = i * 6;
      strip.setPixelColor((offset + myIndex) % np, 0, 0, 0);
      strip.setPixelColor((offset + myIndex + 1) % np, red, green, blue);
    }
  strip.show();
  delay(3); 
}
