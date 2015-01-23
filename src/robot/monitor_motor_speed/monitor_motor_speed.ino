int potPin = A0;    // select the input pin for the potentiometer
int motorPinA = 5;    // select the pin for the LED
int motorPinB = 7;    // select the pin for the LED

int potValue = 0;  // variable to store the value coming from the sensor

void setup() {
  pinMode(potPin, INPUT);
  pinMode(motorPinA, OUTPUT);
  pinMode(motorPinA, OUTPUT);
}

void loop() {
  // read the value from the Potentiometer
  potValue = analogRead(sensorPin);
  // turn the ledPin on
  digitalWrite(ledPin, HIGH);
  // stop the program for <sensorValue> milliseconds:
  delay(sensorValue);
  // turn the ledPin off:
  digitalWrite(ledPin, LOW);
  // stop the program for for <sensorValue> milliseconds:
  delay(sensorValue);
}
