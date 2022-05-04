// this version automatically cycles through each of the modes.
#include <Adafruit_NeoPixel.h>

#define LEDPIN 12 // connect the Data In pin
#define NUMBER_PIEXELS 60// connect the Data In pin
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);
// this constant won't change:
const int  buttonPin = 3;    // the pin that the pushbutton is attached to
// must be 2 or 3 to use interupts
const int ledPin = 13;       // the pin that the LED is attached to to show mode changes
int waitTime = 50;  // Delay time between a pixel movement

void setup() {
  // initialize the LED as an output:
  pinMode(ledPin, OUTPUT);
  strip.begin(); // sets up the memory
  // initialize serial communication:
  Serial.begin(9600);
  Serial.println("Start");
}

void loop() {
  backAndForth(10, waitTime);
  /*
  stripeChase(5, waitTime);
  stripeChase(10, waitTime);
  stripeChase(20, waitTime);
  stripeChase(30, waitTime);
  stripeChase(40, waitTime);
  theaterChase(strip.Color(255, 0, 0), waitTime);
  theaterChase(strip.Color(0, 255, 0), waitTime);
  randomRedGreen(waitTime);
  rainbow7(waitTime);
  twinkle(waitTime);
  colorWipe(strip.Color(255, 0, 0), waitTime);
  colorWipe(strip.Color(0, 255, 0), waitTime);
  */
}

// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
    for(int j=0; j<strip.numPixels(); j++) {
        strip.setPixelColor(j, c);
        strip.show();
        delay(wait);
    }
    for(int j=0; j<strip.numPixels(); j++)
      strip.setPixelColor(j, 0,0,0);
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
      delay(wait);
  }
}


// draw 100 random red and green for 1/10th of a second
void randomRedGreen(uint8_t wait) {
int position;
  for(int i=0; i<100; i++) {
     position = random(strip.numPixels());
     // half red and half green
     if (random(2) > 0 )
        strip.setPixelColor(position, 255, 0, 0);
      else strip.setPixelColor(position, 0, 255, 0);
     strip.show();
     delay(wait*3);
     strip.setPixelColor(position, 0, 0, 0);
     strip.show();
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
void theaterChase(uint32_t color, uint8_t wait) {

    for (int j=0; j < 10; j++) {
      for (int q=0; q < 5; q++) {
          for (int i=0; i < strip.numPixels(); i=i+5) {
            strip.setPixelColor(i+q, color);    //turn every 5th pixel on
          }
          strip.show();
          delay(wait * 3);
          
          for (int i=0; i < strip.numPixels(); i=i+5) {
            strip.setPixelColor(i+q, 0);        //turn every fifth pixel off
          }
          strip.show();
      }
    }
}

// alternating bands of color that move down the strip
void stripeChase(int bandWidth, uint8_t wait) {
   for (int j=0; j <= strip.numPixels(); j++) {
       for (int i=0; i < strip.numPixels(); i++) {
          if ((i / bandWidth) % 2)
             strip.setPixelColor((i+j) % strip.numPixels(), 255,0,0);
          else strip.setPixelColor((i+j) % strip.numPixels(), 0,255,0);
       }
        strip.show();
        delay(wait * 2);
   }
}


// alternating bands of color that move down the strip
void backAndForth(int bandWidth, uint8_t wait) {
   // forward
   Serial.println("Forward");
   for (int j=0; j <= strip.numPixels() - bandWidth; j++) {
       for (int i=0; i < strip.numPixels(); i++) {
          if (i < bandWidth) strip.setPixelColor((i+j) % strip.numPixels(), 255,0,0);
          else strip.setPixelColor((i+j) % strip.numPixels(), 0,255,0);
       }
        strip.show();
        delay(wait);
   }
   //reverse
   Serial.println("Reverse");
   for (int j=strip.numPixels(); j > 0; j--) {
       for (int i=strip.numPixels(); i > 0; i--) {
          if (i > strip.numPixels() - bandWidth) strip.setPixelColor( (i+j) % strip.numPixels(), 255,0,0);
          else strip.setPixelColor((i+j) % strip.numPixels(), 0,255,0);
       }
        strip.show();
        delay(wait);
   }
}


void twinkle(uint8_t wait) {
  int random_index;
  for (int i=0; i < wait/100; i++) {
    strip.setPixelColor(i, 0, 0, 0);
    random_index = random(strip.numPixels()); // get a random number from 0 to Num Pixels
    strip.setPixelColor(random_index, 255, 0, 0); // turn a random pixel on
    strip.show();
    delay(100);
    
    strip.setPixelColor(random_index, 0, 255, 0); // turn a random pixel on
    strip.show();
    delay(100);
    strip.setPixelColor(random_index, 0, 0, 0); // turn it off
  }
}
