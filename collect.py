import serial
import csv
from time import sleep
import numpy

#configuration
cfg = {
    'BAUD': 19200,
    'FILENAME': 'data.csv',
    'PORT': 'COM3',
    'SAMPLE_SIZE': 200,
    'WAIT_TIME': 33.21,
    'LOUD': True,
}

def printcfg(s=''):
    for key in cfg.keys():
        print('{:15}'.format(key + ':'), cfg[key])
    print(s)

#customize config
def initialize():
    print("Would you like to configure yourself or use default values?")
    print("Enter 'configure' to configure or type anything else to continue.\n")
    printcfg()
    selection = input()

    if selection == 'configure' or selection.upper() in list(cfg.keys()):
        while True:
            if selection.upper() not in list(cfg.keys()):
                print("\nSelect an item to configure or type QUIT to end configuration\n")
                printcfg('\n')
                selection = input()

            selection = selection.upper()

            if 'QUIT' in selection :
                break
            elif selection not in list(cfg.keys()):
                print("I don't know what that means. Try again")
            else:
                value = input("What do you want to change " + selection + " to?\n")


                if isnumeric(value):
                    if selection in ['BAUD', 'SAMPLE_SIZE']:
                        cfg[selection] = int(value)
                    else:
                        cfg[selection] = float(value) 
                elif selection == 'LOUD':
                    cfg[selection] = value in ['True', 'true', 't', 'T']

            selection = ''

def isnumeric(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def collectToCSV():
    initialize()

    try:
        ser = serial.Serial(cfg['PORT'], cfg['BAUD'])
        print("Connected to " + cfg['PORT'])

        sleep(1)

        ser.reset_output_buffer()
        ser.reset_input_buffer()

        try:
            with open(cfg['FILENAME'], 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, dialect='excel', delimiter=',')

                for i in range(cfg['SAMPLE_SIZE']):
                    line = ser.readline().decode('utf-8')
                    
                    if "Desired" in line:
                        ser.write(bytes(str(cfg["WAIT_TIME"]) + "\n",'utf-8'))
                    elif line and not line.isspace() and 'Wait' not in line:
                        arr = line.rstrip().split(',')
                        arr[0] = float(arr[0]) / 1000
                        writer.writerow(arr)

                    if cfg['LOUD']: 
                        if "Desired" in line or "Wait" in line:
                            print(line)
                        elif line and not line.isspace():
                            print(line.rstrip()) 

        except PermissionError:
            print("Cannot open " + cfg['FILENAME'] + ". Do you have it open?")


    except serial.SerialException:
        print("Something's broken. Is the arduino connected?")

def collectToMatrix():

    initialize()

    try:
        ser = serial.Serial(cfg['PORT'], cfg['BAUD'])
        print("Connected to " + cfg['PORT'])

        sleep(1)

        ser.reset_output_buffer()
        ser.reset_input_buffer()

        mat = numpy.zeros((cfg['SAMPLE_SIZE'],2))

        try:

            for i in range(cfg['SAMPLE_SIZE']):
                line = ser.readline().decode('utf-8')

                if "Desired" in line:
                    ser.write(bytes(str(cfg["WAIT_TIME"]) + "\n",'utf-8'))
                elif line and not line.isspace() and 'Wait' not in line:
                    mat[i, 0] = int(line.rstrip().split(',')[0]) / 1000
                    mat[i, 1] = line.rstrip().split(',')[1]

                if cfg['LOUD']: 
                    if "Desired" in line or "Wait" in line:
                        print(line)
                    elif line and not line.isspace():
                        print(line.rstrip())                    
            
            return mat[~(mat==0).all(1)]
        except PermissionError:
            print("Cannot open " + cfg['FILENAME'] + ". Do you have it open?")
    except serial.SerialException:
        print("Something's broken.")


if __name__ == '__main__':
    collectToCSV()