'''
David Smith
This class represents a motor and can be used to construct a robot.
'''

# import statements
import constants as c
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim

# class declaration
class MOTOR:
        
    # constructor
    def __init__(self, newJointName):
        self.jointName = newJointName
        self.Prepare_To_Act()
        
    # create a vector of values for motor movement
    def Prepare_To_Act(self):
        
        # create vars for the motor movement
        self.amplitude = c.amplitude
        self.offset = c.FLphaseOffset
        self.motorForce = c.motorForce
        
        # conditional for the 
        if (self.jointName == "Torso_FrontLeg"):
            self.frequency = c.frequency
            
        else:
            self.frequency = c.frequency / 2
        
        # create a vector of desired motor values
        self.targetAngles = np.linspace(-1, 1, c.simSteps)  
        

    # set the motor to a given value
    def Set_Value(self, t, robotID):
        
        # simulate motors
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotID,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.amplitude * np.sin(self.frequency * self.targetAngles[t] + self.offset),
            maxForce = self.motorForce)
            
    # create function to save the values
    def Save_Values(self):
        
        # create the save file
        np.save("data/" + self.jointName + "motor.npy", backLegMotorValues, allow_pickle=True, fix_imports=True)
