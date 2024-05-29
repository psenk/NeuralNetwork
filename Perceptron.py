import random


# Activation function
def sign(number) -> int:
    
    if number >= 0:
        return 1
    return -1


class Perceptron:
    
    learning_rate = 0.1
        
    # Constructor
    def __init__(self, weights_size=3):
        
        self.weights = [None] * weights_size
        
        # Initialize random weight values
        for i in range(0, len(self.weights)):
            self.weights[i] = random.uniform(-1.0, 1.0)
            
    
    def guess(self, inputs) -> int:
        
        sum = 0;
        
        for i in range(0, len(inputs)):
            sum += (inputs[i] * self.weights[i])
        
        return sign(sum)
            
    def train(self, inputs, target):
        
        guess = self.guess(inputs)
        
        error = target - guess
        
        # Tuning the weights
        for i in range(0, len(self.weights)):
            self.weights[i] += (error * inputs[i]) * self.learning_rate