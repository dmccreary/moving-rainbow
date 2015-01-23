int potPin = A0;    // select the input pin for the potentiometer
int motorPin = 3;   // The pin for the motor
int potValue = 0;   // variable to store the value from the pot

void setup() {
  pinMode(potPin, INPUT);
  pinMode(motorPin, OUTPUT);
}

void loop() {
  potValue = analogRead(potPin); // get the value from the pot
  speedValue = map(potValue, 0, 1023, 0, 255) // convert into proper range
  analogWrite(motorPin, speedValue); // set the speed
  delay(100); // wait 1/10th of a second
}