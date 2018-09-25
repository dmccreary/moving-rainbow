




/* LED Strip with Two Buttons 

This lab allows you to change display "modes" of a WS-2811B addressible LED Strip (NeoPixels)
To use this program hook up two momentary push buttons from pins 2 and 3 to Ground (GND).  
One button will increment the display mode (an integer), the other will decrment the mode.
You MUST use pins 2 and 3 because they are the only Interrupt pins on the Arduino (Uno, Nano).
Remember to connect the other ends of the momentary push buttons to GND.  We use the internal
Arduino 20K resistors to pull up the signals to 5 volts when the buttons are open.
Connect the LED Strip to to power, ground and pin 12 in the lower left corner of the Nano.

*/

#include <Adafruit_NeoPixel.h>

int mode = 0; // This is the "mode" of the device.  It starts at 0 and gets incremented or decremented
int newModeInc = 0; // Set to 1 by the ISR when the Green Increment Mode button is pressed.
int newModeDec = 0; // Set to 1 by the ISR when the Red Decrment Mode button is pressed.
long lastDebounceTime = 0;  // the last time the output pin was toggled
long debounceDelay = 150;   // the debounce time; increase if the output flickers

const int LED_STRIP_PIN = 12; // Connect the Data pin of the LED strip here
const int NUMBER_PIXELS = 30;


; // Number of pixels in the LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LED_STRIP_PIN, NEO_GRB + NEO_KHZ800);

int modeCount = 17; // The number of display modes, we mode the mode to get the actual mode
int mainLoopCount = 0;  // The number of times we go through the main loop

void setup()
{
  pinMode(13, OUTPUT);     // Pin 13 is output to which an LED is connected
  digitalWrite(13, LOW);   // Make pin 13 low, switch LED off
  pinMode(2, INPUT_PULLUP);     // Pin 2 is input to which a switch is connected = INT0
  pinMode(3, INPUT_PULLUP);    // Pin 3 is input to which a switch is connected = INT1
  attachInterrupt(0, changeModeInc, FALLING  ); // pin 2
  attachInterrupt(1, changeModeDec, FALLING  ); // pin 3
  Serial.begin(9600);
  strip.begin(); // sets up the memory for the LED strip
  Serial.println("Start");
  Serial.print("Mode=");
  Serial.println(mode, DEC);
  rainbow7();
  delay(100);
  newModeInc=0; // must be reset to 0 at the end of setup!
  newModeDec=0;
}

void loop() {
  if (newModeInc == 1) {
    if ((millis() - lastDebounceTime) > debounceDelay) {
      mode++;
      mode = mode % modeCount;
      Serial.print("Inc Mode=");
      Serial.println(mode, DEC);
      digitalWrite(13, LOW);
      newModeInc = 0;
    }
    else {
    }
  };
  
  if (newModeDec == 1) {
    if ((millis() - lastDebounceTime) > debounceDelay) {
      if (mode == 0) {
        mode = modeCount - 1;
      } else {
        mode--;
      }
      Serial.print("Dec Mode=");
      Serial.println(mode, DEC);
      digitalWrite(13, LOW);
      newModeDec = 0;
    }
    
  };
  
  // select the mode
  switch (mode) {
        case 0:rainbow7();break; // 7 pixel rainbow
        case 1: dot(255, 0, 0);break; // red
        case 2: dot(0, 255, 0);break; // green
        case 3: dot(0, 0, 255);break; // blue
        case 4: colorWipe(255 ,0, 0);break;
        case 5: colorWipe(0, 255, 0);break;
        case 6: colorWipe(0, 0, 255);break;
        case 7: swoosh(255 ,0, 0);break;
        case 8: swoosh(0, 255, 0);break;
        case 9: swoosh(0, 0, 255);break;
        case 10: theaterChase(255, 0, 0);break;
        case 11: theaterChase(0, 255, 0);break;
        case 12: theaterChase(0, 0, 255);break;
        case 13: rainbowSlide();break;
        case 14: candle();break;
        case 15: randomColor();break;
        case 16: sparkle();break;
     }
  delay(50
  ); // keep this pattern for 1/10th of a second
  mainLoopCount++;
}  

