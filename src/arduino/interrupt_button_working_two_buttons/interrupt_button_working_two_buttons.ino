#include <avr/interrupt.h>

volatile int state;
volatile int counter;

void setup()
{
  pinMode(13, OUTPUT);     // Pin 13 is output to which an LED is connected
  digitalWrite(13, LOW);   // Make pin 13 low, switch LED off
  pinMode(2, INPUT_PULLUP);	   // Pin 2 is input to which a switch is connected = INT0
  pinMode(3, INPUT_PULLUP);	   // Pin 3 is input to which a switch is connected = INT1
  attachInterrupt(0, blink1, RISING  ); // pin 2
  attachInterrupt(1, blink2, RISING  ); // pin 3
  Serial.begin(9600);
  Serial.println("Start");
}

void loop() {
  if (state == 1) {
      Serial.print("State=");
      Serial.print(state, DEC);
      Serial.print(" Counter=");
      Serial.println(counter, DEC);
      delay(200);
      counter++;
      state = 0;
  }
}  


void blink1(){              // Interrupt service routine
  digitalWrite(13, HIGH);
  state = 1;
}

void blink2(){              // Interrupt service routine
  digitalWrite(13, LOW);
  state = 1;
}
