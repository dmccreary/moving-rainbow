

int sensorPin = A0;    // select the input pin for the potentiometer
int ledPin = 13;      // select the pin for the LED
int sensorValue = 0;  // variable to store the value coming from the sensor
int max_SensorValue = 0;  // max value from sensor
int min_SensorValue = 1023;  // max value from sensor
int sample_count = 2;
int top_led = 0;

// the range of pins
int start_pin = 3;
int end_pin = 12;
void setup() {
  // declare the ledPin as an OUTPUT:
  for (int pin = start_pin; pin < top_led; pin++ )
    pinMode(pin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Sound Meter Test");
}

void loop() {
  sensorValue = 0;
  // sample the sensor sample_count times
  for (int s = 1; s <= sample_count; s++ ) {
     sensorValue += analogRead(sensorPin);
     delay(1);
  }
  sensorValue = sensorValue/sample_count;
  
  Serial.print("Sensor=");
  Serial.print(sensorValue);
  
  
  if (sensorValue < min_SensorValue)
     min_SensorValue = sensorValue;
  Serial.print(" Min=");
  Serial.print(min_SensorValue);

  if (sensorValue > max_SensorValue)
     max_SensorValue = sensorValue;
  Serial.print(" Max=");
  Serial.print(max_SensorValue);
  
  top_led = map(sensorValue, min_SensorValue, max_SensorValue, 0, 9);
  
  Serial.print(" top pin=");
  Serial.println(top_led);
  
  for (int pin = start_pin; pin <= top_led; pin++ )
    digitalWrite(pin, HIGH);
  delay(100);
  //for (int pin = start_pin; pin <= top_led; pin++ )
     //digitalWrite(pin, LOW);

}
