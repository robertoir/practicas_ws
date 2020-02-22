const int Echo=5; 
const int Trigger=6; 

void setup(){
  Serial.begin(9600);
  pinMode(Trigger,OUTPUT); 
  pinMode(Echo,INPUT);
  digitalWrite(Trigger,LOW);
}

void loop(){
  long t; 
  long d; 
  
  digitalWrite(Trigger,HIGH);
  delayMicroseconds(10); 
  digitalWrite(Trigger,LOW);
  
  t=pulseIn(Echo,HIGH); 
  d=t/59;
  
  
  Serial.print("Distancia: ");
  Serial.print(d);
  Serial.println("cm");
  
  delay(100); 
}
