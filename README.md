# simpleumd
Basic ultrasonic motion detector powered by Arduino and Python

## How It Works
The Arduino is running code that collects position data with a sensor that shoots out ultrasonic sound several times per second. This data is fed into the python program through serial ports (with help from `PySerial`).

The python program then formats the data and uses it to create a Position versus Time graph.
