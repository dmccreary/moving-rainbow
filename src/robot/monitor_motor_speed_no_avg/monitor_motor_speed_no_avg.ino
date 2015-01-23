int potPin = A0;    // select the input pin for the potentiometer
int photosensorPin = A3;    // select the input pin for the potentiometer
int motorPin = 5;    // select the pin for the LED

int potValue = 0;  // variable to store the value coming from the sensor
int speedValue = 0;
int photoSensorValue = 0;
int displayValue = 0;

void setup() {
  pinMode(potPin, INPUT);
  pinMode(photosensorPin, INPUT_PULLUP);
  pinMode(motorPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
   potValue = analogRead(potPin); // get the value from the Potentiometer
   speedValue = map(potValue, 0, 1023, 0, 255);  // convert to the right range
   analogWrite(motorPin, speedValue);  // set the motor speed
   photoSensorValue = analogRead(photosensorPin);
    displayValue = map(photoSensorValue, 90, 220, 0, 100);
    Serial.print(photoSensorValue);
    for (int i=0; i < displayValue; i++)
      Serial.print("-");
    Serial.println("");
  }

