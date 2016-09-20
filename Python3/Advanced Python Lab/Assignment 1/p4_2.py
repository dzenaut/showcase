#Assignment 4.2
#Dennis Ledwon

from p1_2 import makemove
from p2_1 import randomMove, smartMove
from p2_2 import modifyBoard
from p3_2 import Board2
from p4_1 import Player


class RandomPlayer(Player):
    '''Player that makes a random move when getMove is called.'''

    def getMove(self, Board2):
        '''gets coordinates for a random move, stored in a tuple. NOTE: In the same tuple, as tuple[2], the new boardlist is saved.'''
        boardlist = Board2.getBoard()
        player = Board2.getCurrentPlayer()

        #randMove just fills a random tile that is zero with either 1 or 2, depending on which player is currently making a move.
        return randomMove(boardlist, player)


class SmartPlayer(Player):
    '''Player that makes a smart move when getMove is called.'''

    def getMove(self, Board2):
        '''gets coordinates for a smart move, stored in a tuple. NOTE: In the same tuple, as tuple[2], the new boardlist is saved.'''
        boardlist = Board2.getBoard()
        player = Board2.getCurrentPlayer()

        #smartMove prioritizes central>corner>edge tiles, if they are empty (checked in the described order) the tile is filled with the symbol of the currently active player (1 or 2).
        return smartMove(boardlist, player)


class HumanPlayer(Player):
    '''Player that lets a human player decide on a move if getMove is called'''

    def getMove(self, Board2):
        '''asks human player for coordinates x (row 1-3) and y (column 1-3)'''

        #these 2 lines are not really necessary right now
        boardlist = Board2.getBoard()
        player = Board2.getCurrentPlayer()

        #values of x and y are subtracted by 1 because the x and y values for the generated from the computer getMove methods are the values of the indices (0-2) instead of number of rows and columns (1-3), which is more intuitive for humans
        while True:
            try:
                x = int(input('Enter row: '))
                break
            except ValueError:
                print('Please enter coordinates.')
        x -= 1
        while True:
            try:
                y = int(input('Enter column: '))
                break
            except ValueError:
                print('Please enter coordinates.')
        y -= 1
        return (x, y)








