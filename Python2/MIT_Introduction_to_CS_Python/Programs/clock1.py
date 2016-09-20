class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, Coordinate):
        if self.x == Coordinate.x and self.y == Coordinate.y:
            return True

    def __repr__(self):
        x = self.x
        y = self.y
        return 'Coordinate(' + str(x) + ',' + str(y) + ')'

a = Coordinate(1,1)
b = Coordinate(1,1)

print(a.__eq__(b))
print(a.__repr__())
