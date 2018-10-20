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

How the program works is a bit complex.  It uses note one, not two, but THREE nested for loops.

1. The outer loop is just a wrapper that repeats 10 times.  We use the letter "j" to count up to 10.
2. The middle loop just counts from 0 to 2 (three items).  It uses the letter "q" to do this.  We can call this the offset.
3. The most inner loop goes from the first to the last pixel turning each third one on.  The increment is by three each time.  The letter used is "i" for the index.

The main function inside these three loops sets the q+i pixel on.  The effect is to turn every third pixel on.  We skip over two because we are adding 3 to the index each time.


```
strip.setPixelColor(q+i, color);
```
After we display the strip and wait a bit then we reverse the operation by turning each third pixel off. 

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

// Theatre-style crawling lights with a spacing of 3
void theaterChase(uint32_t color, uint8_t wait) {
  for (int j=0; j<10; j++) {  //do 10 cycles of chasing
    for (int q=0; q < 4; q++) {
      for (int i=0; i < strip.numPixels(); i=i+4) {
        strip.setPixelColor(q+i, color);    //turn every third pixel on
      }
      strip.show();
      delay(wait);
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(q+i, 0);        //turn every third pixel off
      }
    }
  }
}
```

## More to explore
Can you change the spacing between the "on" pixels.  Right now they are set to be 3.  Can you change it to be 4?  Note that you will have to make the change it two places in the middle and inner-most for loops.  Try it out!