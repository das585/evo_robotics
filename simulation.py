'''
David Smith
A class that contians the functionality needed to run a simulation of a
robot with pyrosim and pybullet. The class structure is meant to give a 
more modular approach for the simulation
'''

# import statements
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from robot import ROBOT
import time
from world import WORLD


# class declaration
class SIMULATION:
    
    # constructor
    def __init__(self):
        
        # add the world and robot into the simulation
        self.world = WORLD()
        self.robot = ROBOT()
        
        # physics engine init
        self.physicsClient = p.connect(p.GUI)
        
        # add pybullet data path to be usable
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # set the gravity in the world
        p.setGravity(0, 0, c.gravConst)
        
        # create the floor
        self.planeID = p.loadURDF("plane.urdf")

        # load the robot
        self.robotID = p.loadURDF("body.urdf")

        # load in the world
        p.loadSDF("world.sdf")

        # prepare to use sensor values
        pyrosim.Prepare_To_Simulate(self.robotID)
        
        # add sensors to the robot
        self.robot.Prepare_To_Sense()
        
        # add motors to the robot
        self.robot.Prepare_To_Act()
        
    # method to run the simulation
    def Run(self):
        # step through the world
        for x in range(c.simSteps):
            
            # step simulation
            p.stepSimulation()
            
            # get the sensor input
            self.robot.Sense(x)
            
            # make the robot think before it acts
            self.robot.Think()
            
            # give motor output
            self.robot.Act(x, self.robotID)
             
            # print the step number and wait 
            #print(x)
            time.sleep(c.sleepTime)
    
        
    # create destructor
    def __del__(self):
        
        # save all values in the vectors
        self.robot.Save_All()
        
        # physics engine disconnect
        p.disconnect
