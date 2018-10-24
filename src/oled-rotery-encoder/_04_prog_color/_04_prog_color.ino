
#include <Arduino.h>
#include <U8g2lib.h>
#include <SPI.h>
#include <Encoder.h>
#include <Bounce2.h>
#include <Adafruit_NeoPixel.h>
#define LEDPIN 7 // connect the Data from the strip to this pin on the Arduino
#define NUMBER_PIEXELS 12 // the number of pixels in your LED strip
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMBER_PIEXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

// we will hog both the interrupt pins for best rotery encoder performance
#define ENC_A_PIN 2
#define ENC_B_PIN 3
#define SET_PIN 4 // momentary push button set the current encoder value to be the new variable
#define PROG_PIN 5 // momentary push button change the programming mode


/* from https://store.arduino.cc/usa/arduino-nano
SPI: 10 (SS), 11 (MOSI), 12 (MISO), 13 (SCK). These pins support SPI communication, which, although provided by the underlying hardware, is not currently included in the Arduino language.
*/
#define CS_PIN 9
#define DC_PIN 10
#define RS_PIN 11
#define SDA_PIN 12 // also called Data or MISO
#define SCL_PIN 13 // also called Clock SCK


// Software 4-wire SPI
U8G2_SSD1306_128X64_NONAME_1_4W_SW_SPI u8g2(U8G2_R0, SCL_PIN, SDA_PIN, CS_PIN, DC_PIN, RS_PIN);
Encoder myEnc(ENC_A_PIN, ENC_B_PIN);
Bounce debouncer_set = Bounce();
Bounce debouncer_prog = Bounce(); 

// set_value is 0 if we are setting the current program mode
int set_value = 1;
// if prog_mode_value goes low we increment the mode
int prog_mode_value = 1;

int mode = 0;
int num_modes = 6;
int newPosition = 0;
int oldPosition  = -999;
int update_display = 0;

int red = 10;
int old_red  = 0;
int green = 20;
int old_green  = 0;
int blue = 30;
int old_blue  = 0;
int pattern = 0;
int old_pattern  = 0;
int delay_value = 10;
int old_delay_value  = 0;
int brightness = 100;
int old_brightness  = 0;

void setup(void) {
  // normal value is HIGH - press button to make LOW
  pinMode(SET_PIN, INPUT_PULLUP);
  pinMode(PROG_PIN, INPUT_PULLUP);
  
  debouncer_set.attach(SET_PIN);
  debouncer_set.interval(25); // interval in ms
  
  debouncer_prog.attach(PROG_PIN);
  debouncer_prog.interval(25); // interval in ms
  
  u8g2.begin();
  // Set font to Helvetica regurlar 8 pixel font
  // For other options see https://github.com/olikraus/u8g2/wiki/fntlistall#8-pixel-height
  u8g2.setFont(u8g2_font_helvR08_tf);
  Serial.begin(9600);
  // Serial.println("Basic Encoder Test:");

}

void loop(void) {
  // look for the new encoder number
  newPosition = myEnc.read();
  if (newPosition != oldPosition) {
    oldPosition = newPosition;
    switch (mode) {
      case 0:
        red = newPosition;
        break;
      case 1:
        green = newPosition;
        break;
      case 2:
        blue = newPosition;
        break;
      case 3:
        pattern = newPosition;
        break;
      case 4:
        delay_value = newPosition;
        break;
      case 5:
        brightness = newPosition;
        break;
    }
    update_display = 1;
  }
  
  debouncer_set.update();
  if ( debouncer_set.fell() ) {
    set_value  = !set_value;
    switch (mode) {
      case 0:
        red = newPosition;
        break;
      case 1:
        green = newPosition;
        break;
      case 2:
        blue = newPosition;
        break;
      case 3:
        pattern = newPosition;
        break;
      case 4:
        delay_value = newPosition;
        break;
      case 5:
        brightness = newPosition;
        break;
    }
    update_display = 1;
  }
  
  debouncer_prog.update();
  if (debouncer_prog.fell()) {
    prog_mode_value = debouncer_prog.read();
    mode++;
    mode = mode % num_modes;
    update_display = 1;
  } else prog_mode_value = 1;
  
  if (update_display == 1) {
      u8g2.firstPage();
      do {    
            u8g2.drawStr(0,15,"Red:");
            u8g2.setCursor(23,15);
            u8g2.print(u8x8_u8toa(red, 3));
            if (mode==0) u8g2.drawLine(0,17, 40, 17);
            
            u8g2.drawStr(45,15,"Grn:");
            u8g2.setCursor(68,15);
            u8g2.print(u8x8_u8toa(green, 3));
            if (mode==1) u8g2.drawLine(45,17, 85, 17);
            
            u8g2.drawStr(92,15,"Blu:");
            u8g2.setCursor(110,15);
            u8g2.print(u8x8_u8toa(blue, 3));
            if (mode==2) u8g2.drawLine(92,17, 130,17);
  
            u8g2.drawStr(0,30,"Pattern:");
            u8g2.setCursor(70,30);
            // right justify but only works up to 3 digits
            u8g2.print(u8x8_u8toa(pattern, 3));
            if (mode==3) u8g2.drawLine(0,32, 87,32);
  
            u8g2.drawStr(0,46,"Delay:");
            u8g2.setCursor(70,46);
            // right justify but only works up to 3 digits
            u8g2.print(u8x8_u8toa(delay_value, 3));
            if (mode==4) u8g2.drawLine(0,48, 87,48);

            u8g2.drawStr(0,61,"Brightness:");
            u8g2.setCursor(70,61);
            // right justify but only works up to 3 digits
            u8g2.print(u8x8_u8toa(brightness, 3));
            if (mode==5) u8g2.drawLine(0,63, 87,63);
            
            } while ( u8g2.nextPage() );
      update_display = 0;   
   }
   Serial.print("Encoder:");
   Serial.print(newPosition);
   
   Serial.print(" Set:");
   Serial.print(set_value);
   Serial.print(" Prog:");
   
   Serial.print(prog_mode_value);
   Serial.print(" Mode:");
   Serial.print(mode);

   Serial.print(" Pattern:");
   Serial.print(pattern);

   Serial.print(" Delay:");
   Serial.print(delay_value);

   Serial.print("Brightness:");
   Serial.print(brightness);
   
   Serial.println(mode);
   delay(delay_value);
}

void drawColor(int red, int green, int blue) {
   for (int i=0; i<strip.numPixels(); i++) {
    strip.setPixelColor(i, red, green, blue);
   }
   strip.show();
}



