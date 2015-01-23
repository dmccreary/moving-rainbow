
int motorPin = 5;  // This is the pin on the Arduino going to the motor controller

void setup() {
  pinMode(motorPin, OUTPUT);
}

void loop() {
  digitalWrite(motorPin, HIGH);  // turn the motor on
  delay(1000); // wait one second
  digitalWrite(motorPin, LOW); // turn the motor off
  delay(1000); // wait one second
}
