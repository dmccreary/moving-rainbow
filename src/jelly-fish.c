//http://www.instructables.com/id/The-LED-Strip-Jellyfish-Costume-with-Arduino-LPD88/step5/CODE/
#include "LPD8806.h"
#include "SPI.h"

//s1 variables
LPD8806 s1 = LPD8806(160,2,3);
int s1track[200];
unsigned int s1ti = 0;
unsigned int s1tf = 0;
int sx = 0;
//CONTROLS;
int s1speed = 50; //How far apart are the patterns on a single line?
int s1sep = 30; //How many LEDS in between each pattern?

void setup() {
  Serial.begin(9600);
  s1.begin();
  for (int i = 0; i < s1.numPixels()+40; i++) {
    s1track[i] = 0;
  }
  for (int i = 0; i < s1.numPixels(); i++) {
    s1.setPixelColor(i, s1.Color(127,0,0));
  }
  s1.show();
}

void loop() {
  //s1speed = analogRead(A0);
  //s1speed = map(s1speed,0,1023,10,500);
  //Serial.println(s1speed);
  s1strip();
  s1.show();
}

void s1strip() {
    if (s1ti == 0) { s1ti = millis(); }
  s1tf = millis();
  if ( s1tf-s1ti >= s1speed ) {
    Serial.println(s1speed);
    s1ti = millis();
    if (sx == 0) {
      s1track[0] = 1;
    }
    for (int i = 0; i < s1.numPixels()+40; i++) {
      if (s1track[i] == 1) {
        s1track[i] = 2;
        for (int z = 0; z < 3; z++) {
          s1.setPixelColor(i-z,s1.Color(0,0,127));
        }
        for (int z = 3; z < 8; z++) {
          s1.setPixelColor(i-z,s1.Color(127,0,127));
        }
        for (int z = 8; z < 11; z++) {
          s1.setPixelColor(i-z,s1.Color(127,0,0));
        }
        for (int z = 11; z < 13; z++) {
          s1.setPixelColor(i-z,s1.Color(0,0,0));
        }
        for (int z = 13; z < 14; z++) {
          s1.setPixelColor(i-z,s1.Color(127,0,0));
        }       
      }
    }
    for (int i = 0; i < s1.numPixels()+40; i++) {
      if (s1track[i] == 2) {
        s1track[i] = 0;
        s1track[i+1] = 1;
      }
    }
    sx++;
    if (sx == s1sep) {
      sx = 0;
    }
  }
}