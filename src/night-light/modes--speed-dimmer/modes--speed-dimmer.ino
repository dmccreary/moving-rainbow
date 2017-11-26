/*
 * Arduino Moving Rainbow Kit Mode Demo
 * For use with an Arduino with an WS2812 LED strip, a mode button and two potentiometers
 * Dan McCreary
 * Nov. 2017
 */
#include <Adafruit_NeoPixel.h>
#include <Encoder.h>

#include <avr/interrupt.h>

// Input pins
#define MODE_PIN 2 // pull down to groud to get a new mode
#define BRIGHTNESS_POT_PIN A0 // connect center pin of a potentiometer, sides go to +5 and GND
#define SPEED_POT_PIN A1 // connect center pin of a potentiometer, sides go to +5 and GND

// Output pin
#define LED_PIN 12 // connect the Data In pin

#define NUMBER_PIXELS 12// connect the Data In pin
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LED_PIN, NEO_GRB + NEO_KHZ800);

// hook up two momentary push buttons to pin and keep them in memory
volatile int newMode = 0; // the interrupts set this to 1 to indicate that we have a new mode on the way
volatile int mode = 0; // The starting mode.  This gets incremented each button press
const int modeCount = 27; // The number of display modes

// used for debouncing the mode button
long lastDebounceTime = 0;  // the last time the output pin was toggled
long debounceDelay = 60;   // the debounce time; increase if the output flickers

// these variables updated with each loop
int brightness = 512; // The brightness value from 0 to 1023
int speed_value =  512; // The inverse of speed
int loop_delay =  512; // The inverse of speed
int index = 0; // the index of where we are drawing to the LED strip
long counter = 0; // number of times through the loop
int random_pos = strip.numPixels() / 2; // random index position for random walker

void setup() {
  strip.begin(); // sets up the memory for the LED strip
  pinMode(LED_PIN, OUTPUT);     // Pin 13 is output to which an LED is connected
  pinMode(BRIGHTNESS_POT_PIN, INPUT);
  pinMode(SPEED_POT_PIN, INPUT);

  pinMode(MODE_PIN, INPUT_PULLUP);	// Pin 2 is input to which a button to GND is connected normally HIGH
  digitalWrite(MODE_PIN, HIGH);
  attachInterrupt(0, change_mode, RISING); // connect the mode to pin 2
  Serial.begin(9600);
  Serial.print("LED on pin ");
  Serial.println(LED_PIN);
  Serial.print("Mode button on pin ");
  Serial.println(MODE_PIN);
  Serial.print("Brightness on pin ");
  Serial.println(BRIGHTNESS_POT_PIN);
  Serial.print("Brightness pot on pin ");
  Serial.println(MODE_PIN);
  Serial.println("Start Function Finished");
}

// Interrupt service routine - get in and out quickly, no printing to serial ports allowed here
void change_mode(){        
  newMode = 1;
  lastDebounceTime = millis(); // record when we got the interrupt for debouncin
}

