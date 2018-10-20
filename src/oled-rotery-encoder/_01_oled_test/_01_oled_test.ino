
#include <Arduino.h>
#include <U8g2lib.h>

#include <SPI.h>

/* from https://store.arduino.cc/usa/arduino-nano
SPI: 10 (SS), 11 (MOSI), 12 (MISO), 13 (SCK). These pins support SPI communication, which, although provided by the underlying hardware, is not currently included in the Arduino language.
*/
#define CS_PIN 9
#define DC_PIN 10
#define RS_PIN 11
#define SDA_PIN 12 // also called Data or MISO
#define SCL_PIN 13 // also called Clock SCK

// this works
U8G2_SSD1306_128X64_NONAME_1_4W_SW_SPI u8g2(U8G2_R0, /* clock=*/ SCL_PIN, /* data=*/ SDA_PIN, /* cs=*/ CS_PIN, /* dc=*/ DC_PIN, /* reset=*/ RS_PIN);

int counter = 0;

void setup(void) {
  u8g2.begin();
  // Set font to Helvetica regurlar 8 pixel font
  // For other options see https://github.com/olikraus/u8g2/wiki/fntlistall#8-pixel-height
  u8g2.setFont(u8g2_font_helvR08_tf);
}

void loop(void) {
  u8g2.firstPage();
  do {    
    u8g2.drawStr(0,20,"Hello World!");
    u8g2.setCursor(0,40);
    u8g2.print(counter);
    u8g2.setCursor(30,60);
    // right justify but only works up to 3 digits
    u8g2.print(u8x8_u8toa(counter, digits));
  } while ( u8g2.nextPage() );
  delay(10);
  counter++;
}

