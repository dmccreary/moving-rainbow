/* Debouncing Increment and Decrement Buttons
   Dan McCreary

Hook up two momentary push buttons to pins 2 and 3.
One button will increment the mode, one will decrment the mode
You MUST use pins 2 and 3 because they are the only Interrupt pins on the Arduino (Uno, Nano)
Connect the other ends of the momentary push buttons to GND
Note that we are using internal 20K resistors to pull up the inputs to +5 when the buttons are open
*/
int mode = 0; // This is the "mode" of the device.  It starts at 0 and gets incremented or decremented
int newModePlus = 0; // the interrupts set this to 1 to indicate that we have a new increment to handle
int newModeMinus = 0; // the interrupts set this to 1 to indicate that we have a new decrement to handle
int numberTimesModePlusCalled = 0; // just for fun, we count the number of "noise" transitions
int numberTimesModeMinusCalled = 0;  // many buttons have noise from 1 to 5 transitions within 200ms

long lastDebounceTime = 0;  // the last time the output pin was toggled
long debounceDelay = 200;   // the debounce time; increase if the output flickers

void setup()
{
  pinMode(13, OUTPUT);     // Pin 13 is output to which an LED is connected
  digitalWrite(13, LOW);   // Make pin 13 low, switch LED off
  pinMode(2, INPUT_PULLUP);	   // Pin 2 is input to which a switch is connected = INT0
  pinMode(3, INPUT_PULLUP);	   // Pin 3 is input to which a switch is connected = INT1
  attachInterrupt(0, changeModeAdd, FALLING  ); // pin 2
  attachInterrupt(1, changeModeMinus, FALLING  ); // pin 3
  Serial.begin(9600);
  Serial.println("Start");
  Serial.print("Mode=");
  Serial.println(mode, DEC);
}

void loop() {
  if (newModePlus == 1) {
    if ((millis() - lastDebounceTime) > debounceDelay) {
      mode++;
      Serial.print("Inc Mode=");
      Serial.print(mode, DEC);
      Serial.print(" N=");
      Serial.println(numberTimesModePlusCalled, DEC);
      digitalWrite(13, LOW);
      newModePlus = 0;
      numberTimesModePlusCalled = 0;
    }
    else {
    }
  }
  
  if (newModeMinus == 1) {
    if ((millis() - lastDebounceTime) > debounceDelay) {
      mode--;
      Serial.print("Dec Mode=");
      Serial.print(mode, DEC);
      Serial.print(" N=");
      Serial.println(numberTimesModeMinusCalled, DEC);
      digitalWrite(13, LOW);
      newModeMinus = 0;
      numberTimesModeMinusCalled = 0;
    }
  }
}  

void changeModeAdd(){        // Interrupt service routine
  digitalWrite(13, HIGH); // we have a new mode
  newModePlus = 1;
  numberTimesModePlusCalled++;
  lastDebounceTime = millis();
}

void changeModeMinus(){        // Interrupt service routine
  digitalWrite(13, HIGH); // we have a new mode
  newModeMinus = 1;
  numberTimesModeMinusCalled++;
  lastDebounceTime = millis();
}
