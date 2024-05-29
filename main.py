import Perceptron as p
import Training

if __name__ == "__main__":
    
    perceptron = p.Perceptron()
    correct_guesses = 0
    incorrect_guesses = 0
    
    # test_inputs = [1, 0.5]
    test_points = [None] * 10000
    
    for i in range(0, len(test_points)):
        test_points[i] = Training.Point()
    
    for point in test_points:
        print(str(point))
        print("Weights: " + str(perceptron.weights))
        
        inputs = [point.x, point.y, point.bias] # where is the point - ADD BIAS
        target = point.label # correct answer
        print("Target: " + str(target))
        
        perceptron.train(inputs, target)
        
        guess = perceptron.guess(inputs)
        print("Guess: " + str(guess))
        
        if (guess == target):
            print("Correct guess")
            correct_guesses += 1
        else:
            print("Incorrect guess")
            incorrect_guesses += 1
            
        print()
        
print("Correct guesses: " + str(correct_guesses))
print("Inorrect guesses: " + str(incorrect_guesses))