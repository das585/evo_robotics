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
    def __init__(self, directOrGUI):
        
        # add the world and robot into the simulation
        self.world = WORLD()
        
        # physics engine init
        if(directOrGUI == 'GUI'):
            self.physicsClient = p.connect(p.GUI)

        else:
            self.physicsClient = p.connect(p.DIRECT)
        
        
        # add pybullet data path to be usable
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # load in robotID
        self.robotID = p.loadURDF("body.urdf")

        # create the robot
        self.robot = ROBOT(self.robotID)

        # set the gravity in the world
        p.setGravity(0, 0, c.gravConst)
        
        # create the floor
        self.planeID = p.loadURDF("plane.urdf")

        # load in the world
        self.worldID = p.loadSDF("world.sdf")

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

    # method to get the fitness score for the run
    def Get_Fitness(self):

        # call robot's fitness function
        self.robot.Get_Fitness()
    
        
    # create destructor
    def __del__(self):
        
        # save all values in the vectors
        #self.robot.Save_All()
        
        # physics engine disconnect
        p.disconnect
