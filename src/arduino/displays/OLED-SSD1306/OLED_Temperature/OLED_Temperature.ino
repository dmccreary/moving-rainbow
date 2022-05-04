/*
 * Display the temperature from the Dallas to the OLED
 */

#include <Arduino.h>
// https://github.com/olikraus/u8g2/wiki
#include <U8g2lib.h>
#include <SPI.h>
#include <OneWire.h> 
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2
OneWire oneWire(ONE_WIRE_BUS); 
DallasTemperature sensors(&oneWire);

// order on OLED - GND, VCC, SCL, SDA, RDS, DC, CS
#define SCL_PIN 13 // SCL clock - 3rd from bottom
#define SDA_PIN 11 // SDA, Data, MOSI - must be on pin 11 on the Nano
#define RDS_PIN 10 // reset
#define DC_PIN 9 // DC moved from pin 9 which is needed as a PWM pin
#define CS_PIN 8 // chip select top
// https://github.com/olikraus/u8g2/wiki/u8x8setupcpp#constructor-reference
// We are using the 128 byte 4W Hardware SPI with no rotation which only uses 27% of dynamic memory
U8G2_SSD1306_128X64_NONAME_1_4W_HW_SPI u8g2(U8G2_R0, CS_PIN, DC_PIN, RDS_PIN);

int counter = 0;

void setup()   {
  sensors.begin(); 
  Serial.begin(9600);
  u8g2.begin();
  // Set font to Helvetica regular 8 pixel font
  // For other options see https://github.com/olikraus/u8g2/wiki/fntlistall#8-pixel-height
  u8g2.setFont(u8g2_font_helvR08_tf);
}

void loop() {
  sensors.requestTemperatures();
  u8g2.firstPage();
  do {
    u8g2.setFont(u8g2_font_helvR08_tf);
    u8g2.drawStr(0, 8, "CoderDojo Rocks!");

    //set 24 pt helvetica roman font
    u8g2.setFont(u8g2_font_helvR24_tf);
    u8g2.setCursor(20, 40);
    u8g2.print(sensors.getTempFByIndex(0));
    
    u8g2.setFont(u8g2_font_helvR08_tf);
    u8g2.setCursor(0, 63);
    u8g2.print(counter);
  } while ( u8g2.nextPage() );
  counter++;
  
  Serial.print(counter);
  Serial.print(" ");
  Serial.println(sensors.getTempFByIndex(0));

  delay(1000);
  counter++;
}
