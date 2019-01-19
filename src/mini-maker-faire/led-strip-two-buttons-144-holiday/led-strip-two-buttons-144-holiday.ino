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
long debounceDelay = 150;   // the debounce time in ms; increase if the output flickers

const int LED_STRIP_PIN = 12; // Connect the Data pin of the LED strip here
const int NUMBER_PIXELS = 144;


; // Number of pixels in the LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LED_STRIP_PIN, NEO_GRB + NEO_KHZ800);

int modeCount = 18; // The number of display modes, we mode the mode to get the actual mode
int mainLoopCount = 0;  // The number of times we go through the main loop
int mainLoopDelay = 30; // The delay at the end of the main loop - make it a little faster for longer strips

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
  
// catch the interrupts
  if (newModeInc == 1) {
    if ((millis() - lastDebounceTime) > debounceDelay) {
      mode++;
      mode = mode % modeCount;
      newModeInc = 0;
    }
  };
  
  if (newModeDec == 1) {
    if ((millis() - lastDebounceTime) > debounceDelay) {
      mode--;
      if (mode < 0) mode = modeCount - 1;
      newModeDec = 0;
    }
  };
  
  // select the mode
  switch (mode) {
        case 0: rainbow7();break; // 7 pixel rainbow
        case 1: dot(255, 0, 0);break; // red
        case 2: dot(0, 255, 0);break; // green
        case 3: dot(0, 0, 255);break; // blue
        case 4: green_red(1);break;
        case 5: green_red(2);break;
        case 6: green_red(3);break;
        case 7: swoosh(255 ,0, 0);break;
        case 8: swoosh(0, 255, 0);break;
        case 9: swoosh(0, 0, 255);break;
        case 10: theaterChase(255, 0, 0);break;
        case 11: theaterChase(0, 255, 0);break;
        case 12: theaterChase_red_green();break;
        case 13: rainbowSlide();break;
        case 14: candle();break;
        case 15: randomColor();break;
        case 16: sparkle();break;
        case 17: all_one_color();break;
     }
     
  delay(mainLoopDelay); // keep this pattern on for this time
  mainLoopCount++;
}

// Interrupt service routine - keep this fast
void changeModeInc() {        
  newModeInc = 1; // indicate we have a new increment mode
  lastDebounceTime = millis(); // record when we got the interrupt for debouncing
}

// Interrupt service routine
void changeModeDec( ){        
  newModeDec = 1; // indicate we have a new decrement mode
  lastDebounceTime = millis(); // record when we got the interrupt for debouncing
}

