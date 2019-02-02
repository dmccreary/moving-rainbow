/*
 * Arduino Moving Rainbow Kit Mode Demo
 * For use with an Arduino with an WS2812 LED strip, a mode button and two potentiometers
 * Dan McCreary
 * Nov. 2017
 */
#include <Adafruit_NeoPixel.h>#include <Encoder.h>

#include <avr/interrupt.h>

// Input pins
#define MODE_NEXT_PIN 2 // pull down to groud to get a new mode
#define MODE_PREV_PIN 3 // pull down to groud to get a new mode
#define BRIGHTNESS_POT_PIN A0 // connect center pin of a potentiometer, sides go to +5 and GND
#define SPEED_POT_PIN A1 // connect center pin of a potentiometer, sides go to +5 and GND

// Output pin
#define LED_PIN 12 // connect the Data In pin
#define NUMBER_PIXELS 60 // connect the Data In pin
#define MODE_COUNT 28
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LED_PIN, NEO_GRB + NEO_KHZ800);

// hook up two momentary push buttons to pin and keep them in memory
volatile int newMode = 0; // the interrupts set this to 1 to indicate that we have a new mode on the way
volatile int mode = 0; // The display mode.  This gets incremented each button press.  Set inital mode in setup().
volatile int demo_mode = 0; // The display mode.  This gets incremented each button press.  Set inital mode in setup().
volatile int display_mode = 1; // the demo display mode
const int modeCount = 28;// The number of display modes

// used for debouncing the mode button
long lastDebounceTime = 0;  // the last time the output pin was toggled
long debounceDelay = 60;   // the debounce time; increase if the output flickers

// these variables updated with each loop
int brightness = 50; // The brightness from the pot is from 0 to 1023 but to the LEDs are 1 to 254
int speed_value =  512; // The inverse of speed
int loop_delay =  512; // The inverse of speed
int index = 0; // the index of where we are drawing to the LED strip - cycles from 0 to NUMBER_PIXELS
int ri; // the reverse index NUMBER_PIXELS - index
int random_pos = strip.numPixels() / 2; // random index position for random walker
int print_debug_indicator = 1; // set to be 1 if you want to display values on the console
int candle_initilize = 1; // setup the initial candle to yellow
int demo_brightness = 15; // very dim in demo mode

void setup() {
  strip.begin(); // sets up the memory for the LED strip
  pinMode(LED_PIN, OUTPUT);     // Pin 13 is output to which an LED is connected
  pinMode(BRIGHTNESS_POT_PIN, INPUT);
  pinMode(SPEED_POT_PIN, INPUT);
  pinMode(MODE_NEXT_PIN, INPUT_PULLUP);	// Pin 2 is an input button tied to GND
  pinMode(MODE_PREV_PIN, INPUT_PULLUP); // Pin 3 is an input button tied to GND
  digitalWrite(MODE_NEXT_PIN, HIGH);
  digitalWrite(MODE_PREV_PIN, HIGH);
  attachInterrupt(0, mode_next, RISING); // connect the mode to pin 2
  attachInterrupt(1, mode_prev, RISING); // connect the mode to pin 3
  Serial.begin(9600);

  Serial.println("Start Function Finished");

  newMode = 0;
  mode = 0;
}

// Interrupt service routine - get in and out quickly, no printing to serial ports allowed here
void mode_next(){        
  newMode = 1;
  lastDebounceTime = millis(); // record when we got the interrupt for debouncin
}

void mode_prev(){        
  newMode = -1;
  lastDebounceTime = millis(); // record when we got the interrupt for debouncin
}

