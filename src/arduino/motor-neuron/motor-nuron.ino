#include <Adafruit_NeoPixel.h>
#include <avr/interrupt.h>

#define LEFT_PIN 5 // left branch
#define LEFT_COUNT 14

#define CENTER_PIN 6 // center branch
#define CENTER_COUNT 24

#define RIGHT_PIN 7 // right branch
#define RIGHT_COUNT 24

#define RING_PIN 8 // ring branch
#define RING_COUNT 12

#define MODEPIN 2 // pull down to groud to get a new mode
#define NUMBER_PIEXELS 12// connect the Data In pin

Adafruit_NeoPixel left_branch  = Adafruit_NeoPixel(LEFT_COUNT,   LEFT_PIN,   NEO_GRB + NEO_KHZ800);

Adafruit_NeoPixel center_banch = Adafruit_NeoPixel(CENTER_COUNT, CENTER_PIN, NEO_GRB + NEO_KHZ800);

Adafruit_NeoPixel right_branch = Adafruit_NeoPixel(RIGHT_COUNT,  RIGHT_PIN,  NEO_GRB + NEO_KHZ800);

Adafruit_NeoPixel ring         = Adafruit_NeoPixel(RING_COUNT,   RING_PIN,   NEO_GRB + NEO_KHZ800);

// hook up two momentary push buttons to pins 
volatile int newMode = 0; // the interrupts set this to 1 to indicate that we have a new mode on the way
volatile int mode = -1; // This gets incremented each button press
int waitTime = 70; //Typical delay between draws
int modeCount = 11; // The number of display modes

void setup() {
  left_branch.begin(); // sets up the memory for the LED strip
  center_banch.begin();
  right_branch.begin();
  ring.begin();
  
  pinMode(13, OUTPUT);     // Pin 13 is output to which an LED is connected
  digitalWrite(13, LOW);   // Make pin 13 low, switch LED off
  pinMode(2, INPUT_PULLUP);	   // Pin 2 is input to which a switch is connected = INT0
  pinMode(3, INPUT_PULLUP);	   // Pin 3 is input to which a switch is connected = INT1
  attachInterrupt(0, changeMode, RISING); // connect the mode to pin 2
  Serial.begin(9600);
  Serial.println("Start");
}

void changeMode(){        // Interrupt service routine
  digitalWrite(13, HIGH); // we have a new mode
  newMode = 1;
}

void loop() {
  // check to see if we should change the mode
  if (newMode == 1) {
      delay(waitTime); // wait for the switch to settle down used to de-bounce
      mode = (mode + 1) % modeCount;
      Serial.print("mode=");
      Serial.println(mode, DEC);
      digitalWrite(13, LOW);
      newMode = 0;
  }
  
  for (int i=0; i<LEFT_COUNT; i++) {
    left_branch.setPixelColor(i, 100, 100, 100);
    left_branch.show();
    delay(20);
    left_branch.setPixelColor(i, 0, 0, 0);
    left_branch.show();
  }
  
  for (int i=0; i<CENTER_COUNT; i++) {
    center_banch.setPixelColor(i, 100, 100, 100);
    center_banch.show();
    delay(20);
    center_banch.setPixelColor(i, 0, 0, 0);
    center_banch.show();
  }
  
  for (int i=0; i<RIGHT_COUNT; i++) {
    right_branch.setPixelColor(i, 100, 100, 100);
    right_branch.show();
    delay(20);
    right_branch.setPixelColor(i, 0, 0, 0);
    right_branch.show();
  }
  
  for (int i=0; i<RING_COUNT; i++) {
    ring.setPixelColor(i, 100, 100, 100);
    ring.show();
    delay(20);
    ring.setPixelColor(i, 0, 0, 0);
    ring.show();
  }

  
    
}


