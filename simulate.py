'''
    David Smith
    simulate.py: This program will be used to simulate the world that the robot will exist in as well as
    the body of the robot eventually. Pybullet will be used as the physics engine for this world along 
    with other provided files to help build the world.
'''
# import statements
import pybullet as p
import pybullet_data
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

# step through the world
for x in range(1000):
    p.stepSimulation()
    print(x)
    time.sleep(.01)

# physics engine disconnect
p.disconnect
