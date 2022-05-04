
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

int mode = 0;
int num_modes = 7;
int oldPosition  = 1; // change from -999
int update_display = 0;

// initail values
int red = 10;
int green = 20;
int blue = 30;
int pattern = 0;
int counter = 0; // main loop counter
int last_random_index = 0;

int delay_value = 100; // make it 1/10 of a sec by default
int brightness = 100;

int pattern_count = 11;
char* pattern_label[]={"Moving Rainbow", "Solid", "Dot", "Comet", "Chase", "Swipe", "Pong", "Candle", "Random", "Sparkle", "Color Cycle"};
byte* adjust_speed[]= {               1,       0,     1,       1,       1,       1,      1,        0,        1,         1,             1};

int delta;
int tmp_display; // the temporay value on the display

void setup(void) {
  // normal value is HIGH - press button to make LOW
  pinMode(SET_PIN, INPUT_PULLUP);
  pinMode(PROG_PIN, INPUT_PULLUP);
  
  debouncer_set.attach(SET_PIN);
  debouncer_set.interval(10); // interval in ms
  
  debouncer_prog.attach(PROG_PIN);
  debouncer_prog.interval(10); // interval in ms
  
  u8g2.begin();
  // Set font to Helvetica regurlar 8 pixel font
  // For other options see https://github.com/olikraus/u8g2/wiki/fntlistall#8-pixel-height
  u8g2.setFont(u8g2_font_helvR08_tf);
  strip.begin();
  Serial.begin(9600);
  // Serial.println("Basic Encoder Test:");
  tmp_display = red; // set to the initial mode=0 display value
}

