//output pin for emitting transducer
#define trigPin 10

//input pin for receiving transducer
#define echoPin 13

//speed of sound in given medium in cm/microsecond
#define speed_of_sound 0.0344

//desired sample rate in Hz (cannot exceed 83333 Hz)
#define frequency 30

/*  THEORY:
 *    Transducer will measure amount of time it takes for an emitted sound wave 
 *    to return and be detected. Therefore, the amount of time taken for the  
 *    sound wave to reach the object is half the measured time:
 *    
 *    T_{obj} = T_{trip} / 2
 * 
 *    We don't really care about time, though. We're interested in how far away
 *    the object is. To do this, we use the definition of velocity to derive an
 *    expression:
 *        
 *    X = V * T    
 */

void setup() {
  Serial.begin(57600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  float duration, distance;

  //ensure trigPin is OFF before sending ON signal
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  //send ON signal
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  //stop ON signal with cheeky OFF signal
  digitalWrite(trigPin, LOW);

  //output of HIGH signal on echoPin is equal to the measured time
  duration = pulseIn(echoPin, HIGH);

  //distance calculation using 'derivation' (heh) above
  distance = ( duration / 2) * speed_of_sound;

  Serial.print("Distance = ");

  //HC-SR04 module is only accurate for x in (2,400) cm range.
  if ( distance >= 400 || distance <= 2){
    Serial.println("Out of range");
  } else {
    Serial.print(distance);
    Serial.println(" cm");
  }
  
  delay( 33 );
}

