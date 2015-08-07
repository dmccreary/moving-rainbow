/* Rotary encoder read example without any interrupt
http://www.circuitsathome.com/mcu/programming/reading-rotary-encoder-on-arduino
connect the center wire to ground.  Connect the side pins to Analog ports 
Connect the middle pin of the rotery encoder to ground */
#define ENC_A A0 // Hook one end of the rotery encoder to analog pin A0
#define ENC_B A1 // Hook the other end of the rotery encoder to Analog pin A1
#define ENC_PORT PINC
#define MODE_PIN 2 // Put one of the push knob here and the other to ground
#define NUM_MODES 4 // The number of display pattern modes

#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

uint8_t patternMode = 0;
uint8_t patternMode2 = 0;

int oldPixel = 0;
int newPixel = 0;

// Used to debounce the pattern mode button
// Variables will change:
int ledState = HIGH;         // the current state of the output pin
int buttonState;             // the current reading from the input pin
int lastButtonState = LOW;   // the previous reading from the input pin

// the following variables are long's because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
long lastDebounceTime = 0;  // the last time the output pin was toggled
long debounceDelay = 150;    // the debounce time; increase if the output flickers

void setup()
{
  strip.begin(); // initialize the LED strip
  /* Setup encoder pins as inputs */
  pinMode(ENC_A, INPUT);
  digitalWrite(ENC_A, HIGH);
  pinMode(ENC_B, INPUT);
  digitalWrite(ENC_B, HIGH);
  pinMode(MODE_PIN, INPUT_PULLUP);
  
  attachInterrupt(0, isr, FALLING);  // run the isr program when the push button goes down
  
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
    Serial.print("Counter=");
    Serial.print(counter, DEC);
    Serial.print("  Display mode1=: ");
    Serial.print(patternMode, DEC);
    
    Serial.print("  Time=: ");
    Serial.print(lastDebounceTime, DEC);
    
    Serial.print("  Display mode2=: ");
    Serial.println(patternMode2, DEC);
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

// Interrupt Service Routine for the pattern mode button press
void isr() {
  // read the state of the push button into a local variable:
  int reading = digitalRead(MODE_PIN);

  // check to see if you just pressed the button 
  // (i.e. the input went from LOW to HIGH),  and you've waited 
  // long enough since the last press to ignore any noise:  

  // If the switch changed, due to noise or pressing:
  if (reading != LOW) {
    // reset the debouncing timer
    lastDebounceTime = millis(); // this is the number of milliseconds since power on
  } 
  
  if ((millis() - lastDebounceTime) > debounceDelay) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:
    // only increment the pattern mode if the new button state is HIGH
    patternMode = (patternMode + 1) % NUM_MODES;
    lastButtonState = LOW;
  }
  
  patternMode2 = (patternMode2 + 1) % NUM_MODES;

}

// draw a pattern, erase at the old and draw at the new one
void drawPattern(uint8_t oldPiexl, uint8_t counter) {
  // turn the old pixels off
  strip.setPixelColor(oldPixel, 0, 0, 0);
  strip.setPixelColor((oldPixel+1) % NUMBER_PIXELS, 0, 0, 0);
  strip.setPixelColor((oldPixel+2) % NUMBER_PIXELS, 0, 0, 0);
  // make the new pixel the counter modulo the number of pixels
  newPixel = counter % NUMBER_PIXELS;
  
  // turn on the new pixel
  if (patternMode == 0) {
    strip.setPixelColor(newPixel, 255, 0, 0);
    strip.setPixelColor((newPixel + 1) % NUMBER_PIXELS, 0, 255, 0);
    strip.setPixelColor((newPixel + 2) % NUMBER_PIXELS, 0, 0, 255);
  }
  if (patternMode == 1) {  // red
    strip.setPixelColor(newPixel, 255, 0, 0);
  }
  if (patternMode == 2) {  //  green
    strip.setPixelColor(newPixel, 0, 255, 0);
  }
    if (patternMode == 3) { // blue
    strip.setPixelColor(newPixel, 0, 0, 255);
  }
  strip.show();
};
