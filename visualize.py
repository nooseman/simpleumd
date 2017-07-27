import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

data = np.genfromtxt('data.csv', delimiter=',',  names=['x','y'])

figure = plt.figure(figsize=(10,10))

ax1 = figure.add_subplot(111)

ax1.set_title("Displacement versus Time")
ax1.set_xlabel("Time [s]")
ax1.set_ylabel("Displacement [cm]")

ax1.plot(data['x'], data['y'], color='r', label='Displacement')

leg = ax1.legend()

plt.show()