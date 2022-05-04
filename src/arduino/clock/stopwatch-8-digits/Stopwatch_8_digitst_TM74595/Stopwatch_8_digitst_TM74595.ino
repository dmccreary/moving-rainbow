#include <TM74HC595Display.h>

/*
An attempte to turn the color of the clock on by changing the mst and lst to be 0. 
Did not work since the library must be masking the bits also.
*/

int SCLK = 10;
int RCLK = 11;
int DIO = 12;
byte position = 0b00000001;

TM74HC595Display disp(SCLK, RCLK, DIO);
unsigned char LED_0F[29];
// current character in loop
unsigned char cc;
unsigned char ccm;

void setup() {
  LED_0F[0] = 0xC0; //0
  LED_0F[1] = 0xF9; //1
  LED_0F[2] = 0xA4; //2
  LED_0F[3] = 0xB0; //3
  LED_0F[4] = 0x99; //4
  LED_0F[5] = 0x92; //5
  LED_0F[6] = 0x82; //6
  LED_0F[7] = 0xF8; //7
  LED_0F[8] = 0x80; //8
  LED_0F[9] = 0x90; //9
  Serial.begin(9600);
}

void loop() {  

for (int digit=0; digit<=9; digit++) {
    
    for (int i=0; i<=9; i++) {
      disp.send(LED_0F[i], position);    //send digital "0" to 2nd indicator
      delay(100);
     }
      position = position << 1;
      delay(1000);
   }
}

