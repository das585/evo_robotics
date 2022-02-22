'''
David Smith
This class is meant to represent the robot to be simulated in the world.
The modular nature of a class will alow for easy changes of the structure
of the robot, along with allowing for easy creation of multiple robots
in the simulated world
'''

# import statements
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

# class declaration
class ROBOT:
    
    # constructor
    def __init__(self):
        # empty, do nothing
        pass
        
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
        
        # loop through all motors and make them act
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName].Set_Value(t, robotID)
            
    # method to save the vectors
    def Save_All(self):
        
        # save all sensor values
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Save_Values()
            
        # save all motor values
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName].Save_Values()
            
        
