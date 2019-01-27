// servo with averaging
#include <Servo.h>
Servo myservo;  // create servo object to control a servo

#define POT_PIN A0
#define SERVO_PIN 12
#define SAMPLE_DELAY 30
// analog pin used to connect the potentiometer
int val_avg, val1, val2, val3, val4, val5;    // variable to read the value from the analog pin

void setup()
{
  myservo.attach(SERVO_PIN);  // attaches the servo on pin 12 to the servo object
  Serial.begin(9600); // Open serial monitor at 9600 baud to see ping results.
  Serial.print("Start");
}

void loop() {
  // read 5 values at 50ms intervals and take an average
  val1 = analogRead(POT_PIN);  // reads the value of the potentiometer (value between 0 and 1023)
  delay(SAMPLE_DELAY);
  val2 = analogRead(POT_PIN);
  delay(SAMPLE_DELAY);
  val3 = analogRead(POT_PIN);
  delay(SAMPLE_DELAY);
  val4 = analogRead(POT_PIN);
  delay(SAMPLE_DELAY);
  val5 = analogRead(POT_PIN);
  
  val_avg = (val1 + val2 + val3 + val4 + val5) / 5; // calculate the average of 5 readings

  Serial.print("val1=");
  Serial.print(val1);
  
  Serial.print(" pot avg=");
  Serial.print(val_avg);
  
  val_avg = map(val_avg, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  Serial.print(" Angle average =");
  Serial.println(val_avg);
  myservo.write(val_avg);
  delay(15);
} 
