#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIXELS 150
// the number of pixels in your LED strip

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int delayTime = 100;
int halfCount = round( NUMBER_PIXELS / 2);
int quarterCount = round( NUMBER_PIXELS / 4);

void setup() {
  strip.begin(); // initialize the strip
}

void loop() {
  singleRunner();
  crossRunner();
  allOrange();
  halfPurpleOrange();
  quarterPurpleOrange();
  theaterChase(strip.Color(255, 100, 0), delayTime); // orange
  randomOrangePurple();
  randomWalk();
};

// turn all pixels off
void allOff() {
  for (int i=0; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, 0, 0, 0);
  };
  strip.show();
};

void allOrange() {
  for (int i=0; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, 255, 100, 0);
  };
  strip.show();
  delay(1000);
  allOff();
  delay(500);
};

void halfPurpleOrange() {
  for (int i=0; i<halfCount; i++) {
    strip.setPixelColor(i, 255, 0, 255);
  };
  
  strip.show();
  delay(1000);
  for (int i=halfCount + 1; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, 255, 102, 0); // orange
  };
  strip.show();
  delay(1000);
  allOff();
  delay(500);
};

void quarterPurpleOrange() {
  for (int i=0; i<quarterCount; i++) {
    strip.setPixelColor(i, 255, 0, 255); //purple
  };
  strip.show();
  delay(1000);
  
  for (int i=quarterCount; i<halfCount; i++) {
    strip.setPixelColor(i, 255, 102, 0); // orange
  };
  strip.show();
  delay(1000);
  
  for (int i=halfCount; i<halfCount + quarterCount; i++) {
    strip.setPixelColor(i, 255, 0, 255); //purple
  };
  strip.show();
  delay(1000);
  
  for (int i=halfCount + quarterCount + 1; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, 255, 102, 0); // orange
  };
  strip.show();
  delay(1000);
  
  allOff();
  delay(500);
};

void singleRunner() {
  for (int i=1; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i-1, 0, 0, 0);
    strip.setPixelColor(i, 255, 100, 0); // orange
    delay(15);
    strip.show();
  };
  
  
  for (int i=1; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i-1, 0, 0, 0);
    strip.setPixelColor(i, 255, 0, 255); // purple
    delay(15);
    strip.show();
  };
  
};

void crossRunner() {
  for (int i=1; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i-1, 0, 0, 0);
    strip.setPixelColor(i, 255, 0, 255);
    strip.setPixelColor(NUMBER_PIXELS-i, 0, 0, 0);
    strip.setPixelColor(NUMBER_PIXELS-i-1, 255, 102, 0); // orange
    delay(15);
    strip.show();
  };  
};
  
// Theatre-style crawling lights.
void theaterChase(uint32_t c, uint8_t wait) {
  for (int j=0; j<10; j++) {  //do 10 cycles of chasing
    for (int q=0; q < 3; q++) {
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, c);    //turn every third pixel on
      }
      strip.show();
      delay(wait);
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
}


void randomOrangePurple() {
  for (int i=1; i<NUMBER_PIXELS * 1.5; i++) {
    strip.setPixelColor(random(NUMBER_PIXELS), 255, 100, 0); // orange
    delay(15);
    strip.show();
    strip.setPixelColor(random(NUMBER_PIXELS), 255, 0, 255); // purple
    delay(15);
    strip.show();
  };
  allOff();
};

void randomWalk(){
int orangePosition = NUMBER_PIXELS * .666 ; // start at 2/3
int purplePosition = NUMBER_PIXELS * .333 ; // start at 1/3

for (int i=1; i<NUMBER_PIXELS / 2; i++) {
    orangePosition = orangePosition + random(-1, 1);
    strip.setPixelColor(orangePosition, 255, 100, 0); // orange
    strip.show();
    delay(20);
    strip.setPixelColor(orangePosition, 0, 0, 0);
    strip.show();
    
    purplePosition = purplePosition + random(-2, 2);
    strip.setPixelColor(purplePosition, 255, 0, 255); // purple
    
    strip.show();
    delay(20);
    strip.setPixelColor(purplePosition, 0, 0, 0);
    strip.show();
  }
}
