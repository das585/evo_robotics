'''
David Smith
This class represents the solutions to each search algorithm. They can be stored
and accessed through instances of this class
'''

# import statements
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random

# class declaration
class SOLUTION:

    # constructor
    def __init__(self):

        # create first solution matrix of random values in range -1 to 1
        self.weights = np.random.rand(3, 2)
        self.weights = self.weights * 2 - 1


    # method to evaluate the performace of a solution set
    def Evaluate(self, directOrGUI):

        # call all needed generations
        self.Create_World()
        self.Create_Robot_Body()
        self.Create_Robot_Brain()

        # run the simulation
        os.system('python3 simulate.py ' + directOrGUI)

        # open the file and read in value
        fitnessFile = open('fitness.txt', 'r')
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()

    # creates the world sdf for use in simulate.py
    def Create_World(self):

        # start sdf creation
        pyrosim.Start_SDF("world.sdf")

        # terminate the creation
        pyrosim.End()


    # creates the body of the robot	
    def Create_Robot_Body(self):
        
        # start urdf creation
        pyrosim.Start_URDF("body.urdf")
        
        # set the dimention variables
        length = 1
        width = 1
        height = 1

        # generate torso
        pyrosim.Send_Cube(name = "Torso", pos = [1.5, 0, 1.5], size = [width, length, height])
        
        # create torso-front leg joint
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2, 0, 1])
        
        # generate front leg
        pyrosim.Send_Cube(name = "FrontLeg", pos = [.5, 0, -.5], size = [width, length, height])
        
        # create joint between torso-back leg
        pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg", type = "revolute", position = [1, 0, 1])
        
        # add back leg
        pyrosim.Send_Cube(name = "BackLeg", pos = [-.5, 0, -.5], size = [width, length, height])
        
        # terminate urdf creation
        pyrosim.End()


    # creates the mind of the robot	
    def Create_Robot_Brain(self):

        # start nndf creation
        pyrosim.Start_NeuralNetwork("brain.nndf")
        
        # create a neuron for the torso sensor
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        
        # create neuron for back leg sensor
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        
        # create neuron for front leg sensor
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
        
        # create a motor neuron for the back leg joint
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")

        # create a motor neuron for the back leg joint
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        # for loop to connect all neurons
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + 3, weight = self.weights[currentRow][currentColumn])
        
        # terminate urdf creation
        pyrosim.End()

    # method to mutate the synaptic weights
    def Mutate(self):

        # get the col and row of the synapse to mutate
        mutateCol = random.randint(0, 1)
        mutateRow = random.randint(0, 2)

        # randomly change that value in the matrix
        self.weights[mutateRow, mutateCol] = random.random() * 2 -1

    # method to return weights
    def Get_Weights(self):
        return self.weights

    # method to return the fitness of the solution
    def Get_Fitness(self):
        return self.fitness
