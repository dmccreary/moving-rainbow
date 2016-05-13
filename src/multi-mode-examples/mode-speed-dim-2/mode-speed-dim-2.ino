/* Mode, Speed and Dimming
   Dan McCreary

Hook up two momentary push buttons to pins 2 and 3.
One button will increment the mode, one will decrment the mode
You MUST use pins 2 and 3 because they are the only Interrupt pins on the Arduino (Uno, Nano)
Connect the other ends of the momentary push buttons to GND
Note that we are using internal 20K resistors to pull up the inputs to +5 when the buttons are open
*/
#include <Adafruit_NeoPixel.h>

int mode = 3; // This is the "mode" of the device.  It starts at 0 and gets incremented or decremented
int newModeInc = 0; // the interrupts set this to 1 to indicate that we have a new increment to handle
int newModeDec = 0; // the interrupts set this to 1 to indicate that we have a new decrement to handle
long lastDebounceTime = 0;  // the last time the output pin was toggled
long debounceDelay = 200;   // the debounce time; increase if the output flickers

const int SPEED_POT = A0; // attache the center tap of a potentiometer to Analog Input A0 to control pattern speent
const int BRIGHTNESS_POT = A1; // attache the center tap of a potentiometer to Analog Input A1 to contral brightness
int speed_val = 510; // default speed
int brightness_val = 512; // default brightness

const int LED_STRIP_PIN = 12; // Connect the Data pin of the LED strip here
const int NUMBER_PIXELS = 16; // Number of pixels in the LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LED_STRIP_PIN, NEO_GRB + NEO_KHZ800);

int modeCount = 10; // The number of display modes, we mode the mode to get the actual mode
int mainLoopCount = 0;  // The number of times we go through the main loop

void setup()
{
  pinMode(13, OUTPUT);     // Pin 13 is output to which an LED is connected
  digitalWrite(13, LOW);   // Make pin 13 low, switch LED off
  pinMode(2, INPUT_PULLUP);	   // Pin 2 is input to which a switch is connected = INT0
  pinMode(3, INPUT_PULLUP);	   // Pin 3 is input to which a switch is connected = INT1
  attachInterrupt(0, changeModeInc, FALLING  ); // pin 2
  attachInterrupt(1, changeModeDec, FALLING  ); // pin 3
  Serial.begin(9600);
  strip.begin(); // sets up the memory for the LED strip
  Serial.println("Start");
  Serial.print("Mode=");
  Serial.println(mode, DEC);
}

void loop() {
  if (newModeInc == 1) {
    if ((millis() - lastDebounceTime) > debounceDelay) {
      mode++;
      mode = mode % modeCount;
      Serial.print("Inc Mode=");
      Serial.print(mode, DEC);
      digitalWrite(13, LOW);
      newModeInc = 0;
    }
    else {
    }
  };
  
  if (newModeDec == 1) {
    if ((millis() - lastDebounceTime) > debounceDelay) {
      mode--;
      mode = mode % modeCount;
      Serial.print("Dec Mode=");
      Serial.print(mode, DEC);
      digitalWrite(13, LOW);
      newModeDec = 0;
    }
  };
  
  
  speed_val = analogRead(SPEED_POT); // get the value of speed from the Pot
  Serial.print("Speed=");
  Serial.print(speed_val, DEC);
  brightness_val = analogRead(BRIGHTNESS_POT);
  // scale brightness to 1 to 255
  brightness_val = map(brightness_val, 0, 1023, 1, 255);
  Serial.print(" Bright=");
  Serial.println(brightness_val, DEC);
  // the delay is 1024 minus the speed
  delay(1024 - speed_val);
  
  // select the mode
   switch (mode) {
        case 0: dot(brightness_val,0, 0);break; // red
        case 1: dot(0, brightness_val, 0);break; // green
        case 2: dot(0, 0, brightness_val);break; // blue
        case 3: colorWipe(brightness_val,0, 0);break;
        case 4: colorWipe(0, brightness_val, 0);break;
        case 5: colorWipe(0, 0, brightness_val);break;
        case 6: swoosh(brightness_val,0, 0);break;
        case 7: swoosh(0, brightness_val, 0);break;
        case 8: swoosh(0, 0, brightness_val);break;
        case 9: RainbowCycleUpdate();break;
     }
  
  mainLoopCount++;
}

void changeModeInc(){        // Interrupt service routine
  digitalWrite(13, HIGH); // we have a new mode
  newModeInc = 1;
  lastDebounceTime = millis();
}

void changeModeDec(){        // Interrupt service routine
  digitalWrite(13, HIGH); // we have a new mode
  newModeDec = 1;
  lastDebounceTime = millis();
}

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

void RainbowCycleUpdate() {
    for(int i=0; i< strip.numPixels(); i++)
    {
        strip.setPixelColor((i + mainLoopCount) % strip.numPixels(), Wheel(((i * 256 / strip.numPixels()) + mainLoopCount) & 255));
    }
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
