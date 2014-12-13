
// ping sensor
const int pingPin = 12;
int dist_in_cm = 120;

// LED for distance feedback
#include <Adafruit_NeoPixel.h>
#define LEDPIN 11 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);
int old_strip_index = 0;
int new_strip_index = 0;
// motor pins
int right_forward = 4;
int right_reverse = 5;
int left_forward = 7;
int left_reverse = 6;
// try this time to make a right turn
int delay_time_ninty_turn = 800;
// if we are under this distance, make a turn
int cm_for_turn = 10;
int delay_time_forward = 100;

void setup() {
  Serial.begin(9600);
  
  strip.begin();
  strip.setPixelColor(0, 10, 0, 0);
  strip.show();
  
  pinMode(pingPin, OUTPUT);
  
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
  Serial.println('Start');
}

void loop() {
  
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
    // turn on new value
     strip.setPixelColor(new_strip_index, 0, 0, 20);
     strip.show();
  };
  
  // if there is something in front, turn right
  if (dist_in_cm < cm_for_turn) {
      turn_right();
    } else {
      move_forward();
    }
  
  Serial.print(" new=");
  Serial.print(new_strip_index);

  delay(100);
  
}

void turn_right() {
  Serial.println("turning right");
  digitalWrite(right_forward, LOW);
  digitalWrite(right_reverse, HIGH);
  digitalWrite(left_forward, HIGH);
  digitalWrite(left_reverse, LOW);
  delay(delay_time_ninty_turn);
  
}

void move_forward() {
  Serial.println("moving forward");
  digitalWrite(right_forward, HIGH);
  digitalWrite(right_reverse, LOW);
  digitalWrite(left_forward, HIGH);
  digitalWrite(left_reverse, LOW);
  delay(delay_time_forward);
}


int get_distance_cm()
{
  long duration, inches, cm;
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

long microsecondsToInches(long microseconds)
{
  // According to Parallax's datasheet for the PING))), there are
  // 73.746 microseconds per inch (i.e. sound travels at 1130 feet per
  // second).  This gives the distance travelled by the ping, outbound
  // and return, so we divide by 2 to get the distance of the obstacle.
  // See: http://www.parallax.com/dl/docs/prod/acc/28015-PING-v1.3.pdf
  return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds)
{
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}
