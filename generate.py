'''
    David Smith
    generate.py: This program will be used to generate the body of any robots
    created for this class using the provided pyrosim files
'''

# import statements
import pyrosim.pyrosim as pyrosim

# start the simulation
pyrosim.Start_SDF("box.sdf")

pyrosim.Send_Cube(name = "Box", pos = [0, 0, 0.5], size = [1, 1, 1])

pyrosim.End()