// move a dot
void dot(int red, int blue, int green) {
  int index = mainLoopCount % strip.numPixels();
  strip.setPixelColor(index, 0, 0, 0);
  strip.setPixelColor(index+1, red, blue, green);
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

  strip.setPixelColor(index + 6, red, blue, green);
  strip.setPixelColor(index + 5, red / 1.5, blue / 1.5, green / 1.5);
  strip.setPixelColor(index + 4, red / 2, blue/ 2, green/ 2);
  strip.setPixelColor(index + 3, red / 4, blue/ 4, green/ 4);
  strip.setPixelColor(index + 2, red / 8, blue/ 8, green/ 8);
  strip.setPixelColor(index + 1, red / 16, blue/ 16, green/ 16);
  strip.setPixelColor(index, 0, 0, 0);
  
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
    strip.setPixelColor((i+3) % np, 0, 0, 255); // blue
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

void green_red(int mode) {
    int i = mainLoopCount;
    int np = strip.numPixels();  // we use the modulo function with this
    if (mode==1) {
      strip.setPixelColor(i     % np, 0,   0, 0); // off
      strip.setPixelColor((i+1) % np, 0,  10, 0); // very light green
      strip.setPixelColor((i+2) % np, 0,  20, 0); // indigo
      strip.setPixelColor((i+3) % np, 0,  30, 0); // blue
      strip.setPixelColor((i+4) % np, 0,  50, 0); // green
      strip.setPixelColor((i+5) % np, 0,  75, 0); // yellow
      strip.setPixelColor((i+6) % np, 0, 120, 0); // orange
      strip.setPixelColor((i+7) % np, 0, 180, 0); // red
      strip.setPixelColor((i+8) % np, 0, 225, 0); // red
      // erase the rest
      strip.setPixelColor((i+8) %np , 0, 0, 0);
      strip.show();
    }

    if (mode==2) {
      strip.setPixelColor(i     % np, 0,   0, 0); // off
      strip.setPixelColor((i+1) % np, 10,  0, 0); // very light green
      strip.setPixelColor((i+2) % np, 20,  0, 0);
      strip.setPixelColor((i+3) % np, 30,  0, 0);
      strip.setPixelColor((i+4) % np, 50,  0, 0);
      strip.setPixelColor((i+5) % np, 75,  0, 0);
      strip.setPixelColor((i+6) % np, 120, 0, 0);
      strip.setPixelColor((i+7) % np, 180, 0, 0); 
      strip.setPixelColor((i+8) % np, 255, 0, 0); // bright green
      // erase the rest
      strip.setPixelColor((i+8) %np , 0, 0, 0);
      strip.show();
    }

    if (mode==3) {
      strip.setPixelColor(i     % np, 0,   0, 0); // off
      strip.setPixelColor((i+1) % np, 10,  0, 0); // very light red
      strip.setPixelColor((i+2) % np, 20,  0, 0);
      strip.setPixelColor((i+3) % np, 30,  0, 0);
      strip.setPixelColor((i+4) % np, 50,  0, 0);
      strip.setPixelColor((i+5) % np, 75,  0, 0);
      strip.setPixelColor((i+6) % np, 120, 0, 0);
      strip.setPixelColor((i+7) % np, 180, 0, 0);
      strip.setPixelColor((i+8) % np, 225, 0, 0);
      // erase the rest
      strip.setPixelColor((i+8) %np , 0, 0, 0);

      strip.setPixelColor(np - i    % np, 0,   0, 0); // off
      strip.setPixelColor(np -(i+1) % np, 0,  10, 0); // very light red
      strip.setPixelColor(np -(i+2) % np, 0,  20, 0);
      strip.setPixelColor(np -(i+3) % np, 0,  30, 0);
      strip.setPixelColor(np -(i+4) % np, 0,  50, 0);
      strip.setPixelColor(np -(i+5) % np, 0,  75, 0);
      strip.setPixelColor(np -(i+6) % np, 0, 120, 0);
      strip.setPixelColor(np -(i+7) % np, 0, 180, 0);
      strip.setPixelColor(np -(i+8) % np, 0, 255, 0);
      // erase the rest
      strip.setPixelColor((i+8) %np , 0, 0, 0);
      strip.show();
      
      strip.show();
    }
}

void rainbowSlide() {
    for(int i=0; i< strip.numPixels(); i++) {
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

void all_one_color() {
int color = Wheel(mainLoopCount % 256);
  for (int i=0; i<strip.numPixels(); i++) {
    strip.setPixelColor(i, color);
  }
  strip.show();
}

void candle() {
   uint8_t green; // brightness of the green 
   uint8_t red;  // add a bit for red
   // make 20 random pixels flicker
   for (char i=0; i<10; i++) {
     green = 50 + random(155);
     red = green + random(50);
     strip.setPixelColor(random(strip.numPixels()), red, green, 0);
   }
   strip.show();
}

// turn every 4th pixel on and move the offset
void theaterChase(int red, int blue, int green) {
int index = mainLoopCount % strip.numPixels();
for(int i=0; i < strip.numPixels(); i++) {
      if ((i + index) % 5 == 0)
      {
          strip.setPixelColor(i, red, green, blue);
      }
      else
      {
          strip.setPixelColor(i, 0, 0, 0);
      }
  }
  delay(mainLoopDelay * 3);
  strip.show();
}

// turn every 4th pixel on and move the offset
void theaterChase_red_green() {
int index = mainLoopCount % strip.numPixels();
for(int i=0; i < strip.numPixels(); i++) {
      if ((i + index) % 10 == 0)
      {
          strip.setPixelColor(i, 50, 0, 0);
      } else
      if ((i + index) % 5 == 0)
      {
          strip.setPixelColor(i, 0, 50, 0);
      }
      else
      {
          strip.setPixelColor(i, 0, 0, 0);
      }
  }
  delay(mainLoopDelay * 3);
  strip.show();
}
