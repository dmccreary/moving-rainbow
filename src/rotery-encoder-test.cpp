#include <Adafruit_NeoPixel.h>
 
/* Rotary encoder read example 
http://www.circuitsathome.com/mcu/programming/reading-rotary-encoder-on-arduino
connect the center wire to ground.  Connect the side pins to Analog ports */
#define ENC_A 14 // Analog pin A0
#define ENC_B 15 // Analog pin A1
#define ENC_PORT PINC
 
#define LEDPIN 10 // connect the Data In pin
#define NUMPIXELS 12 // connect the Data In pin
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMPIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);
 
void setup()
{
  strip.begin();
  // a quick startup test of the first and last pixel for 1/2 second
  strip.setPixelColor(0, 100, 100, 100);
  strip.setPixelColor(11, 100, 100, 100);
  strip.show();
  delay(500);
  strip.setPixelColor(0, 0);
  strip.setPixelColor(11, 0);
  strip.begin(); // Now initialize all pixels to 'off'
  strip.show(); 
  
  /* Setup encoder pins as inputs */
  pinMode(ENC_A, INPUT);
  digitalWrite(ENC_A, HIGH);
  pinMode(ENC_B, INPUT);
  digitalWrite(ENC_B, HIGH);
  
  Serial.begin (19200);
  Serial.println("Start");
}
 
void loop()
{
 static int counter = 0;      //this variable will be changed by encoder input
 static int pix_num = 0; // the number pixel we will light
 static int old_pix_num = 0; // the number pixel we will turn off
 static int red = 0;
 static int green = 0;
 static int blue = 0;
 int8_t tmpdata;
 
  /* this will be -1, 0 or 1 */
  tmpdata = read_encoder();
  if( tmpdata ) {
    // Serial.print("Counter value: ");
    // Serial.println(counter, DEC);
    old_pix_num = pix_num;
    counter += tmpdata;
    pix_num = abs(counter % NUMPIXELS); // the pix number is the remainer after divsion by 12
    // lets change the colors based on the counter
    // the % is the modulo functin that returns the remainder after a division
    // we want 0 to be red, 1 to be green, 2 to be blue, 3 to be red, 4 to be green, 5 to be blue etc...
    if (counter % 3)
       {red = 0;}
       else {red = 255;};
    if ( (counter + 1) % 3)
       {blue = 0;}
       else {blue = 255;};
     if ( (counter + 2) % 3 )
       {green = 0;}
       else {green = 255;};
    strip.setPixelColor(pix_num, red, green, blue); // turn on the new one
    strip.setPixelColor(old_pix_num, 0, 0, 0); // turn off the old one
    strip.show();
    Serial.print("pn=");
    Serial.print(pix_num, DEC);
    Serial.print(" r=");
    Serial.print(red, DEC);
    Serial.print(" g=");
    Serial.print(green, DEC);
    Serial.print(" b=");
    Serial.println(blue, DEC);
  };  
}
 
/* returns change in encoder state (-1,0,1) */
int8_t read_encoder()
{
  static int8_t enc_states[] = {0,-1,1,0,1,0,0,-1,-1,0,0,1,0,1,-1,0}; // lookup table
  static uint8_t old_AB = 0; // static values remain on between calls
  /**/
  old_AB <<= 2;                   //remember previous state and shift the bits over
  old_AB |= ( ENC_PORT & 0x03 );  //add current state
  return ( enc_states[( old_AB & 0x0f )]);
}