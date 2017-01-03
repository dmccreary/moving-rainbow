#include <Adafruit_NeoPixel.h>

/* Rotary encoder read example 
http://www.circuitsathome.com/mcu/programming/reading-rotary-encoder-on-arduino
connect the center wire to ground.  Connect the side pins to Analog ports */
#define ENC_A 14 // Analog pin A0
#define ENC_B 15 // Analog pin A1
#define ENC_PORT PINC // WTF?  Pin C???

#define LEDPIN 12 // connect the Data In pin
#define NUMBER_PIEXELS 24// connect the Data In pin
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);
int np = strip.numPixels();  // we use the modulo function with this
volatile int stripIndex = 0;

void setup()
{
  strip.begin(); // sets up the memory for the LED strip
  pinMode(13, OUTPUT);     // Pin 13 is usually on an onboard LED
  digitalWrite(13, LOW);
  /* Setup encoder pins as inputs */
  pinMode(ENC_A, INPUT);
  digitalWrite(ENC_A, HIGH);
  pinMode(ENC_B, INPUT);
  digitalWrite(ENC_B, HIGH);
  
  Serial.begin (9600);
  Serial.println("Start");
  rainbow7(0);
}

void loop()
{
 static uint8_t counter = 0; // this unsigned byte will be changed by encoder input
 int8_t tmpdata; // signed byte
 /**/
  tmpdata = read_encoder(); // this will be -1, 0 or 1
  
  if( tmpdata ) {
    Serial.print("counter=");
    Serial.print(counter, DEC);
    stripIndex = counter % strip.numPixels();
    Serial.print(" strip index=");
    Serial.println(stripIndex, DEC);
    counter = counter + tmpdata;
    rainbow7(stripIndex); // draw the rainbow starting at this index
    delay(50);  // an attempt to debounce
  };
  
}
 
/* Kind of like a Interrup Service Routine.  Feturns change in encoder state (-1,0,1) 
   Based on the lower four bits of the value at the Encoder PORT */
int8_t read_encoder()
{
  static int8_t enc_states[] = {0,-1,1,0,1,0,0,-1,-1,0,0,1,0,1,-1,0};
  static uint8_t old_AB = 0;
  /**/
  old_AB <<= 2;                   //remember previous state
  old_AB |= ( ENC_PORT & 0x03 );  //add current state
  return ( enc_states[( old_AB & 0x0f )]);
}

// draw the rainbow starting at startIndex
void rainbow7(int startIndex) {
  
    for (int i=startIndex; i<startIndex+7; i++) {
      if (i>0) {
         strip.setPixelColor( (i - 1) % np, 0, 0, 0); // turn off
      };
      strip.setPixelColor(i     % np, 25, 0, 25); // violet
      strip.setPixelColor((i+1) % np, 255, 0, 255); // indigo
      strip.setPixelColor((i+2) % np, 0, 0, 150); // blue
      strip.setPixelColor((i+3) % np, 0, 150, 0); // green
      strip.setPixelColor((i+4) % np, 255, 255, 0); // yellow
      strip.setPixelColor((i+5) % np, 110, 70, 0); // orange
      strip.setPixelColor((i+6) % np, 150, 0, 0); // red
      strip.setPixelColor((i+8) % np, 0, 0, 0); // off
      strip.show();
    }
}

