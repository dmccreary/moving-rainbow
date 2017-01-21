
#include <OneWire.h>
#include <DallasTemperature.h>
#include <Adafruit_NeoPixel.h>

#define LEDPIN 12 // connect the Data wire from the strip to this pin on the Arduino
#define NUMBER_PIXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

#include <stdio.h>
#define ONE_WIRE_BUS 3 // put the temperature wire in this pin

float temperature;
char buffer[25];
byte maxlines = 2;
char line1[16];
char line2[16];
byte x = 0;
byte y = 1;
byte maxsensors = 0;

int LED_index;
 
/*
DS18S20 Temperature chip i/o
Note.  You must add the OneWire and DallasTemerature libraries
to your Arduino Library.
At startup you should see this

R=28 FF 5B 9D 3C 4 0 8F Device is a DS18B20 family device.
P=1 1A 1 55 0 7F FF C 10 30  CRC=30

No more addresses.
Temperature = 63.72F

 */
OneWire  ds(ONE_WIRE_BUS);
DallasTemperature sensors(&ds);

void scanSensors(void)
{
  byte i;
  byte present = 0;
  byte data[12];
  byte addr[8];
  while (ds.search(addr))
  {
    Serial.print("R=");
    for( i = 0; i < 8; i++) {
      Serial.print(addr[i], HEX);
      Serial.print(" ");
    }
  
    if ( OneWire::crc8( addr, 7) != addr[7]) {
        Serial.print("CRC is not valid!\n");
        return;
    }
    
    if ( addr[0] == 0x10) {
        Serial.print("Device is a DS18S20 family device.\n");
        maxsensors++;
    }
    else {
      if (addr[0] == 0x28) {
        Serial.print("Device is a DS18B20 family device.\n");
        maxsensors++;
      }
      else {
        Serial.print("Device is unknown!\n");
        Serial.print("Device ID: ");
        Serial.print(addr[0],HEX);
        Serial.println();
        return;
      }
    }
    // The DallasTemperature library can do all this work for you!
    ds.reset();
    ds.select(addr);
    ds.write(0x44,1);         // start conversion, with parasite power on at the end
    delay(1000);     // maybe 750ms is enough, maybe not
    // we might do a ds.depower() here, but the reset will take care of it.
    present = ds.reset();
    ds.select(addr);    
    ds.write(0xBE);         // Read Scratchpad
    Serial.print("P=");
    Serial.print(present,HEX);
    Serial.print(" ");
    for ( i = 0; i < 9; i++) {           // we need 9 bytes
      data[i] = ds.read();
      Serial.print(data[i], HEX);
      Serial.print(" ");
    }
    Serial.print(" CRC=");
    Serial.print( OneWire::crc8( data, 8), HEX);
    Serial.println();

  }
  Serial.print("No more addresses.\n");
  ds.reset_search();
  delay(250);
}

void setup(void) {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  sensors.begin();
  scanSensors();
  strip.begin(); // initialize the LED strip
}

void loop(void) {
  sensors.requestTemperatures(); 
  temperature = sensors.getTempFByIndex(0);
  
  // send the current temp to the serial port
  Serial.print("Temperature =");
  Serial.print(dtostrf(temperature, 6, 2, buffer));
  Serial.println("F");
  
  // this converts the temperature into which LEDs are on
  // we map temperatures 70 degrees F to all off and 90 degrees F to all on
  // turn on an LED 0= if the temp is 70, and turn on 11 if we are above 90
  LED_index = map(temperature, 70.0, 90.0, 0, 11);
  
  // this shows what pixels are on
  Serial.println(LED_index);
  
  // turn all off
  for (int i=0; i< LED_index; i++){
    strip.setPixelColor(i, 0, 0, 0);
  };
  
  // turn the LEDs red up to the LED index
  for (int i=0; i<= LED_index; i++){
    strip.setPixelColor(i, 25, 0, 0);
  };
  
  // update the LED strip
  strip.show();
  
  // wait one second
  delay(1000);
}




