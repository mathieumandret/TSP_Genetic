from math import sqrt, pow

class City:

    def __init__(self, x, y):
        self.coords = (x,y)


    def getX(self):
        return self.coords[0]

    def getY(self):
        return self.coords[1]

    def __repr__(self):
        return str(self.coords)
    
    def distanceTo(self,c):
        h = pow(self.getX() - c.getX(), 2)
        v = pow(self.getY() - c.getY(), 2)
        return sqrt(h + v)

    def __eq__(self, other):
        if isinstance(other, City):
            return(self.coords == other.coords)
        else:
            return False

    def __hash__(self):
        return hash(self.coords)
