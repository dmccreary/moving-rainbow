#include <Wire.h>  // Comes with Arduino IDE
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);  // Set the LCD I2C address

int redPin = A0;
int greenPin = A1;
int bluePin = A2;

int redValue = 0;
int greenValue = 0;
int blueValue = 0;

void setup()   /*----( SETUP: RUNS ONCE )----*/
{
  Serial.begin(9600);  // Used to type in characters

  lcd.begin(16,2);   // initialize the lcd for 16 chars 2 lines, turn on backlight
  lcd.setCursor(0,0);
  lcd.print("Display RGB Pots");
  lcd.setCursor(0,1);
  lcd.print("Set Serial 9600");  
  delay(2000);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Red=");
  lcd.setCursor(9,0);
  lcd.print("Gn=");
  lcd.setCursor(0,1);
  lcd.print("Blue=");
  delay(2000);
}


void loop()   /*----( LOOP: RUNS CONSTANTLY )----*/
{
  redValue = analogRead(redPin);
  greenValue = analogRead(greenPin);
  blueValue = analogRead(bluePin);
  Serial.print("Red=");
  Serial.print(redValue);
  Serial.print("  Green=");
  Serial.print(greenValue);
  Serial.print("  Blue=");
  Serial.println(blueValue);

  lcd.setCursor(4,0);
  print_right_aligned(redValue);

  lcd.setCursor(12,0);
  print_right_aligned(greenValue);

  lcd.setCursor(5,1);
  print_right_aligned(blueValue);

  delay(200);
}

// print right aligned into space
void print_right_aligned(int in) {
  if (in < 1000) lcd.print(" ");
  if (in < 100) lcd.print(" ");
  if (in < 10) lcd.print(" ");
  lcd.print(in);
}
