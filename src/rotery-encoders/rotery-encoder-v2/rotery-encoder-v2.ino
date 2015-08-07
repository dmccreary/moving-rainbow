/* Rotery encoder with a single interrupt. Based on a demo by Budd Churchward.
See: https://www.youtube.com/watch?v=FGxLXqzPe3Q
*/

const byte pinA = 2; // encoder pin A to Arduino pin 2 which is also interrupt pin 0 which we will use
const byte pinB = 3; // encoder pin B to Arduino pin 3 which is also interrupt pin 1 but we won't use it
byte state = 0; // will store two bits for pins A & B on the encoder which we will get from the pins above
int level = 0; // a value bumped up or down by the encoder
int haveNewInterrupt = 0; // 1 if we have a new interrupt to show, 0 otherwise


/* For demo purposes we will create an array of these binary digits */
String bits[] = {"00", "01", "10", "11"};

/* A truth table of possible moves 1 for clockwise
 -1 for counter clockwwise 0 for error - keybounce */
int bump[] = {0,0,-1,1};

void setup() {
 pinMode(pinA,INPUT); // reads Pin A of the encoder
 pinMode(pinB,INPUT); // reads Pin B of the encoder * Writing to an Input pin turns on an internal pull up resistor *
 digitalWrite(pinA,HIGH);
 digitalWrite(pinB,HIGH); // Set up to call our knob function any time pinA rises
 attachInterrupt(0, knobTurned, RISING); // calls our 'knobTurned()' function when pinA goes from LOW to HIGH level = 50; -- a value to start with * Set up for using the on-screen monitor *
 Serial.begin(115200); // make sure your monitor baud rate matches this
 
 Serial.println("Encoder Ready");
 Serial.print("level = ");
 Serial.println(level); // to remind us where we're starting
}

void loop() {
 if (haveNewInterrupt == 1)
    {
     Serial.print(bits[state]); // show us the two bits
     Serial.print("   ");
     Serial.print(bump[state]); // show us the direction of the turn
     Serial.print("   ");
     Serial.println(level); // show us the new value
     haveNewInterrupt = 0; // now we are done
    }
}

/* The Interrup Service Routine ISR for the knob being turned 
   Note that the Arduino has two hardware interrups but we only need one. 
   Never put Serial.printing in an ISR.  Just get in and get out fast.
   */
   
void knobTurned() {
 /* AH HA! the knob was turned */
 haveNewInterrupt = 1; // this is for the main loop to catch
 state = 0; // reset this value each time
 state = state + digitalRead(pinA); // add the state of Pin A
 state <<= 1; // shift the bit over one spot
 state = state + digitalRead(pinB); // add the state of Pin B * now we have a two bit binary number that holds the state of both pins 00 - something is wrong we must have got here with a key bounce 01 - sames as above - first bit should never be 0 10 - knob was turned backwards 11 - knob was turned forwards   We can pull a value out of our truth table and add it to the current level *
 level = level + bump[state]; // Let's see what happened
}
