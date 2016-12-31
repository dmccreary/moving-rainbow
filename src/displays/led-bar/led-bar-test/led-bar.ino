
// the range of pins
int start_pin = 3;
int end_pin = 12;
int delay_time = 100;
void setup() {
  // declare the ledPin as an OUTPUT:
  for (int pin = start_pin; pin <= end_pin; pin++ )
    pinMode(pin, OUTPUT);
  Serial.begin(9600);
  Serial.println("LED Bar Test");
}

void loop() {
  
  // turn them on, one-by-one
  for (int pin = end_pin; pin >= start_pin; pin-- ) {
    digitalWrite(pin, HIGH);
    delay(delay_time);
  }
  // turn them off, one-by-one
   for (int pin = start_pin; pin <= end_pin; pin++ ) {
    digitalWrite(pin, LOW);
    delay(delay_time);
  }
}
