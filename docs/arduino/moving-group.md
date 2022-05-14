# Moving Pixel

This loop will move a group of pixels from one end of the LED strip to the other.  The central pixel in the group will be brighter then the other pixels
```
void loop() {
  for (int i=0; i<NUMBER_PIEXELS-4; i++) {
    strip.setPixelColor(i,    5, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+1,  50, 0, 0); // turn the i+1 pixel
    strip.setPixelColor(i+2, 255, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+3,  50, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+4,  5, 0, 0); // turn the "i"th pixel on
    strip.show();
    delay(500); // wait 2/10th of a second
    strip.setPixelColor(i,   0, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+1, 0, 0, 0); // turn the i+1 pixel
    strip.setPixelColor(i+2, 0, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+3, 0, 0, 0); // turn the "i"th pixel on
    strip.setPixelColor(i+4, 0, 0, 0); // turn the "i"th pixel on
    strip.show();
  }
}
```