
#include <Arduino.h>
#include <U8g2lib.h>

#include <Encoder.h>

// we will hog both the interrupt pins for best performance
#define ENC_A_PIN 2
#define ENC_B_PIN 4

#define SET_PIN 4 // set the current encoder value to be the new variable
#define PROG_PIN 5 // change the programming mode

// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder myEnc(ENC_A_PIN, ENC_B_PIN);
long oldPosition  = -999;

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
U8G2_SSD1306_128X64_NONAME_1_4W_SW_SPI u8g2(U8G2_R0, SCL_PIN, SDA_PIN, CS_PIN, DC_PIN, RS_PIN);

void setup(void) {
  u8g2.begin();
  // Set font to Helvetica regurlar 8 pixel font
  // For other options see https://github.com/olikraus/u8g2/wiki/fntlistall#8-pixel-height
  u8g2.setFont(u8g2_font_helvR08_tf);
  Serial.begin(9600);
  Serial.println("Basic Encoder Test:");
}

void loop(void) {
  // look for the new encoder number
  long newPosition = myEnc.read();
  if (newPosition != oldPosition) {
    oldPosition = newPosition;
    u8g2.firstPage();
      do {    
          u8g2.drawStr(0,20,"Encoder Value:");
          u8g2.setCursor(80,20);
          // right justify but only works up to 3 digits
          u8g2.print(u8x8_u8toa(newPosition, 3));
          } while ( u8g2.nextPage() );
   }
  delay(10);
}

