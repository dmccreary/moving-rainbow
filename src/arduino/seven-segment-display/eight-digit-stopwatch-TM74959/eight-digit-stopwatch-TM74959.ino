#include <TimerOne.h>
#define NDIGITS         8
#define NDIGITS_MASK    7

// SPI bus connection pins
// DIO yellow 12
// RCLK white 11
// SCLK orange 10

const int latchpin = 11 ;       // connect to RCK of display
const int clockpin = 10 ;       // connect to SCK of display
const int datapin = 12 ;        // connect to DIO of display
const byte start_stop_interrupt_pin = 2; // a momentary push button to GND
const byte reset_interrupt_pin = 3; // a momentary push button to GND

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

// the leftmost bit is the decimal place
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
    0b11111111,  // blank
} ;

byte segbuf[NDIGITS] ;
int segcnt = 0;

long interval = 10;       // wait interval in the main loop, update time to refresh buffer
byte running = 0;         // 1 if we are running
int seconds;
int minutes;
int hours;
long startTime;                    // start time for stop watch set to zero when the start button is pressed
long elapsedTime;                  // elapsed time for stop watch
int fractional;                    // variable used to store fractional part of time

int start_stop_button_pressed = 0; // set to 1 when the button is pressed
int reset_button_pressed = 0; // set to 1 when the button is pressed
long lastDebounceTime = 0;  // the last time the output pin was toggled
long debounceDelay = 170;   // the debounce time; increase if the output flickers

// this is an interrupt service routine that gets called every 3 milliseconds
void update_display(void) {
    // setting the latch pin LOW means we are ready to send two bytes of data to the display
    digitalWrite(latchpin, LOW);
    // the order of these two lines might need to be changed depending on your display
    shiftOut(datapin, clockpin, MSBFIRST, segbuf[segcnt]) ;
    shiftOut(datapin, clockpin, MSBFIRST, col[segcnt]) ;
    // not that the data has been sent, tell the display we are done by setting the latch HIGH
    digitalWrite(latchpin, HIGH) ;
    segcnt ++ ;
    segcnt &= NDIGITS_MASK ;
}

// we keep these very short since all other IRQs are disabled during a call
void start__stop_button_pressed_irq() {
  start_stop_button_pressed = 1;
  lastDebounceTime = millis();
}

void reset_button_pressed_irq() {
  reset_button_pressed = 1;
  lastDebounceTime = millis();
}

void setup() {
    pinMode(latchpin, OUTPUT);
    pinMode(clockpin, OUTPUT);
    pinMode(datapin, OUTPUT);

    // we use the internal resistors to pull these high
    pinMode(start_stop_interrupt_pin, INPUT_PULLUP);
    pinMode(reset_interrupt_pin, INPUT_PULLUP);

    Serial.begin(9600);
    Serial.println("Stopwatch using an eight digit seven segment display that uses two 74595 shift registers.");

    Timer1.initialize(2000); // a timer that fires every 2-3 ms seems to avoid flicker
    Timer1.attachInterrupt(update_display);
    Timer1.start();

    // this watches for an external FALLING event from HIGH to LOW on pin 2
    attachInterrupt(digitalPinToInterrupt(start_stop_interrupt_pin), start__stop_button_pressed_irq, FALLING);
    attachInterrupt(digitalPinToInterrupt(reset_interrupt_pin), reset_button_pressed_irq, FALLING);
    start_stop_button_pressed = 0;
    reset_button_pressed = 0;
    running = 0;
}

void loop() {

    // first check if we have any external events
    if (start_stop_button_pressed == 1) {
      if ((millis() - lastDebounceTime) > debounceDelay) {

        running = !running; // toggle the running mode each time it is pressed
        start_stop_button_pressed = 0;
        Serial.println("The start-stop button has been pressed.");
      }
    }

    if (reset_button_pressed == 1) {
      if ((millis() - lastDebounceTime) > debounceDelay) {
        running = 0; // toggle the running bit each time it is pressed
        startTime = millis();
        elapsedTime = 0;
        seconds = 0;
        minutes = 0;
        hours = 0;
        reset_button_pressed = 0;
        Serial.println("The reset button has been pressed.");
      }
    }
    
    if (running == 1) {
      elapsedTime =   millis() - startTime; // elapsed time in milliseconds
      seconds = elapsedTime/1000; // a second is 1000 milliseconds
      minutes = elapsedTime/60000; // 60,000 milliseconds in a minute
      hours = minutes/60;
    }
    
    // print to the console every second when running
    if (running == 1 && (elapsedTime/100) % 10 == 0 && (elapsedTime/10) % 10 == 0) {
      Serial.print("h=");
      Serial.print(hours); 
      Serial.print(" m=");
      Serial.print(minutes); 
      Serial.print(" s=");
      Serial.println(seconds); 
    }
    
    // update the buffer from left to right
    // 100th of a second
    segbuf[7] = seg[(elapsedTime/10) % 10];
    // 10th of a second
    segbuf[6] = seg[(elapsedTime/100) % 10];
    
    // seconds
    segbuf[5] = seg[seconds % 10];

    // tens of seconds
    if (hours == 0 && minutes == 0 && seconds < 9 )
       segbuf[4] = seg[10]; // blank tens of seconds
    else segbuf[4] = seg[seconds/10 % 6];
    
    // minutes
      if (minutes == 0 && hours == 0)
          segbuf[3] = seg[10]; // blank
      else segbuf[3] = seg[minutes % 10];
      
    // tens of minutes
      if (minutes > 9 && hours == 0)
         segbuf[2] = seg[(minutes/10) % 6];
      else segbuf[2] = seg[10]; // blank if under 9 minutes and no hours

    // hours
    if (hours == 0)
       segbuf[1] = seg[10]; // blank for no hours
    else segbuf[1] = seg[hours % 10];

    // tens of hours
    if (hours > 9)
       segbuf[0] = seg[(hours/10) % 10];
    else segbuf[0] =  seg[10]; // blank if hours under 9

    // wait 1/100 of a second to update anything
    delay(interval);

}
