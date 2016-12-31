
int ledPins[] = {3,4,5,6,7,8,9,10,11,12};
int pin_count = 10;
int delayTime = 100;
int mode = 0;

void setup() {
  int index;
  for(index = 0; index <= pin_count -1; index++)
  {
    pinMode(ledPins[index],OUTPUT);
  }
  Serial.begin(9600);
}


void loop()
{
  oneAfterAnotherLoop();  // Same as oneAfterAnotherNoLoop,
                          // but with much less typing
  oneOnAtATime();         // Turn on one LED at a time,
                          // scrolling down the line
  pingPong();             // Light the LEDs middle to the edges
  marquee();              // Chase lights like you see on signs
  randomLEDs();            // Blink LEDs randomly
  Serial.println("n");
}
 
void oneAfterAnotherLoop() {
  int index;
  for(index = 0; index <= pin_count - 1; index++)
  {
    digitalWrite(ledPins[index], HIGH);
    delay(delayTime);                
  }                                  

  for(index = pin_count - 1; index >= 0; index--)
  {
    digitalWrite(ledPins[index], LOW);
    delay(delayTime);
  }               
}

 
void oneOnAtATime() {
  int index;
  
  // step through the LEDs, from 0 to pin_count - 1
  
  for(index = 0; index <= pin_count - 1; index++)
  {
    digitalWrite(ledPins[index], HIGH);  // turn LED on
    delay(delayTime);                    // pause to slow down
    digitalWrite(ledPins[index], LOW);   // turn LED off
  }
}

 
/*
pingPong()

This function will step through the LEDs,
lighting one at at time in both directions.
*/

void pingPong() {
  int index;
  for(index = 0; index <= pin_count - 1; index++)
  {
    digitalWrite(ledPins[index], HIGH);  // turn LED on
    delay(delayTime);                    // pause to slow down
    digitalWrite(ledPins[index], LOW);   // turn LED off
  }

  // step through the LEDs, from pin_count - 1 to 0
  
  for(index = pin_count - 1; index >= 0; index--)
  {
    digitalWrite(ledPins[index], HIGH);  // turn LED on
    delay(delayTime);                    // pause to slow down
    digitalWrite(ledPins[index], LOW);   // turn LED off
  }
}


/*
This function will mimic "chase lights" like those around signs.
*/

void marquee() {
  int index;
  
  // Step through the first four LEDs
  // (We'll light up one in the lower 4 and one in the upper 4)
  
  for(index = 0; index <= 3; index++) // Step from 0 to 3
  {
    digitalWrite(ledPins[index], HIGH);    // Turn a LED on
    digitalWrite(ledPins[index+4], HIGH);  // Skip four, and turn that LED on
    delay(delayTime * 2);                      // Pause to slow down the sequence
    digitalWrite(ledPins[index], LOW);     // Turn the LED off
    digitalWrite(ledPins[index+4], LOW);   // Skip four, and turn that LED off
  }
}


void randomLEDs(){
  for(int index = 0; index <=  30; index++) 
      randomLED();
}

void randomLED()
{
  int index;
  index = random(pin_count);	// pick a random number between 0 and pin_count - 1
  digitalWrite(ledPins[index], HIGH);  // turn LED on
  delay(delayTime * 1.5);                    // pause to slow down
  digitalWrite(ledPins[index], LOW);   // turn LED off
}

