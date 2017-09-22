# simpleumd
Basic ultrasonic motion detector powered by Arduino and Python

## How It Works
The Arduino is running code that collects position data with a sensor that shoots out ultrasonic sound several times per second. This data is fed into the python program through serial ports (with help from `PySerial`).

The python program then formats the data and uses it to create a Position versus Time graph.

## How To Use simpleumd
First, download the code for yourself:

```
git clone https://github.com/nooseman/simpleumd.git
```

Then, using the Arduino IDE, upload `simpleumd.ino` to your board. The Arduino IDE can be downloaded from `https://www.arduino.cc/en/Main/Software`.

Once you've uploaded the sketch to your board, all that is left to do is actually get the data. Running 
```
python main.py
```
is the easiest way to do so. Configure the program however you'd like and begin. 

Generally, a sample size of 200 takes about 10 seconds to collect. You can, however, configure the amount of samples to take and the length of time between each sample. I was able to get around 30 samples/sec maximum after playing around with baud rates and sampling delay which is more than enough for most simple applications.
