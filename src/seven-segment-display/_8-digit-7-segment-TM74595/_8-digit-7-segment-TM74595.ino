//   ___     ____
//  ( _ )_ _/_  /
// / _  \ \ // / 
// \___/_\_\/_/  
//               
// 8x7.ino
// 
// A simple, interrupt driven routine that will drive an 8 segment, 8 digit
// display attached to the Teensy, with as little muss and fuss as I can 
// think.

#include <TimerOne.h>

#define NDIGITS         8
#define NDIGITS_MASK    7

const int latchpin = 11;       // connect to RCK
const int clockpin = 10;       // connect to SCK
const int datapin = 12;        // connect to DIO


byte col[NDIGITS] = {
    0b10000000,
    0b01000000,
    0b00100000,
    0b00010000,
    0b00001000,
    0b00000100,
    0b00000010,
    0b00000001
} ;


/*
byte seg[] = {
    0b11000000,  // 0
    0b11111001,  // 1
    0b10100100,  // 2
    0b10110000,  // 3
    0b10011001,  // 4
    0b10010010,  // 5
    0b10000010,  // 6
    0b11111000,  // 7
    0b10000000,  // 8
    0b10010000,  // 9  
};
*/
byte seg[] = {
    0xC0,  // 0
    0xF9,  // 1
    0xA4,  // 2
    0xB0,  // 3
    0x99,  // 4
    0x92,  // 5
    0x82,  // 6
    0xF8,  // 7
    0x80,  // 8
    0x90,  // 9  
};

// in memory segment buffer
byte segbuf[NDIGITS];
int segcnt = 0;

int loop_counter =0;

void LED_irq(void) {
    digitalWrite(latchpin, LOW);

    // select the digit...
    shiftOut(datapin, clockpin, MSBFIRST, col[segcnt]);
    // and select the segments
    shiftOut(datapin, clockpin, MSBFIRST, segbuf[segcnt]);

    digitalWrite(latchpin, HIGH);
    segcnt++;
    segcnt &= NDIGITS_MASK;
}

void
setup()
{
    // setup all the data pins...

    pinMode(latchpin, OUTPUT);
    pinMode(clockpin, OUTPUT);
    pinMode(datapin, OUTPUT);

    // Initialize the segment buffers...

    for (int i=0; i<8; i++)
       segbuf[i] = seg[i]; 

    Serial.begin(9600);
    Serial.println("8x7 TEST");

    Timer1.initialize(3000); // 3 ms refresh has no flicker
    Timer1.attachInterrupt(LED_irq);
    Timer1.start();

    // Should auto-run at this point... 
}


void
loop()
{
    segbuf[0] = loop_counter % 10;
    segbuf[1] = loop_counter/10 % 10;
    segbuf[2] = loop_counter/100 % 10;
    segbuf[3] = loop_counter/1000 % 10;
    segbuf[4] = loop_counter/10000 % 10;
    segbuf[5] = loop_counter/100000 % 10;
    segbuf[6] = loop_counter/1000000 % 10;
    segbuf[7] = loop_counter/10000000 % 10;
    for (int i=7; i >= 0; i--) {
       Serial.print(segbuf[i]);
       Serial.print(" ");
    }
    Serial.println("");
    loop_counter++;
    delay(1000) ;
}
