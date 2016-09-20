#Assignment 3.3
#Dennis Ledwon

from p1_1 import board
from p3_2 import Board2

class Game():
    def __init__(self, player1, player2):
        '''takes two arguments -the names of the players- and stores them in attributes. Creates an instance of Board2 and stores it in an attribute'''
        self.player1 = player1
        self.player2 = player2
        self.playboard = Board2()

    def run(self):
        #prints current board
        board(self.playboard.fields)

        while True:

            #Ask Player for move
            if self.playboard.current == 1:
                print(self.player1, ', please make your move')
            else:
                print(self.player2, ', please make your move')

            #ask for coordinates from player
            x = int(input('Enter row: '))
            y = int(input('Enter column: '))

            #makes the move
            self.playboard.makeMove(x,y)

            #prints board after new move
            board(self.playboard.fields)

            #check if the game is over
            if self.playboard.isOver() == True:
                #return result of the game
                return self.playboard.getResult()

#commented out so that import to works flawlessly
'''
game = Game('Dennis', 'Leticia')
result = game.run()
print(result)
'''
