'''
    David Smith
    simulate.py: This program will be used to simulate the world that the robot will exist in as well as
    the body of the robot eventually. Pybullet will be used as the physics engine for this world along 
    with other provided files to help build the world.
'''
# import statements
import constants as c
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
from simulation import SIMULATION
import sys
import time

directOrGUI = sys.argv[1]


# create simulation object
simulation = SIMULATION(directOrGUI)

# run the simulation
simulation.Run()

simulation.Get_Fitness()

