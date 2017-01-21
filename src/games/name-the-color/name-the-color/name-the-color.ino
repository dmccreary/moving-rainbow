
#include <Adafruit_NeoPixel.h>
#include <LiquidCrystal_I2C.h>
//https://www.pjrc.com/teensy/td_libs_Encoder.html
#include <Encoder.h>


#define LEDPIN 12 // connect the Data In pin
#define NUMBER_PIXELS 12// connect the Data In pin
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

// Put SDA on pin A4 and SLC on A5
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);  // Set the LCD I2C address

Encoder knob(2, 3);
long knobPosition  = -999;
// game level, start at 0
int level  = 0;

// our push button but debounced
// read https://www.arduino.cc/en/Tutorial/Debounce
const int buttonPin = 4;
int ledState = HIGH;         // the current state of the output pin
int buttonState;             // the current reading from the input pin
int lastButtonState = LOW;   // the previous reading from the input pin
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers

String colors1[] = {"Red", "Green", "Blue"};
String colors2[] = {"Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"};

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
  Serial.println("Welcome to name the color.");

  // set the first pixel to a very light red
  strip.begin();
  strip.setPixelColor(0, 10, 0, 0);
  strip.show();

  // display a name on the LCD
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  lcd.print("Name the color");
  delay(2000);
}

void loop() {
  long newValue = knob.read();;
  int reading = digitalRead(buttonPin);
  
  if (newValue != knobPosition) {
    Serial.print("KnobValue = ");
    Serial.print(newValue);
    Serial.println();
    // turn off the old pixel
    strip.setPixelColor(abs(knobPosition) % NUMBER_PIXELS, 0, 0, 0);
    knobPosition = newValue;
    // turn on the new pixel
    strip.setPixelColor(abs(newValue) % NUMBER_PIXELS, 10, 0, 0);
    strip.show();
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print(newValue);
    lcd.setCursor(0,1);
    lcd.print(colors1[newValue % 3]);
  }



  // check to see if you just pressed the button
  // (i.e. the input went from LOW to HIGH),  and you've waited
  // long enough since the last press to ignore any noise:

  // If the switch changed, due to noise or pressing:
  if (reading != lastButtonState) {
    // reset the debouncing timer
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:

    // if the button state has changed:
    if (reading != buttonState) {
      buttonState = reading;

      // only toggle the LED if the new button state is HIGH
      if (buttonState == HIGH) {
        ledState = !ledState;
      }
    }
  }

  // set the LED:
  lcd.setCursor(11,0);
  lcd.print(buttonState);
  lcd.setCursor(13,0);
  lcd.print(ledState);

  // save the reading.  Next time through the loop,
  // it'll be the lastButtonState:
  lastButtonState = reading;
}

