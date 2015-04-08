# Theater Chase

A [Chase](http://en.wikipedia.org/wiki/Chase_%28lighting%29) is a pattern of lights where adjacent lights turn on an off to give the illusion of motion.  Chase lights are often used in the marquee signs of movie theaters so they are referred to as Theater Chase patterns.

We will create a single function that will set a theater chase pattern on our LED strip.  It will take two input parameters, one for the color and one for the delay time in milliseconds between changes.
```
void theaterChase(uint32_t color, uint8_t wait) {
... put your code here...
};
```

Here is the full program that will turn our LED strip into red, white and blue chase patterns.  Perfect for the 4th of July celebrations in the US.

Note that we use the strip.Color() function to set a red, green and blue value.
```
#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int delayTime = 100;

void setup() {
  strip.begin(); // initialize the strip
}

void loop() {
  theaterChase(strip.Color(127, 0, 0), delayTime); // red
  theaterChase(strip.Color(127, 127, 127), delayTime); // white
  theaterChase(strip.Color(0, 0, 127), delayTime); // blue
}

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
```

## More to explore
What happens if you change the second parameter from 150 milliseconds to 50 milliseconds?  What about 5 milliseconds?  Can you still see the motion when the delay is very small?