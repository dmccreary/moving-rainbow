#include <Adafruit_NeoPixel.h>
#include <avr/interrupt.h>

#define LEFT_PIN 5 // left branch
#define LEFT_COUNT 2
4


#define CENTER_PIN 6 // center branch
#define CENTER_COUNT 24

#define RIGHT_PIN 7 // right branch
#define RIGHT_COUNT 24


#define RING_PIN 8 // ring branch
#define RING_COUNT 24

#define MODEPIN 2 // pull down to groud to get a new mode
#define NUMBER_PIEXELS 12// connect the Data In pin

Adafruit_NeoPixel left_branch  = Adafruit_NeoPixel(LEFT_COUNT,   LEFT_PIN,   NEO_GRB + NEO_KHZ800);

Adafruit_NeoPixel center_banch = Adafruit_NeoPixel(CENTER_COUNT, CENTER_PIN, NEO_GRB + NEO_KHZ800);

Adafruit_NeoPixel right_branch = Adafruit_NeoPixel(RIGHT_COUNT,  RIGHT_PIN,  NEO_GRB + NEO_KHZ800);

Adafruit_NeoPixel ring         = Adafruit_NeoPixel(RING_COUNT,   RING_PIN,   NEO_GRB + NEO_KHZ800);

// hook up two momentary push buttons to pins 
volatile int mode = 0; // This gets incremented each button press
int waitTime = 70; //Typical delay between draws
int modeCount = 6; // The number of display modes

void setup() {
  left_branch.begin(); // sets up the memory for the LED strip
  center_banch.begin();
  right_branch.begin();
  ring.begin();
  
  pinMode(13, OUTPUT);     // Pin 13 is output to which an LED is connected
  digitalWrite(13, LOW);   // Make pin 13 low, switch LED off
  pinMode(2, INPUT_PULLUP);	   // Pin 2 is input to which a switch is connected = INT0

  attachInterrupt(0, changeMode, RISING); // connect the mode to pin 2
  Serial.begin(9600);
  Serial.println("Start");
}

void changeMode(){        // Interrupt service routine
  digitalWrite(13, HIGH); // we have a new mode
  mode = (mode + 1) % modeCount;
  loop();
}

void loop() {  
  switch (mode) {
       case 0: driftUp(); break;
       case 1: bubbleUp(255, 0, 0); break;
       case 2: bubbleUp(255, 125, 0); break;
       case 3: bubbleUp(255, 255, 0); break;
       case 4: bubbleUp(0, 0, 255); break;
       case 5: bubbleUp(255, 0, 255); break;
   }
    
   Serial.print("mode=");
   Serial.println(mode);
}

void bubbleUp(int red, int green, int blue) {
  // make the ring spin  
  for (int i=0; i<RING_COUNT; i++) {
    ring.setPixelColor(i, red, green, blue);
    ring.show();
    delay(50);
    ring.setPixelColor(i, 0, 0, 0);
    ring.show();
  }
  ringSparkOn(red, green, blue);
  
  // make the color move up all three branches
  for (int i=0; i<24; i++) {
      // draw a point
      left_branch.setPixelColor(i, red, green, blue);
      center_banch.setPixelColor(i, red, green, blue);
      right_branch.setPixelColor(i, red, green, blue);
      left_branch.show();
      center_banch.show();
      right_branch.show();
      delay(50);
      left_branch.setPixelColor(i, 0, 0, 0);
      center_banch.setPixelColor(i, 0, 0, 0);
      right_branch.setPixelColor(i, 0, 0, 0);
      left_branch.show();
      center_banch.show();
      right_branch.show();
    }
    
    ringSparkOff();
    
}

void ringSparkOn(int red, int green, int blue) {
  // turn the entire ring on this color
    for (int i=0; i<RING_COUNT; i++) {
      ring.setPixelColor(i, red, green, blue);
      ring.show();
    }
}

void ringSparkOff() {
  // turn the entire ring on this color
    for (int i=0; i<24; i++) {
      ring.setPixelColor(i, 0, 0, 0);
    }
}

void driftUp() {
  // turn the entire ring on this color
    for (int i=0; i<RING_COUNT; i++) {
      ring.setPixelColor((i % 12), 25, 25, 25);
      left_branch.setPixelColor(i, 25, 25, 25);
      center_banch.setPixelColor(i, 25, 25, 25);
      right_branch.setPixelColor(i, 25, 25, 25);
      ring.show();
      left_branch.show();
      center_banch.show();
      right_branch.show();
      delay(250);
      ring.setPixelColor((i % 12), 0, 0, 0);
      left_branch.setPixelColor(i, 0, 0, 0);
      center_banch.setPixelColor(i, 0, 0, 0);
      right_branch.setPixelColor(i, 0, 0, 0);
      ring.show();
      left_branch.show();
      center_banch.show();
      right_branch.show();
    }
}
