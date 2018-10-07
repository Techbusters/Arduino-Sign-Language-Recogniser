/*
* Motion Sensor Camera built
*
* by Team TechBusters
*
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo

// defines pins numbers
const int ledLeft = 8;
const int ledRight = 12;
const int trigPinLeft = 9;
const int echoPinLeft = 10;
const int trigPinRight = 5;
const int echoPinRight = 6;

const int threshold = 150;
const int threshold2 = 100;
const int changeDelay = 150;


// defines variables
int stateLeft = LOW;
int stateRight = LOW;
long durationLeft;
int distanceLeft;
long durationRight;
int distanceRight;
int pos = 0; 


void setup() {
  pinMode(trigPinLeft, OUTPUT); // Sets the trigPinLeft as an Output
  pinMode(echoPinLeft, INPUT); // Sets the echoPinLeft as an Input
  pinMode(ledLeft, OUTPUT);      // initalize LED as an output

  pinMode(trigPinRight, OUTPUT); // Sets the trigPinLeft as an Output
  pinMode(echoPinRight, INPUT); // Sets the echoPinLeft as an Input
  pinMode(ledRight, OUTPUT);      // initalize LED as an output

  myservo.attach(13);
  myservo.write(90);
  pos = 90;
  
  Serial.begin(9600); // Starts the serial communication
}

void updateLeft()
{
  // Clears the trigPinLeft
  digitalWrite(trigPinLeft, LOW);
  //delayMicroseconds(2);
  delay(1);
  // Sets the trigPinLeft on HIGH state for 10 micro seconds
  digitalWrite(trigPinLeft, HIGH);
  //delayMicroseconds(10);
  delay(200);
  digitalWrite(trigPinLeft, LOW);
  // Reads the echoPinLeft, returns the sound wave travel time in microseconds
  durationLeft = pulseIn(echoPinLeft, HIGH);
  // Calculating the distance
  distanceLeft= durationLeft*0.034/2;
}

void updateRight()
{
  // Clears the trigPinLeft
  digitalWrite(trigPinRight, LOW);
  //delayMicroseconds(2);
  delay(1);
  // Sets the trigPinLeft on HIGH state for 10 micro seconds
  digitalWrite(trigPinRight, HIGH);
  //delayMicroseconds(10);
  delay(200);
  digitalWrite(trigPinRight, LOW);
  // Reads the echoPinLeft, returns the sound wave travel time in microseconds
  durationRight = pulseIn(echoPinRight, HIGH);
  // Calculating the distance
  distanceRight= durationRight*0.034/2;
}

void loop() {
  updateLeft();
  updateRight();
  
  if(distanceLeft<threshold && stateLeft == LOW)
  {
    delay(changeDelay);
    updateLeft();
    if(distanceLeft<threshold)
    {
      digitalWrite(ledLeft, HIGH);   // turn LED ON
      stateLeft = HIGH;
    }
  }
  else if(distanceLeft>threshold && stateLeft == HIGH)
  {
    delay(changeDelay);
    updateLeft();
    if(distanceLeft>threshold)
    {
    digitalWrite(ledLeft, LOW);   // turn LED OFF
    stateLeft = LOW;
    }
  }
  else if(distanceRight<threshold2 && stateRight == LOW)
  {
    delay(changeDelay);
    updateRight();
    if(distanceRight<threshold2)
    {
      digitalWrite(ledRight, HIGH);   // turn LED ON
      stateRight = HIGH;
    }
  }
  else if(distanceRight>threshold2 && stateRight == HIGH)
  {
    delay(changeDelay);
    updateRight();
    if(distanceRight>threshold2)
    {
    digitalWrite(ledRight, LOW);   // turn LED OFF
    stateRight = LOW;
    }
  }
  
  // Prints the distance on the Serial Monitor
  Serial.print("Distance Left: ");
  Serial.println(distanceLeft);
  Serial.print("Distance Right: ");
  Serial.println(distanceRight);

  if((stateLeft == LOW && stateRight == HIGH))
  {
    if(pos<180) {
      pos+=2;
      myservo.write(pos);
      delay(15);
    }
  }
  else if((stateLeft == HIGH && stateRight == LOW))
  {
    if(pos>0) {
      pos-=2;
      myservo.write(pos);
      delay(15);
    }
  }
}