void loop() {
  // check to see if we should change the mode
  if (newMode == 1 || newMode == -1) {
    if ((millis() - lastDebounceTime) > debounceDelay) {
      // delay(100); // wait for the switch to settle down used to de-bounce
      // increment the mode and 
      mode = (mode + newMode) % MODE_COUNT;
      if (mode < 0) mode = MODE_COUNT; // start at the top
      Serial.print("New Mode mode=");
      Serial.println(mode, DEC);      
      newMode = 0;
    }
  }

   // select the mode
      switch (mode) {
        case 0:  demo();break; // this auto-incements the display_mode
        case 1:  display_rainbow7(brightness);break;
        case 2:  display_comet(brightness, 255, 0, 0);break; // Red coment
        case 3:  display_comet(brightness, 0, 255, 0);break; // Green
        case 4:  display_comet(brightness, 0, 0, 255);break; // Blue
        case 5:  display_comet(brightness, 255, 255, 0);break; // yellow
        case 6:  display_comet(brightness, 200, 150, 0);break; // orange
        case 7:  display_comet(brightness, 0, 255, 255);break; // cyan comet
        case 8:  display_comet(brightness, 255, 0, 255);break; // purple comet
        case 9:  display_comet(brightness, 255, 255, 255);break; // white comet
        case 10: display_theater_chase(brightness, 255, 0, 0);break;
        case 11: display_theater_chase(brightness, 0, 255, 0);break;
        case 12: display_theater_chase(brightness, 0, 0, 255);break;
        case 13:  candle_initilize == 0;
                 init_candle(brightness);
                 display_candle(brightness);
                 break; // Candle flicker
        case 14:  candle_initilize == 0;
                 display_random_colors(brightness, 0); // don't erase between flash
                 break;
        case 15: display_random_colors(brightness, 1);break; // with erase between flashs
        case 16: display_rainbow_12(brightness);break;

        case 17: display_color_wipe(brightness, 255, 0, 0);break;
        case 18: display_color_wipe(brightness, 0, 255, 0);break;
        case 19: display_color_wipe(brightness, 0, 0, 255);break;
        case 20: display_over_and_back(brightness, 255, 0, 0);break;
        case 21: display_over_and_back(brightness, 0, 255, 0);break;
        case 22: display_over_and_back(brightness, 0, 0, 255);break;
        case 23: display_cylon(brightness, 255, 0, 0);break;
        case 24: display_cylon(brightness, 0, 255, 0);break;
        case 25: display_cylon(brightness, 0, 0, 255);break;
        case 26: display_random_walk(brightness, 255, 0, 0);break;
        case 27: display_random_walk(brightness, 0, 255, 0);break;
        case 29: display_random_walk(brightness, 0, 0, 255);break;
        case 30: display_rainbow_cycle();break;
     }
    // update the values from the pot
    brightness = analogRead(BRIGHTNESS_POT_PIN);
    brightness = map(brightness, 0, 1023, 1, 255); // make the min brightness be at 1east 1
    speed_value = analogRead(SPEED_POT_PIN);
    loop_delay = map(speed_value, 0, 1023, 1000, 0);  // map from 1 second to 0 milliseconds
    loop_delay = constrain(loop_delay, 0, 1000);

    if (print_debug_indicator == 1) print_debug();
    
    index++; // increment the index
    if (index > NUMBER_PIXELS) {
      index = 0; // index reset
      if (mode == 0) display_mode++;
      if (display_mode > MODE_COUNT) display_mode = 1;
    }
    ri = NUMBER_PIXELS - index;
    if (print_debug_indicator == 1)
      print_debug();
    
    delay(loop_delay);
}

