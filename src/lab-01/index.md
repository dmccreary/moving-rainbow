Lab #1
Set Pixel Color

In this lab we will set the first pixel to be red, then green, then blue.  We will wait 1 second (1000 milliseconds) for each color.

Each of our programs will begin with the following lines:

    #include <Adafruit_NeoPixel.h>
    #define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
    #define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
    Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

These lines will import the Adafruit NeoPixel library, set the number of pixels in our strip and then initialize the memory for our NeoPixel LED strip.

    #include <Adafruit_NeoPixel.h>
    #define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
    #define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
    Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);
    
    void setup() {
      strip.begin(); // initialize all the variables
      strip.show(); // Initialize all pixels in the strip to be off
    }
    
    void loop() {
      strip.setPixelColor(0, 255, 0, 0); // set pixel 0 to be red
      strip.show();
      delay(1000);
      strip.setPixelColor(0, 0, 255, 0); // set pixel 0 to be green
      strip.show();
      delay(1000);
      strip.setPixelColor(0, 0, 0, 255); // set pixel 0 to be blue
      strip.show();
      delay(1000);
    }