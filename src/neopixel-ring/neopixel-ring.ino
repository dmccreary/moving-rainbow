#include <Adafruit_NeoPixel.h>
#include <avr/interrupt.h>

#define LEDPIN 12 // connect the Data In pin
#define MODEPIN 2 // pull down to groud to get a new mode
#define NUMBER_PIEXELS 12// connect the Data In pin
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

// hook up two momentary push buttons to pins 
volatile int newMode = 0; // the interrupts set this to 1 to indicate that we have a new mode on the way
volatile int mode = -1; // This gets incremented each button press
int waitTime = 70; //Typical delay between draws
int modeCount = 11; // The number of display modes

void setup() {
  strip.begin(); // sets up the memory for the LED strip
  pinMode(13, OUTPUT);     // Pin 13 is output to which an LED is connected
  digitalWrite(13, LOW);   // Make pin 13 low, switch LED off
  pinMode(2, INPUT_PULLUP);	   // Pin 2 is input to which a switch is connected = INT0
  pinMode(3, INPUT_PULLUP);	   // Pin 3 is input to which a switch is connected = INT1
  attachInterrupt(0, changeMode, RISING); // connect the mode to pin 2
  Serial.begin(9600);
  Serial.println("Start");
}

void changeMode(){        // Interrupt service routine
  digitalWrite(13, HIGH); // we have a new mode
  newMode = 1;
}

void loop() {
  // check to see if we should change the mode
  if (newMode == 1) {
      delay(waitTime); // wait for the switch to settle down used to de-bounce
      mode = (mode + 1) % modeCount;
      Serial.print("mode=");
      Serial.println(mode, DEC);
      digitalWrite(13, LOW);
      newMode = 0;
  }

   // select the mode
      switch (mode) {
        case 0: rainbow7(waitTime);break;
        case 1: colorWipe(strip.Color(255, 0, 0), waitTime);break; // Red
        case 2: colorWipe(strip.Color(0, 255, 0), waitTime);break; // Green
        case 3: colorWipe(strip.Color(0, 0, 255), waitTime);break; // Blue
        case 4: singlePixel(waitTime);break;
        case 5: rainbow(5);break;
        case 6: rainbowCycle(5);break;
        case 7: randomRGB(waitTime);break;
        case 8: randomColor(waitTime);break;
        case 9: candle();break;
        case 10: theaterChaseRainbow(100);break;
     }
    
}

// a seven segment rainbow with red on the highest pixel
void rainbow7(uint16_t wait) {
  int np = strip.numPixels();  // we use the modulo function with this
  for (int i=0; i<strip.numPixels()-1; i++) { 
      strip.setPixelColor(i     % np, 0, 0, 0); // off
      strip.setPixelColor((i+1)   % np, 25, 0, 25); // violet
      strip.setPixelColor((i+2) % np, 255, 0, 255); // indigo
      strip.setPixelColor((i+3) % np, 0, 0, 150); // blue
      strip.setPixelColor((i+4) % np, 0, 150, 0); // green
      strip.setPixelColor((i+5) % np, 255, 255, 0); // yellow
      strip.setPixelColor((i+6) % np, 110, 70, 0); // orange
      strip.setPixelColor((i+7) % np, 150, 0, 0); // red
      strip.show();
      delay(wait);
  }
}

// See https://en.wikipedia.org/wiki/Web_colors
void singlePixel(uint8_t wait) {
   for(uint8_t i=0; i<strip.numPixels(); i++) {
     // turn it on
      strip.setPixelColor(i , 255, 0, 0);
      // show it
      strip.show();
      // wait
      delay(wait);
      // turn it off
      strip.setPixelColor(i , 0, 0, 0);  
  }
}

// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
  }
  // turn them all off
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, 0);
  }
  strip.show();
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

