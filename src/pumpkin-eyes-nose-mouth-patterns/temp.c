// a seven segment rainbow with red on the highest pixel
void rainbow7(uint16_t wait) {
  int np = left_eye.numPixels();  // we use the modulo function with this
  for (int i=0; i<np; i++) { 
      mouth.setPixelColor(i     % np, 0, 0, 0); // off
      mouth.setPixelColor((i+1) % np, 25, 0, 25); // violet
      mouth.setPixelColor((i+2) % np, 255, 0, 255); // indigo
      mouth.setPixelColor((i+3) % np, 0, 0, 150); // blue
      mouth.setPixelColor((i+4) % np, 0, 150, 0); // green
      mouth.setPixelColor((i+5) % np, 255, 255, 0); // yellow
      mouth.setPixelColor((i+6) % np, 110, 70, 0); // orange
      mouth.setPixelColor((i+7) % np, 150, 0, 0); // red
      mouth.setPixelColor((i+8) % np, 0, 0, 0); // off
      mouth.setPixelColor((i+10) % np, 0, 0, 0); // off
      mouth.setPixelColor((i+11) % np, 0, 0, 0); // off
      mouth.show();
      increment_eyes();
      delay(wait);
  }
}

void increment_eyes() {
  left_eye.setPixelColor(0, Wheel(loop_count*ear_ring_increment_steps % 255));
  left_eye.show();
  right_eye.setPixelColor(0, Wheel(loop_count*ear_ring_increment_steps % 255));
  right_eye.show();
};

// See https://en.wikipedia.org/wiki/Web_colors
void singlePixel(uint8_t wait) {
   for(uint8_t i=0; i<mouth.numPixels(); i++) {
     // turn it on
      mouth.setPixelColor(i , 255, 0, 0);
      // show it
      mouth.show();
      // wait
      delay(wait);
      // turn it off
      mouth.setPixelColor(i , 0, 0, 0);  
  }
}

// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<mouth.numPixels(); i++) {
      mouth.setPixelColor(i, c);
      mouth.show();
      delay(wait);
  }
  // turn them all off
  for(uint16_t i=0; i<mouth.numPixels(); i++) {
      mouth.setPixelColor(i, 0);
      mouth.show();
      delay(wait);
  }
  mouth.show();
  increment_eyes();
}
 
void rainbow(uint8_t wait) {
  uint16_t i, j;
 
  for(j=0; j<256; j++) {
    for(i=0; i<mouth.numPixels(); i++) {
      mouth.setPixelColor(i, Wheel((i+j) & 255));
    }
    mouth.show();
    increment_eyes();
    delay(wait);
  }
}
 
// Slightly different, this makes the rainbow equally distributed throughout
void rainbowCycle(uint8_t wait) {
  uint16_t i, j;
 
  for(j=0; j<256; j++) { // all colors on wheel
    for(i=0; i< mouth.numPixels(); i++) {
      mouth.setPixelColor(i, Wheel(((i * 256 / mouth.numPixels()) + j) & 255));
    }
    mouth.show();
    increment_eyes();
    delay(wait/20); // it takes longer to do the double loop so shorten the wait
  }
}
 
// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  if(WheelPos < 85) {
   return mouth.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  } else if(WheelPos < 170) {
   WheelPos -= 85;
   return mouth.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else {
   WheelPos -= 170;
   return mouth.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
}

void candle() {
   uint8_t green; // brightness of the green 
   uint8_t red;  // add a bit for red
   for(uint8_t i=0; i<100; i++) {
     green = 50 + random(155);
     red = green + random(50);
     mouth.setPixelColor(random(mouth.numPixels()), red, green, 0);
     mouth.show();
     increment_eyes();
     delay(5);
  }
}

void randomRGB(uint8_t wait) {
  for(uint16_t i=0; i<mouth.numPixels(); i++) {
     mouth.setPixelColor(i, random(255), random(255), random(255));
     mouth.show();
     increment_eyes();
     delay(wait);
  }
}

void randomColor(uint8_t wait) {
int newColor;
  for(uint16_t i=0; i<mouth.numPixels(); i++) {
     newColor = Wheel(random(255));
     mouth.setPixelColor(i, newColor);
     mouth.show();
     increment_eyes();
     delay(wait);
  }
}

//Theatre-style crawling lights with rainbow effect
void theaterChaseRainbow(uint8_t wait) {
  for (int j=0; j < 256; j=j+32) {     // cycle all 256 colors in the wheel
    for (int q=0; q < 3; q++) {
        for (int i=0; i < mouth.numPixels(); i=i+3) {
          mouth.setPixelColor(i+q, Wheel( (i+j) % 255));    //turn every third pixel on
        }
        mouth.show();
        increment_eyes();
        delay(wait);
        for (int i=0; i < mouth.numPixels(); i=i+3) {
          mouth.setPixelColor(i+q, 0);        //turn every third pixel off
        }
    }
  }
}
