#include <Servo.h>
Servo myservo; 
int sensorPin = A0;    // select the input pin for the flex sensor.  Use a 10K resistor to pull it up.
int sensorValue = 0;  // variable to store the value coming from the sensor
int angle = 0;

void setup() {
  Serial.begin(9600);
  myservo.attach(4);
}

void loop() {
  sensorValue = analogRead(sensorPin);
  angle = map(sensorValue, 650, 850, 0, 180);
  Serial.print("sensor=");
  Serial.print(sensorValue, DEC);
  Serial.print(" angle=");
  Serial.println(angle, DEC);
  myservo.write(angle);
  
  delay(200);
}
