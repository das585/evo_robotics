'''
David Smith
This program will eventualy be modified to preform different search algorithms
to find ideal synapse weights to make the robot walk
'''

# import statements
from parallelHillclimber import PARALLEL_HILL_CLIMBER
import os

# repeat the search 10 times so that an average can be taken from collected data
### SHOW BEST HAS BEEN MODIFIED TO BE DIRECT NOT GUI. CHANGE BACK IF DESIRED
for x in range(50):
    # create a hill climber instance
    phc = PARALLEL_HILL_CLIMBER()

    # carry out the evolution process
    phc.Evolve()

    # show the best performer
    phc.Show_Best()



