'''
David Smith
This file is meant to hold all of the constant values used in the simulation
of the program. This allows for the variables to be tidied up and changed
all from one location
'''
# import needed libs
import numpy as np

# motor movement variables
amplitude = np.pi/4
frequency = 200
FLphaseOffset = 0
BLphaseOffset = np.pi/4

# motor force
motorForce = 500

# number of steps in the simulation
simSteps = 10000

# sleep length in the simulation
sleepTime = .004167

# gravity constant
gravConst = -9.81
