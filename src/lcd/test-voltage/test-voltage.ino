#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2); //set the LCD address to 0x27 for a 16 chars and 2 line display
void setup()
{
    lcd.init(); 
    lcd.backlight();
    lcd.setCursor(0, 0);
    lcd.print("www.b2cqshop.com");
    lcd.setCursor(0, 1);
    lcd.print("Voltage: ");
    lcd.setCursor(13, 1);
    lcd.print("V");
}
void loop()
{
    int val;
    float temp;
     val=analogRead(0);
    temp=val/4.092;
    val=(int)temp;//
    lcd.setCursor(9, 1);
    lcd.print(0x30+val/100,BYTE); 
    lcd.print(0x30+(val%100)/10,BYTE); 
    lcd.print('.');
    lcd.print(0x30+val%10,BYTE);
    delay(100);
}

