#include <avr/interrupt.h>

// hook up two momentary push buttons to pins 
volatile int newModePlus; // the interrupts set this to 1 to indicate that we have a new mode on the way
volatile int newModeMinus;
volatile int mode; // This gets incremented each button press

void setup()
{
  pinMode(13, OUTPUT);     // Pin 13 is output to which an LED is connected
  digitalWrite(13, LOW);   // Make pin 13 low, switch LED off
  pinMode(2, INPUT_PULLUP);	   // Pin 2 is input to which a switch is connected = INT0
  pinMode(3, INPUT_PULLUP);	   // Pin 3 is input to which a switch is connected = INT1
  attachInterrupt(0, changeModeAdd, RISING  ); // pin 2
  attachInterrupt(1, changeModeMinus, RISING  ); // pin 3
  Serial.begin(9600);
  Serial.println("Start");
}

void loop() {
  if (newModePlus == 1) {
      Serial.print("Next Mode=");
      Serial.println(mode, DEC);
      digitalWrite(13, LOW);
      newModePlus = 0;
  }
  
  if (newModeMinus == 1) {
      Serial.print("Pref Mode=");
      Serial.println(mode, DEC);
      digitalWrite(13, LOW);
      newModePlus = 0;
  }
}  


void changeModeAdd(){        // Interrupt service routine
  digitalWrite(13, HIGH); // we have a new mode
  newModePlus = 1;
  mode++;
}

void changeModeMinus(){        // Interrupt service routine
  digitalWrite(13, HIGH); // we have a new mode
  newModeMinus = 1;
  mode--;
}
