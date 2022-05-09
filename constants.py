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
simSteps = 2000

# sleep length in the simulation
sleepTime = .00833

# gravity constant
gravConst = -9.81

# number of generations to evolve
numberOfGenerations = 25

# number of robots to evolve in parallel
populationSize = 25

# neural net constants
numSensorNeurons = 9
numMotorNeurons = 8

# bias for the motor movement
motorJointRange = .8
