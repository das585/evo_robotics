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

# store the GUI/noGUI options
directOrGUI = sys.argv[1]

# store the brain/fitness file ID to use
solutionID = sys.argv[2]

# create simulation object
simulation = SIMULATION(directOrGUI, solutionID)

# run the simulation
simulation.Run()

simulation.Get_Fitness()

simulation.Write_Fitness()

