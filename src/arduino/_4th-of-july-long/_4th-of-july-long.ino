#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
// 5 meter strip at 30 LEDs per meter is 150
// 5 meter strip at 60 LEDs per meter is 240
#define NUMBER_PIXELS 150
// the number of pixels in your LED strip

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int halfCount = round( NUMBER_PIXELS / 2);
int thirdCount = round( NUMBER_PIXELS / 3);
int quarterCount = round( NUMBER_PIXELS / 4);
int sixthCount = round( NUMBER_PIXELS / 6);

void setup() {
  strip.begin(); // initialize the strip
  allOff();
}

void loop() {
  
  // red, white and blue
  allOneColor(255, 0, 0, 1000);
  allOneColor(210, 255, 255, 1000);
  allOneColor(0, 0, 255, 1000);
  
  oneThirdRedWhiteBlue(1000);
  
  // divide by div segments and keep on for wait period
  segmentsRedWhiteBlue(6, 1000);
  segmentsRedWhiteBlue(10, 1000);
  
  // divide by div segments and keep on for wait period
  movingSegmentsRedWhiteBlue(6, 50);
  
  // color and milliseconds per pixel
  singleRunner(255,0,0, 7);
  singleRunner(255,255,255, 7);
  singleRunner(0,0,255, 7);
  
  crossRunner(255,0,0, 7);
  crossRunner(255,255,255, 75);
  crossRunner(0,0,255, 7);
  
  theaterChase(strip.Color(255, 0, 0), 70); // red
  theaterChase(strip.Color(255, 255, 255), 70); // white
  theaterChase(strip.Color(0, 0, 255), 70); // blue
  
  allOff();
  delay(1000);
};



void allOneColor(uint8_t red, uint8_t green, uint8_t blue, int wait) {
  for (int i=0; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, red, green, blue);
  };
  strip.show();
  delay(wait);
  allOff();
};

void oneThirdRedWhiteBlue(int wait) {
  
  // 1/3 red
  for (int i=0; i<thirdCount; i++) {
    strip.setPixelColor(i, 255, 0, 0); // red
  };
  strip.show();
  delay(wait);
  
  // 1/3 white
  for (int i=thirdCount; i < (2 * thirdCount); i++) {
    strip.setPixelColor(i, 255, 255, 255); // white
  };
  strip.show();
  delay(wait);
  
  // 1/3 white
  for (int i=(2 * thirdCount); i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, 0, 0, 255); // blue
  };
  strip.show();  
  delay(wait);
  
  allOff();

};

// div is the number of divisions to light
// div = 6 means 1/6 will be turned on each time
void segmentsRedWhiteBlue(int div , int wait) {
  int pixelsPerSegment = (NUMBER_PIXELS / div);
  // d ranges from 0 to 5
  for (int d=0; d < div; d++) {
    for (int i= d*pixelsPerSegment; i < (d+1)*(pixelsPerSegment); i++) {
      if (!(d % 3))
        strip.setPixelColor(i, 255, 0, 0); //red
        else if (!((d + 1) % 3))
           strip.setPixelColor(i, 0, 0, 255); //blue
           else strip.setPixelColor(i, 255, 255, 255); //white
    };
    strip.show();
    delay(wait);
  };
  allOff();
};

// div is the number of divisions to light up
// div = 6 means 1/6 will be on at any time
void movingSegmentsRedWhiteBlue(int div , int wait) {
  int pixelsPerSegment = (NUMBER_PIXELS / div); 
  for (int offset=0; offset< 200; offset++) {
    // d ranges from 0 to div
    for (int d=0; d < div; d++) {
      for (int i= d*pixelsPerSegment; i < (d+1)*(pixelsPerSegment); i++) {
        if (!(d % 3))
          strip.setPixelColor( (i+offset) % NUMBER_PIXELS, 255, 0, 0); //red
          else if (!((d + 1) % 3))
             strip.setPixelColor( (i+offset) % NUMBER_PIXELS, 0, 0, 255); //blue
             else strip.setPixelColor( (i+offset) % NUMBER_PIXELS, 255, 255, 255); //white
      };
      
    };
    strip.show();
    delay(wait);
  };
};

void singleRunner(uint8_t red, uint8_t green, uint8_t blue, int wait) {
  for (int i=1; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, red, green, blue);
    strip.show();
    delay(wait);
    strip.setPixelColor(i, 0, 0, 0);
  };  
};

void crossRunner(uint8_t red, uint8_t green, uint8_t blue, int wait) {
  for (int i=1; i<NUMBER_PIXELS; i++) {
    // turn the first and last on for a wait
    strip.setPixelColor(i, red, green, blue);
    strip.setPixelColor(NUMBER_PIXELS-i-1, red, green, blue);
    delay(wait);
    strip.show();
    // turn them both off
    strip.setPixelColor(i, 0, 0, 0);
    strip.setPixelColor(NUMBER_PIXELS-i-1, 0, 0, 0);
    delay(15);
    strip.show();
  };  
};
  
// Theatre-style crawling lights.
// Change so only 1 in 6 is on
void theaterChase(uint32_t c, uint8_t wait) {
  for (int j=0; j<10; j++) {  //do 10 cycles of chasing
    for (int q=0; q < 6; q++) {
      for (int i=0; i < strip.numPixels(); i=i+6) {
        strip.setPixelColor(i+q, c);    //turn every third pixel on
      }
      strip.show();
      delay(wait);
      for (int i=0; i < strip.numPixels(); i=i+6) {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
};

// turn all pixels off
void allOff() {
  for (int i=0; i<NUMBER_PIXELS; i++) {
    strip.setPixelColor(i, 0, 0, 0);
  };
  strip.show();
};
