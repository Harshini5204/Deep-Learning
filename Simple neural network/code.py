import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x*(1-x)
    #training data consisting of 4 examples--3 input values and 1 output
training_inputs = np.array([[0,0,1],
                                [1,1,1],
                                [1,0,1],
                                [0,1,1]])
training_outputs = np.array([[0,1,1,0]]).T
np.random.seed(1)
synaptic_weights = 2 * np.random.random((3, 1)) - 1
print("Random Generated Weights: ")
print(synaptic_weights)
for iteration in range(200000):
    input_layer=training_inputs
    outputs=sigmoid(np.dot(input_layer,synaptic_weights))
    error=training_outputs-outputs
    adjustments=error*sigmoid_derivative(outputs)
    synaptic_weights+=np.dot(input_layer.T,adjustments)
print("synaptic weights after training:")
print(synaptic_weights)
print("outputs after training:")
print(outputs)
