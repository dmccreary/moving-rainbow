// Date and time functions using a DS1307 RTC connected via I2C and Wire lib
#include <Wire.h>
#include "RTClib.h"

RTC_DS1307 rtc;

char daysOfTheWeek[8][12] = {"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};

void setup () {
  while (!Serial); // for Leonardo/Micro/Zero

  Serial.begin(57600);
  if (! rtc.begin()) {
    Serial.println("Couldn't find RTC");
    while (1);
  }

  if (! rtc.isrunning()) {
    Serial.println("RTC is NOT running!");
    // following line sets the RTC to the date & time this sketch was compiled
    // rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
    // This line sets the RTC with an explicit date & time, for example to set
    // January 21, 2014 at 3am you would call:
    rtc.adjust(DateTime(2016, 12, 24, 13, 45, 0));
  }
}

void loop () {
    DateTime now = rtc.now();

    Serial.print("Current Time: y=");
    Serial.print(now.year(), DEC);
    Serial.print(" month=");
    // WTF?
    Serial.print(now.month() - 1, DEC);
    Serial.print(" day=");
    Serial.print(now.day(), DEC);
    Serial.print(" day-of-week=");
    Serial.print(now.dayOfTheWeek(), DEC);
    // WTF?
    Serial.print(" day-of-week-string=");
    Serial.print(daysOfTheWeek[now.dayOfTheWeek() - 2]);
    Serial.print(" hour=");
    Serial.print(now.hour(), DEC);
    Serial.print(" min=");
    Serial.print(now.minute(), DEC);
    Serial.print(" sec=");
    Serial.print(now.second(), DEC);

    Serial.println();
    delay(3000);
}
