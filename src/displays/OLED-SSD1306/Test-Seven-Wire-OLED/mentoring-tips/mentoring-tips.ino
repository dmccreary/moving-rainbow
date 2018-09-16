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
// both the 136 and 139 work: U8GLIB_SSD136_128X64 U8GLIB_SSD1309_128X64
U8GLIB_SSD1309_128X64 u8g(CLOCK_PIN, DATA_PIN, CS_PIN, DC_PIN, RESET_PIN);

void setup() 
{
  u8g.setFont(u8g_font_unifont);
  u8g.setColorIndex(1); // Instructs the display to draw with a pixel on. 
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
    };
    delay(1000);
  draw();
  delay(1000);
      
  } while(u8g.nextPage());
  
}

void draw1(){
  u8g.drawStr( 0, 20, "Tips to stay in STEM");
}

void draw2(){
  u8g.drawStr( 0, 20, "2 hours of mentoring every 2 weeks");
}
