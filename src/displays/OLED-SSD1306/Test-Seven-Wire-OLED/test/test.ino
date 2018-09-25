#include <Arduino.h>
#include <U8g2lib.h>
#include <SPI.h>
#include <Wire.h>

// my pins are: Pins are GND, VCC, SCL, SDA, RES, DC, CS
// U8G2_ST7920_128X64_1_SW_SPI(rotation, clock, data, cs [, reset])
// clock is SCL? on A5
// data is SDA? on A4
// CS is chip select
// reset is RES

U8G2_ST7920_128X64_1_SW_SPI u8g2(U8G2_R0, 7, 8, 9, 10);

void setup(void) {
  u8g2.begin();
}

void loop(void) {
  u8g2.firstPage();
  do {
    u8g2.setFont(u8g2_font_ncenB14_tr);
    u8g2.drawStr(0,24,"Hello World!");
  } while ( u8g2.nextPage() );
}
