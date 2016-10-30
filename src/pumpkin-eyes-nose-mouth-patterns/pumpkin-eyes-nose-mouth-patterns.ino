
#include <Adafruit_NeoPixel.h>

#define LEFT_EYE_PIN 9 // pin to left eye
#define RIGHT_EYE_PIN 10 // pin to left eye
#define NUMBER_EYE_PIXELS 7

#define NOSE_PIN 11
#define NUMBER_NOSE_PIXELS 8

#define MOUTH_PIN 12
#define NUMBER_MOUTH_PIXELS 12// connect the Data In pin

Adafruit_NeoPixel right_eye = Adafruit_NeoPixel(NUMBER_EYE_PIXELS, RIGHT_EYE_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel left_eye = Adafruit_NeoPixel(NUMBER_EYE_PIXELS, LEFT_EYE_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel nose = Adafruit_NeoPixel(NUMBER_NOSE_PIXELS, NOSE_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel mouth = Adafruit_NeoPixel(NUMBER_MOUTH_PIXELS, MOUTH_PIN, NEO_GRB + NEO_KHZ800);

// hook up two momentary push buttons to pins 
volatile int newMode = 1; // the interrupts set this to 1 to indicate that we have a new mode on the way
volatile int mode = -1; // This gets incremented each button press
int hold_on_pattern = 1000; //Typical delay between draws
int modeCount = 11; // The number of display modes
int loop_count; // the number of times through the main loop
int ear_ring_increment_steps = 5; //

void setup() {
  right_eye.begin(); // sets up the memory for the LED strip
  left_eye.begin();
  nose.begin();
  mouth.begin();
  Serial.begin(9600);
  Serial.println("Start");
}

void loop() {
    solid_color(255,0,0);
    delay(hold_on_pattern);
    
    solid_color(110,70,0);
    delay(hold_on_pattern);
    
    solid_color(255,255,0);
    delay(hold_on_pattern);
    
    solid_color(0,255,0);
    delay(hold_on_pattern);
    
    solid_color(0,0,255);
    delay(hold_on_pattern);
    
    solid_color(255,0,255);
    delay(hold_on_pattern);
    
    solid_color(50,0,50);
    delay(hold_on_pattern);
    
    loop_count++;
    Serial.print("loop count=");
    Serial.println(loop_count);
}

void solid_color(int r, int g, int b){
  for (int i=0; i < left_eye.numPixels();i++) {
    left_eye.setPixelColor(i, r, g, b);
  }
  
  for (int i=0; i < right_eye.numPixels();i++) {
    right_eye.setPixelColor(i, r, g, b);
  }
  
  for (int i=0; i < nose.numPixels();i++) {
    nose.setPixelColor(i, r, g, b);
  }
  
  for (int i=0; i < mouth.numPixels();i++) {
    mouth.setPixelColor(i, r, g, b);
  }
  
  left_eye.show();
  right_eye.show();
  nose.show();
  mouth.show();
};
