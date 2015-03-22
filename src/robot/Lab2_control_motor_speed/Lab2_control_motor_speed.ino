int potPin = A0;    // select the input pin for the potentiometer
int motorPin = 3;   // The pin for the motor
int potValue = 0;   // variable to store the value from the pot
int speedValue = 0;
void setup() {
  pinMode(potPin, INPUT);
  pinMode(motorPin, OUTPUT);
}

void loop() {
  potValue = analogRead(potPin);
  speedValue = map(potValue, 0, 1023, 0, 255);
  analogWrite(motorPin, speedValue);
  delay(100);
}
