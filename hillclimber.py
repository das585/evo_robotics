'''
David Smith
This class will use the hill climber algorithm to try and find the optimum
weights for each synapse that allows the robot to act in the desired manner
'''

# import statements
import constants as c
import copy
from solution import SOLUTION

# class declaration
class HILL_CLIMBER:

    # constructors
    def __init__(self):
        self.parent = SOLUTION()

    # method to change the matrix based on previous performance
    def Evolve(self):
        # evaluate the current solution
        self.parent.Evaluate('GUI')

        # loop through to create criteria for evolving
        for currentGeneration in range(c.numberOfGenerations):

            # call method that will evolve one generation
            self.Evolve_For_One_Generation()
        
    # method to evole one generation of a robot
    def Evolve_For_One_Generation(self):
        # call the functions needed to evolve a robot
        self.Spawn()
        self.Mutate()
        self.child.Evaluate('DIRECT')
        self.Print()
        self.Select()

    # method to create a copy of the parent in preparation for mutation
    def Spawn(self):
        # create the copy
        self.child = copy.deepcopy(self.parent)

    # mutate the child robot's weights from the copy created
    def Mutate(self):
        # mutate the child
        self.child.Mutate()

    # select the better performing robot
    def Select(self):
        # if the child is better than the parent, it can have children. It dies otherwise
        if(self.parent.Get_Fitness() > self.child.Get_Fitness()):
            self.parent = self.child

    # print out the parent and child values to see who is selected
    def Print(self):
        print("\nParent: ", str(self.parent.Get_Fitness()), " Child: ", str(self.child.Get_Fitness()))

    # method to show the best performer of the group
    def Show_Best(self):
        # call evaluate to show the parent with the GUI turned on
        self.parent.Evaluate('GUI')
        
