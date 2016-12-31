
int ledPins[] = {3,4,5,6,7,8,9,10,11,12};
int pin_count = 10;
int delayTime = 100;
int mode = 0;
int newModeInc = 0;
int number_modes = 5;
long lastDebounceTime = 0;  // the last time the output pin was toggled
long debounceDelay = 150;   // the debounce time; increase if the output flickers

void setup() {
  pinMode(2, INPUT_PULLUP);
  for(int index = 0; index <= pin_count -1; index++)
  {
    pinMode(ledPins[index],OUTPUT);
  }
  attachInterrupt(0, modeChange, FALLING);
  newModeInc = 0;
  Serial.begin(9600);
}

void modeChange() {
  newModeInc = 1;
}

void loop()
{
  if (newModeInc == 1) {
    if ((millis() - lastDebounceTime) > debounceDelay) {
      mode++;
      mode = mode % number_modes;
      Serial.print("Inc Mode=");
      Serial.println(mode, DEC);
      digitalWrite(13, LOW);
      newModeInc = 0;
    }
    else {
    }
  };
  switch (mode) {
      case 0: oneAfterAnotherLoop();break;
      case 1: oneOnAtATime();break;
      case 2: pingPong();break;
      case 3: marquee();break;
      case 4: randomLEDs();break;
     }
  Serial.print("mode=");
  Serial.println(mode);
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
    digitalWrite(ledPins[index+8], HIGH);  
    delay(delayTime * 2);                      // Pause to slow down the sequence
    digitalWrite(ledPins[index], LOW);     // Turn the LED off
    digitalWrite(ledPins[index+4], LOW);   // Skip four, and turn that LED off
    digitalWrite(ledPins[index+8], LOW);
  }
}


void randomLEDs(){
  for(int index = 0; index <=  20; index++) 
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

