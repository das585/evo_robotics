'''
    David Smith
    simulate.py: This program will be used to simulate the world that the robot will exist in as well as
    the body of the robot eventually. Pybullet will be used as the physics engine for this world along 
    with other provided files to help build the world.
'''
# import statements
import pybullet as p
import time

# physics engine init
physicsClient = p.connect(p.GUI)

# load in the box
p.loadSDF("box.sdf")

# step through the world
for x in range(1000):
    p.stepSimulation()
    print(x)
    time.sleep(.005)

# physics engine disconnect
p.disconnect
