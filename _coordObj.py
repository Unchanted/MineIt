class Coord():
    
    def __init__(self, x, y = None):
        if(y == None):
            if(isinstance(x, str)):
                ln = x.split(', ')
                newX = int(ln[0][1:])
                newY = int(ln[1][:-1])
                self.x = newX
                self.y = newY
            else:
                self.x = x
                self.y = 0
        else:
            self.x = x
            self.y = y

    def getCoord(self):
        return self

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "{" + str(self.x) + ", " + str(self.y) + "}"

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
