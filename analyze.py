'''
David Smith
analyze.py: This program takes the created .npy files from running a 
simulation and creates a graph of the sensor values
'''

# import statements
import numpy as np
import matplotlib.pyplot as plt

# load in the file for use in a plot
backLegSensorValues = np.load("data/BackLegSensors.npy", mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')
frontLegSensorValues = np.load("data/FrontLegSensors.npy", mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')

# plot the values
plt.plot(backLegSensorValues, label = "back leg", linewidth=.4)
plt.plot(frontLegSensorValues, label = "front leg", linewidth=1)

# show a legend
plt.legend()

# show the plot
plt.show()
