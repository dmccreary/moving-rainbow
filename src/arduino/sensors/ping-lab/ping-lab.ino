// 
// http://playground.arduino.cc/Code/NewPing
// Example NewPing library sketch that does a ping about 20 times per second.
// ---------------------------------------------------------------------------

#include <Adafruit_NeoPixel.h>
#include <NewPing.h>

#define LEDPIN 12 // connect the Data In pin
#define NUMBER_PIXELS 12// connect the Data In pin
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

#define TRIGGER_PIN  6  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     7  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.

unsigned int LED_index = 0;
unsigned int old_index1 = 0;
unsigned int old_index2 = 0;
unsigned int old_index3 = 0;
unsigned int uS = 0;
unsigned int distance_in_cm = 0;
unsigned int direction = 0;

void setup() {
  strip.begin(); // initialize memory for the LED strip
  strip.setPixelColor(0, 255, 0, 0); //
  strip.setPixelColor(1, 0, 255, 0); //
  strip.setPixelColor(2, 0, 0, 255); //
  strip.show();
  delay(1000);
  Serial.begin(9600); // Open serial monitor at 9600 baud to see ping results.
  Serial.print("Start");
}

void loop() {
  delay(50);                      // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  uS = sonar.ping(); // Send ping, get ping time in microseconds (uS).
  distance_in_cm = uS / US_ROUNDTRIP_CM;
  Serial.print("Ping: ");
  Serial.print(distance_in_cm); // Convert ping time to distance in cm and print result (0 = outside set distance range)
  Serial.print("cm ");
  
  // map from 
  LED_index = map(distance_in_cm, 0, 50, 0, NUMBER_PIXELS - 1) % NUMBER_PIXELS; // convert to index into LED strip
  
  // redraw only if we have a change
  if (LED_index != old_index1) {
    if (LED_index > old_index1)
      {
        direction = 1;
      }
      else {
         direction = -1;
      }
    Serial.print("Index=");
    Serial.println(LED_index); // Convert ping time to distance in cm and print result (0 = outside set distance range)
    for (int i=0; i < NUMBER_PIXELS; i++) {
      strip.setPixelColor(i, 0, 0, 0);
    };
    strip.setPixelColor(LED_index, 100, 100, 100); // turn redraw the new pixel
    strip.setPixelColor(LED_index - direction, 0, 0, 100); // recolor old pixel
    strip.setPixelColor(LED_index - direction * 2, 0, 0, 50); // turn off the old pixel
    strip.setPixelColor(LED_index - direction * 3, 0, 0, 10); // turn off the old pixel
    strip.show();
    
    old_index1 = LED_index;
    old_index2 = old_index1;
    old_index3 = old_index2;
    strip.show();
  };
  
}
