

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
  myDFPlayer.volume(30);  //Set volume value (0~30).
//  myDFPlayer.volumeUp(); //Volume Up
//  myDFPlayer.volumeDown(); //Volume Down
  
  //----Set different EQ----
//  myDFPlayer.EQ(DFPLAYER_EQ_NORMAL);
//  myDFPlayer.EQ(DFPLAYER_EQ_POP);
//  myDFPlayer.EQ(DFPLAYER_EQ_ROCK);
//  myDFPlayer.EQ(DFPLAYER_EQ_JAZZ);
//  myDFPlayer.EQ(DFPLAYER_EQ_CLASSIC);
//  myDFPlayer.EQ(DFPLAYER_EQ_BASS);
  
  //----Set device we use SD as default----
//  myDFPlayer.outputDevice(DFPLAYER_DEVICE_U_DISK);
  myDFPlayer.outputDevice(DFPLAYER_DEVICE_SD);
//  myDFPlayer.outputDevice(DFPLAYER_DEVICE_AUX);
//  myDFPlayer.outputDevice(DFPLAYER_DEVICE_SLEEP);
//  myDFPlayer.outputDevice(DFPLAYER_DEVICE_FLASH);
  
  //----Mp3 control----
//  myDFPlayer.sleep();     //sleep
//  myDFPlayer.reset();     //Reset the module
//  myDFPlayer.enableDAC();  //Enable On-chip DAC
//  myDFPlayer.disableDAC();  //Disable On-chip DAC
//  myDFPlayer.outputSetting(true, 15); //output setting, enable the output and set the gain to 15
  
  //----Mp3 play----
 // myDFPlayer.next();  //Play next mp3
  /*
  delay(1000);
  myDFPlayer.previous();  //Play previous mp3
  delay(1000);
  myDFPlayer.play(1);  //Play the first mp3
  delay(1000);
  myDFPlayer.loop(1);  //Loop the first mp3
  delay(1000);
  myDFPlayer.pause();  //pause the mp3
  delay(1000);
  myDFPlayer.start();  //start the mp3 from the pause
  delay(1000);
  myDFPlayer.playFolder(15, 4);  //play specific mp3 in SD:/15/004.mp3; Folder Name(1~99); File Name(1~255)
  delay(1000);
  myDFPlayer.enableLoopAll(); //loop all mp3 files.
  delay(1000);
  myDFPlayer.disableLoopAll(); //stop loop all mp3 files.
  delay(1000);
  myDFPlayer.playMp3Folder(4); //play specific mp3 in SD:/MP3/0004.mp3; File Name(0~65535)
  delay(1000);
  myDFPlayer.advertise(3); //advertise specific mp3 in SD:/ADVERT/0003.mp3; File Name(0~65535)
  delay(1000);
  myDFPlayer.stopAdvertise(); //stop advertise
  delay(1000);
  myDFPlayer.playLargeFolder(2, 999); //play specific mp3 in SD:/02/004.mp3; Folder Name(1~10); File Name(1~1000)
  delay(1000);
  myDFPlayer.loopFolder(5); //loop all mp3 files in folder SD:/05.
  delay(1000);
  myDFPlayer.randomAll(); //Random play all the mp3.
  delay(1000);
  myDFPlayer.enableLoop(); //enable loop.
  delay(1000);
  myDFPlayer.disableLoop(); //disable loop.
  delay(1000);
  */

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

  Serial.print("File Counts in Folder 3=");
  Serial.println(myDFPlayer.readFileCountsInFolder(3)); //read fill counts in folder SD:/03

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
      if (isPlaying == 0) {
        myDFPlayer.start();
        isPlaying = 1;
        Serial.print("Continue");
      }
  }
  
  if (myDFPlayer.available()) {
    printDetail(myDFPlayer.readType(), myDFPlayer.read()); //Print the detail message from DFPlayer to handle different errors and states.
  }

  volumePotValue = analogRead(volumePotPin);
//  Serial.print("Vol=");
//  Serial.println(volumePotValue);
  newVolumeValue = map(volumePotValue, 0, 1023, 0, 30);
  if (newVolumeValue != volumeValue) {
     myDFPlayer.volume(newVolumeValue);
     volumeValue = newVolumeValue;
     Serial.print("New vol=");
     Serial.println(volumeValue);
  };
  Serial.print("Playing=");
  Serial.print(isPlaying);
  Serial.print("Track=");
  Serial.print(track);
  Serial.print("Vol=");
  Serial.println(volumeValue);
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
