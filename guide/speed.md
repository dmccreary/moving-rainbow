# Changing Motor Speed with PWM
In this lab we will change motor speed using Pulse Wave Modulation (PWM).  We will read a value from a potentiometer and change the motor speed as the value changes.

To use this lab, connect the ends of a 10K potentiomer to the ground and +5 volts.  Then connect the center pin of the pot to the Analog pin 0 (A0) of the Arduino.  Then connect a male-female wire from Digital Pin 3 to one of the input pins of the motor control.  For this lab you can use any one of the four input pins.

```
int potPin = A0;   // select the input pin for the potentiometer
int motorPin = 3;  // select the pin for the motor - immutable
int potValue;      // variable to store the incomming value from the a potentiometer
int speed;         // The speed of our motor (0=stop, 255=full speed)

void setup() {
  pinMode(potPin, INPUT);
  pinMode(motorPin, OUTPUT);
}

void loop() {
  // read the value from the Potentiometer
  potValue = analogRead(potPin);
  
  // convert the range from 1 to 1023 in to 0 to 255 out
  speed = map(potValue, 0, 1023, 0, 255);
  
  // use PWM to change the speed
  analogWrite(motorPin, speed);
  
  // wait for 1/10 of a second before we continue
  delay(100);
}
```

Note that we can only use one of the 6 PWM pins (3, 5, 6, 9, 10 or 11) to control the speed.  The other digital outptus do not support PWM.

## More to Explore
While the program is running, try moving the wire from the digital output pin to any of the other input pins on the motor controller.  What happens?  Can you make both wheels move?  What direction are they moving?


