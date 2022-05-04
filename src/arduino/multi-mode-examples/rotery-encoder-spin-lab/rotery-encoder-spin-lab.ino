/* Multi-mode speed change by rotery
   Dan McCreary

Hook up two momentary push buttons to pins 2 and 3.
One button will increment the mode, one will decrment the mode
You MUST use pins 2 and 3 because they are the only Interrupt pins on the Arduino (Uno, Nano)
Connect the other ends of the momentary push buttons to GND
Note that we are using internal 20K resistors to pull up the inputs to +5 when the buttons are open
*/
#include <Adafruit_NeoPixel.h>

int mode; // This is the "mode" of the device.  It starts at 0 and gets incremented or decremented
int newModeInc = 0; // the interrupts set this to 1 to indicate that we have a new increment to handle
int brightness_val = 255;
long lastDebounceTime = 0;  // the last time the output pin was toggled
long debounceDelay = 200;   // the debounce time; increase if the output flickers

const int ENCODER_PIN_A = 3;
const int ENCODER_PIN_B = 4;

int haveNewInterrupt = 0; // 1 if we have a new interrupt to show, 0 otherwise
byte state = 0; // will store two bits for pins A & B on the encoder which we 
// will get from the pins above
int level = 0; // a value bumped up or down by the encoder
/* For demo purposes we will create an array of these binary digits */
String bits[] = {"00", "01", "10", "11"};
/* A truth table of possible moves 1 for clockwise
 -1 for counter clockwwise 0 for error - keybounce */
int bump[] = {0,0,-1,1};

const int LED_STRIP_PIN = 12; // Connect the Data pin of the LED strip here
const int NUMBER_PIXELS = 24; // Number of pixels in the LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LED_STRIP_PIN, NEO_GRB + NEO_KHZ800);

int modeCount = 10; // The number of display modes, we mode the mode to get the actual mode
int mainLoopCount = 0;  // The number of times we go through the main loop
int delayms = 100; // delay in ms

void setup()
{
  pinMode(13, OUTPUT);     // Pin 13 is output to which an LED is connected
  pinMode(2, INPUT_PULLUP); // Pin 2 is the push button on the encoder used to change modes = INT0
  pinMode(3, INPUT_PULLUP); // Pin 3 is one of the two encoder pins to change speed = INT1
  pinMode(4, INPUT_PULLUP); // Pin 4 is one of the two encoder pins no interrrup
  
  // both pins must be high
  digitalWrite(ENCODER_PIN_A,HIGH);
  digitalWrite(ENCODER_PIN_B,HIGH);
  
  attachInterrupt(0, changeModeInc, FALLING  ); // pin 2
  attachInterrupt(1, knobTurned, RISING  ); // pin 3
  Serial.begin(9600);
  strip.begin(); // sets up the memory for the LED strip
  Serial.println("Start");
  newModeInc = 0;
  mode = 0;
  Serial.print("Mode=");
  Serial.println(mode, DEC);
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
  
  // select the mode
   switch (mode) {
        case 0: rainbow7(mainLoopCount % NUMBER_PIXELS);break;
        case 1: dot(brightness_val,0, 0);break; // red
        case 2: dot(0, brightness_val, 0);break; // green
        case 3: dot(0, 0, brightness_val);break; // blue
        case 4: swoosh(brightness_val,0, 0);break;
        case 5: swoosh(0, brightness_val, 0);break;
        case 6: swoosh(0, 0, brightness_val);break;
        case 7: RainbowCycleUpdate();break;
        case 8: rainbow();break;
        case 9: candle();break;
     }
  
  
  if (haveNewInterrupt == 1) {
     Serial.print(bits[state]); // show us the two bits
     Serial.print("   ");
     Serial.print(bump[state]); // show us the direction of the turn
     Serial.print("   ");
     Serial.println(level); // show us the new value
     haveNewInterrupt = 0; // now we are done
  }
  
 //  delayms = delayms - (level);
  // limit the delay from 10ms to 5 seconds
  delayms = constrain(delayms, 10, 500);
  Serial.print("delay=");
  Serial.println(delayms);
  delay(delayms);
  
  mainLoopCount++;
}

void changeModeInc(){        // Interrupt service routine
  digitalWrite(13, HIGH); // we have a new mode
  newModeInc = 1;
  lastDebounceTime = millis();
}

void knobTurned() {
 /* AH HA! the knob was turned */
 haveNewInterrupt = 1; // this is for the main loop to catch
 state = 0; // reset this value each time
 state = state + digitalRead(ENCODER_PIN_A); // add the state of Pin A
 state <<= 1; // shift the bit over one spot
// add the state of Pin B * now we have a two bit binary number that holds the state of both pins 00
// - something is wrong we must have got here with a key bounce 01 - sames as above
// - first bit should never be 0 10 - knob was turned backwards 11
// - knob was turned forwards   We can pull a value out of our truth table and add it to the current level *
 state = state + digitalRead(ENCODER_PIN_B); 
 level = level + bump[state]; // Let's see what happened
 delayms = delayms - (bump[state] * 4);
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

// a seven segment rainbow with red on the highest pixel
void rainbow7(int i) {
  int np = strip.numPixels();  // we use the modulo function with this
  strip.setPixelColor(i     % np, 0, 0, 0); // off
  strip.setPixelColor((i+1) % np, 25, 0, 25); // violet
  strip.setPixelColor((i+2) % np, 255, 0, 255); // indigo
  strip.setPixelColor((i+3) % np, 0, 0, 150); // blue
  strip.setPixelColor((i+4) % np, 0, 150, 0); // green
  strip.setPixelColor((i+5) % np, 255, 255, 0); // yellow
  strip.setPixelColor((i+6) % np, 110, 70, 0); // orange
  strip.setPixelColor((i+7) % np, 150, 0, 0); // red
  strip.setPixelColor((i+8) % np, 0, 0, 0); // off
  strip.show();
}
void RainbowCycleUpdate() {
    for(int i=0; i< strip.numPixels(); i++)
    {
        strip.setPixelColor((i + mainLoopCount) % strip.numPixels(), Wheel(((i * 256 / strip.numPixels()) + mainLoopCount) & 255));
    }
    strip.show();
}

void rainbow() {
  uint16_t i, j;
  for(j=0; j<256; j++) {
    for(i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel((i+j) & 255));
    }
    delay(10);
    strip.show();
  }
}

void candle() {
   uint8_t green; // brightness of the green 
   uint8_t red;  // add a bit for red
   for(uint8_t i=0; i<100; i++) {
     green = 50 + random(155);
     red = green + random(50);
     strip.setPixelColor(random(strip.numPixels()), red, green, 0);
     strip.show();
  }
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


