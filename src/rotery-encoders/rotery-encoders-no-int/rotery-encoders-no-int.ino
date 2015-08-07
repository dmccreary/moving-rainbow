/* Rotary encoder read example without any interrupt
http://www.circuitsathome.com/mcu/programming/reading-rotary-encoder-on-arduino
connect the center wire to ground.  Connect the side pins to Analog ports */
#define ENC_A A0 // Analog pin A0
#define ENC_B A1 // Analog pin A1
#define ENC_PORT PINC

#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int oldPixel = 0;
int newPixel = 0;
void setup()
{
  strip.begin(); // initialize the LED strip
  /* Setup encoder pins as inputs */
  pinMode(ENC_A, INPUT);
  digitalWrite(ENC_A, HIGH);
  pinMode(ENC_B, INPUT);
  digitalWrite(ENC_B, HIGH);
  
  Serial.begin (9600);
  Serial.println("Start");
}

void loop()
{
 static uint8_t counter = 0;      //this variable will be changed by encoder input
 int8_t tmpdata;                  // temporary place to store our encoder reading, -1, 0 or +1
 oldPixel = counter % NUMBER_PIXELS;
 
  // get the new data
  tmpdata = read_encoder(); // get the new value, -1, 0, or 1
  if (tmpdata) {            // we only change if we have a new value
    Serial.print("Counter value: ");
    Serial.println(counter, DEC);
    counter += tmpdata;  // make the counter go down, or up by one - every "click" is 4 changes
  };
  drawPattern(oldPixel, counter);  // draw a pattern, erase the old and draw the new
}
 
/* Returns change in encoder state (-1,0,1) 
   This must be in the main loop() with no delay to make sure we don't
   skip over some changes.  To avoid missing clicks, we should use
   the example that uses and interrupt service routing (ISR)
*/
int8_t read_encoder()
{
  static int8_t enc_states[] = {0,-1,1,0,1,0,0,-1,-1,0,0,1,0,1,-1,0};
  static uint8_t old_AB = 0;
  /**/
  old_AB <<= 2;                   //remember previous state
  old_AB |= ( ENC_PORT & 0x03 );  //add current state
  return ( enc_states[( old_AB & 0x0f )]);
}

// draw a pattern, erase at the old and draw at the new one
void drawPattern(uint8_t oldPiexl, uint8_t counter) {
  // turn the the old pixel off
  strip.setPixelColor(oldPixel, 0, 0, 0);
  strip.setPixelColor((oldPixel+1) % NUMBER_PIXELS, 0, 0, 0);
  strip.setPixelColor((oldPixel+2) % NUMBER_PIXELS, 0, 0, 0);
  // make the new pixel the counter modulo the number of pixels
  newPixel = counter % NUMBER_PIXELS;
  // turn on the new pixel
  strip.setPixelColor(newPixel, 255, 0, 0);
  strip.setPixelColor((newPixel + 1) % NUMBER_PIXELS, 0, 255, 0);
  strip.setPixelColor((newPixel + 2) % NUMBER_PIXELS, 0, 0, 255);
  strip.setPixelColor(newPixel, 255, 0, 0);
  strip.show();
};
