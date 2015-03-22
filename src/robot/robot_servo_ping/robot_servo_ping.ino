#include <Servo.h>
#include <Adafruit_NeoPixel.h>
// the pin that the servo is on
const int servoPin = 11;
// ping sensor
const int pingPin = 10;
const int ledPin = 12; // the pin that the LED strip is on
const int numberPixels = 10;

int dist_in_cm = 120;
Servo myservo;  // create servo object to control a servo 
int servoInitPos = 90;    // variable to store the servo position 
// This LED strip is used for distance feedback
// The closer we get to an object in front of us, the further up the blue pixel is on

Adafruit_NeoPixel strip = Adafruit_NeoPixel(numberPixels, ledPin, NEO_GRB + NEO_KHZ800);

int old_strip_index = 0;
int new_strip_index = 0;
int power_turn_level = 150; /* full power on turns */

// adjust these till the robot goes streight to compensate for motor differences
int power_forward_right = 180; /* half power on turns */
int power_forward_left = 180; /* half power on turns */

// motor pins.  Note that only pins 2,5,6, 9 and 10 can be used for pwm
int right_forward = 5;
int right_reverse = 3;
int left_forward = 6;
int left_reverse = 9;

// try this time to make a right turn just above 90 degrees
int delay_time_ninty_turn = 200;
// if we are under this distance, make a turn
int cm_for_turn = 10;
int delay_time_forward = 100;
int look_delay = 1000;

void setup() {
  Serial.begin(9600);
  
  strip.begin();
  // make the front pixel red
  strip.setPixelColor(numberPixels - 1, 10, 0, 0);
  // make the back pixel green
  strip.setPixelColor(0, 0, 10, 0);
  strip.show();
  
  pinMode(pingPin, INPUT);
  
  pinMode(right_forward, OUTPUT);
  pinMode(right_reverse, OUTPUT); 
  pinMode(left_forward, OUTPUT); 
  pinMode(left_reverse, OUTPUT);
  // turn all off
  digitalWrite(right_forward, LOW);
  digitalWrite(right_reverse, LOW);
  digitalWrite(left_forward, LOW);
  digitalWrite(left_reverse, LOW);
  // for debugging
  // Serial.println('Start');
  myservo.attach(servoPin);  // attaches the servo on pin 11 to the servo object 
  myservo.write(servoInitPos); // the servo scans from 0 to 180
  delay(1000); // wait to see that we are good to go
}

void loop() {
  myservo.write(servoInitPos);
  delay(100);
  
  // get the distance from the ping sensor in CM
  dist_in_cm = get_distance_cm();
  
  // we are counting 0 in the rear
  new_strip_index = numberPixels - (dist_in_cm / 5);
  
  // don't go over the max distance
  if (new_strip_index < 0) {
    new_strip_index = 0;
  }
  
  // only draw if there is a change
  if ( old_strip_index != new_strip_index) {
    // erase the old strip
     for (int i=0; i < numberPixels; i++)
        strip.setPixelColor(i, 0, 0, 0);
    // turn on new value to a light blue
     strip.setPixelColor(new_strip_index, 0, 0, 30);
     strip.show();
  };
  
  // if there is something in front, turn right
  if (dist_in_cm < cm_for_turn) {
      stop();
      // look left
      myservo.write(0);
      delay(look_delay);
      // look front
      myservo.write(90);
      delay(look_delay);
      // look right
      myservo.write(180);
      delay(look_delay);
      turn_right();
    } else {
      move_forward();
    }
  
  // Serial.print(" new=");
  // Serial.print(new_strip_index);

}

void turn_right() {
  Serial.println("turning right");
  analogWrite(right_forward, LOW);
  analogWrite(right_reverse, power_turn_level);
  analogWrite(left_forward, power_turn_level);
  analogWrite(left_reverse, LOW);
  delay(delay_time_ninty_turn);
}

void turn_left() {
  Serial.println("turning right");
  analogWrite(right_forward, LOW);
  analogWrite(right_reverse, power_turn_level);
  analogWrite(left_forward, power_turn_level);
  analogWrite(left_reverse, LOW);
  delay(delay_time_ninty_turn);
}

void stop() {
  Serial.println("stop");
  analogWrite(right_forward, LOW);
  analogWrite(right_reverse, LOW);
  analogWrite(left_forward, LOW);
  analogWrite(left_reverse, LOW);
}

void move_forward() {
  Serial.println("moving forward");
  analogWrite(right_forward, power_forward_right);
  analogWrite(right_reverse, LOW);
  analogWrite(left_forward, power_forward_left);
  analogWrite(left_reverse, LOW);
  delay(delay_time_forward);
}


int get_distance_cm()
{
  long duration, cm=0;
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);
  // The same pin is used to read the signal from the PING))): a HIGH
  // pulse whose duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(pingPin, INPUT);
  duration = pulseIn(pingPin, HIGH);
  // convert the time into a distance
  cm = microsecondsToCentimeters(duration);
  Serial.print(" cm=");
  Serial.println(cm);
  return cm;
}

long microsecondsToCentimeters(long microseconds)
{
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}
