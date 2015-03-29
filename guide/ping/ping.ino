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
  
  // use PWM to 
  analogWrite(motorPin, speed);
  
  // wait for 1/10 of a second before we continue
  delay(100);
}
