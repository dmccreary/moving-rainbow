#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIXELS 35
// the number of pixels in your LED strip

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int delayTime = 100;
int halfCount = round( NUMBER_PIXELS / 2);
int quarterCount = round( NUMBER_PIXELS / 4);

void setup() {
  strip.begin(); // initialize the strip
  lastGreen();
}

void loop() {
  fadeIn(1);
  randomOn(50);
  singleRunner();
  crossRunner();
  allGreen();
  halfGreenOrange();
  quarterGreenOrange();
  theaterChase(strip.Color(0, 255, 0), delayTime); // green
};

// turn all pixels off
void allOff() {
  for (int i=0; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, 0, 0, 0);
  };
  strip.show();
};

// set the last pixel to be green for one second
void lastGreen() {
  strip.setPixelColor(NUMBER_PIXELS-1, 0, 255, 0);
  strip.show();
  delay(1000);
  allOff();
  strip.show();
};

void allGreen() {
  for (int i=0; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, 0, 255, 0);
  };
  strip.show();
  delay(1000);
  allOff();
  delay(500);
};

void halfGreenOrange() {
  for (int i=0; i<halfCount+1; i++) {
    strip.setPixelColor(i, 0, 255, 0);
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

void quarterGreenOrange() {
  for (int i=0; i<quarterCount; i++) {
    strip.setPixelColor(i, 0, 255, 0); //green
  };
  strip.show();
  delay(1000);
  
  for (int i=quarterCount; i<halfCount; i++) {
    strip.setPixelColor(i, 255, 102, 0); // orange
  };
  strip.show();
  delay(1000);
  
  for (int i=halfCount; i<halfCount + quarterCount + 1; i++) {
    strip.setPixelColor(i, 0, 255, 0); // green
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
    strip.setPixelColor(i, 0, 255, 0);
    delay(15);
    strip.show();
  };
  
  
  for (int i=1; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i-1, 0, 0, 0);
    strip.setPixelColor(i, 255, 102, 0); // orange
    delay(15);
    strip.show();
  };
  
};

void crossRunner() {
  for (int i=1; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i-1, 0, 0, 0);
    strip.setPixelColor(i, 0, 255, 0);
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
};

void randomOn(uint8_t dealyEach) {
  for (int i=0; i < strip.numPixels(); i++) {
    int randomIndex = round(random(strip.numPixels()+1));
    strip.setPixelColor(randomIndex, 0, 255, 0); // green
    strip.show();
    delay(dealyEach);
    randomIndex = round(random(strip.numPixels()+1));
    strip.setPixelColor(randomIndex, 255, 102, 0); // orange
    strip.show();
    delay(dealyEach);
  }
  allOff();
  delay(500);
};

void fadeIn(uint8_t delaySpeed) {
  for (int brightness=0; brightness < 255; brightness = brightness + 5) {
    for (int i=0; i < strip.numPixels(); i++) {
      strip.setPixelColor(i, 0, brightness, 0); // green brightness
      strip.show();
      delay(delaySpeed);
    }
  }
   allOff();
  delay(500);
};
