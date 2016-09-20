#Assignment 3.2
#Dennis Ledwon

from p1_2 import checkgame, haswon
from p3_1 import Board
from p5_1 import OccupiedMove, InvalidMove

class Board2(Board):

    def makeMove(self, x, y):
        '''takes 2 integers x (row 1-3), y (column 1-3) and makes a move in that field for the current player. Switches value of current to the other player'''
        if not x in range(1,4) or not y in range(1,4):
            raise InvalidMove()

        if self.fields[x-1][y-1] != 0:
            raise OccupiedMove()

        self.fields[x-1][y-1] = self.current
        if self.current == 1:
            self.current = 2
        else:
            self.current = 1


    def isOver(self):
        '''returns True if the game is over and False otherwise'''
        #if all tiles are occupied, return True, as the game is over
        if checkgame(self.fields) == 0:
            return True
        #if there is a winner, game is over
        return haswon(self.fields, self.current)

    def getResult(self):
        '''returns the current result: 1, if player 1 won, 2 if palyer 2 won, 0 otherwise'''
        #if there is a winner, either 1 or 2 will be returned
        if haswon(self.fields, self.current) == True:
            #because self.current is changed after the move in the method makemove, it is actually the opposite player of self.current that won
            if self.current == 1:
                return 2
            else:
                return 1
        #if there is no winner, 0 will be returned
        else:
            return 0
