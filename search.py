'''
David Smith
This program will eventualy be modified to preform different search algorithms
to find ideal synapse weights to make the robot walk
'''

# import statements
from hillclimber import HILL_CLIMBER
import os

# create a hill climber instance
hc = HILL_CLIMBER()

# carry out the evolution process
hc.Evolve()

# show the best performer
hc.Show_Best()



# for loop to call the following functions twice
#for i in range(2):
    # call generate before simulating
    #os.system("python3 generate.py")

    # call simulation
    #os.system("python3 simulate.py")
