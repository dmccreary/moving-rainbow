#include <Arduino.h>
#include <SPI.h>
#include <Wire.h>
#include "U8glib.h"

/* Create an instance for the SSD1306 OLED display in SPI mode 
 * connection scheme: 
 *   D0=sck=Pin 12 
 *   D1=mosi=Pin 11 
 *   CS=Pin 8 
 *   DC=A0=Pin 9
 *   Reset=Pin 10
 */
#define CLOCK_PIN 13
#define DATA_PIN 11
#define RESET_PIN 8
#define DC_PIN 9
#define CS_PIN 10

// https://forum.arduino.cc/index.php?topic=442255.0
U8GLIB_SSD1309_128X64 u8g(CLOCK_PIN, DATA_PIN, CS_PIN, DC_PIN, RESET_PIN);

void setup() 
{
  /* nothing to do here */
}

void loop() 
{
  u8g.firstPage();  
  
  /* Keep looping until finished drawing screen */
  do 
  {
    int steps = 16;
    int dx = 128/steps;
    int dy = 64/steps;
    int y = 0;
    for(int x=0; x<128; x+=dx) {
        u8g.drawLine(x, 0, 127, y);
        u8g.drawLine(127-x, 63, 0, 63-y);
       y+=dy;     
    }
      
  } while(u8g.nextPage());
}
