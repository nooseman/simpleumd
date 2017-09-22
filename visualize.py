import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import collect

def graphCSV(filename, size=(7,7)):
	data = np.genfromtxt(filename, delimiter=',',  names=['x','y'])

	figure = plt.figure(figsize=size)
	ax1 = figure.add_subplot(111)

	ax1.set_title("Displacement versus Time")
	ax1.set_xlabel("Time [s]")
	ax1.set_ylabel("Displacement [cm]")

	ax1.plot(data['x'], data['y'], color='r', label='Displacement')
	leg = ax1.legend()

	plt.show()
	return ax1

def graphMatrix(matrix, size=(7,7)):
	figure = plt.figure(figsize=size)
	ax1 = figure.add_subplot(111)

	ax1.set_title("Displacement versus Time")
	ax1.set_xlabel("Time [s]")
	ax1.set_ylabel("Displacement [cm]")

	#remove erroneous first and last datapoints
	matrix = np.delete(matrix, (0), axis=0)
	matrix = np.delete(matrix, (matrix.shape[1] - 1), axis=0)

	ax1.plot(matrix[:,0], matrix[:,1], color='r', label='Displacement')
	leg = ax1.legend()

	plt.show()
	return ax1

if __name__ == '__main__':
	graphMatrix(collect.collectToMatrix())