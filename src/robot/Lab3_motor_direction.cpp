int potPin = A0; // the pin for the potentiometer
int motorAForwardPin = 3;  // Pin to make the motor go forward
int motorABackwardPin = 5; // Pin to make the motor go backward
// one of the inputs on the Motor controller
int potValue = 128;  // variable to store the value coming from the sensor
int speedValue = 0; // variable to store the value going to the motor

void setup() { 
   pinMode(potPin, INPUT);  
   pinMode(motorAForwardPin, OUTPUT);
   pinMode(motorABackwardPin, OUTPUT);
   Serial.begin(9600);
}

void loop() {
   potValue = analogRead(potPin); // get the value from the Potentiometer from 0 to 1023
   Serial.print("pot=");
  Serial.print(potValue);
   if (potValue < 512) { // we will go backward if the value us under this
      speedValue = map(potValue, 0, 511, 255, 0);  // convert to the right range
      Serial.print(" speed backward=");
      Serial.println(speedValue);
      analogWrite(motorABackwardPin, speedValue); // go back this speed
      analogWrite(motorAForwardPin, 0);
 } else {
   speedValue = map(potValue, 512, 1023, 0, 255);  
   Serial.print(" speed forward=");
   Serial.println(speedValue);
   analogWrite(motorAForwardPin, speedValue);  // go forward this speed
   analogWrite(motorABackwardPin, 0);
 }
delay(100); // sample ever 1/10th of a second
}
