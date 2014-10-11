#include <Adafruit_NeoPixel.h>

// Sample code for using a breadboard Arduino to drive WS2812B LED strip with Adafruit NeoPixel library
// I got mine on e-bay:
// http://www.ebay.com/itm/181268207260?ssPageName=STRK:MEWNX:IT&_trksid=p3984.m1439.l2649
// Note - colors for data and ground vary
// I used a 16MHZ Crystal Oscilator
#define LEDPIN 10 // connect the Data In pin
#define NUMBER_PIEXELS 12// connect the Data In pin
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);
// this constant won't change:
const int  buttonPin = 9;    // the pin that the pushbutton is attached to
const int ledPin = 13;       // the pin that the LED is attached to to show mode changes

// Variables will change:
int buttonPushCounter = 0;   // counter for the number of button presses
int buttonState = 1;         // current state of the button using a pull up is 1
int lastButtonState = 1;     // previous state of the button
int mode = 0; // the mode starts at 0 a cycles up to 10 and re-starts
int number_modes = 5; // the number of different modes

void setup() {
  // initialize the button pin as a input:
  pinMode(buttonPin, INPUT_PULLUP);
  // initialize the LED as an output:
  pinMode(ledPin, OUTPUT);
  
  // we assume that interrupt 0 is on pin 2
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  attachInterrupt(0, modeChange, FALLING );
  attachInterrupt(1, modeChange, FALLING );
  // initialize serial communication:
  Serial.begin(9600);
  Serial.println("Start");
  Serial.print(" mode: ");
  Serial.println(mode);
  mainMenu(); // show the initial menu
}

void modeChange() {
  Serial.print("In mode change");
  Serial.println(mode);
  delay(50);
  mode = (mode + 1) % number_modes;
  switch (mode) {
        case 0: mainMenu();break;
        case 1: colorWipe(strip.Color(255, 0, 0), 50);break; // Red
        case 2: colorWipe(strip.Color(0, 255, 0), 50);break; // Green
        case 3: colorWipe(strip.Color(0, 0, 255), 50);break; // Blue
        case 4: rainbow(20);break;
        case 5: rainbowCycle(20);break;
     }
}

void loop() {
  // read the pushbutton input pin:
  buttonState = digitalRead(buttonPin);

  // compare the buttonState to its previous state
  if (buttonState != lastButtonState) {
    // if the state has changed, increment the counter
    if (buttonState == HIGH) {
      // if the current state is HIGH then the button
      // wend from off to on:
      buttonPushCounter++;
      mode = (mode + 1) % number_modes;
      Serial.print("Number of button pushes:");
      Serial.print(buttonPushCounter);
      Serial.print(" mode: ");
      Serial.println(mode);
      switch (mode) {
        case 0: mainMenu();break;
        case 1: colorWipe(strip.Color(255, 0, 0), 50);break; // Red
        case 2: colorWipe(strip.Color(0, 255, 0), 50);break; // Green
        case 3: colorWipe(strip.Color(0, 0, 255), 50);break; // Blue
        case 4: rainbow(20);break;
        case 5: rainbowCycle(20);break;
     }
    }
    
    // Delay a little bit to avoid bouncing
    delay(50);
    
    
  }
  // save the current state as the last state,
  //for next time through the loop
  lastButtonState = buttonState;

    
  // turns on the LED every other button pushes by
  if (buttonPushCounter % 2) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }

}

// See https://en.wikipedia.org/wiki/Web_colors
void mainMenu() {
   strip.begin(); // sets up the memory
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
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
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







