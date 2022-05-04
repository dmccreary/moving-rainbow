//From bildr article: http://bildr.org/2012/08/rotary-encoder-arduino/

// these pins cannot be changed.  Pins 2 and 3 are the interrupt pins
int encoderPin1 = 2;
int encoderPin2 = 3;

volatile int lastEncoded = 0;
volatile long encoderValue = 0;
volatile long newValue4 = 0; // 1/4 the value of the encoder

long lastencoderValue = 0;

int lastMSB = 0;
int lastLSB = 0;

void setup() {
  Serial.begin (9600);

  pinMode(encoderPin1, INPUT); 
  pinMode(encoderPin2, INPUT);

  digitalWrite(encoderPin1, HIGH); //turn pullup resistor on
  digitalWrite(encoderPin2, HIGH); //turn pullup resistor on

  //call updateEncoder() when any high/low changed seen
  //on interrupt 0 (pin 2), or interrupt 1 (pin 3) 
  attachInterrupt(0, updateEncoder, CHANGE); 
  attachInterrupt(1, updateEncoder, CHANGE);

}

void loop(){ 
  // this gets a new click every 4th change in value - cuts down noise
  if (newValue4 != encoderValue / 4) {
    /*
     Serial.print("e=");
     Serial.print(encoderValue);
     Serial.print(" n4=");
     Serial.print(newValue4);
     Serial.print(" e/4=");
     Serial.println(encoderValue / 4);
     */
     for (int i=0; i<=abs(newValue4); i++) {
       Serial.print("=");
     }
      Serial.println("");
     newValue4 = encoderValue / 4;
  }
}


void updateEncoder(){
  int MSB = digitalRead(encoderPin1); //MSB = most significant bit
  int LSB = digitalRead(encoderPin2); //LSB = least significant bit

  int encoded = (MSB << 1) |LSB; //converting the 2 pin value to single number
  int sum  = (lastEncoded << 2) | encoded; //adding it to the previous encoded value

  if(sum == 0b1101 || sum == 0b0100 || sum == 0b0010 || sum == 0b1011) encoderValue ++;
  if(sum == 0b1110 || sum == 0b0111 || sum == 0b0001 || sum == 0b1000) encoderValue --;

  lastEncoded = encoded; //store this value for next time
}
