'''
David Smith
This class will use the hill climber algorithm, optimized with parallelism to try and
find the optimum weights for each synapse that allows the robot to act in the
desired manner
'''

# import statements
import constants as c
import copy
import os
from solution import SOLUTION

# class declaration
class PARALLEL_HILL_CLIMBER:

    # constructors
    def __init__(self):
        # create unique id for file IO
        self.nextAvailableID = 0
        
        # maintain dict of all parents
        self.parents = {}

        # fill the dictionary with the pop size
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        # clean up potentail corrupt or reminant files
        os.system('rm brain*.nndf')
        os.system('rm fitness*.txt')

    # method to change the matrix based on previous performance
    def Evolve(self):
        # evaluate the parents before creating future generations
        self.Evaluate(self.parents)

        # loop through to create criteria for evolving
        for currentGeneration in range(c.numberOfGenerations):
            # call method that will evolve one generation
            self.Evolve_For_One_Generation()
        
    # method to evole one generation of a robot
    def Evolve_For_One_Generation(self):
        # call the functions needed to evolve a robot
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    # method to create a copy of the parent in preparation for mutation
    def Spawn(self):
        # create dictionary to hold all children
        self.children = {}

        # iterate over parents and copy into children dict
        for i in range(c.populationSize):
            self.children[i] = copy.deepcopy(self.parents[i])

            # assign each child a unique id and incriment next
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    # mutate the child robot's weights from the copy created
    def Mutate(self):
        # mutate the children in te dictionary
        for i in range(c.populationSize):
            self.children[i].Mutate()

    # function to evaluate all children in the dictionary
    def Evaluate(self, solutions):
        # evaluate the current solution for each parent
        for i in range(c.populationSize):
            solutions[i].Start_Simulation('DIRECT')

        # retrieve the fitness for each parent
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_Finish()
       
    # select the better performing robot
    def Select(self):
        # if the child is better than the parent, it can have children. It dies otherwise
        for i in range(c.populationSize):
            if(self.parents[i].Get_Fitness() > self.children[i].Get_Fitness()):
                self.parents[i] = self.children[i]

    # print out the parent and child values to see who is selected
    def Print(self):
        for i in range(c.populationSize):
            print("\nParent: ", str(self.parents[i].Get_Fitness()), " Child: ", str(self.children[i].Get_Fitness()))

    # method to show the best performer of the group
    def Show_Best(self):
        # variable to hold the best parent
        best = self.parents[0]
        
        # find the best parent
        for i in range(1, c.populationSize):
                if(best.Get_Fitness() > self.parents[i].Get_Fitness()):
                    best = self.parents[i]
                    
        # call evaluate to show the parent with the GUI turned on
        best.Start_Simulation('DIRECT')

        # write the data to a file
        best.Write_Data()
