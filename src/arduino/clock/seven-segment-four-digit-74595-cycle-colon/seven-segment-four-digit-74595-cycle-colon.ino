int datapin = 12; // DIO
int clockpin = 11; // SCLK
int latchpin = 10; // LCLK
unsigned char ch; // LED segment to turn on.
unsigned char ch_pos = 1; // 8 bits that we will display - one for each pin
unsigned char digit = 1; // The digit to use, 1,2,3 or 4
unsigned char digit_bit = 1; // the bit position of the digit 0x01, 0x02, 0x04, 0x08
int index;
int delayTime = 100; // Time (milliseconds) to pause between LEDs

void setup() {
  pinMode(datapin, OUTPUT);
  pinMode(clockpin, OUTPUT);  
  pinMode(latchpin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // the colon is part of the third digit
  for(unsigned char digit=1; digit <=4; digit ++) {
       for(ch = 1; ch < 128; ch = ch * 2)
        {
          Serial.print("digit=");
          Serial.print(digit);
          Serial.print(" digit-bit=");
          Serial.print(digit_bit);
          Serial.print(" ch=");
          Serial.print(ch);
          
          Serial.print(" positive=");
          Serial.print(ch_pos, BIN);
          Serial.print(" flip=");
          Serial.println(ch, BIN);
          // toggle each of the bits using the bitwise not operator
          ch_pos = ~ch;
          send2(ch_pos, digit_bit);
          delay(delayTime);
          // display the colon between the 2nd and third digits
          if (digit == 3 && ch == 64) {
            ch_pos = 0b01111111;
            send2(ch_pos, digit_bit);
            delay(delayTime * 4);
          }
          // right shift 1 bit
          ch_pos << 1;
        }
       if (digit_bit >= 0x08) digit_bit = 1;
       else digit_bit <<= 1;
  }
}


void send1(unsigned char X)
{

  for (int i = 8; i >= 1; i--)
  {
    if (X & 0x80)
    {
      digitalWrite(datapin, HIGH);
    }
    else
    {
      digitalWrite(datapin, LOW);
    }
    X <<= 1;
    digitalWrite(latchpin, LOW);
    digitalWrite(latchpin, HIGH);  
  }
}

void send2(unsigned char X, unsigned char digit)
{
  send1(X);
  send1(digit);
  digitalWrite(clockpin, LOW);
  digitalWrite(clockpin, HIGH);
}





