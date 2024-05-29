import Perceptron as p
import Training
import random

if __name__ == "__main__":

    perceptron = p.Perceptron()

    correct_guesses = 0
    incorrect_guesses = 0
    test_points_list_size = 10000
    test_points_list = []
    # test_inputs = [1, 0.5]

    for i in range(test_points_list_size):
        test_points_list.append(
            Training.Point(random.randint(0, 1000), random.randint(0, 1000))
        )

    for point in test_points_list:
        print("Point: " + str(point))
        print("Weights: " + str(perceptron.weights))

        inputs = [point.x, point.y, point.bias]  # where is the point - ADD BIAS
        target = point.label  # correct answer
        print("Target: " + str(target))

        perceptron.train(inputs, target)

        guess = perceptron.guess(inputs)
        print("Guess: " + str(guess))

        if guess == target:
            print("Correct guess")
            correct_guesses += 1
        else:
            print("Incorrect guess")
            incorrect_guesses += 1

        print()

print("Correct guesses: " + str(correct_guesses))
print("Inorrect guesses: " + str(incorrect_guesses))
