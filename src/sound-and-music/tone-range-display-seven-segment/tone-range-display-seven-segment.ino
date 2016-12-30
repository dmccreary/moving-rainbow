#include <Wire.h> // Include the Arduino SPI library
#include <TM1650.h>
TM1650 d;

int sensorValue;
int frequency;
int speaker_pin = 3;

char display_array[5] = "helo";

void setup() {
  Wire.begin();  // Initialize hardware I2C pins
  d.init();
  d.setBrightness(TM1650_MIN_BRIGHT);
  d.displayOn();
  d.displayString(display_array);
  Serial.begin(9600);
  Serial.println("Using TM1650 seven segment display library");
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  sensorValue = analogRead(A0);

  // scale the value to the range used by tone()
  // tone can go from 31 to 65535 but the must useful tones are 100 to 5,000 Htz using a piezo crystal
  frequency = map(sensorValue, 5, 1023, 100, 5000);
  
  // print out the value you read:
  Serial.print("Pot value=");
  Serial.print(sensorValue);
  Serial.print("  tone frequency=");
  Serial.println(frequency);

  // send the frequency to the display
  display_array[3] = char(48 + (frequency % 10));
  display_array[2] = char(48 + (frequency / 10) % 10);
  display_array[1] = char(48 + (frequency / 100) % 10);
  display_array[0] = char(48 + (frequency / 1000) % 10);
  d.displayString(display_array);

  // only send if the sensor value is above 3
  if (sensorValue > 3)
    tone(speaker_pin, frequency);
  else noTone(100); // silence
  
  delay(100); // wait for a 1/10th of second
}
