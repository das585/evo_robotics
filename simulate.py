'''
    David Smith
    simulate.py: This program will be used to simulate the world that the robot will exist in as well as
    the body of the robot eventually. Pybullet will be used as the physics engine for this world along 
    with other provided files to help build the world.
'''
# import statements
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import random

# motor movement variables
amplitude = np.pi/4
frequency = 20
FLphaseOffset = 0
BLphaseOffset = np.pi/4

# physics engine init
physicsClient = p.connect(p.GUI)

# add pybullet data path to be usable
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# set the gravity in the world
p.setGravity(0, 0,-9.81)

# create the floor
planeID = p.loadURDF("plane.urdf")

# load the robot
robotID = p.loadURDF("body.urdf")

# load in the world
p.loadSDF("world.sdf")

# prepare to use sensor values
pyrosim.Prepare_To_Simulate(robotID)

# numpy vector for storing sensor values
backLegMotorValues = np.zeros(1000)
frontLegMotorValues = np.zeros(1000)

# create a vector of desired motor values
targetAngles = np.linspace(-1, 1, 1000)

# step through the world
for x in range(1000):
	
	# step simulation
    p.stepSimulation()
    
    # simulate motors
    pyrosim.Set_Motor_For_Joint(
		bodyIndex = robotID,
		jointName = "Torso_BackLeg",
		controlMode = p.POSITION_CONTROL,
		targetPosition = amplitude * np.sin(frequency * targetAngles[x] + BLphaseOffset),
		maxForce = 500)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = amplitude * np.sin(frequency * targetAngles[x] + FLphaseOffset),
        maxForce = 500)
    
    # get touch value of legs and add to vector
    backLegMotorValues[x] = amplitude * np.sin(frequency * targetAngles[x] + BLphaseOffset)
    frontLegMotorValues[x] = amplitude * np.sin(frequency * targetAngles[x] + FLphaseOffset)
     
    # print the step number and wait 
    print(x)
    time.sleep(.004167)
    
#  save the vectors
np.save("data/BackLegMotors.npy", backLegMotorValues, allow_pickle=True, fix_imports=True)
np.save("data/FrontLegMotors.npy", frontLegMotorValues, allow_pickle=True, fix_imports=True)

# physics engine disconnect
p.disconnect
