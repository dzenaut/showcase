#Assignment 3.1
#Dennis Ledwon

class Board():
    def __init__(self):
        '''creates an object that contains fields (a list of lists) and current, that stores the current player (integer that is 1 or 2)'''
        self.fields = [[0,0,0],[0,0,0],[0,0,0]]
        self.current = 1

    def getField(self, x, y):
        '''takes two integers x (row), y (column) and returns the value of that field.'''
        return self.fields[x-1][y-1]

    def getCurrentPlayer(self):
        '''returns current player'''
        return self.current

    def __str__(self):
        '''returns a string representing the board'''
        return str(self.fields)

    def getBoard(self):
        return self.fields

    def resetBoard(self):
        '''resets board to an empty board, player is player 1 again'''
        self.fields = [[0,0,0],[0,0,0],[0,0,0]]
        self.current = 1





