#include <LilBot.h>
#include <Wire.h>
#include <EEPROM.h>

LilBot Bot;

int i;

void setup() {
  Bot.begin();


}


void loop() {
  for (i = 0; i <= 3; i++) {
    Bot.go(10);
    Bot.wait(1000);
    Bot.rotate(90);
    Bot.wait(1000);
  }

  Bot.balance();
}
