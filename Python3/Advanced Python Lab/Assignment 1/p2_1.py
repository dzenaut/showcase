#Assignment 2.1
#Dennis Ledwon

from p1_1 import board
from random import randint



def randomMove(list, player):
    '''Input: List: nested list with three sublists of length 3 that shows the current state of the tictactoe game. Player: Player Number (1 or 2). Makes a valid move in a game of tictactoe by returning the coordinates of the move to be played and a list that represents the board after the move. The output is a tuple'''

    #finds a random element in the nested list. Checks if the element is empty, i.e. occupied by a 0. If so, the field is replaced by the number of the player
    while True:
        x = randint(0, 2)
        y = randint(0, 2)
        if list[x][y] == 0:
            return (x,y)

def smartMove(list, player):
    '''BONUS WORK: plays a move in tictactoe, but prioritizes center>corner>edge tiles'''

    #list of corner tiles
    cornertiles = [(0,0), (2,0), (0,2), (2,2)]

    #list of edgetiles
    edgetiles = [(0,1), (1,0), (1,2), (2,1)]

    #highest priority: central tile
    if list[1][1] == 0:
        return (1,1)

    #second priority: corner tiles
    empty = []
    for sub in cornertiles:
        x = sub[0]
        y = sub[1]
        if list[x][y] == 0:
            empty.append(sub)
    if len(empty) != 0:
        return empty[randint(0, len(empty)-1)]



    #third priority: edge tiles
    empty = []
    for sub in edgetiles:
        x = sub[0]
        y = sub[1]
        if list[x][y] == 0:
            empty.append(sub)
    return empty[randint(0, len(empty)-1)]













