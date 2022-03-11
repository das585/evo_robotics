from pyrosim.neuron  import NEURON

from pyrosim.synapse import SYNAPSE

class NEURAL_NETWORK: 

    def __init__(self,nndfFileName):

        self.neurons = {}

        self.synapses = {}

        f = open(nndfFileName,"r")

        for line in f.readlines():

            self.Digest(line)

        f.close()
        
    def Print(self):

        self.Print_Sensor_Neuron_Values()

        self.Print_Hidden_Neuron_Values()

        self.Print_Motor_Neuron_Values()

        print("")

    # method to update the neuron values
    def Update(self):
        
        # print the names of the neurons
        for neuronName in self.neurons:
            
            # get value from sensor to update sensor neuron
            if self.neurons[neuronName].Is_Sensor_Neuron():
                self.neurons[neuronName].Update_Sensor_Neuron()
                
            # use function to update motor/hidden neuron based on sensors
            else:
                self.neurons[neuronName].Update_Hidden_Or_Motor_Neuron(self.neurons, self.synapses)
                
    # method to return the keys of the neurons dict
    def Get_Neuron_Names(self):
        return self.neurons.keys()

    # method to return if the neuron is a motor neuron or not
    def Is_Motor_Neuron(self, neuronName):
        return self.neurons[neuronName].Is_Motor_Neuron()
        
    # method to return the name of the joint for a motor neuron
    def Get_Motor_Neurons_Joint(self, neuronName):
        return self.neurons[neuronName].Get_Joint_Name()
        
    # method to return the value of a given neuron
    def Get_Value_Of(self, neuronName):
        return self.neurons[neuronName].Get_Value()



# ---------------- Private methods --------------------------------------

    def Add_Neuron_According_To(self,line):

        neuron = NEURON(line)

        self.neurons[ neuron.Get_Name() ] = neuron

    def Add_Synapse_According_To(self,line):

        synapse = SYNAPSE(line)

        sourceNeuronName = synapse.Get_Source_Neuron_Name()

        targetNeuronName = synapse.Get_Target_Neuron_Name()

        self.synapses[sourceNeuronName , targetNeuronName] = synapse

    def Digest(self,line):

        if self.Line_Contains_Neuron_Definition(line):

            self.Add_Neuron_According_To(line)

        if self.Line_Contains_Synapse_Definition(line):

            self.Add_Synapse_According_To(line)

    def Line_Contains_Neuron_Definition(self,line):

        return "neuron" in line

    def Line_Contains_Synapse_Definition(self,line):

        return "synapse" in line

    def Print_Sensor_Neuron_Values(self):

        print("sensor neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Sensor_Neuron():

                self.neurons[neuronName].Print()

        print("")

    def Print_Hidden_Neuron_Values(self):

        print("hidden neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Hidden_Neuron():

                self.neurons[neuronName].Print()

        print("")

    def Print_Motor_Neuron_Values(self):

        print("motor neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Motor_Neuron():

                self.neurons[neuronName].Print()

        print("")
