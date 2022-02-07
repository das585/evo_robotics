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

# physics engine init
physicsClient = p.connect(p.GUI)

# add pybullet data path to be usable
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# set the gravity in the world
p.setGravity(0, 0,-9.8)

# create the floor
planeID = p.loadURDF("plane.urdf")

# load the robot
robotID = p.loadURDF("body.urdf")

# load in the box
p.loadSDF("world.sdf")

# prepare to use sensor values
pyrosim.Prepare_To_Simulate(robotID)

# numpy vector for storing sensor values
backLegSensorValues = np.zeros(1000)

# step through the world
for x in range(1000):
	
	# step simulation
    p.stepSimulation()
    
    # get touch value of back leg and add to vector
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
     
    # print the step number and wait 
    print(x)
    time.sleep(.01)
    
#  save the vector
np.save("data/sensors.npy", backLegSensorValues, allow_pickle=True, fix_imports=True)

# physics engine disconnect
p.disconnect
