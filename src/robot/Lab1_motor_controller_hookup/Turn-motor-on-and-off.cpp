int motorPin = 5;    // one of the inputs on the motor controller (L293D)

void setup() {
  pinMode(motorPin, OUTPUT);
}

void loop() {
  digitalWrite(motorPin, HIGH);  // turn the motor on
  delay(1000); // wait 1 second
  digitalWrite(motorPin, LOW);  // turn the motor off
  delay(1000); // wait 1 second
}