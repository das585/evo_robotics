'''
    David Smith
    generate.py: This program will be used to generate the body of any robots
    created for this class using the provided pyrosim files
'''

# import statements
import pyrosim.pyrosim as pyrosim

# start the simulation
pyrosim.Start_SDF("boxes.sdf")

# set the dimention variables
length = 1
width = 1
height = 1

# generate box
pyrosim.Send_Cube(name = "Box", pos = [0, 0, .5], size = [width, length, height])

# box 2
pyrosim.Send_Cube(name = "Box2", pos = [0, 0, .5], size = [width, length, height])

# terminate program
pyrosim.End()

