'''
David Smith
This program will eventualy be modified to preform different search algorithms
to find ideal synapse weights to make the robot walk
'''

# import statements
from parallelHillclimber import PARALLEL_HILL_CLIMBER
import os

# loop to repeatedly simulate
#for x in range(5):
# create a hill climber instance
phc = PARALLEL_HILL_CLIMBER()

# carry out the evolution process
phc.Evolve()

# show the best performer
phc.Show_Best()



# for loop to call the following functions twice
#for i in range(2):
    # call generate before simulating
    #os.system("python3 generate.py")

    # call simulation
    #os.system("python3 simulate.py")
