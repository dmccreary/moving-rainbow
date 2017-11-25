#include <Adafruit_NeoPixel.h>
#define LEDPIN 12 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 16 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);
int n = strip.numPixels();
int color_step = (int) 255/n; // 1/16 of the way around the 255 element color wheel

static int encoder_PinA = 2; // Our first hardware interrupt pin is digital pin 2
static int encoder_PinB = 3; // Our second hardware interrupt pin is digital pin 3
static int push_Knob_Pin = 5; // The push button function on the encoder
static int menu_state = 1; // 1=menu, 2=color
static int flash_delay = 100;

//this variable stores our current value of encoder position. Change to int or uin16_t instead of byte if you want to record a larger range than 0-255
volatile unsigned int encoder_Pos = 0;

volatile byte aFlag = 0; // let's us know when we're expecting a rising edge on pinA to signal that the encoder has arrived at a detent
volatile byte bFlag = 0; // let's us know when we're expecting a rising edge on pinB to signal that the encoder has arrived at a detent (opposite direction to when aFlag is set)
volatile byte encoderPos = 0; 
volatile byte oldEncPos = 0; //stores the last encoder position value so we can compare to the current reading and see if it has changed (so we know when to print to the serial monitor)
volatile byte reading = 0; //somewhere to store the direct values we read from our interrupt pins before checking to see if we have moved a whole detent

int ledState = HIGH;         // the current state of the output pin
int lastButtonState = LOW;   // the previous reading from the input pin
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers
unsigned long loop_counter = 0;    // times through the main loop

void setup() {
  strip.begin();
  draw_color_menu(0);

  pinMode(encoder_PinA, INPUT_PULLUP); 
  pinMode(encoder_PinB, INPUT_PULLUP);
  pinMode(push_Knob_Pin, INPUT_PULLUP); 
  attachInterrupt(0,PinA, RISING); // set an interrupt on PinA, looking for a rising edge signal and executing the "PinA" Interrupt Service Routine (below)
  attachInterrupt(1,PinB, RISING); // set an interrupt on PinB, looking for a rising edge signal and executing the "PinB" Interrupt Service Routine (below)
  
  Serial.begin (9600);
  Serial.println("start");                // a personal quirk
}

void PinA(){
  cli(); //stop interrupts happening before we read pin values
  reading = PIND & 0xC; // read all eight pin values then strip away all but pinA and pinB's values
  if(reading == B00001100 && aFlag) { //check that we have both pins at detent (HIGH) and that we are expecting detent on this pin's rising edge
    encoder_Pos--; //decrement the encoder's position count
    bFlag = 0; //reset flags for the next turn
    aFlag = 0; //reset flags for the next turn
  }
  else if (reading == B00000100) bFlag = 1; //signal that we're expecting pinB to signal the transition to detent from free rotation
  sei(); //restart interrupts
}

void PinB(){
  cli(); //stop interrupts happening before we read pin values
  reading = PIND & 0xC; //read all eight pin values then strip away all but pinA and pinB's values
  if (reading == B00001100 && bFlag) { //check that we have both pins at detent (HIGH) and that we are expecting detent on this pin's rising edge
    encoder_Pos++; //increment the encoder's position count
    bFlag = 0; //reset flags for the next turn
    aFlag = 0; //reset flags for the next turn
  }
  else if (reading == B00001000) aFlag = 1; //signal that we're expecting pinA to signal the transition to detent from free rotation
  sei(); //restart interrupts
}

void loop() {
  int reading = digitalRead(push_Knob_Pin);
  
  if (reading != lastButtonState) {
    // reset the debouncing timer
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    menu_state = 2;
    Serial.print("Push Knob Pulled Down state=");
    Serial.println(menu_state);
  }
  else {
    menu_state = 1;
  }
  
  if (oldEncPos != encoder_Pos) {
    Serial.print("new encoder pos=");
    Serial.println(encoder_Pos);
    oldEncPos = encoder_Pos;
  }

  if (menu_state == 1) {
    draw_color_menu(encoder_Pos);
  }
  else {
    draw_color(encoder_Pos);
  }

  delay(flash_delay);
  loop_counter++;
}

// draw each pixel in the ring with a different color on the color wheel
void draw_color_menu(int encoder_Pos) {
   for (int i=0; i<strip.numPixels(); i++) {
        if (i == (encoder_Pos % n) && (loop_counter % 2) == 0)
           strip.setPixelColor(i, 0,0,0);
        else strip.setPixelColor(i, Wheel(color_step * i));
  }
  strip.show();
}

void draw_color(int encoder_Pos) {
   for (int i=0; i<strip.numPixels(); i++) {
        strip.setPixelColor(i, Wheel(color_step * encoder_Pos));
  }
  strip.show();
  Serial.print("Drawing Color=");
  Serial.println(encoder_Pos * color_step);
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
   return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else if(WheelPos < 170) {
    WheelPos -= 85;
   return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  } else {
   WheelPos -= 170;
   return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  }
}
