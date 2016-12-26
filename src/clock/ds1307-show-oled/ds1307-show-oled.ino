// Date and time functions using a DS1307 RTC connected via I2C and Wire lib
#include <Wire.h>
#include "RTClib.h"
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

RTC_DS1307 rtc;
#define OLED_RESET 4
Adafruit_SSD1306 display(OLED_RESET);


char daysOfTheWeek[8][12] = {"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};

int counter = 10;
int clock_down = 30;
int twelve_hour = 0;

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
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
    // This line sets the RTC with an explicit date & time, for example to set
    // January 21, 2014 at 3am you would call:
    // rtc.adjust(DateTime(2016, 12, 24, 13, 45, 0));
  }

   display.begin(SSD1306_SWITCHCAPVCC, 0x3C);

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

    
   
    display.clearDisplay();
    display.drawPixel(now.second() * 2, 10, WHITE);
   

    display.setTextSize(2);
    display.setTextColor(WHITE);

    // hour
    // calculate 12 hour time
    twelve_hour = now.hour() % 12;
    display.setCursor(20,clock_down);
    if (twelve_hour < 10) display.print(" ");
    display.print(twelve_hour);
    
    // min
    display.setCursor(45,clock_down);
    display.print(":");
    if (now.minute() < 10) display.print("0");
    display.print(now.minute());

    // sec
   
    display.setCursor(80,clock_down);
    display.print(":");
    if (now.second() < 10) display.print("0");
    display.print(now.second());
    display.display();
     
    delay(1000);
    counter++;
}
