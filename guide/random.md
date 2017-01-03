# Random

Lets face it.  Computers are really good at repeating the same pattern over and over.  But after a while this gets pretty boring.  What might be fun is to add a little bit of random behavior into our patterns.  Luckily the Arduino software has just the function for us!  It is called, you guessed it [random](http://arduino.cc/en/reference/random).  By the way, that link is to the Arduino Reference 
```
#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int index, red, green, blue;

void setup() {
  strip.begin(); // initialize the strip
}

void loop() {
  index = random(12);
  red = random(255);
  green = random(255);
  blue = random(255);
  strip.setPixelColor(index, strip.Color(red, green, blue));
  strip.show();
  delay(100);
}
```
## More to Explore
Look at the intensity of the colors.  You will find that although there are some darker colors, most of them tend to skew toward the white colors.  This is because on the average, there are at least two colors that are over half on.  We usually only get a deep color if two colors are almost off and the third one is on.  How can you change the program so that we get a more full spectrum of colors?