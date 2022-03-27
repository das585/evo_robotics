'''
David Smith
This class is meant to represent the robot to be simulated in the world.
The modular nature of a class will alow for easy changes of the structure
of the robot, along with allowing for easy creation of multiple robots
in the simulated world
'''

# import statements
import constants as c
from motor import MOTOR
import os
import pybullet as p
import pybullet_data
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

# class declaration
class ROBOT:
    
    # constructor
    def __init__(self, ID, fileID):

        # create the robots value
        self.robot = ID

        # id for file IO
        self.fileID = fileID
        
        # create neural net from nndf with given id
        self.nn = NEURAL_NETWORK("brain" + str(self.fileID) +".nndf")

        # delete the nndf after
        os.system("rm brain" + str(fileID) + ".nndf")

    
    # method to set up the sensors in the robot
    def Prepare_To_Sense(self):
        
        # create a dictionary to hold all sensors
        self.sensors = {}
        
        # print out all link names
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            
    # method to get sensor input for the robot
    def Sense(self, t):
        
        # loop through all sensors and add the sensor value to the vector
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(t)
            
    # method to setup motors for movement
    def Prepare_To_Act(self):
        
        # dictionary to hold all motors
        self.motors = {}
        
        # loop through all joints and add motors
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            
    # method to cause the motors to act
    def Act(self, t, robotID):
        
        # loop through all neurons, get angle value, and set angle
        for neuronName in self.nn.Get_Neuron_Names():
            
            # move only if a motor neuron
            if self.nn.Is_Motor_Neuron(neuronName):
                
                # get the value for the angle of the motor
                desiredAngle = c.motorJointRange * self.nn.Get_Value_Of(neuronName)
                
                # get the joint name
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                
                # cause the motors to move
                self.motors[jointName].Set_Value(desiredAngle, robotID)
            
            
    # method to let the robot think and make decisions
    def Think(self):
        
        # update the neural net values
        self.nn.Update()
        
        # print the neural net values
        #self.nn.Print()

    # function to get the robot's fitness score
    def Get_Fitness(self):

        # get the state of link 0 to analyze position
        stateOfLinkZero = p.getLinkState(self.robot, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        # open a file to write the x coordinate to
        fitnessFile = open("tmp" + str(self.fileID) + ".txt", 'w')
        fitnessFile.write(str(xCoordinateOfLinkZero))
        fitnessFile.close()

        # move the temp file to fitness file to prevent reading before file
        # is written to
        os.system('mv tmp' + str(self.fileID) + '.txt fitness' + str(self.fileID) + '.txt')

            
    # method to save the vectors
    def Save_All(self):
        
        # save all sensor values
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Save_Values()

