#Assingment 4.3
#Dennis Ledwon

from p1_1 import board
from p3_2 import Board2
from p4_2 import RandomPlayer, SmartPlayer, HumanPlayer
from p5_1 import OccupiedMove, InvalidMove

class Game():
    '''Game class for tictactoe'''

    def __init__(self, player1, player2):
        '''Sets player to instances of the Player class (more specifically subclasses of the Player class and creates an instance of the board as an attribute of a Game'''
        self.player1 = player1
        self.player2 = player2
        self.playboard = Board2()

    def run(self):
        '''Runs a game that makes different moves depending on the chosen player classes'''

        #print board
        board(self.playboard.fields)

        while True:

            #if it is player 1's turn
            if self.playboard.current == 1:
                #ask player 1 to make a move
                print(self.player1.getName() + ', please make your move.')
                #get coordinates for the position of the next symbol to be placed. based on respective way of playing (depending on chosen subclass and according getMove function). Coordinates will be the first 2 positions of the tuple that results from calling the getMove method.
                coordinates = self.player1.getMove(self.playboard)

                #change the boardlist that is an attribute of the instance self.playboard of the class Board2 according to coordinates and the current player number.
                try:
                    self.playboard.makeMove(coordinates[0]+1, coordinates[1]+1)
                except OccupiedMove as e:
                    print(e)
                    print(2)
                    return 2
                except InvalidMove as e:
                    print(e)
                    print(2)
                    return 2

                #draws board after new move
                board(self.playboard.getBoard())

            #if it is player 2's turn
            else:

                #for comments, see above
                print(self.player2.getName() + ', please make your move.')
                coordinates = self.player2.getMove(self.playboard)
                try:
                    self.playboard.makeMove(coordinates[0]+1, coordinates[1]+1)
                except OccupiedMove as e:
                    print(e)
                    print(1)
                    return 1
                except InvalidMove as e:
                    print(e)
                    print(1)
                    return 1

                board(self.playboard.fields)

            #if the game is over
            if self.playboard.isOver() == True:

                #return the result of the game
                winner = self.playboard.getResult()
                if winner == 0:
                    print('Draw')
                else:
                    print(winner)
                return winner

