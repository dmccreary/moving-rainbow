#include <Adafruit_NeoPixel.h>
 
int sensorPin = A0; // note analog input
int numPixels = 12; // the number of pixels
int PIN = 10; // connect the Data In pin
 
// Parameter 1 = number of pixels in strip - I used 12
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_GRB     Pixels are wired for GRB bitstream
//   NEO_KHZ800  800 KHz bitstream (e.g. High Density LED strip)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(numPixels, PIN, NEO_GRB + NEO_KHZ800);

int newIndex = 0;
int oldIndex = 0;
int sensorValue = 0;
int sensorOffset = 77; // DC offset - the value of the sensor with no ambient noise
int maxSensorValue = 10; // the max value away from the offset
int maxEver; // The highest it has been since reset

// how many reading should be used to create an average?
// typical value is 5 to 10 readings
int avgCount = 10;

int absSensor; // the absolute value away from the DC offset

void setup() {
  
  // analogReference(EXTERNAL); // for 5 volt Arduinos like the Uno
  Serial.begin(9600);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}
 
void loop() {
  sensorValue = 0; // need to init at the top of each loop
  
  // get several values and average them to get rid of the noise
  for (int i=1; i<=avgCount; i++) {
    sensorValue += analogRead(sensorPin);
    delay(1); // wait a bit between reads
  };
  sensorValue = sensorValue / avgCount;
  
  Serial.print("s=");
  Serial.print(sensorValue);
  Serial.print(" ");
  
  // absolute value of the distance from the offset
  absSensor = abs(sensorValue - sensorOffset);
  Serial.print("a=");
  Serial.print(absSensor);
  Serial.print(" ");
  
  // make the sensor to the nth pixel - the index value
  newIndex = map(absSensor, 0, maxSensorValue, 0, numPixels - 1);
  
  // keep track of the highest level
  if (newIndex > maxEver)
     maxEver = newIndex;
    
  for (int i=0; i<=maxEver; i++) {
     if (newIndex >= i)
        strip.setPixelColor(i, 0, 0, 100); // make the new one blue
     else
          strip.setPixelColor(i, 5, 5, 5); // dim the old one
  };
  Serial.print(" i=");
  Serial.println(newIndex);
  strip.show();
  delay(100);
  oldIndex = newIndex;
}
