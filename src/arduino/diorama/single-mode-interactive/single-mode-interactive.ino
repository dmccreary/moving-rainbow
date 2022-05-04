#include <Servo.h>
Servo myservo;  // create servo object to control servo
// these constant values never change
const int potpin = A0; // Analog pin connected to middle of POT
const int Light_Sensor_Pin = A1;
const int momentary_button_music_pin = 2;
const int momentary_button_motor_pin = 3;
const int motorPin =4;
const int servoPin =5;
const int ledPin = 9;
const int buzzerPin = 7;


// my photoresistor goes from 500 (dark) to 1020 (light)
// I have a 50K pull down resistor
int lightLevel = 0, high = 1020, low = 700;
int potValue = 512; // 1/2 way
int servoAngle = 90; // 1/2 way
int music_on = 0; // 0 is off, 1 is on
int motor_on = 0; // 0 is off, 1 is on

void setup() {
  attachInterrupt(0, toggle_music, FALLING); // this says call the toggle_music function if the value goes down
  attachInterrupt(1, toggle_motor, FALLING); // this says call the toggle_motor function if the value goes dow
  pinMode(momentary_button_music_pin, INPUT_PULLUP); // attach a momentary push button to pin 2, this pulls it up HIGH
  pinMode(momentary_button_motor_pin, INPUT_PULLUP); // attach a momentary push button to pin 3, this pulls it up HIGH
  pinMode(ledPin, OUTPUT);
  pinMode(motorPin, OUTPUT);
  myservo.attach(servoPin);
  // to see what is happening in the main loop(), press the magnify icon in the upper right
  Serial.begin(9600); 
}

// each interrupt on pin 2 we toggle music
void toggle_music() {
  if (music_on == 0)
     {music_on = 1;}
  else {music_on = 0;}
};

// each interrupt on pin 3 we toggle a motor
void toggle_motor() {
  if (motor_on == 0)
     {motor_on = 1;}
  else {motor_on = 0;}
};

// the loop function runs over and over again forever
void loop() {
  if (music_on == 1)
  {
      Serial.print("Music on ");
      playSong();
  }
  if (music_on == 0)
  {
      Serial.print("Music off ");
      
  }
  
  if (motor_on == 1)
  {
      digitalWrite(motorPin, HIGH);
      Serial.print("Motor on ");
  }
  if (motor_on == 0)
  {
    digitalWrite(motorPin, LOW);
    Serial.print("Motor off ");
  }
  
  // do the continious things
  // adjust the LED
  lightLevel = analogRead(Light_Sensor_Pin);
  Serial.print("read=");
  Serial.print(lightLevel);
  Serial.print(" tune=");
  autoTune();
  Serial.print(lightLevel);
  analogWrite(ledPin, 255 - lightLevel);
  
  // now adjust the servo from the pot value
  potValue = analogRead(potpin);
  Serial.print(" servo pot=");
  Serial.print(potValue);
  servoAngle = map(potValue, 0, 1023, 0, 180);
  Serial.print(" angle=");
  Serial.print(servoAngle);
  myservo.write(servoAngle);
  Serial.println(""); // send a new line
}

void autoTune()
{
  if (lightLevel < low)
  {
    low = lightLevel;
  }
  if (lightLevel > high)
  {
    high = lightLevel;
  }
  lightLevel = map(lightLevel, low + 100, high - 30, 0, 255);
  lightLevel = constrain(lightLevel, 0, 255);
}

void playSong() {
  // a space represents a rest
  const int songLength = 52;
  char notes[] = "GGAGEC ccdcAF GGAGECED GG GGAGEC ccdcAF GGAGFDEC CC ";
  int beats[] = {1,2,1,1,1,2,1,1,2,1,1,1,2,1,1,2,1,1,1,1,1,2,1,2,2,1,1,2,
                 1,1,1,2,1,1,2,1,1,1,2,1,1,2,1,1,1,1,1,2,1,2,2,5};
  int tempo = 300;
  int i, duration;

  for (i = 0; i < songLength; i++) // step through the song arrays
  {
    if (music_on == 1 ) {
        digitalWrite(ledPin, HIGH);
        duration = beats[i] * tempo;  // length of note/rest in ms
        if (notes[i] == ' ')          // is this a rest? 
        {
          delay(duration);            // then pause for a moment
        }
        else                          // otherwise, play the note
        {
          tone(buzzerPin, frequency(notes[i]), duration);
          delay(duration);            // wait for tone to finish
          digitalWrite(ledPin, LOW);
        }
        delay(tempo/10);              // brief pause between notes
    }
  }
};
  
int frequency(char note) 
{
  int i;
  const int numNotes = 8;  // number of notes we're storing
  char names[] = { 'G', 'A', 'E', 'C', 'c', 'd', 'F', 'D' };
  int frequencies[] = {392, 440, 329, 262, 523, 587, 349, 293};
  for (i = 0; i < numNotes; i++)  // Step through the notes
  {
    if (names[i] == note)         // Is this the one?
    {
      return(frequencies[i]);     // Yes! Return the frequency
    }
  }
  return(0);
};