void loop(void) {

  // look for the new encoder number
  int newPosition = myEnc.read();
  
  if (newPosition != oldPosition) {
     delta = newPosition - oldPosition;
     tmp_display += delta; // add the new delta - plus or minus 1
     tmp_display = constrain(tmp_display, 0, 255); // constrain to positve byte values
    
     Serial.print("NewPos:");
     Serial.print(newPosition);
  
     Serial.print(" Old:");
     Serial.print(oldPosition);
  
     Serial.print(" Delta:");
     Serial.print(delta);
     if (mode == 4) pattern = (tmp_display / 4) % pattern_count;
    oldPosition = newPosition;
    update_display = 1;
  }

  // if the set button gets pressed
  debouncer_set.update();
  if ( debouncer_set.fell() ) {
    switch (mode) {
      case 0:
        break;
      case 1:
        red = tmp_display;
        break;
      case 2:
        green = tmp_display;
        break;
      case 3:
        blue = tmp_display;
        break;
      case 4:
        pattern = (tmp_display / 4) % pattern_count; // don't go beyond the number of patterns we have
        break;
      case 5:
        delay_value = constrain(tmp_display, 1, 100);
        break;
      case 6:
        brightness = tmp_display;
        break;
    }
    mode++; // move to the next field
    mode = mode % num_modes;
    switch (mode) {
        case 0:
        break;
      case 1:
        tmp_display = red;
        break;
      case 2:
        tmp_display = green;
        break;
      case 3:
        tmp_display = blue;
        break;
      case 4:
        tmp_display = pattern;
        break;
      case 5:
        tmp_display = delay_value;
        break;
      case 6:
        tmp_display = brightness;
        break;
    }
    update_display = 1;
  }

  // if the prog button gets pressed
  debouncer_prog.update();
  if (debouncer_prog.fell()) {
    mode++;
    mode = mode % num_modes;
    switch (mode) {
      case 0:
        break;
      case 1:
        tmp_display = red;
        break;
      case 2:
        tmp_display = green;
        break;
      case 3:
        tmp_display = blue;
        break;
      case 4:
        tmp_display = pattern;
        break;
      case 5:
        tmp_display = delay_value;
        break;
      case 6:
        tmp_display = brightness;
        break;
    }
    update_display = 1;
  };
  
  if (update_display == 1) {
      u8g2.firstPage();
      do {    
            u8g2.drawStr(0,15,"Red:");
            u8g2.setCursor(23,15);
            if (mode==1) {
              u8g2.print(u8x8_u8toa(tmp_display, 3));
              u8g2.drawLine(0,17, 40, 17);
              drawColor(tmp_display, green, blue);
            } else u8g2.print(u8x8_u8toa(red, 3));
            
            u8g2.drawStr(45,15,"Grn:");
            u8g2.setCursor(68,15);
            if (mode==2) {
              u8g2.print(u8x8_u8toa(tmp_display, 3));
              u8g2.drawLine(45,17, 85, 17);
              drawColor(red, tmp_display, blue);
            } else u8g2.print(u8x8_u8toa(green, 3));
            
            u8g2.drawStr(92,15,"Blu:");
            u8g2.setCursor(110,15);
            if (mode==3) {
              u8g2.drawLine(92,17, 130,17);
              u8g2.print(u8x8_u8toa(tmp_display, 3));
              drawColor(red, green, tmp_display);
            } else u8g2.print(u8x8_u8toa(blue, 3));

 
            u8g2.drawStr(0,30,"Pattern:");
            u8g2.setCursor(40,30); 
            u8g2.print(pattern_label[pattern]);
            if (mode==4) u8g2.drawLine(0,32, 127,32);
            
  
            u8g2.drawStr(0,46,"Delay:");
            u8g2.setCursor(70,46);
            // right justify but only works up to 3 digits
            
            if (mode==5) {
              u8g2.drawLine(0,48, 87,48);
              u8g2.print(u8x8_u8toa(tmp_display, 3));
            } else u8g2.print(u8x8_u8toa(delay_value, 3));

            u8g2.drawStr(0,61,"Brightness:");
            u8g2.setCursor(70,61);
            // right justify but only works up to 3 digits
            
            if (mode==6) {
              u8g2.print(u8x8_u8toa(tmp_display, 3));
              u8g2.drawLine(0,63, 87,63);
            } else u8g2.print(u8x8_u8toa(brightness, 3));
            
         } while ( u8g2.nextPage() );
   
   
   Serial.print(" Mode:");
   Serial.print(mode);

   Serial.print(" Pattern:");
   Serial.print(pattern);

   Serial.print(" Delay:");
   Serial.print(delay_value);

   Serial.print(" Brightness:");
   Serial.print(brightness);

   Serial.print(" Temp Display:");
   Serial.println(tmp_display);
   
   update_display = 0; // we have updated the display
  } // end update display

// "Moving Rainbow", "Solid", "Dot", "Comet", "Chase", "Swipe", "Pong", "Candle", "Random", "Sparkle", "Color Cycle"
  switch (pattern) {
      case 0:
        rainbow7(counter % strip.numPixels());
        break;
      case 1:
        drawColor(red, green, blue);
        break;
      case 2:
        dot(red, green, blue);
        break;
      case 3:
        comet(red, green, blue);
        break;
      case 4:
        chase(red, green, blue);
        break;
      case 5:
        wipe(red, green, blue);
        break;
      case 6:
        pong(red, green, blue);
        break;
      case 7:
        candle();
        break;
      case 8:
        randomRGB();
        break;
      case 9:
        sparkle(red, green, blue);
        break;
      case 10:
        rainbowCycle();
        break;
  }
  // increment and mod
  counter++;
  counter = counter % strip.numPixels(); 
  delay(delay_value);
}

void drawColor(int red, int green, int blue) {
   for (int i=0; i<strip.numPixels(); i++) {
     strip.setPixelColor(i, red, green, blue);
   }
   strip.show();
}

void dot(int red, int green, int blue) {
   strip.setPixelColor(counter + 1, red, green, blue);
   strip.setPixelColor(counter, 0, 0, 0);
   strip.show();
}

