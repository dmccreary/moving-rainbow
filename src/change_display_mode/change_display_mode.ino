#include <avr/interrupt.h>

// hook up two momentary push buttons to pins 
volatile int newMode; // the interrupts set this to 1 to indicate that we have a new mode on the way
volatile int mode; // This gets incremented each button press

void setup()
{
  pinMode(13, OUTPUT);     // Pin 13 is output to which an LED is connected
  digitalWrite(13, LOW);   // Make pin 13 low, switch LED off
  pinMode(2, INPUT_PULLUP);	   // Pin 2 is input to which a switch is connected = INT0
  pinMode(3, INPUT_PULLUP);	   // Pin 3 is input to which a switch is connected = INT1
  attachInterrupt(0, changeMode, RISING  ); // pin 2
  Serial.begin(9600);
  Serial.println("Start");
}

void loop() {
  if (newMode == 1) {
      Serial.print("Mode=");
      Serial.println(mode, DEC);
      delay(200); // wait for the switch to settle down used to de-bounce
      mode++;
      digitalWrite(13, LOW);
      newMode = 0;
  }
}  


void changeMode(){        // Interrupt service routine
  digitalWrite(13, HIGH); // we have a new mode
  newMode = 1;
}
