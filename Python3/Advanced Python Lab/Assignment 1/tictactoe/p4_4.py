#Assingment 4.4
#Dennis Ledwon

from p1_1 import board
from p3_2 import Board2
from p4_2 import RandomPlayer, SmartPlayer, HumanPlayer
from p4_3 import Game

class Competition(Game):

    def startComp(self):
        '''Starts a competition between 2 players, that make moves based on their respective getMove methods. Keeps track of victories for both players and gives the overall result in the end.'''

        #counters for victories of players and draws
        counter1 = 0
        counter2 = 0
        drawcounter = 0

        #just run game between to players 10 times and store the winner in the variable result
        for games in range(10):
            result = self.run()

            #depending on winner, update the respective counter
            if result == 1:
                counter1 += 1
            elif result == 2:
                counter2 += 1
            else:
                drawcounter += 1

            #reset to empty board and player to 1
            self.playboard.resetBoard()

        #switch around players players so that player1 moves second and player2 moves first now
        self.player1 = player2
        self.player2 = player1

        #now, if player1 (now acts as player 2, i.e. moves second) wins, self.run() will return 2. So counter1 has to be increased if self.run() returns 2
        for games in range(10):
            result = self.run()
            if result == 2:
                counter1 += 1
            elif result == 1:
                counter2 += 1
            else:
                drawcounter += 1

            #reset
            self.playboard.resetBoard()

        print('Victories for', self.player2.getName(), ':', counter1, '\nVictories for', self.player1.getName(), ':', counter2, '\nDraws: ', drawcounter)

#commented out, so that import from other files works flawlessly
'''
player1 = SmartPlayer('Dennis')
player2 = HumanPlayer('Jake')
game1 = Competition(player1, player2)
game1.startComp()
'''
