
#include <Arduino.h>
#include <U8g2lib.h>
#include <SPI.h>
#include <Encoder.h>
#include <Bounce2.h>

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
int num_modes = 4;
int newPosition = 0;
int oldPosition  = -999;
int update_display = 0;

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
    update_display = 1;
  }
  
  debouncer_set.update();
  if ( debouncer_set.fell() ) {
    set_value  = !set_value;
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
            u8g2.drawStr(0,20,"Encoder Value:");
            u8g2.setCursor(80,20);
            // right justify but only works up to 3 digits
            u8g2.print(u8x8_u8toa(newPosition, 3));
  
            u8g2.drawStr(0,35,"Set Value:");
            u8g2.setCursor(80,35);
            // right justify but only works up to 3 digits
            u8g2.print(u8x8_u8toa(set_value, 3));
  
            u8g2.drawStr(0,50,"Prog Value:");
            u8g2.setCursor(80,50);
            // right justify but only works up to 3 digits
            u8g2.print(u8x8_u8toa(prog_mode_value, 3));

            u8g2.drawStr(0,64,"Mode:");
            u8g2.setCursor(80,64);
            // right justify but only works up to 3 digits
            u8g2.print(u8x8_u8toa(mode, 3));
            
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
   Serial.println(mode);
   delay(10);
}

