// Arduino single severn segment display with decimal point

// Define the LED digit patters, from 0 - 9
// Note that these patterns are for common cathode displays
// For common anode displays, change the 1's to 0's and 0's to 1's
// 1 = LED on, 0 = LED off, in this order:
//  Arduino pin: 5,6,7,8,9,10,11,12
// segments a (top), b (top right), c (bottom right), d (bottom)
// e (lower left), f (upper left), g (middle segment)
byte seven_seg_digits[10][7] = { 
   { 1,1,1,1,1,1,0 },  // = 0
   { 0,1,1,0,0,0,0 },  // = 1
   { 1,1,0,1,1,0,1 },  // = 2
   { 1,1,1,1,0,0,1 },  // = 3
   { 0,1,1,0,0,1,1 },  // = 4
   { 1,0,1,1,0,1,1 },  // = 5
   { 1,0,1,1,1,1,1 },  // = 6
   { 1,1,1,0,0,0,0 },  // = 7
   { 1,1,1,1,1,1,1 },  // = 8
   { 1,1,1,0,0,1,1 }   // = 9
};

int mode = 0; // This is the "mode" of the device.  It starts at 0 and gets incremented
byte newModeInc = 0; // set to 1 if we get an interrupt
int modeCount = 10; // The number of display modes, we mode the mode to get the actual mode

int decimal_pin = 12;
long lastDebounceTime = 0;  // the last time the output pin was toggled
long debounceDelay = 150;   // the debounce time; increase if the output flickers

void setup() {
  pinMode(2, INPUT_PULLUP);         
  pinMode(5, OUTPUT); // top a
  pinMode(6, OUTPUT); // upper right b
  pinMode(7, OUTPUT); // lower right c
  pinMode(8, OUTPUT); // bottom d
  pinMode(9, OUTPUT); // lower left e
  pinMode(10, OUTPUT); // upper left f
  pinMode(11, OUTPUT); // middle g
  pinMode(12, OUTPUT); // decimal point
  writeDot(LOW);  // start with the "dot" off
  attachInterrupt(0, changeModeInc, FALLING  ); // when pin 2 gets grounded
  Serial.begin(9600);
}

void writeDot(byte state) {
  digitalWrite(decimal_pin, state);
}
    
void sevenSegWrite(byte digit) {
  byte pin = 5;
  for (byte segCount = 0; segCount < 7; ++segCount) {
    digitalWrite(pin, seven_seg_digits[digit][segCount]);
    ++pin;
  }
}

void loop() {
  if (newModeInc == 1) {
    if ((millis() - lastDebounceTime) > debounceDelay) {
      mode++;
      mode = mode % modeCount;
      Serial.print("Inc Mode=");
      Serial.println(mode, DEC);
      digitalWrite(13, LOW);
      newModeInc = 0;
    }
    else {
    }
  };sevenSegWrite(mode); 
  writeDot(mode % 2); // make the decimal point go on odd numbers
  Serial.print("Mode =");
  Serial.println(mode);
  delay(100);
  digitalWrite(13, LOW); // show we have a new mode
}

// Interrupt service routine
void changeModeInc(){        
  digitalWrite(13, HIGH); //  show we have a new mode
  newModeInc = 1; // indicate we have a new increment mode
  lastDebounceTime = millis(); // record when we got the interrupt for debouncing
}
 
