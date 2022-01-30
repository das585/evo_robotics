'''
    David Smith
    generate.py: This program will be used to generate the body of any robots
    created for this class using the provided pyrosim files
'''

# import statements
import pyrosim.pyrosim as pyrosim

# main calls to other functions
def main():
	Create_World()
	Create_Robot()

# creates the world sdf for use in simulate.py
def Create_World():

	# start sdf creation
	pyrosim.Start_SDF("world.sdf")

	# terminate the creation
	pyrosim.End()

# creates the body and mind of the robot	
def Create_Robot():
	
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
	
	
main()
