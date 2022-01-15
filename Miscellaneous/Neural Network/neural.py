import numpy
import scipy.special
import imageio

class neuralNetwork:

    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.wih = numpy.random.normal(0.0,pow(self.hnodes,-0.5),(self.hnodes,self.inodes))
        self.who = numpy.random.normal(0.0,pow(self.onodes,-0.5),(self.onodes,self.hnodes))

        self.lr = learningrate

        self.activationfunction = lambda x: scipy.special.expit(x)


    def train(self,inputs_list,target_list):
        inputs = numpy.array(inputs_list,ndmin=2).T
        targets = numpy.array(target_list,ndmin=2).T

        hidden_inputs = numpy.dot(self.wih,inputs)
        hidden_outputs = self.activationfunction(hidden_inputs)

        final_inputs = numpy.dot(self.who,hidden_outputs)
        final_outputs = self.activationfunction(final_inputs)

        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.who.T,output_errors)

        self.who += self.lr*numpy.dot((output_errors*final_outputs*(1-final_outputs)),numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1- hidden_outputs)), numpy.transpose(inputs))


    def query(self,inputs_list):
        inputs = numpy.array(inputs_list,ndmin=2).T

        hidden_inputs = numpy.dot(self.wih,inputs)
        hidden_outputs = self.activationfunction(hidden_inputs)

        final_inputs = numpy.dot(self.who,hidden_outputs)
        final_outputs = self.activationfunction(final_inputs)

        return final_outputs

    def file(self,f):
        f.write(str(self.wih))
        f.write("\n\n\n")
        f.write(str(self.who))

inputnodes = 784
hiddennodes = 200
outputnodes = 10

learningrate = 0.1

n = neuralNetwork(inputnodes,hiddennodes,outputnodes,learningrate)

training_data = open("mnist_test.csv",'r')
training_data_list = training_data.readlines()
training_data.close()

for record in training_data_list:
    all_values = record.split(',')
    #print(len(all_values))
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    targets = numpy.zeros(outputnodes)+0.01
    targets[int(all_values[0])] = 0.99
    n.train(inputs,targets)


img_array = imageio.imread('one.png',as_gray = True)
img_data = 255.0 - img_array.reshape(784)
img_data = (img_data/255.0 * 0.99) + 0.01


outputs = n.query(img_data)
label = numpy.argmax(outputs)

print(label)
print(outputs)
#print(img_data)

f = open("weights.txt",'w')
n.file(f)
f.close()

#testing_data = open("training data.txt",'r')
#testing_data_list = testing_data.readlines()
#testing_data.close()

#correct = 0
#for record in testing_data_list:
#    all_values = record.split(",")
#    correct_answer = int(all_values[0])
#    inputs = (numpy.asfarray(all_values[1:])/255.0*0.99) + 0.01
#    outputs = n.query(inputs)
#    label = numpy.argmax(outputs)
#    if label == correct_answer:
#        correct+=1
#print("\tThe accuracy of the neural network is ",correct/len(testing_data_list))
