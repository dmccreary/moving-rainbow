// Display Temp (in F) and Humidity to the Serial Monitor
// Based on public domain Ladyada sketch at
//See https://github.com/adafruit/DHT-sensor-library

#include "DHT.h"
#define DHTPIN 2     // what pin we're connected to

// Uncomment whatever type you're using!
//#define DHTTYPE DHT11   // DHT 11
#define DHTTYPE DHT22   // DHT 22  (AM2302)
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

// Connect pin 1 (on the left) of the sensor to +5V
// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1
// to 3.3V instead of 5V!
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor - BTW I skipped this step

// Initialize DHT sensor.
DHT dht(DHTPIN, DHTTYPE);

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

void setup() {
  Serial.begin(9600);
  Serial.println("Begin test of AM 2302 Temperature and Humidity Sensor");
  dht.begin();
  lcd.begin(16,2); // initialize the lcd for 16 chars 2 lines
  lcd.backlight(); // turn the backlight on  
}

void loop() {
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();

  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);

  lcd.setCursor(0,0); //Start at character 0 on line 0
  lcd.print("T=");
  lcd.print(f);
  
  Serial.print("Temperature: ");
  Serial.print(f);
  
  
  Serial.print(" Humidity: ");
  Serial.print(h);
  lcd.print(" H=");
  lcd.print(h);
  
  lcd.setCursor(0,1);
  Serial.print(" Heat index: ");
  Serial.println(hif);
  lcd.print("Heat index=");
  lcd.print(hif);
  
  // Wait a two seconds between measurements.
  delay(2000);
}
