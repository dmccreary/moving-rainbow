
int right_forward = 4;
int right_backward = 5;
int left_forward = 6;
int left_backward = 7;
int delay_time = 1000;  // 1 second

void setup() {
  pinMode(right_forward, OUTPUT);
  pinMode(right_backward, OUTPUT); 
  pinMode(left_forward, OUTPUT); 
  pinMode(left_backward, OUTPUT);
  // turn all off
  digitalWrite(right_forward, LOW);
  digitalWrite(right_backward, LOW);
  digitalWrite(left_forward, LOW);
  digitalWrite(left_backward, LOW);

}

// repeat this function
void loop() {
  // move forward
  digitalWrite(right_forward, HIGH);
  digitalWrite(left_forward, HIGH);
  delay(delay_time);
  
  // stop
  digitalWrite(right_forward, LOW);
  digitalWrite(left_forward, LOW);
  delay(delay_time);
  
  // reverse
  digitalWrite(right_backward, HIGH);
  digitalWrite(left_backward, HIGH);
  delay(delay_time);
  
  // stop
  digitalWrite(right_backward, LOW);
  digitalWrite(left_backward, LOW);
  delay(delay_time);
  
  // turn right
  digitalWrite(left_forward, HIGH);
  digitalWrite(right_backward, HIGH);
  delay(delay_time);

  // stop
  digitalWrite(left_forward, LOW);
  digitalWrite(right_backward, LOW);
  delay(delay_time);
  
  // repeat (go to the top of the loop)
}