void demo() {
  switch (display_mode) {
        case 1:  display_rainbow7(demo_brightness);break;
        case 2:  display_comet(demo_brightness, 255, 0, 0);break; // Red coment
        case 3:  display_comet(demo_brightness, 0, 255, 0);break; // Green
        case 4:  display_comet(demo_brightness, 0, 0, 255);break; // Blue
        case 5:  display_comet(demo_brightness, 255, 255, 0);break; // yellow
        case 6:  display_comet(demo_brightness, 200, 150, 0);break; // orange
        case 7:  display_comet(demo_brightness, 0, 255, 255);break; // cyan comet
        case 8:  display_comet(demo_brightness, 255, 0, 255);break; // purple comet
        case 9:  display_comet(demo_brightness, 255, 255, 255);break; // white comet
        case 10: display_theater_chase(demo_brightness, 255, 0, 0);break;
        case 11: display_theater_chase(demo_brightness, 0, 255, 0);break;
        case 12: display_theater_chase(demo_brightness, 0, 0, 255);break;
        case 13:  candle_initilize == 0;
                 init_candle(demo_brightness);
                 display_candle(brightness);
                 break; // Candle flicker
        case 14:  candle_initilize == 0;
                 display_random_colors(demo_brightness, 0); // don't erase between flash
                 break;
        case 15: display_random_colors(demo_brightness, 1);break; // with erase between flashs
        case 16: display_rainbow_12(demo_brightness);break;

        case 17: display_color_wipe(demo_brightness, 255, 0, 0);break;
        case 18: display_color_wipe(demo_brightness, 0, 255, 0);break;
        case 19: display_color_wipe(demo_brightness, 0, 0, 255);break;
        case 20: display_over_and_back(demo_brightness, 255, 0, 0);break;
        case 21: display_over_and_back(demo_brightness, 0, 255, 0);break;
        case 22: display_over_and_back(demo_brightness, 0, 0, 255);break;
        case 23: display_cylon(demo_brightness, 255, 0, 0);break;
        case 24: display_cylon(demo_brightness, 0, 255, 0);break;
        case 25: display_cylon(demo_brightness, 0, 0, 255);break;
        case 26: display_random_walk(demo_brightness, 255, 0, 0);break;
        case 27: display_random_walk(demo_brightness, 0, 255, 0);break;
        case 29: display_random_walk(demo_brightness, 0, 0, 255);break;
     }
}
// all display functions start with the string "display_"
// each display function must only draw a single pattern at the index using the brightness parameter
// index is a global variable
// the main loop does all the delays

// a seven segment rainbow with red on the highest pixel
void display_rainbow7(int brightness) {
  
    int low,med,med_high,high_val,very_high;
    // scale the numbers to the appropriate brightness levels
    low      = map(brightness, 1, 254, 1, 10);
    med      = map(brightness, 1, 254, 1, 50);
    med_high  = map(brightness, 1, 254, 1, 70);
    // high_val  = map(brightness, 1  254, 1, 150);
    very_high = map(brightness, 1, 254, 1, 254);
    
    // reset_LED_memory(); // make everything 0
    int np = strip.numPixels();  // we use the modulo function with this shorthand
    strip.setPixelColor(index  , 0, 0, 0); // off
    strip.setPixelColor(index+1  , med, 0, med); // violet
    strip.setPixelColor(index+2, very_high, 0, very_high); // indigo
    strip.setPixelColor(index+3, 0, 0, very_high); // blue
    strip.setPixelColor(index+4, 0, very_high, 0); // green
    strip.setPixelColor(index+5, very_high, very_high, 0); // yellow
    strip.setPixelColor(index+6, very_high, med_high, 0); // orange is 255, 165, 0 but looks yellow
    strip.setPixelColor(index+7, very_high, 0, 0); // red
    
    strip.setPixelColor(ri - 1, 0, 0, 0); // violet
    strip.setPixelColor(ri - 2, med, 0, med); // violet
    strip.setPixelColor(ri - 3  , very_high, 0, very_high); // indigo
    strip.setPixelColor(ri - 4, 0, 0, very_high); // blue
    strip.setPixelColor(ri - 5, 0, very_high, 0); // green
    strip.setPixelColor(ri - 6, very_high, very_high, 0); // yellow
    strip.setPixelColor(ri - 7, very_high, med_high, 0); // orange is 255, 165, 0 but looks yellow
    strip.setPixelColor(ri - 8, very_high, 0, 0); // red 
    strip.show();
}

// move a single pixel at brigness with values red, green and blue - all input parameters are 0 to 255
void display_moving_pixel(int brightness, int red, int green, int blue) {
  reset_LED_memory();
  red = map(red, 0, 255, 1, brightness);
  green = map(green, 0, 255, 1, brightness);
  blue = map(blue, 0, 255, 1, brightness);
  strip.setPixelColor(index, red, green, blue);
  strip.show();
}

