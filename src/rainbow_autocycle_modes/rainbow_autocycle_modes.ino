// this version automatically cycles through each of the modes.
#include <Adafruit_NeoPixel.h>

#define LEDPIN 12 // connect the Data In pin
#define NUMBER_PIEXELS 12// connect the Data In pin
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);
// this constant won't change:
const int  buttonPin = 3;    // the pin that the pushbutton is attached to
// must be 2 or 3 to use interupts
const int ledPin = 13;       // the pin that the LED is attached to to show mode changes

// Variables will change:
volatile int newMode = 1; // the interrupts set this to 1 to indicate that we have a new mode on the way
int buttonPushCounter = 0;   // counter for the number of button presses
int buttonState = 1;         // current state of the button using a pull up is 1
int lastButtonState = 1;     // previous state of the button
int mode = 0; // the mode starts at 0 a cycles up to 10 and re-starts
int number_modes = 12; // the number of different modes
int waitTime = 7000; // Time to show each mode - seven seconds

void setup() {
  // initialize the button pin as a input:
  attachInterrupt(1, changeMode, RISING); // connect the mode to pin 3
  pinMode(buttonPin, INPUT_PULLUP);
  // initialize the LED as an output:
  pinMode(ledPin, OUTPUT);
  strip.begin(); // sets up the memory
  // initialize serial communication:
  Serial.begin(9600);
  Serial.println("Start");
  Serial.print(" mode: ");
  Serial.println(mode);
}

// Interrupt service routine
void changeMode(){        // Interrupt service routine
  digitalWrite(13, HIGH); // we have a new mode
  newMode = 1;
}

void loop() {

  // compare the buttonState to its previous state
  if (newMode == 1) {  
      mode = (mode + 1) % number_modes;
      digitalWrite(13, LOW); // we have incemented the mode
      Serial.print("Number of button pushes:");
      Serial.print(buttonPushCounter);
      Serial.print(" mode: ");
      Serial.println(mode);
      switch (mode) {
        case 0: rainbow7(waitTime);break;
        case 1: twinkle(waitTime);break;
        case 2: colorWipe(strip.Color(0, 255, 0), waitTime);break; // Green
        case 3: colorWipe(strip.Color(0, 0, 255), waitTime);break; // Blue
        case 4: rainbow(10);break;
        case 5: rainbowCycle(5);break;
        case 6: candle(waitTime);break;
        case 7: randomRGB(waitTime);break;
        case 8: randomColor(waitTime);break;
        case 9: candle(waitTime);break;
        case 10: theaterChaseRainbow(100);break;
        case 11: colorWipe(strip.Color(255, 0, 0), waitTime);break; // Red
    }
    
    // Delay a little bit to avoid bouncing
    delay(50);
    
  }


    
  // turns on the LED every other button pushes by
  if (buttonPushCounter % 2) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }

}

// See https://en.wikipedia.org/wiki/Web_colors
void mainMenu() {
   strip.setPixelColor(0, 255, 0, 0);     // make the 1st pixel red
   strip.setPixelColor(1, 0, 255, 0);     // make the 2nd pixel green
   strip.setPixelColor(2, 0, 0, 255);     // make the 3rd pixel blue
   strip.setPixelColor(3, 255, 255, 255); // make the 4th pixel white
   strip.setPixelColor(4, 255, 255, 0);   // make the 5th pixel yellow
   strip.setPixelColor(5, 0, 255, 255);   // make the 6th pixel aqua
   strip.setPixelColor(6, 255, 0, 255);   // make the 7th pixel fuchsia
   strip.setPixelColor(7, 200, 130, 0);   // make the 8th pixel orange (changed from 255, 165, 0)
   strip.setPixelColor(8, 80, 0, 80);     // make the 9th pixel purple
   strip.setPixelColor(9, 143, 188, 143); // make the 10th pixel DarkSeaGreen
   strip.setPixelColor(10, 218, 165, 32);  // make the 11th pixel Goldenrod
   strip.setPixelColor(11, 127, 255, 212);  // make the 11th pixel Aquamarine
   strip.show(); // must use to refresh the strip
}

// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i < wait/20; i++) {
    for(uint16_t j=0; j<strip.numPixels(); j++) {
        strip.setPixelColor(j, c);
        strip.show();
        delay(50);
    }
  }
}
 
void rainbow(uint8_t wait) {
  uint16_t i, j;
 
  for(j=0; j<256; j++) {
    for(i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel((i+j) & 255));
    }
    strip.show();
    delay(wait);
  }
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

void candle(int waitTime) {
   uint8_t green; // brightness of the green 
   uint8_t red;  // add a bit for red
   for (int i=0; i<waitTime/10; i++) {
       green = 50 + random(155);
       red = green + random(50);
       strip.setPixelColor(random(strip.numPixels()), red, green, 0);
       strip.show();
       delay(10);
    }
}

// a seven segment rainbow with red on the highest pixel
void rainbow7(uint16_t wait) {
  int np = strip.numPixels();  // we use the modulo function with this
  
  for (int i=0; i<strip.numPixels(); i++) { 
      strip.setPixelColor(i     % np, 0, 0, 0); // off
      strip.setPixelColor((i+1) % np, 25, 0, 25); // violet
      strip.setPixelColor((i+2) % np, 255, 0, 255); // indigo
      strip.setPixelColor((i+3) % np, 0, 0, 150); // blue
      strip.setPixelColor((i+4) % np, 0, 150, 0); // green
      strip.setPixelColor((i+5) % np, 255, 255, 0); // yellow
      strip.setPixelColor((i+6) % np, 110, 70, 0); // orange
      strip.setPixelColor((i+7) % np, 150, 0, 0); // red
      strip.setPixelColor((i+8) % np, 0, 0, 0); // off
      strip.setPixelColor((i+10) % np, 0, 0, 0); // off
      strip.setPixelColor((i+11) % np, 0, 0, 0); // off
      strip.show();
      delay(wait/100);
  }
}


void randomRGB(uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
     strip.setPixelColor(i, random(255), random(255), random(255));
     strip.show();
     delay(wait);
  }
}

void randomColor(uint8_t wait) {
int newColor;
  for(uint16_t i=0; i<strip.numPixels(); i++) {
     newColor = Wheel(random(255));
     strip.setPixelColor(i, newColor);
     strip.show();
     delay(wait);
  }
}

//Theatre-style crawling lights with rainbow effect
void theaterChaseRainbow(uint8_t wait) {
  for (int j=0; j < 256; j=j+32) {     // cycle all 256 colors in the wheel
    for (int q=0; q < 3; q++) {
        for (int i=0; i < strip.numPixels(); i=i+3) {
          strip.setPixelColor(i+q, Wheel( (i+j) % 255));    //turn every third pixel on
        }
        strip.show();
        delay(wait);
        for (int i=0; i < strip.numPixels(); i=i+3) {
          strip.setPixelColor(i+q, 0);        //turn every third pixel off
        }
    }
  }
}

void twinkle(uint8_t wait) {
  int random_index;
  for (int i=0; i < wait/100; i++) {
    strip.setPixelColor(i, 0, 0, 0);
    random_index = random(strip.numPixels()); // get a random number from 0 to Num Pixels
    strip.setPixelColor(random_index, 255, 255, 255); // turn a random pixel on
    strip.show();
    delay(100);
    strip.setPixelColor(random_index, 0, 0, 0); // turn it off
  }
}


