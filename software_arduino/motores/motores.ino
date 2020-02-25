
int ENA=10;
int IN1=9;
int IN2=8;

int ENB=7;
int IN3=6;
int IN4=25;


void setup() {
  // put your setup code here, to run once:
  pinMode (ENA,OUTPUT);
  pinMode (IN1,OUTPUT);
  pinMode (IN2,OUTPUT);

  pinMode (ENB,OUTPUT);
  pinMode (IN3,OUTPUT);
  pinMode (IN4,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite (IN1, HIGH);
  digitalWrite (IN2,LOW);
  analogWrite (ENA,0);

  digitalWrite (IN3, HIGH);
  digitalWrite (IN4,LOW);
  analogWrite  (ENB,0);
  
}
