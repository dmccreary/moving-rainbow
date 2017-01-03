#include "Wire.h"
#include <TM1650.h>

// connect your 4-digit display up to A4 and A5
#define DS3231_I2C_ADDRESS 0x68

// data structure for the TM1650 display driver
// https://github.com/arkhipenko/TM1650
// http://playground.arduino.cc/Main/TM1650
// http://www.datasheetcafe.com/tm1650-datasheet-led-controller/
TM1650 d;

char time_array[5] = "hElo";
int counter = 2000;

void setup()
{
  Wire.begin();
  Serial.begin(9600);
  d.init();
  d.setBrightness(TM1650_MIN_BRIGHT);
  d.displayOn();
  d.displayString(time_array);
  delay(1000);
}

void loop() {
  time_array[0] = char(48 + (counter/1000 % 10));
  time_array[1] = char(48 + (counter/100 % 10));
  time_array[2] = char(48 + (counter/10 % 10));
  time_array[3] = char(48 + (counter % 10));
//  if (counter % 2)
//     d.controlPosition(3, 8); // this turns on the colon between the digits
//  else d.controlPosition(3, 0);
  d.displayString(time_array);
  Serial.println(counter);
  delay(1000);
  if (counter == 0) {
       counter = 2000;
       sound_alarm();
  };
    
  counter--;
}

void sound_alarm() {
  // play a sound on the speaker
}

