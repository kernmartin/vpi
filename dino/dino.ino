#define dirPin 3
#define stepPin 2
#define enaPin 4
#define stepsPerRevolution 8000
#define stepsPerDegree 800

bool running = false;
bool EN = false;
long  steps = 0;
int dir = 0;
int speed = 50;
long final = 0;
int pos = 0;




void setup() {
  Serial.begin(9600);
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enaPin, OUTPUT);
  digitalWrite(enaPin, HIGH);
}
void loop() {

  if(final == steps && running == true){
     Serial.println("DONE");
     delay(250);
     digitalWrite(enaPin, HIGH);
  }

  if(final == steps){
    running = false;
    final = 0;
    steps = 0;

  }else{
    running = true;
    motorPulse();
    steps++;
      if(steps % 800 == 0) {
        if(dir){
          pos++;
          if(pos >= 360){ pos = 0; }
        }else{
          pos--;
          if(pos <= 0){ pos = 360; }
        }
      }
  }
}

void motorPulse(){
  digitalWrite(stepPin, HIGH);
  delayMicroseconds(speed);
  digitalWrite(stepPin, LOW);
  delayMicroseconds(speed);
}

void serialEvent() {
   if (Serial.available() > 0 ) {
    String data = Serial.readString();
    
    steps = 0;
    
    if(data.length() == 1){
      // COMMAND (R = RESET | S = STOP)
      if(data == "S"){
        digitalWrite(enaPin, HIGH);
        steps = 0;
        final = 0;
      }
      
      if(data == "R"){
        // COMMAND RESET
        pos = 0;
      }
      
    }else if(data.length() == 4){
      // GO TO LOCATION MSG: "L090"
        speed = 20;
        final = data.substring(1, 3).toInt();
        
        // Which one is shorter CCW or CW
        if((final - pos) <= (360 - final + pos)){
          dir == 1;
          final = final - pos;
        }else{
          dir == 0;
          final = 360 - final + pos;
        }
      
    }else if(data.length() == 9){
      // RUN DEGREES: D + SPEED ### + DIR # + DEGREE #### = "D10010180"
      speed = data.substring(1, 4).toInt();
      dir = data.substring(4, 5).toInt();
      final = data.substring(5, 9).toInt();
    }

    if(dir == 1){
      digitalWrite(dirPin, HIGH);
      } else {
      digitalWrite(dirPin, LOW);
    }

    final = final * stepsPerDegree;
    running = true;

    digitalWrite(enaPin, LOW);
    delay(250);
    
  }
}