// Interrupt service routine - keep this fast
void changeModeInc(){        
  digitalWrite(13, HIGH); // show we have a new mode
  newModeInc = 1; // indicate we have a new increment mode
  lastDebounceTime = millis(); // record when we got the interrupt for debouncing
}

// Interrupt service routine
void changeModeDec(){        
  digitalWrite(13, HIGH); //  show we have a new mode
  newModeDec = 1; // indicate we have a new increment mode
  lastDebounceTime = millis(); // record when we got the interrupt for debouncing
}

// move a dot
void dot(int red, int blue, int green) {
  int index = mainLoopCount % strip.numPixels();
  clear();
  strip.setPixelColor(index, red, blue, green);
  strip.show();
}

void colorWipe(int red, int blue, int green) {
  int index = mainLoopCount % strip.numPixels();
  if (index == 0) {
    clear();
  }
 else
    for(uint16_t i=0; i<=index; i++) {
      strip.setPixelColor(i, red, blue, green);
    }
  strip.show();
}

// make a single color appear to move as a comet flying by
void swoosh(int red, int blue, int green) {
  int n = strip.numPixels();
  int index = mainLoopCount % n;
  clear();
  strip.setPixelColor((index + 5) % n, red, blue, green);
  strip.setPixelColor((index + 4) % n, red / 1.5, blue / 1.5, green / 1.5);
  strip.setPixelColor((index + 3) % n, red / 2, blue/ 2, green/ 2);
  strip.setPixelColor((index + 2) % n, red / 4, blue/ 4, green/ 4);
  strip.setPixelColor((index + 1) % n, red / 8, blue/ 8, green/ 8);
  strip.setPixelColor((index) % n, red / 16, blue/ 16, green/ 16);
  
  strip.show();
}

// draw a seven segment rainbow on the LED strip with red on the highest pixel
// i is the index of where to start
// strip is the LED strip
void rainbow7() {
    int i = mainLoopCount;
    int np = strip.numPixels();  // we use the modulo function with this
    strip.setPixelColor(i     % np, 0, 0, 0); // off
    strip.setPixelColor((i+1) % np, 25, 0, 25); // violet
    strip.setPixelColor((i+2) % np, 255, 0, 255); // indigo
    strip.setPixelColor((i+3) % np, 0, 0, 150); // blue
    strip.setPixelColor((i+4) % np, 0, 150, 0); // green
    strip.setPixelColor((i+5) % np, 255, 255, 0); // yellow
    strip.setPixelColor((i+6) % np, 110, 70, 0); // orange
    strip.setPixelColor((i+7) % np, 150, 0, 0); // red
    // erase the rest
    strip.setPixelColor((i+8) %np , 0, 0, 0);
    strip.setPixelColor((i+9) %np , 0, 0, 0);
    strip.setPixelColor((i+10) %np , 0, 0, 0);
    strip.setPixelColor((i+11) %np , 0, 0, 0);
    strip.show();
}

void rainbowSlide() {
    for(int i=0; i< strip.numPixels(); i++)
    {
        strip.setPixelColor((i + mainLoopCount) % strip.numPixels(), Wheel(((i * 256 / strip.numPixels()) + mainLoopCount) & 255));
    }
    strip.show();
}

void randomColor() {
  int randomIndex = random(strip.numPixels()); // a number from 0 to 11
    clear();
    strip.setPixelColor(randomIndex, Wheel(random(255)));
    strip.show();
}

void sparkle() {
  int randomIndex = random(strip.numPixels()); // a number from 0 to 11
    clear();
    strip.setPixelColor(randomIndex, 10, 10, 10);
    strip.show();
}

void clear() {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, 0);
      strip.show();
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

void candle() {
   uint8_t green; // brightness of the green 
   uint8_t red;  // add a bit for red
   for(uint8_t i=0; i<100; i++) {
     green = 50 + random(155);
     red = green + random(50);
     strip.setPixelColor(random(strip.numPixels() - 1), red, green, 0);
     strip.show();
     delay(5);
  }
}

void theaterChase(int red, int blue, int green) {
int index = mainLoopCount % strip.numPixels();
for(int i=0; i < strip.numPixels(); i++) {
      if ((i + index) % 3 == 0)
      {
          strip.setPixelColor(i, red, green, blue);
      }
      else
      {
          strip.setPixelColor(i, 0, 0, 0);
      }
  }
  strip.show();
}
