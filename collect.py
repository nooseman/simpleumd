import serial
import csv
from time import sleep
import numpy

#configuration
cfg = {
	'BAUD': 19200,
	'FILENAME': 'data.csv',
	'PORT': 'COM3',
	'SAMPLE_SIZE': 100,
	'WAIT_TIME': 33.21
}

def printcfg(s=''):
	for key in cfg.keys():
		print(key, ": ", cfg[key])
	print(s)



def initialize():

	print("Would you like to configure yourself or use default values?")
	print("Enter 'configure' to configure or type anything else to continue.\n")
	printcfg()
	selection = input()

	if selection == 'configure':
		while True:
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
					value = int(value)

				cfg[selection] = value

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
						print(line)
						ser.write(bytes(str(cfg["WAIT_TIME"]) + "\n",'utf-8'))
					elif "Wait" in line:
						print(line)
					elif line and not line.isspace():
						print(line.rstrip())
						arr = line.rstrip().split(',')
						arr[0] = float(arr[0]) / 1000
						writer.writerow(arr)
		except PermissionError:
			print("Cannot open " + cfg['FILENAME'] + ". Do you have it open?")


	except serial.SerialException:
		print("Something's broken.")

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
					print(line)
					ser.write(bytes(str(cfg["WAIT_TIME"]) + "\n",'utf-8'))
				elif "Wait" in line:
					print(line)
				elif line and not line.isspace():
					print(line.rstrip())
					mat[i, 0] = int(line.rstrip().split(',')[0]) / 1000
					mat[i, 1] = line.rstrip().split(',')[1]
			return mat[~(mat==0).all(1)]
		except PermissionError:
			print("Cannot open " + cfg['FILENAME'] + ". Do you have it open?")
	except serial.SerialException:
		print("Something's broken.")


if __name__ == '__main__':
	collectToCSV()