import random


def line_function(x):
    # y = mx + b
    return 0.3 * x + 0.2


class Point:

    def __init__(self, _x=None, _y=None, bias=1):

        if not _x:
            self.x = random.randint(0, 1000)
        else:
            self.x = _x
        if not _y:
            self.y = random.randint(0, 1000)
        else:
            self.y = _y

        line_y = line_function(self.x)
        self.bias = bias

        if self.y > line_y:  # bottom right of graph
            self.label = 1
        else:
            self.label = -1  # top left of graph

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "], Bias: " + str(self.bias)
