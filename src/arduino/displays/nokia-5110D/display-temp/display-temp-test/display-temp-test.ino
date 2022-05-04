#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>
#include <OneWire.h> 
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2
OneWire oneWire(ONE_WIRE_BUS); 
DallasTemperature sensors(&oneWire);
/********************************************************************/ 

// Software SPI (slower updates, more flexible pin options):
// pin 7 - Serial clock out (SCLK)
// pin 6 - Serial data out (DIN)
// pin 5 - Data/Command select (D/C)
// pin 4 - LCD chip select (CS)
// pin 3 - LCD reset (RST)
Adafruit_PCD8544 display = Adafruit_PCD8544(7, 6, 5, 4, 3);

int count = 0;

void setup()   {
  sensors.begin(); 
  Serial.begin(9600);
  display.begin();
  display.setContrast(55);
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(BLACK);
}

void loop() {
  sensors.requestTemperatures();
  display.setCursor(10,10);
  display.println(sensors.getTempFByIndex(0));
  display.display();
  
  Serial.print(count);
  Serial.print(" ");
  Serial.println(sensors.getTempCByIndex(0));

  delay(1000);
  display.clearDisplay();
  count++;
}
