#Assignment 5.3
#Dennis Ledwon

from p3_2 import Board2
from p4_2 import RandomPlayer, SmartPlayer, HumanPlayer
from p4_3 import Game
from p5_2 import PlayerResultsWithPoints

class AdvCompetition(Game):
    def __init__(self, players):
        '''players: List of instances of the player class'''
        self.indplayer1 = None
        self.indplayer2 = None
        self.player1 = None
        self.player2 = None
        self.players = players
        self.playboard = Board2()
        self.playerResults = []

    def addPlayers(self):
        for player in self.players:
            self.playerResults.append(PlayerResultsWithPoints(player))

    def listofMatches(self):
        matchlist = []
        #makes a matchlist in which every player plays against every player.
        for a in range(len(self.players)):
            for b in range(len(self.players)):
                #However, no match should be played twice and players shouldn't have to face themselves
                if a != b and not (self.players[b],self.players[a]) in matchlist:
                    matchlist.append((self.players[a],self.players[b]))
        return matchlist

    def playerIndex(self):
        #to keep track of the indexes and being able to address the right PlayerResultsWithPoints in the self.playerResults list
        indexlist = []
        for a in range(len(self.players)):
            for b in range(len(self.players)):
                if a != b and not (b,a) in indexlist:
                    indexlist.append((a,b))
        return indexlist

    def advRun(self, numGames):
        #Respective PlayerResultsWithPoints added to list of self.playerResults
        self.addPlayers()

        #for every possible match with the number of players
        for match, index in zip(self.listofMatches(), self.playerIndex()):
            #give self.run all the information it needs and set indices such that the result can be added to the right PlayerResultWithPoints in self.playerResults
            self.player1 = match[0]
            self.player2 = match[1]
            self.indplayer1 = index[0]
            self.indplayer2 = index[1]

            for games in range(numGames):
                #get result of the game
                result = self.run()
                #update results
                self.playerResults[self.indplayer1].addResult(result, True)
                self.playerResults[self.indplayer2].addResult(result, False)

                self.playboard.resetBoard()

            #make players play in different order
            self.player1 = match[1]
            self.player2 = match[0]

            for games in range(numGames):
                result = self.run()
                self.playerResults[self.indplayer1].addResult(result, False)
                self.playerResults[self.indplayer2].addResult(result, True)

                #reset the board for a new game between the opponents
                self.playboard.resetBoard()

        #print results
        for i in range(len(self.playerResults)):
            print(self.playerResults[i])

#initiate players and start the competition
player1 = SmartPlayer('Dennis')
player2 = RandomPlayer('Loser')
player3 = SmartPlayer('Two')

comp1 = AdvCompetition([player1, player2, player3])

comp1.advRun(10)











