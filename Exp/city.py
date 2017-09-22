from math import sqrt, pow

class City:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return str(self.x) + ";" + str(self.y) + " "

    def distanceTo(self,c):
        h = pow(self.x - c.x, 2)
        v = pow(self.y - c.y, 2)
        return sqrt(h + v)