// make a single color swoosh appear to move as a comet flying by with a tail
void display_comet(int brightness, int red, int blue, int green) {
  reset_LED_memory();
  // scale for brightness
  red = map(red, 0, 255, 1, brightness);
  green = map(green, 0, 255, 1, brightness);
  blue = map(blue, 0, 255, 1, brightness); 
  // draw the comet doing a swoosh  
  strip.setPixelColor(index + 6, red, blue, green);
  strip.setPixelColor(index + 5, red/1.5, blue/1.5, green/1.5);
  strip.setPixelColor(index + 4, red/2, blue/2, green/2);
  strip.setPixelColor(index + 3, red/4, blue/4, green/4);
  strip.setPixelColor(index + 2, red/8, blue/8, green/8);
  strip.setPixelColor(index + 1, red/16, blue/16, green/16);
  strip.setPixelColor(index, red/32, blue/32, green/32);

  strip.setPixelColor(ri - 6, red, blue, green);
  strip.setPixelColor(ri - 5, red/1.5, blue/1.5, green/1.5);
  strip.setPixelColor(ri - 4, red/2, blue/2, green/2);
  strip.setPixelColor(ri - 3, red/4, blue/4, green/4);
  strip.setPixelColor(ri - 2, red/8, blue/8, green/8);
  strip.setPixelColor(ri - 1, red/16, blue/16, green/16);
  strip.setPixelColor(ri    , red/32, blue/32, green/32);
  strip.show();
}

// make a single color swoosh appear to move as a comet flying by with a tail
void display_comet_wrap(int brightness, int red, int blue, int green) {
  reset_LED_memory();
  // scale for brightness
  red = map(red, 0, 255, 1, brightness);
  green = map(green, 0, 255, 1, brightness);
  blue = map(blue, 0, 255, 1, brightness); 
  // draw the comet doing a swoosh  
  strip.setPixelColor((index + 6) % strip.numPixels(), red, blue, green);
  strip.setPixelColor((index + 5) % strip.numPixels(), red/1.5, blue /1.5, green/ 1.5);
  strip.setPixelColor((index + 4) % strip.numPixels(), red/2, blue/2, green/2);
  strip.setPixelColor((index + 3) % strip.numPixels(), red/4, blue/4, green/4);
  strip.setPixelColor((index + 2) % strip.numPixels(), red/8, blue/8, green/8);
  strip.setPixelColor((index + 1) % strip.numPixels(), red/16, blue/16, green/16);
  strip.setPixelColor(index % strip.numPixels(), red/32, blue/32, green/32);
  strip.show();
}

// See https://en.wikipedia.org/wiki/Web_colors
void display_rainbow_12(int brightness) {
   int low=5, low_med=20, med=70, med_high=110, high=150, very_high=200, maximum=255;
    // scale the numbers to the appropriate brightness levels
    low        = map(low,       0, low,       1, brightness);
    low_med    = map(low_med,   0, low_med,   1, brightness);
    med        = map(med,       0, med,       1, brightness);
    med_high   = map(med_high,  0, med_high,  1, brightness);
    high       = map(high,      0, high,      1, brightness);
    very_high  = map(very_high, 0, very_high, 1, brightness);
    maximum    = map(maximum,   0, maximum,   1, brightness);
   reset_LED_memory();
   int np = strip.numPixels();
   strip.setPixelColor(index,     maximum, 0,       0);      // make the 1st pixel red
   strip.setPixelColor(index + 1, maximum, maximum, 0);     // make the 2nd pixel yellow
   strip.setPixelColor(index + 2, 0, maximum, 0);     // make the 3rd pixel green
   strip.setPixelColor(index + 3, 0, maximum, maximum); // make the 4th pixel white
   strip.setPixelColor(index + 4, maximum, maximum, 0);   // make the 5th pixel yellow
   strip.setPixelColor(index + 5, 0, maximum, maximum);   // make the 6th pixel aqua
   strip.setPixelColor(index + 6, maximum, 0, maximum);   // make the 7th pixel fuchsia
   strip.setPixelColor(index + 7, very_high, high, 0);   // make the 8th pixel orange (changed from 255, 165, 0)
   strip.setPixelColor(index + 8, med, 0, med);     // make the 9th pixel purple
   // these are all white?
   strip.setPixelColor(index + 9,  low, med, low); // make the 10th pixel DarkSeaGreen
   strip.setPixelColor(index + 10, high, med, low_med);  // make the 11th pixel Goldenrod
   strip.setPixelColor(index + 11, low, high, high);  // make the 11th pixel Aquamarine
   strip.show(); // must use to refresh the strip
}

