#Assignment 4.1
#Dennis Ledwon

from p5_2 import PlayerResultsWithPoints

class Player():

    def __init__(self, name):
        '''Takes the name of a player and stores it as an attribute.'''
        self.name = name
        self.results = PlayerResultsWithPoints(self.name)

    def getName(self):
        '''Returns the name of the player.'''
        return self.name


    def getMove(self, Board2, player):
        '''Abstract method getMove. Creates a method, getMove for the parent class Player that can be elaborated on and called in subclasses (RandomPlayer, SmartPlayer, HumanPlayer). This allows for the use of different getMove functions for instances of different subclasses. Technically, it is not useful to ask for the player, because the player is stored in the instance of the Board2 class as well and can be extracted via the method .getCurrentPlayer(). For that reason, later, I only took Board2 as an argument for specialied getMove functions in assignment 4.2'''
        pass


