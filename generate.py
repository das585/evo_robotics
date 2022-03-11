'''
    David Smith
    generate.py: This program will be used to generate the body of any robots
    created for this class using the provided pyrosim files
'''

# import statements
import pyrosim.pyrosim as pyrosim
import random

# main calls to other functions
def main():
    Create_World()
    Create_Robot_Body()
    Create_Robot_Brain()

# creates the world sdf for use in simulate.py
def Create_World():

	# start sdf creation
	pyrosim.Start_SDF("world.sdf")

	# terminate the creation
	pyrosim.End()

# creates the body of the robot	
def Create_Robot_Body():
	
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
def Create_Robot_Brain():

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
    for sensor in range(3):
        for motor in range(3, 5):
            pyrosim.Send_Synapse(sourceNeuronName = sensor, targetNeuronName = motor, weight = random.triangular(-1.0, 1.0))
    
    # terminate urdf creation
    pyrosim.End()
	
main()
