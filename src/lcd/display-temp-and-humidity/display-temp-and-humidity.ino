/* YourDuino.com Example Software Sketch
 20 character 4 line I2C Display
 Backpack Interface labelled "YwRobot Arduino LCM1602 IIC V1"
 Connect Vcc and Ground, SDA to A4, SCL to A5 on Arduino
 terry@yourduino.com */

/*-----( Import needed libraries )-----*/
#include <Wire.h>  // Comes with Arduino IDE
// Get the LCD I2C Library here: 
// https://bitbucket.org/fmalpartida/new-liquidcrystal/downloads
// Move any other LCD libraries to another folder or delete them
// See Library "Docs" folder for possible commands etc.
#include <LiquidCrystal_I2C.h>

// set the LCD address to 0x27 for a 20 chars 4 line display
// Set the pins on the I2C chip used for LCD connections:
//                    addr, en,rw,rs,d4,d5,d6,d7,bl,blpol
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);  // Set the LCD I2C address

void setup()   /*----( SETUP: RUNS ONCE )----*/
{
  Serial.begin(9600);  // Used to type in characters
  lcd.begin(16,2);         // initialize the lcd for 20 chars 4 lines, turn on backlight
  lcd.backlight(); // turn the backlight on  

//-------- Write characters on the display ------------------
  // NOTE: Cursor Position: Lines and Characters start at 0  
  lcd.setCursor(0,0); //Start at character 4 on line 0
  // write 16 chars on line 1
  lcd.print("1234567890123456");
  // write 16 chars on line 1
  lcd.setCursor(0,1);
  lcd.print("1134567890123456");
}

void loop()
{
    // when characters arrive over the serial port...
    if (Serial.available()) {
      // wait a bit for the entire message to arrive
      delay(100);
      // clear the screen
      lcd.clear();
      // read all the available characters
      while (Serial.available() > 0) {
        // display each character to the LCD
        lcd.write(Serial.read());
      }
  }

}


#include "DHT.h"
 
#define DHTPIN 2     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
#define fan 4
 
int maxHum = 60;
int maxTemp = 40;
 
DHT dht(DHTPIN, DHTTYPE);
 
void setup() {
  pinMode(fan, OUTPUT);
  Serial.begin(9600); 
  dht.begin();
}
 
void loop() {
  // Wait a few seconds between measurements.
  delay(2000);
 
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius
  float t = dht.readTemperature();
  
  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