// Fill the dots one after the other with a color
void display_color_wipe(int brightness, int red, int blue, int green) {
  reset_LED_memory();
  red = map(red, 0, 255, 1, brightness);
  green = map(green, 0, 255, 1, brightness);
  blue = map(blue, 0, 255, 1, brightness); 
  for(int i=0; i <= index; i++) 
      strip.setPixelColor(i, red, green, blue); 
  strip.show();
}

// wipe right and then go back - we need a counter
void display_over_and_back(int brightness, int red, int blue, int green) {
  int double_index = index % (strip.numPixels() * 2);
  reset_LED_memory();
  red = map(red, 0, 255, 1, brightness);
  green = map(green, 0, 255, 1, brightness);
  blue = map(blue, 0, 255, 1, brightness);
  // Serial.print(" double_index=");
  // Serial.println(double_index);
  if (double_index < strip.numPixels()) {
       // double is 0 to 11
        for(int i=0; i < index; i++)  // just like color whipe
            strip.setPixelColor(i, red, green, blue);   
      }
  else {
    // double is 12 to 23 - at 12 we want to start going backwards
    for(int i=strip.numPixels() - index - 1; i > -1; i--)
       strip.setPixelColor(i, red, green, blue);
  }
  strip.show();
}

// Larson Scanner - aka Cylon pattern
void display_cylon(int brightness, int red, int green, int blue) {
  int np = strip.numPixels();
  int steps = np - 5; // how many steps to the right we move
  int upcounter = (index % (steps * 2)); // counts double the steps
  int offset;
  // needs to go up to 8 and down
  if (upcounter <= steps)
    offset = upcounter;
    else offset = steps - (upcounter - steps) ;
  //Serial.print("upcounter=");
  //Serial.print(upcounter);
  //Serial.print(" offset=");
  //Serial.println(offset);
  float low=.05, med=.2;
  reset_LED_memory();
  red = map(red, 0, 255, 1, brightness);
  green = map(green, 0, 255, 1, brightness);
  blue = map(blue, 0, 255, 1, brightness);
  strip.setPixelColor( offset    % np, (int)(red*low), (int)(green*low), (int)(blue*low)); // first pixel
  strip.setPixelColor((offset+1) % np, (int)(red*med), (int)(green*med), (int)(blue*med)); // second pixel med
  strip.setPixelColor((offset+2) % np, red, green, blue); // third center pixel high
  strip.setPixelColor((offset+3) % np, (int)(red*med),(int)(green*med), (int)(blue*med)); // fourth pixel med
  strip.setPixelColor((offset+4) % np, (int)(red*low), (int)(green*low), (int)(blue*low)); // fight pixel low 
  strip.show();
}

// Slightly different, this makes the rainbow equally distributed throughout
// todo - add a brightness
void display_rainbow_cycle() {
  uint16_t i;
    for(i=0; i< strip.numPixels(); i++) {
      strip.setPixelColor( (i + index) % strip.numPixels(), Wheel(((i * 256 / strip.numPixels()) ) & 255));
    }
    strip.show();
}
 
// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  if(WheelPos < 85) {
   return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  } else if(WheelPos < 170) {
   WheelPos -= 85;
   return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else {
   WheelPos -= 170;
   return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
}

// display a glowing candel by updating 10 pixels
void init_candle(int brightness) {
  if (candle_initilize == 1)
    {
     uint8_t red = brightness; // base brightness of the yellow 
     uint8_t green = brightness * .5; // brightness of the green 
     for (int i=0; i<strip.numPixels(); i++) {
        strip.setPixelColor(i, red, green, 0);
     }
     strip.show();
    }
}

// display a glowing candel by updating 10 pixels
void display_candle(int brightness) {
   set_random_flame(brightness, 10);
   strip.show();
}

void set_random_flame(int brightness, int count) {
  for (int i=0; i<count; i++) {
   uint8_t base; // base brightness of the yellow 
   uint8_t green; // brightness of the green 
   uint8_t red;  // add a bit for red
   base = 50 + random(2); // the base brightness of the current update
   green = map(base, 0, 255, 1, brightness * .8); // update green to 80% of the base brightness
   red = map(base, 0, 255, 1, brightness);  // make the read be 100% of the base
   strip.setPixelColor(random(strip.numPixels()), red, green, 0);
  }
}

// display a random color at a random index pixel and conditionally erase the prior art
void display_random_colors(int brightness, int erase) {
  int index, red, green, blue;
  index = random(strip.numPixels());
  if (erase==1) reset_LED_memory();
  red = map(random(255), 0, 255, 5, brightness);
  green = map(random(255), 0, 255, 5, brightness);
  blue = map(random(255), 0, 255, 5, brightness);   
  strip.setPixelColor(index, red, green, blue);
  strip.show();
}

// display a randome color at a random index
// random_pos is a global variable
void display_random_walk(int brightness, int red, int green, int blue) {
  reset_LED_memory();
  int move_dir = random(3) - 1; // 0, 1 or 2
  // Serial.print("move_dir=");
  // Serial.print(move_dir);
  random_pos = ( random_pos + move_dir ) % strip.numPixels();
  // Serial.print(" random_pos=");
  // Serial.println(random_pos);
  red = map(red, 0, 255, 5, brightness);
  green = map(green, 0, 255, 5, brightness);
  blue = map(blue, 0, 255, 5, brightness);   
  strip.setPixelColor(random_pos, red, green, blue);
  strip.show();
}

// Theatre-style crawling lights 
void display_theater_chase(int brightness, int red, int green, int blue) {
  int offset = index % 6; // where we start
  red = map(red, 0, 255, 1, brightness);
  green = map(green, 0, 255, 1, brightness);
  blue = map(blue, 0, 255, 1, brightness);
  reset_LED_memory(); // make everything 0
  // draw every 6th pixel on
   for (int i=0; i < strip.numPixels(); i=i+6) {
      strip.setPixelColor(i + offset, red, green, blue);    //turn every third pixel on
    }
  strip.show();
  delay(3);  // for slowing down the top speed
}

// Theatre-style crawling lights 
void display_theater_chase_rainbow(int brightness, int red, int green, int blue) {
  int offset = index % 6; // where we start
  red = map(red, 0, 255, 1, brightness);
  green = map(green, 0, 255, 1, brightness);
  blue = map(blue, 0, 255, 1, brightness);
  reset_LED_memory(); // make everything 0
  // draw every 6th pixel on
   for (int i=0; i < strip.numPixels(); i=i+6) {
      strip.setPixelColor(i + offset, red, green, blue);    //turn every third pixel on
    }
  strip.show();
  delay(3);  // for slowing down the top speed
}

void display_sparkle(int brightness) {
  int randomIndex = random(strip.numPixels()); // a random number from 0 to 11
    reset_LED_memory();
    strip.setPixelColor(randomIndex, brightness, brightness, brightness);
    strip.show();
}

void reset_LED_memory() {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, 0);
  }
}

void print_debug() {
  Serial.print("Mode=");
    Serial.print(mode);
    
    Serial.print(" Brigh=");
    Serial.print(brightness);
    
    Serial.print(" Speed=");
    Serial.print(speed_value);

    Serial.print(" Delay=");
    Serial.print(loop_delay);
    
    Serial.print(" Ind=");
    Serial.println(index);
};
