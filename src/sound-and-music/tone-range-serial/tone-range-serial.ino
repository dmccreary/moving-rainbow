int sensorValue;
int frequency;
int speaker_pin = 3;

void setup() {
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  sensorValue = analogRead(A0);

  // scale the value to the range used by tone()
  // tone can go from 31 to 65535 but the must useful tones are 100 to 5,000 Htz using a piezo crystal
  frequency = map(sensorValue, 0, 1023, 100, 5000);
  
  // print out the value you read:
  Serial.print("Pot value=");
  Serial.print(sensorValue);
  Serial.print("  tone frequency=");
  Serial.println(frequency);
  
  tone(speaker_pin, frequency);
  delay(100); // wait for a 1/10th of second
}
