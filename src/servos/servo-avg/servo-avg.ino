// servo with averaging
#include <Servo.h>
Servo myservo;  // create servo object to control a servo

int potpin = 0;  // analog pin used to connect the potentiometer
int val_avg, val1, val2, val3, val4, val_servo;    // variable to read the value from the analog pin

void setup()
{
  myservo.attach(12);  // attaches the servo on pin 12 to the servo object
  Serial.begin(9600); // Open serial monitor at 9600 baud to see ping results.
  Serial.print("Start");
  analogReference(EXTERNAL); // connect 5v to REF
}

void loop() 
{ 
  val1 = analogRead(potpin);  // reads the value of the potentiometer (value between 0 and 1023)
  delay(50);
  val2 = analogRead(potpin);
  delay(50);
  val3 = analogRead(potpin);
  delay(50);
  val4 = analogRead(potpin);
  val_avg = (val1 + val2 + val3 + val4) / 4; // calculate the average of 4 readings
  Serial.print("pot avg=");
  Serial.print(val_avg);
  
  val_servo = map(val_avg, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  Serial.print("  sev ang=");
  Serial.println(val_servo);
  myservo.write(val_servo); // sets the servo position according to the scaled value 
} 

