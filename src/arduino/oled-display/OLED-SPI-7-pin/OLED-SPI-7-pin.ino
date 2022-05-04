/* 
 * Demo for SSD1306 based 128x64 OLED module using Adafruit SSD1306 
 * library (https://github.com/adafruit/Adafruit_SSD1306).
 * 
 * See https://github.com/pacodelgado/arduino/wiki/SSD1306-based-OLED-connected-to-Arduino 
 * for more information.
 *
 */
 
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// If using software SPI (the default case):
#define OLED_CLK   12   //D0
#define OLED_MOSI  11   //D1
#define OLED_RESET 10   // RSt
#define OLED_DC    9    // DC
#define OLED_CS    8    //CS


Adafruit_SSD1306 display(OLED_MOSI, OLED_CLK, OLED_DC, OLED_RESET, OLED_CS);

void setup()   {                
//  Serial.begin(9600);
  display.begin(SSD1306_SWITCHCAPVCC);
  display.display();
  delay(1000);
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
}

void loop()
{
  static unsigned long thisMicros = 0;
  static unsigned long lastMicros = 0;
  display.clearDisplay();
  display.setCursor(5,10);

  display.print(thisMicros - lastMicros);
  display.print(" u-sec");
  display.display();
  lastMicros = thisMicros;
  thisMicros = micros();
}

