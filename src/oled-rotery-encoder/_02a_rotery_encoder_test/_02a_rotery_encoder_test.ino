// This example toggles the debug LED (pin 13) on or off
// when a button on pin 2 is pressed.

// Include the Bounce2 library found here :
// https://github.com/thomasfredericks/Bounce2
#include <Bounce2.h>

#define SET_PIN 4 // momentary push button set the current encoder value to be the new variable
#define PROG_PIN 5 // momentary push button change the programming mode
#define LED_PIN 13

int ledState = LOW;

Bounce debouncer_set = Bounce();
Bounce debouncer_prog = Bounce();

void setup() {

  pinMode(SET_PIN, INPUT_PULLUP);
  pinMode(PROG_PIN, INPUT_PULLUP);
  debouncer_set.attach(SET_PIN, INPUT_PULLUP); // Attach the debouncer to a pin with INPUT_PULLUP mode
  debouncer_set.interval(25); // Use a debounce interval of 25 milliseconds
  
  debouncer_prog.attach(PROG_PIN, INPUT_PULLUP); // Attach the debouncer to a pin with INPUT_PULLUP mode
  debouncer_prog.interval(25); // Use a debounce interval of 25 milliseconds 
  
  pinMode(LED_PIN, OUTPUT); // Setup the LED
  digitalWrite(LED_PIN, ledState);
 
}

void loop() {

   debouncer_set.update(); // Update the Bounce instance
   
   if ( debouncer_set.fell() ) {  // Call code if button transitions from HIGH to LOW
     ledState = !ledState; // Toggle LED state
     digitalWrite(LED_PIN,ledState); // Apply new LED state
   }

   debouncer_prog.update();
   if ( debouncer_prog.fell() ) {  // Call code if button transitions from HIGH to LOW
     ledState = !ledState; // Toggle LED state
     digitalWrite(LED_PIN,ledState); // Apply new LED state
   }
}

