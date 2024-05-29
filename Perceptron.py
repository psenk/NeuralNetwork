import random


# Activation function
def sign(number) -> int:
    """Function
    Activation Function, condense input to either 1 and -1
    number - integer input
    returns -> integer, -1 or 1
    """
    if number >= 0:
        return 1
    return -1


class Perceptron:
    
    learning_rate = 0.1
        
    def __init__(self, weights_list_size=3):
        """Constructor
        weights_list_size - size of the list containing input weights, default 3 (2 and 1 for bias)"""
        self.weights = [None] * weights_list_size
        
        # Initialize random weight values
        for i in range(0, len(self.weights)):
            self.weights[i] = random.uniform(-1.0, 1.0)
            
    
    def guess(self, inputs) -> int:
        """Function
        inputs - list of inputs
        returns -> integer, result of sign() function, -1 or 1"""
        sum = 0;
        
        for i in range(0, len(inputs)):
            sum += (inputs[i] * self.weights[i])
        
        return sign(sum)
            
    def train(self, inputs, target) -> None:
        """Function
        Tunes the weights of the perceptron
        inputs - list of inputs
        target - correct answer
        """
        guess = self.guess(inputs)
        
        error = target - guess
        
        # Tuning the weights
        for i in range(0, len(self.weights)):
            self.weights[i] += (error * inputs[i]) * self.learning_rate