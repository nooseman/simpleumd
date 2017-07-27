import serial
import csv
from time import sleep

#configuration
cfg = {
	'BAUD': 19200,
	'FILENAME': 'data.csv',
	'PORT': 'COM3',
	'SAMPLE_SIZE': 300,
	'WAIT_TIME': 33.21
}


def initialize(selection):
	if selection == 'configure':
		while True:
			print("Select an item to configure or type QUIT to end configuration")
			print(str(cfg) + '\n')
			selection = input()

			if selection == 'QUIT':
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

def main():
	print("Would you like to configure yourself or use default values?")
	print("Enter 'configure' to configure or type anything else to continue.")
	print(str(cfg) + '\n')
	selection = input()

	initialize(selection)

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
						arr[0] = int(arr[0]) / 1000
						writer.writerow(arr)
		except PermissionError:
			print("Cannot open " + cfg['FILENAME'] + ". Do you have it open?")


	except serial.SerialException:
		print("Something's broken.")

if __name__ == '__main__':
	main()