void loop() {
  // check to see if we should change the mode
  if (newMode == 1) {
    if ((millis() - lastDebounceTime) > debounceDelay) {
      // delay(100); // wait for the switch to settle down used to de-bounce
      // increment the mode and 
      mode = (mode + 1) % modeCount;
      Serial.print("New Mode mode=");
      Serial.println(mode, DEC);      
      newMode = 0;
    }
  }

   // select the mode
      switch (mode) {
        case 0:  display_rainbow7(brightness);break;
        case 1:  display_moving_pixel(brightness, 255, 0, 0);break; // Red dot
        case 2:  display_moving_pixel(brightness, 0, 255, 0);break; // Green
        case 3:  display_moving_pixel(brightness, 0, 0, 255);break; // Blue
        case 4:  display_comet_wrap(brightness, 255, 0, 0);break; // Red coment
        case 5:  display_comet_wrap(brightness, 0, 255, 0);break; // Blue comet
        case 6:  display_comet_wrap(brightness, 0, 0, 255);break; // Green comet
        case 7:  display_comet_wrap(brightness, 255, 255, 0);break; // Green comet
        case 8:  display_candle(brightness);break; // Candle flicker
        case 9:  display_random_colors(brightness, 0);break; // no erase
        case 10: display_random_colors(brightness, 1);break; // with erase
        case 11: display_rainbow_12(brightness);break;
        case 12: display_theater_chase(brightness, 255, 0, 0);break;
        case 13: display_theater_chase(brightness, 0, 255, 0);break;
        case 14: display_theater_chase(brightness, 0, 0, 255);break;
        case 15: display_color_wipe(brightness, 255, 0, 0);break;
        case 16: display_color_wipe(brightness, 0, 255, 0);break;
        case 17: display_color_wipe(brightness, 0, 0, 255);break;
        case 18: display_over_and_back(brightness, 255, 0, 0);break;
        case 19: display_over_and_back(brightness, 0, 255, 0);break;
        case 20: display_over_and_back(brightness, 0, 0, 255);break;
        case 21: display_cylon(brightness, 255, 0, 0);break;
        case 22: display_cylon(brightness, 0, 255, 0);break;
        case 23: display_cylon(brightness, 0, 0, 255);break;
        case 24: display_random_walk(brightness, 255, 0, 0);break;
        case 25: display_random_walk(brightness, 0, 255, 0);break;
        case 26: display_random_walk(brightness, 0, 0, 255);break;
     }
    // update the values from the pot
    brightness = analogRead(BRIGHTNESS_POT_PIN);
    brightness = map(brightness, 0, 1023, 0, 255);
    speed_value = analogRead(SPEED_POT_PIN);
    loop_delay = map(speed_value, 0, 1023, 1000, 1);  // map from 1 second to 5 milliseconds

    /*
    Serial.print("Mode=");
    Serial.print(mode);
    Serial.print(" Brightness=");
    Serial.print(brightness);
    Serial.print(" Speed=");
    Serial.print(speed_value);
    Serial.print(" Index=");
    Serial.println(index);
    */
    index = (index + 1) % NUMBER_PIXELS; // modulu the number of pixels in the LED strip
    counter++;
    delay(loop_delay);
}

// all display functions start with the string "display_"
// each display function must only draw a single pattern at the index using the brightness parameter
// index is a global variable
// the main loop does all the delays

