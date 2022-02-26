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

    # set the motor to a given value
    def Set_Value(self, t, robotID):
        
        # simulate motors
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotID,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = t,
            maxForce = c.motorForce)
            
