'''
David Smith
This program will eventualy be modified to preform different search algorithms
to find ideal synapse weights to make the robot walk
'''

# import statements
import os


# for loop to call the following functions twice
for i in range(2):
    # call generate before simulating
    os.system("python3 generate.py")

    # call simulation
    os.system("python3 simulate.py")
