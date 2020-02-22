const int Echo=5; //pin digital para el trigger del sensor
const int Trigger=6; //pin par ael echo del sensor

void setup(){
  Serial.begin(9600);//inicializamos la comunicacion
  pinMode(Trigger,OUTPUT); //pin como salida
  pinMode(Echo,INPUT);//pin como entrada
  digitalWrite(Trigger,LOW);
}

void loop(){
  long t; //tiempo que tarde el echo
  long d; //distancia a la que detecta el objeto
  
  digitalWrite(Trigger,HIGH);
  delayMicroseconds(10); //enviamos un pulso de 10us
  digitalWrite(Trigger,LOW);
  
  t=pulseIn(Echo,HIGH); //obtenemos el ancho del pulso
  d=t/59;
  
  
  Serial.print("Distancia: ");
  Serial.print(d);
  Serial.println("cm");
  
  delay(100); //pausa de 1ooms
}
