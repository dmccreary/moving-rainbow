#include <TM74HC595Display.h>

/*
This program writes digits 0-9 to the right most display and
then repeats this pattern for each postion from right to left.
*/

int SCLK = 10;
int RCLK = 11;
int DIO = 12;
byte position = 0b00000001;
int counter =0;
int delay_value = 5;

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


  for (int i=0; i<=9; i++) {
        disp.send(LED_0F[i], 0b00000001);    // right most digit
        delay(delay_value);
        disp.send(LED_0F[i], 0b00000010);    // 2nd from right digit
        delay(delay_value);
        disp.send(LED_0F[i], 0b00000100);
        delay(delay_value);
        disp.send(LED_0F[i], 0b00001000);
        delay(delay_value);
        disp.send(LED_0F[i], 0b00010000);
        delay(delay_value);
        disp.send(LED_0F[i], 0b00100000);
        delay(delay_value);
        disp.send(LED_0F[i], 0b01000000);
        delay(delay_value);
        disp.send(LED_0F[i], 0b10000000);
        delay(delay_value);
     }
}

