'''
David Smith
This class represents the solutions to each search algorithm. They can be stored
and accessed through instances of this class
'''

# import statements
import constants as c
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random
import time

# class declaration
class SOLUTION:

    # constructor
    def __init__(self, ID):

        # create first solution matrix of random values in range -1 to 1
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1

        # id for file io
        self.myID = ID

    # method to start the simulation
    def Start_Simulation(self, directOrGUI):
        # call all needed simulation components
        self.Create_World()
        self.Create_Robot_Body()
        self.Create_Robot_Brain()

        # run the simulation
        os.system('python3 simulate.py ' + directOrGUI + " " + str(self.myID) + " 2&>1 &")

    # method to get the fitness after the termination of the simulation
    def Wait_For_Simulation_To_Finish(self):

        # wait for the creation of the fitness file to read the fitness
        while not os.path.exists('fitness' + str(self.myID) + '.txt'):
            time.sleep(.01)

        # open the file and read in value
        fitnessFile = open('fitness' + str(self.myID) + '.txt', 'r')
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()

        # remove the fitness file after it is used
        os.system('rm ' + 'fitness' + str(self.myID) + '.txt')
        
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
        pyrosim.Send_Cube(name = "Torso", pos = [0, 0, 1], size = [width, length, height])
        
        # create upper legs
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0, .5, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "FrontLeg", pos = [0, .5, 0], size=[0.2,1,0.2])
        
        pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg", type = "revolute", position = [0, -.5, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "BackLeg", pos = [0, -.5, 0], size=[0.2,1,0.2])

        pyrosim.Send_Joint(name = "Torso_LeftLeg", parent = "Torso", child = "LeftLeg", type = "revolute", position = [-.5, 0, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LeftLeg", pos = [-.5, 0, 0], size = [1, .2, .2])

        pyrosim.Send_Joint(name = "Torso_RightLeg", parent = "Torso", child = "RightLeg", type = "revolute", position = [.5, 0, 1], jointAxis = "0 1 0" )
        pyrosim.Send_Cube(name = "RightLeg", pos = [.5, 0, 0], size = [1, .2, .2])

        # create lower legs
        pyrosim.Send_Joint(name = "FrontLeg_LowerFront", parent = "FrontLeg", child = "LowerFront", type = "revolute", position = [0, 1, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LowerFront", pos = [0, 0, -.5], size = [.2, .2, 1])

        pyrosim.Send_Joint(name = "BackLeg_LowerBack", parent = "BackLeg", child = "LowerBack", type = "revolute", position = [0, -1, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LowerBack", pos = [0, 0, -.5], size = [.2, .2, 1])

        pyrosim.Send_Joint(name = "LeftLeg_LowerLeft", parent = "LeftLeg", child = "LowerLeft", type = "revolute", position = [-1, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LowerLeft", pos = [0, 0, -.5], size = [.2, .2, 1])

        pyrosim.Send_Joint(name = "RightLeg_LowerRight", parent = "RightLeg", child = "LowerRight", type = "revolute", position = [1, 0, 0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name = "LowerRight", pos = [0, 0, -.5], size = [.2, .2, 1])
        
        # terminate urdf creation
        pyrosim.End()


    # creates the mind of the robot	
    def Create_Robot_Brain(self):

        # start nndf creation
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        
        # create sensor neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")

        # uncomment to add in these sensors. Taken out because they don't
        # get triggered as often so they don't add much extra info
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName = "RightLeg")
        
        pyrosim.Send_Sensor_Neuron(name = 5, linkName = "LowerFront")
        pyrosim.Send_Sensor_Neuron(name = 6, linkName = "LowerBack")
        pyrosim.Send_Sensor_Neuron(name = 7, linkName = "LowerLeft")
        pyrosim.Send_Sensor_Neuron(name = 8, linkName = "LowerRight")
        
        # create motor neurons
        pyrosim.Send_Motor_Neuron(name = 9, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 10, jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 11, jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name = 12, jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name = 13, jointName = "FrontLeg_LowerFront")
        pyrosim.Send_Motor_Neuron(name = 14, jointName = "BackLeg_LowerBack")
        pyrosim.Send_Motor_Neuron(name = 15, jointName = "LeftLeg_LowerLeft")
        pyrosim.Send_Motor_Neuron(name = 16, jointName = "RightLeg_LowerRight")

        # for loop to connect all neurons
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
        
        # terminate urdf creation
        pyrosim.End()

    # method to mutate the synaptic weights
    def Mutate(self):

        # get the col and row of the synapse to mutate
        mutateCol = random.randint(0, c.numMotorNeurons - 1)
        mutateRow = random.randint(0, c.numSensorNeurons - 1)

        # randomly change that value in the matrix
        self.weights[mutateRow, mutateCol] = random.random() * 2 -1

    # method to return weights
    def Get_Weights(self):
        return self.weights

    # method to return the fitness of the solution
    def Get_Fitness(self):
        return self.fitness

    # method to set the robot's id
    def Set_ID(self, ID):
        self.myID = ID

    # function to write the fitness value to a csv
    def Write_Data(self):
        # open the file to write data to
        outfile = open("reg_leg.csv", "a")

        # format string to write
        temp = '{},{}\n'

        outs = temp.format(c.numberOfGenerations, self.fitness)

        # write and close
        outfile.write(outs)
        outfile.close()
