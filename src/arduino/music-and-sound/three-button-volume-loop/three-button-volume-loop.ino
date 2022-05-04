

#include "Arduino.h"
#include "SoftwareSerial.h"
#include "DFRobotDFPlayerMini.h"

SoftwareSerial mySoftwareSerial(10, 11); // RX, TX
DFRobotDFPlayerMini myDFPlayer;

int buttonNextPin = 2;
int buttonPausePin = 3;
int buttonPreviousPin = 4;
int volumePotPin = A0;
int volumePotValue = 255; // ranges from 0 to 1023
int volumeValue = 10; // ranges from 0 to 30
int newVolumeValue = 10; // ranges from 0 to 30

int track = 1;
int new_track = 1;
void printDetail(uint8_t type, int value);
boolean isPlaying = true;

void setup()
{
  pinMode(buttonNextPin, INPUT_PULLUP);
  pinMode(buttonPausePin, INPUT_PULLUP);
  pinMode(buttonPreviousPin, INPUT_PULLUP);
  
  mySoftwareSerial.begin(9600);
  Serial.begin(115200);
  
  Serial.println();
  Serial.println(F("DFRobot DFPlayer Mini Demo"));
  Serial.println(F("Initializing DFPlayer ... (May take 3~5 seconds)"));
  
  if (!myDFPlayer.begin(mySoftwareSerial)) {  //Use softwareSerial to communicate with mp3.
    Serial.println(F("Unable to begin:"));
    Serial.println(F("1.Please recheck the connection!"));
    Serial.println(F("2.Please insert the SD card!"));
    while(true);
  }
  Serial.println(F("DFPlayer Mini online."));
  
  myDFPlayer.setTimeOut(500); //Set serial communictaion time out 500ms
  
  //----Set volume----
  myDFPlayer.volume(15);  //Set volume value (0~30).

  myDFPlayer.outputDevice(DFPLAYER_DEVICE_SD);

  myDFPlayer.enableLoopAll();

 //   myDFPlayer.randomAll(); //Random play all the mp3.

  //----Read imformation----
  Serial.print("State=");
  Serial.println(myDFPlayer.readState()); //read mp3 state

  Serial.print("Vol=");
  Serial.println(myDFPlayer.readVolume()); //read current volume
  Serial.println(myDFPlayer.readEQ()); //read EQ setting
  
  Serial.print("File Count=");
  Serial.println(myDFPlayer.readFileCounts()); //read all file counts in SD card

  Serial.print("File Number=");
  Serial.println(myDFPlayer.readCurrentFileNumber()); //read current play file number


  myDFPlayer.play(1);  //Play the first mp3
    
}

void loop()
{
  static unsigned long timer = millis();
  
  if (digitalRead(buttonNextPin) == LOW) {
      myDFPlayer.next();
      track++;
  }

   if (digitalRead(buttonPreviousPin) == LOW) {
      myDFPlayer.previous();
      track--;
  }

  if (digitalRead(buttonPausePin) == LOW) {
      if (isPlaying == 1) {
         myDFPlayer.pause();
         isPlaying = 0;
         Serial.print("Pause");
      }
      else {
        myDFPlayer.start();
        isPlaying = 1;
        Serial.print("Continue");
      }
  }
  
  if (myDFPlayer.available()) {
    printDetail(myDFPlayer.readType(), myDFPlayer.read()); //Print the detail message from DFPlayer to handle different errors and states.
  }

  // if we have just finished one song then play the next
  if (myDFPlayer.available()) {
    if (myDFPlayer.readType() == DFPlayerPlayFinished) {
      track++;
      myDFPlayer.next();
      Serial.print("Track finished Playing next track: ");
      Serial.println(track);
    }
  }
  

  volumePotValue = analogRead(volumePotPin);
//  Serial.print("Vol=");
//  Serial.println(volumePotValue);
  newVolumeValue = map(volumePotValue, 0, 1023, 0, 30);
  
  if (newVolumeValue != volumeValue) {
     myDFPlayer.volume(newVolumeValue);
     volumeValue = newVolumeValue;
     Serial.print("Playing=");
     Serial.print(isPlaying);
     Serial.print(" Track=");
     Serial.print(track);
     Serial.print(" New vol=");
     Serial.println(volumeValue);
  };

  // print this only on a track change
  if (track != new_track) {
    Serial.print("Playing=");
    Serial.print(isPlaying);
    Serial.print(" Track=");
    Serial.print(track);
    Serial.print(" Vol=");
    Serial.println(volumeValue);
    new_track = track;
  };
  
  delay(100);
}

void printDetail(uint8_t type, int value){
  switch (type) {
    case TimeOut:
      Serial.println(F("Time Out!"));
      break;
    case WrongStack:
      Serial.println(F("Stack Wrong!"));
      break;
    case DFPlayerCardInserted:
      Serial.println(F("Card Inserted!"));
      break;
    case DFPlayerCardRemoved:
      Serial.println(F("Card Removed!"));
      break;
    case DFPlayerCardOnline:
      Serial.println(F("Card Online!"));
      break;
    case DFPlayerPlayFinished:
      Serial.print(F("Number:"));
      Serial.print(value);
      Serial.println(F(" Play Finished!"));
      break;
    case DFPlayerError:
      Serial.print(F("DFPlayerError:"));
      switch (value) {
        case Busy:
          Serial.println(F("Card not found"));
          break;
        case Sleeping:
          Serial.println(F("Sleeping"));
          break;
        case SerialWrongStack:
          Serial.println(F("Get Wrong Stack"));
          break;
        case CheckSumNotMatch:
          Serial.println(F("Check Sum Not Match"));
          break;
        case FileIndexOut:
          Serial.println(F("File Index Out of Bound"));
          break;
        case FileMismatch:
          Serial.println(F("Cannot Find File"));
          break;
        case Advertise:
          Serial.println(F("In Advertise"));
          break;
        default:
          break;
      }
      break;
    default:
      break;
  }
}
