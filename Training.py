# For testing
def line_function(x):
    # y = mx + b
    return 0.3 * x + 0.2


class Point:
    """Point Class
    For testing purposes only"""
    
    
    def __init__(self, x, y, bias=1):
        """Constructor
        x - x coordinate of point, int
        y - y coordinate of point, int
        bias - input bias, always 1
        label - correct target compared with function"""
        
        self.x = x
        self.y = y
        self.bias = bias

        # function
        line_y = line_function(self.x)

        if self.y > line_y:  # above the line
            self.label = 1
        else:
            self.label = -1  # below the line

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "], Bias: " + str(self.bias)