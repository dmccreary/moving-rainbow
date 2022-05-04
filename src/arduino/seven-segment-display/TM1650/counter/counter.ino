#include <Wire.h>
#include <TM1650.h>

TM1650 d;
int counter = 0;
char time_array[5] = "helo";
String counter_string;

void setup() 
{
  Wire.begin(); //Join the bus as master
  Serial.begin(9600);
  Serial.println("TM1650 Example Code");
  d.init();
  d.setBrightness(TM1650_MIN_BRIGHT);
  d.displayOn();
  d.displayString(time_array);
  delay(2000);
}

void loop() 
{
  counter_string =  String(counter, DEC);
  // this does not work d.displayString(counter_string);
  // so I tried to copy the string to the buffer
  // strncpy(time_array, counter_string, 4);
  time_array[3] = char(48 + (counter % 10));
  time_array[2] = char(48 + (counter / 10) % 10);
  time_array[1] = char(48 + (counter / 100) % 10);
  time_array[0] = char(48 + (counter / 1000) % 10);
  
  d.displayString(time_array);
  delay(100);
  if (counter > 9999)
    counter = 0;
  counter++;
}




