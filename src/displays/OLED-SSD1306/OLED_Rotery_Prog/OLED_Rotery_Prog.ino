#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#include <Adafruit_NeoPixel.h>
#define LED_STRIP_PIN 13 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIXELS, LED_STRIP_PIN, NEO_GRB + NEO_KHZ800);


//Define Pins
#define OLED_CLK   12 //D0
#define OLED_MOSI  11   //D1
#define OLED_RESET 10   //RST
#define OLED_DC    9
#define OLED_CS    8

#define PROG_MODE_PIN 2
// press this momentary push button to change the current value
#define SET_VALUE_PIN 3

#define SOUND 4
#define ROTARY_A_PIN A0
#define ROTARY_B_PIN A1

//Define Visuals
#define FONT_SIZE 1
#define SCREEN_WIDTH 127  //real size minus 1, because coordinate system starts with 0
#define SCREEN_HEIGHT 63  //real size minus 1, because coordinate system starts with 0

//Define Variables
Adafruit_SSD1306 display(OLED_MOSI, OLED_CLK, OLED_DC, OLED_RESET, OLED_CS);

byte mode; // mode 0 is display patterh, mode 1 is program
byte delayTime = 50; // 1/20 of a second - used to program the speed
byte red = 10;
byte green = 10;
byte blue = 10;
byte brightness = 100;
byte mainLoopCount = 0;

byte pressedProgButton = 0;
byte pressedSelectButton = 0;
long lastDebounceTime;
//Setup 
void setup() 
{
  pinMode(LED_STRIP_PIN, OUTPUT);     // Pin 13 is output to which an LED is connected
  pinMode(PROG_MODE_PIN, INPUT_PULLUP);     // Pin 2 is input to which a switch is connected = INT0
  pinMode(SET_VALUE_PIN, INPUT_PULLUP);    // Pin 3 is input to which a switch is connected = INT1
  attachInterrupt(0, pressed_prog_button, FALLING  ); // pin 2
  attachInterrupt(1, pressed_select_button, FALLING  ); // pin 3
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize with the I2C addr 0x3D (for the 128x64)
  
  display.clearDisplay();   // clears the screen and buffer
  display.display();   
  display.setTextWrap(false);

  // splash();
  
  display.setTextColor(WHITE);
  display.setTextSize(FONT_SIZE);
  display.clearDisplay();

  Serial.begin(9600);
  Serial.println("Start");
  Serial.print("Mode=");
  Serial.println(mode, DEC);
}

//Splash Screen
//void splash()
//{
//  display.clearDisplay(); 
//  display.setTextColor(WHITE);
//  centerPrint("Moving Rainbow",5,1);
//  centerPrint("By Dan McCreary",24,1);
//  centerPrint("Version 0.01",33,1);
//  centerPrint("Sept. 2018",42,1);
//  display.display();
//  delay(3000);
//}

//Loop
void loop() {
  if (pressedProgButton == 1) {
     mode = 1;
     pressedProgButton = 0; // move it back to 0
    
   }

  if (mode == 1)
     display_prog_menu();

  switch (mode) {
        case 0:rainbow7();break; // 7 pixel rainbow
        case 1: dot(red, blue, green);break; // red
//        case 2: dot(0, 255, 0);break; // green
//        case 3: dot(0, 0, 255);break; // blue
//        case 4: colorWipe(255 ,0, 0);break;
//        case 5: colorWipe(0, 255, 0);break;
//        case 6: colorWipe(0, 0, 255);break;
//        case 7: swoosh(255 ,0, 0);break;
//        case 8: swoosh(0, 255, 0);break;
//        case 9: swoosh(0, 0, 255);break;
//        case 10: theaterChase(255, 0, 0);break;
//        case 11: theaterChase(0, 255, 0);break;
//        case 12: theaterChase(0, 0, 255);break;
//        case 13: rainbowSlide();break;
//        case 14: candle();break;
//        case 15: randomColor();break;
//        case 16: sparkle();break;
     }
  for (int i=0; i<strip.numPixels(); i++) {
    rainbow7(i, delayTime); // starting at i, draw the 7 color rainbow
  }
  mainLoopCount++;
  
  Serial.print("Mode=");
  Serial.println(mode, DEC);
}

void display_pattern() {
   display.clearDisplay(); 
   display.setTextSize(1);
   display.setCursor(0,10);
   display.print("displaying pattern");
   
   display.setCursor(0,20);
   display.print("delay: ");
   display.print(delayTime);

   display.setCursor(0,30);
   display.print("color R:");
   display.print(red);
   display.print("G:");
   display.print(green);
   display.print("B:");
   display.print(blue);

   display.setCursor(0,40);
   display.print("brightness:");
   display.print(brightness);

   display.setCursor(0,50);
   display.print("pattern:");
   
   display.display();
}

void display_prog_menu() {
   display.clearDisplay(); 
   display.setTextSize(1);
   display.setCursor(0,10);
   display.print("set delay");
   
   display.setCursor(0,20);
   display.print("set color:");

   display.setCursor(0,30);
   display.print("set pattern:");
   
   display.display();
}

// Interrupt service routine - keep this fast
void pressed_prog_button() {        
  pressedProgButton = 1; // indicate have pressed the select button mode
  lastDebounceTime = millis(); // record when we got the interrupt for debouncing
}

// Interrupt service routine
void pressed_select_button() {        
  pressedSelectButton = 1; // indicate we have pressed the select button mode
  lastDebounceTime = millis(); // record when we got the interrupt for debouncing
}


void program_pattern() {
  display.clearDisplay(); 
  
  display.setCursor(0,0);
  display.print("color");

  display.setCursor(SCREEN_WIDTH/2 ,0);
  display.print("pattern");
  
  display.display();
}

void centerPrint(char *text, int y, int size)
{
  display.setTextSize(size);
  display.setCursor(SCREEN_WIDTH/2 - ((strlen(text))*6*size)/2,y);
  display.print(text);
}

// a seven segment rainbow with red on the highest pixel
void rainbow7(int  i, int  wait) {
    int np = strip.numPixels();  // we use the modulo function with this
    strip.setPixelColor(i %np, 255, 255, 0);
    strip.show();
    delay(wait);
}

void dot(int red, int blue, int green) {
  int index = mainLoopCount % strip.numPixels();
  clear();
  strip.setPixelColor(index, red, blue, green);
  strip.show();
}

void rainbow7() {
    int i = mainLoopCount;
    int np = strip.numPixels();  // we use the modulo function with this
    strip.setPixelColor(i     % np, 0, 0, 0); // off
    strip.setPixelColor((i+1) % np, 25, 0, 25); // violet
    strip.setPixelColor((i+2) % np, 255, 0, 255); // indigo
    strip.setPixelColor((i+3) % np, 0, 0, 150); // blue
    strip.setPixelColor((i+4) % np, 0, 150, 0); // green
    strip.setPixelColor((i+5) % np, 255, 255, 0); // yellow
    strip.setPixelColor((i+6) % np, 110, 70, 0); // orange
    strip.setPixelColor((i+7) % np, 150, 0, 0); // red
    // erase the rest
    strip.setPixelColor((i+8) %np , 0, 0, 0);
    strip.setPixelColor((i+9) %np , 0, 0, 0);
    strip.setPixelColor((i+10) %np , 0, 0, 0);
    strip.setPixelColor((i+11) %np , 0, 0, 0);
    strip.show();
}


void clear() {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, 0);
      strip.show();
  }
}
