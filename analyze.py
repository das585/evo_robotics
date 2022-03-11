'''
David Smith
analyze.py: This program takes the created .npy files from running a 
simulation and creates a graph of the sensor values
'''

# import statements
import numpy as np
import matplotlib.pyplot as plt

# load in the file for use in a plot
backLegMotorValues = np.load("data/BackLegMotors.npy", mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')
frontLegMotorValues = np.load("data/FrontLegMotors.npy", mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')

# plot the values
plt.plot(backLegMotorValues, label = "back leg", linewidth=.4)
plt.plot(frontLegMotorValues, label = "front leg", linewidth=1)

# show a legend
plt.legend()

# show the plot
plt.show()
