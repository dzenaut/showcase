#Assignment 5.2
#Dennis Ledwon

class PlayerResult():
    def __init__(self, player):
        #keeps track of victories, defeats and draws of a player
        self.player = player
        self.won = 0
        self.drawn = 0
        self.lost = 0

    def addResult(self, r, wentFirst):
        """first argument: the result of a game (0, 1, or 2)
           second argument: True if this player is the first player"""
        if r == 0:
            self.drawn += 1
        elif r == 1:
            if wentFirst:
                self.won += 1
            else:
                self.lost += 1
        elif r == 2:
            if wentFirst:
                self.lost += 1
            else:
                self.won += 1

    def getNumberOfWins(self):
        return self.wins
    def getNumberOfLosses(self):
        return self.lost
    def getNumberOfDraws(self):
        return self.drawn
    def getPlayer(self):
        return self.player

    def __str__(self):
        result = ""
        result += self.player + ": "
        result += str(self.won) + " wins, "
        result += str(self.drawn) + " draws, "
        result += str(self.lost) + " losses"
        return result

class PlayerResultsWithPoints(PlayerResult):
    def getPoints(self):
        points = 0
        points = self.won * 2 + self.drawn
        return points

    def __str__(self):
        result = ""
        result += str(self.player.getName()) + ": "
        result += str(self.won) + " wins, "
        result += str(self.drawn) + " draws, "
        result += str(self.lost) + " losses, "
        result += str(self.getPoints()) + " points"
        return result

