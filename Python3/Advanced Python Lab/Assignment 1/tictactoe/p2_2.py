#Assignment 2.2
#Dennis Ledwon

from p1_1 import board
from p1_2 import checkgame
from p1_2 import haswon
from p2_1 import randomMove, smartMove


def modifyBoard(boardlist, coordinates, player):
    boardlist[coordinates[0]][coordinates[1]] = player
    return boardlist



def compMatch(list):
    '''Start a computer match of tictactoe in which player 1 and player 2 are played by a computer that makes random moves'''

    boardlist = list
    counter = 0

    while True:

        #determine whether player 1 or player 2 is playing
        if counter%2 == 0:
            player = 1
        else:
            player = 2

        #generate coordinates and new list, all stored in a tuple
        gametuple = randomMove(boardlist, player)

        #extract list from tuple and display board according on the computers move
        boardlist = modifyBoard(boardlist, gametuple, player)
        board(boardlist)

        counter += 1

        #break out of loop if a winning position is on the board
        if haswon(boardlist, player):
            print('Congratulations, Player', player, ", you won!")
            break

        #break if all tiles are occupied
        if checkgame(boardlist) == 0:
            break


def test1():
    compMatch([[0,0,0], [0,0,0], [0,0,0]])

def smartCompMatch(list):
    '''BONUS WORK: start a match of tictactoe, player 1 is a smart computer, player 2 is a computer that makes random moves'''

    #analogous to comments in compMatch

    boardlist = list
    counter = 0

    while True:
        if counter%2 == 0:
            player = 1
            gametuple = smartMove(boardlist, player)
        else:
            player = 2
            gametuple = randomMove(boardlist, player)
        boardlist = modifyBoard(boardlist, gametuple, player)
        board(boardlist)

        counter += 1

        if haswon(boardlist, player):
            print('Congratulations, Player', player, ", you won!")
            break

        if checkgame(boardlist) == 0:
            break

def test2():
    smartCompMatch([[0,0,0],[0,0,0],[0,0,0]])

# --remove comment to try --test1()

# --remove comment to try --test2()



