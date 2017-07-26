//output pin for emitting transducer
#define trigPin 10

//input pin for receiving transducer
#define echoPin 13

//speed of sound in given medium in cm/microsecond
#define speed_of_sound 0.0344

/* desired sample rate in Hz (cannot exceed 83333 Hz)
 * complications require some hard-coding until further notice:
 * 
 *      Frequency (Hz) | waitTime (ms) | baud
 *      5              | 199.88        |
 *      10             | 99.88         |
 *      15             | 66.55         |
 *      20             | 49.88         | 
 *      30             | 33.21         | 9600
 *      45             | 22.10         |
 *      60             | 16.55         |
 * 
 */

//for tracking time spent per cycle (min is 12 microseconds if waitTime =0)
double waitTime;
#define BAUD 19200

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
 *    
 *    Note: HC-SR04 module is only accurate for x in (2,400) cm range.
 */

//for keeping track of elapsed time
unsigned long startTime, currentTime, elapsedTime;

//for calculations
float duration, distance;

//for reading cfg values
String input = "";

void setup() {
  Serial.begin(BAUD);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  Serial.println("\nDesired wait time (3 digits): ");

  while(Serial.available()  < 5) {}
  while(Serial.available() ) {
    char inChar = (char) Serial.read();
    input += inChar;

    if (inChar == '\n') {
      break;
    }
  }

  waitTime = input.toDouble();
  
  Serial.print("Wait time set to ");
  Serial.println(input);

  startTime = millis();

}

void loop() {  
  
  //ensure trigPin is OFF before sending ON signal
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  //send ON signal
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  //stop ON signal with cheeky OFF signal
  digitalWrite(trigPin, LOW);

  currentTime = millis();
  elapsedTime = currentTime - startTime;

  //output of HIGH signal on echoPin is equal to the measured time
  duration = pulseIn(echoPin, HIGH);

  //distance calculation using 'derivation' (heh) above
  distance = ( duration / 2) * speed_of_sound;

  //print to serial port in format 'time, distance'
  Serial.print(elapsedTime);
  Serial.print(",");
  Serial.println(distance);
  
  delay( waitTime );
}

