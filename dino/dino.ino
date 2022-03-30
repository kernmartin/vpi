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
long finalTemp = 0;
int pos = 0;
// Comparings
int a = 0;
int b = 0;
int c = 0;



void setup() {
  Serial.begin(9600);
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(enaPin, OUTPUT);
  digitalWrite(enaPin, HIGH);
  pos = 0;
}
void loop() {

  if(final == steps && running == true){
     //Serial.println("DONE");
     //printPos();
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
          printPos();
        }else{
          pos--;
          if(pos <= 0){ pos = 360; }
          printPos();
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
    //Serial.print("LENGTH: ");
    //Serial.println(data.length());
    steps = 0;
    
    if(data.length() == 2){
      // COMMAND (R = RESET | S = STOP)
      data = data.substring(0, 1);
      if(data == "S"){
        //Serial.println("RECEIVED S: ");
        digitalWrite(enaPin, HIGH);
        steps = 0;
        final = 0;
      }
      
      if(data == "R"){
        // COMMAND RESET
        //Serial.println("RECEIVED R: ");
        pos = 0;
        printPos();
      }

      if(data == "P"){
        // COMMAND RESET
        printPos();
      }
      
    }else if(data.length() == 5){
      // GO TO LOCATION MSG: "L090"
        speed = 20;
        p(data.substring(1, 4).toInt());
        // Which one is shorter CCW or CW
        finalTemp = data.substring(1, 4).toInt();
        
        
        if(finalTemp < pos && (pos - finalTemp) <= 180){
          //CCW
          p(100);
          dir = 0;
          final = pos - finalTemp;
        }

        if(finalTemp < pos && (pos - finalTemp) > 180){
          //CW
          p(107);
          dir = 1;
          final = abs(finalTemp + (360 - pos));
          pp("final", final);
        }

        if(finalTemp > pos && (finalTemp - pos) <= 180){
          //CW
          p(114);
          dir = 1;
          final = abs(finalTemp - pos);
        }

        if(finalTemp > pos && (finalTemp - pos) > 180){
          //CCW
          p(123);
          dir = 0;
          final = abs(pos + (360 - finalTemp));
        }


    }else if(data.length() == 10){
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


void printPos(){
  //Serial.print("Position: ");
  Serial.println(pos);
}

void p(int i){
  //Serial.print("print: ");
  //Serial.println(i);
}

void pp(String s, int i){
  //Serial.print(s);
  //Serial.println(i);
}