// a seven segment rainbow with red on the highest pixel
void display_rainbow7(int brightness) {
    int low=10, med=70, med_high=110, high=150, very_high=255;
    // scale the numbers to the appropriate brightness levels
    low        = map(low,       0, low,       0, brightness);
    med        = map(med,       0, med,       0, brightness);
    med_high   = map(med_high,  0, med_high,  0, brightness);
    high       = map(high,      0, high,      0, brightness);
    very_high =  map(very_high, 0, very_high, 0, brightness);
    reset_LED_memory();
    int np = strip.numPixels();  // we use the modulo function with this shorthand
    strip.setPixelColor( index    % np, low, 0, low); // violet
    strip.setPixelColor((index+1) % np, very_high, 0, very_high); // indigo
    strip.setPixelColor((index+2) % np, 0, 0, very_high); // blue
    strip.setPixelColor((index+3) % np, 0, very_high, 0); // green
    strip.setPixelColor((index+4) % np, very_high, very_high, 0); // yellow
    strip.setPixelColor((index+5) % np, very_high, high, 0); // orange is 255, 165, 0 but looks yellow
    strip.setPixelColor((index+6) % np, very_high, 0, 0); // red 
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
   int low=10, low_med=40, med=70, med_high=110, high=150, very_high=200, maximum=255;
    // scale the numbers to the appropriate brightness levels
    low        = map(low,       0, low,       0, brightness);
    med        = map(med,       0, med,       0, brightness);
    med_high   = map(med_high,  0, med_high,  0, brightness);
    high       = map(high,      0, high,      0, brightness);
    very_high  = map(very_high, 0, very_high, 0, brightness);
    maximum    = map(maximum,   0, maximum,   0, brightness);
   reset_LED_memory();
   int np = strip.numPixels();
   strip.setPixelColor(index % np, maximum, 0, 0);     // make the 1st pixel red
   strip.setPixelColor((1 + index) % np, 0, maximum, 0);     // make the 2nd pixel green
   strip.setPixelColor((2+ index) % np, 0, 0, maximum);     // make the 3rd pixel blue
   strip.setPixelColor((3+ index) % np, maximum, maximum, maximum); // make the 4th pixel white
   strip.setPixelColor((4+ index) % np, maximum, maximum, 0);   // make the 5th pixel yellow
   strip.setPixelColor((5+ index) % np, 0, maximum, maximum);   // make the 6th pixel aqua
   strip.setPixelColor((6+ index) % np, maximum, 0, maximum);   // make the 7th pixel fuchsia
   strip.setPixelColor((7+ index) % np, very_high, high, 0);   // make the 8th pixel orange (changed from 255, 165, 0)
   strip.setPixelColor((8+ index) % np, med, 0, med);     // make the 9th pixel purple
   strip.setPixelColor((9+ index) % np, low, med, low); // make the 10th pixel DarkSeaGreen
   strip.setPixelColor((10+ index) % np, high, med, low_med);  // make the 11th pixel Goldenrod
   strip.setPixelColor((11+ index) % np, low, high, high);  // make the 11th pixel Aquamarine
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
  int double_index = counter % (strip.numPixels() * 2);
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
  int upcounter = (counter % (steps * 2)); // counts double the steps
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
void rainbowCycle(uint8_t wait) {
  uint16_t i, j;
 
  for(j=0; j<256*5; j++) { // 5 cycles of all colors on wheel
    for(i=0; i< strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
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

// display a glowing candel
void display_candle(int brightness) {
   uint8_t base; // base brightness of the yellow 
   uint8_t green; // brightness of the green 
   uint8_t red;  // add a bit for red
   base = 10 + random(245); // the base brightness of the current update
   green = map(base, 0, 255, 1, brightness * .8); // update green to 80% of the base brightness
   red = map(base, 0, 255, 1, brightness);  // make the read be 100% of the base
   strip.setPixelColor(random(strip.numPixels()), red, green, 0);
   strip.show();
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
  Serial.print("move_dir=");
  Serial.print(move_dir);
  random_pos = ( random_pos + move_dir ) % strip.numPixels();
  Serial.print(" random_pos=");
  Serial.println(random_pos);
  red = map(red, 0, 255, 5, brightness);
  green = map(green, 0, 255, 5, brightness);
  blue = map(blue, 0, 255, 5, brightness);   
  strip.setPixelColor(random_pos, red, green, blue);
  strip.show();
}

// Theatre-style crawling lights with rainbow effect
void display_theater_chase(int brightness, int red, int green, int blue) {
  red = map(red, 0, 255, 1, brightness);
  green = map(green, 0, 255, 1, brightness);
  blue = map(blue, 0, 255, 1, brightness); 
  // draw on, off, off three times

        for (int i=0; i < strip.numPixels(); i=i+3) {
          strip.setPixelColor((index+i)%strip.numPixels(), red, green, blue);    //turn every third pixel on
          strip.setPixelColor((index+i+1)%strip.numPixels(), 0);
          strip.setPixelColor((index+i+2)%strip.numPixels(), 0);

    }
  strip.show();
}

void display_rainbowSlide(int brightness) {
    for(int i=0; i< strip.numPixels(); i++)
    {
        strip.setPixelColor((i + index) % strip.numPixels(), Wheel(((i * 256 / strip.numPixels()) + index) & 255));
    }
    strip.show();
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
