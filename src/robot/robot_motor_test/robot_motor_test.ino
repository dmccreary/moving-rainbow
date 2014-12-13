
int right_forward = 4;
int right_backward = 5;
int left_forward = 6;
int left_backward = 7;
int delay_time = 1000;

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
  // for debugging
}
void loop() {
  digitalWrite(right_forward, HIGH);
  delay(delay_time);
  digitalWrite(right_forward, LOW);
  Serial.println("1");
  
  digitalWrite(right_backward, HIGH);
  delay(delay_time);
  digitalWrite(right_backward, LOW);
  Serial.println("2");
  
  digitalWrite(left_forward, HIGH);
  delay(delay_time);
  digitalWrite(left_forward, LOW);
  Serial.println("3");
  
  digitalWrite(left_backward, HIGH);
  delay(delay_time);
  digitalWrite(left_backward, LOW);
  Serial.println("4");
  
  
}
