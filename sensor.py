'''
David Smith
This holds a class to represent different sensors in the robot's structure.
This file will be used to build a robot to be placed into the world
'''

# import statements
import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

# class declaration
class SENSOR:
    
    # constructor
    def __init__(self, newLinkName):
        
        # value to hold the sensor name
        self.linkName = newLinkName
        
        # vector to hold the values of the sensor
        self.values = np.zeros(c.simSteps)
        
        
    # get sensor input
    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
        # print the vector if it is the last iteration
        if(t == c.simSteps - 1):
            print(self.values)

    # create function to save the values
    def Save_Values(self):
        
        # create the save file
        np.save("data/" + self.linkName + "sensor.npy", backLegMotorValues, allow_pickle=True, fix_imports=True)