// Fill the dots one after the other with a color up to the nth pixel
void wipe(int red, int green, int blue) {
  if (counter==0) {
    // erase if counter is 0
    for(int i=0; i<strip.numPixels(); i++)
       strip.setPixelColor(i, 0, 0, 0);
    strip.setPixelColor(0, red, green, blue);
  } 
  else strip.setPixelColor(counter, red, green, blue);
  strip.show();
}

void pong(int red, int green, int blue) {
   strip.setPixelColor(counter, red, green, blue);
   if (counter > 0) strip.setPixelColor(counter - 1, 0, 0, 0);
   strip.setPixelColor(strip.numPixels() - counter, red, green, blue);
   strip.setPixelColor(strip.numPixels() - counter + 1, 0, 0, 0);
   strip.show();
}

void rainbow7(uint16_t i) {
    int np = strip.numPixels();  // we use the modulo function with this
    strip.setPixelColor(    i  % np, 0, 0, 0); // turn off the traling edge
    strip.setPixelColor( (i+1) % np, 25, 0, 25); // violet
    strip.setPixelColor( (i+2) % np, 255, 0, 255); // indigo
    strip.setPixelColor( (i+3) % np, 0, 0, 150); // blue
    strip.setPixelColor( (i+4) % np, 0, 150, 0); // green
    strip.setPixelColor( (i+5) % np, 255, 255, 0); // yellow
    strip.setPixelColor( (i+6) % np, 110, 70, 0); // orange
    strip.setPixelColor( (i+7) % np, 150, 0, 0); // red
    strip.show();
}

void comet(int red, int blue, int green) {
  int n = strip.numPixels();
  int index = counter % n;
  strip.setPixelColor(index + 6, red, blue, green);
  strip.setPixelColor(index + 5, red / 1.5, blue / 1.5, green / 1.5);
  strip.setPixelColor(index + 4, red / 2, blue/ 2, green/ 2);
  strip.setPixelColor(index + 3, red / 4, blue/ 4, green/ 4);
  strip.setPixelColor(index + 2, red / 8, blue/ 8, green/ 8);
  strip.setPixelColor(index + 1, red / 16, blue/ 16, green/ 16);
  strip.setPixelColor(index, 0, 0, 0);
  strip.show();
}

// Slightly different, this makes the rainbow equally distributed throughout
void rainbowCycle() {
  int i, j;
    for(i=0; i< strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + counter) & 255));
    }
    strip.show();

}

uint32_t Wheel(byte WheelPos) {
  if(WheelPos < 85) {
   return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  } else if(WheelPos < 170) {
   WheelPos -= 85;
   return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else {
   WheelPos -= 170;
   return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
}

void candle() {
   uint8_t green; // brightness of the green 
   uint8_t red;  // add a bit for red
   
   for(uint8_t i=0; i<20; i++) { // pick 20 random pixels
     green = (50 + random(155)) ;
     red = green + random(50);
     strip.setPixelColor(random(strip.numPixels()), red, green, 0);
     strip.show();
  }
}

// walk down the strip and set each pixel to a randome color but not too bright
void randomRGB() {
  for(int i=0; i<strip.numPixels(); i++) {
     strip.setPixelColor(i, random(128), random(128), random(128));
     strip.show();
  }
}

//Theatre-style crawling lights with rainbow effect
void chase(int red, int green, int blue) {
   for (int i=0; i < strip.numPixels(); i++) {
      if ((i + counter) % 3 == 0) strip.setPixelColor(i, red, green, blue);
      else strip.setPixelColor(i, 0,0,0);
   }
   strip.show();
}

void sparkle(int red, int blue, int green) {
  int random_index = random(strip.numPixels()); // random number from 0 (inclusive) to number pixels exclusive
  strip.setPixelColor(last_random_index, 0, 0, 0); // turn off the old value
  strip.setPixelColor(random_index, red, blue, green); // make a random one turn on
  strip.show();
  last_random_index = random_index; // update the last index with the current one
}
