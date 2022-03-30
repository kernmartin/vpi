#define pulPin 2
#define dirPin 3
#define enaPin 4

//Defaults
int speed = 0;
long steps = 0;
long final = 0;
bool dir = 1;



void setup() {
  Serial.begin(9600);
  pinMode(pulPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enaPin, OUTPUT);
  digitalWrite(enaPin, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:

}


void motorpulse(){
  digitalWrite(pulPin, HIGH);
  delayMicroseconds(minPulse/spd);
  digitalWrite(pulPin, LOW);
  delayMicroseconds(minPulse/spd);
}

void serialEvent() {
  while (Serial.available()) {
    // GET MESSAGE
  }
}