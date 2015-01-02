
// ping sensor
const int pingPin = 12;
int dist_in_cm = 120;

// This LED strip is used for distance feedback
// The closer we get to an object in front of us, the further up the blue pixel is on
#include <Adafruit_NeoPixel.h>
#define LEDPIN 11 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

int old_strip_index = 0;
int new_strip_index = 0;
int power_turn_level = 255; /* full power on turns */

// adjust these till the robot goes streight to compensate for motor differences
int power_forward_right = 140; /* half power on turns */
int power_forward_left = 120; /* half power on turns */

// motor pins.  Note that only pins 2,5,6, 9 and 10 can be used for pwm
int right_forward = 3;
int right_reverse = 5;
int left_forward = 9;
int left_reverse = 6;

// try this time to make a right turn just above 90 degrees
int delay_time_ninty_turn = 200;
// if we are under this distance, make a turn
int cm_for_turn = 10;
int delay_time_forward = 100;

void setup() {
  Serial.begin(9600);
  
  strip.begin();
  strip.setPixelColor(0, 10, 0, 0);
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
  delay(1000);
}

void loop() {
  
  delay(100);
  
  // get the distance from the ping sensor in CM
  dist_in_cm = get_distance_cm();
  new_strip_index = dist_in_cm / 5;
  
  // don't go over the max
  if (new_strip_index > (NUMBER_PIEXELS - 1)) {
    new_strip_index = 11;
  }
  
  // only draw if there is a change
  if ( old_strip_index != new_strip_index) {
    // erase the old strip
     for (int i=0; i < NUMBER_PIEXELS; i++)
        strip.setPixelColor(i, 0, 0, 0);
    // turn on new value to a light blue
     strip.setPixelColor(new_strip_index, 0, 0, 30);
     strip.show();
  };
  
  // if there is something in front, turn right
  if (dist_in_cm < cm_for_turn) {
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
