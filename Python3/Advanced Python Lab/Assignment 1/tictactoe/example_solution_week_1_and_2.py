#### the board

class Board:
    def __init__(self):
        self.fields = [[0,0,0], [0,0,0], [0,0,0]]
        self.current = 1

    def getField(self, row, col):
        """returns the field in position (row, col): 1 or 2 for player 1 or 2, 0 for empty; row and col must be integers from 0 to 2"""
        return self.fields[row][col]

    def getCurrentPlayer(self):
        """returns the current player (the player of the next move); 1 for the starting, 2 for the other player"""
        return self.current

    def makeMove(self, row, column):
        """makes a move for the current player in field move, which is a pair (row, col)"""
        self.fields[row][column] = self.current
        if self.current == 1:
            self.current = 2
        else:
            self.current = 1

    def getBoard(self):
        return self.fields

    def __str__(self):
        """returns a string representation of the board"""
        res = ""
        for i in range(0,3):
            for j in range(0,3):
                field = self.fields[i][j]
                if field == 1:
                    letter = "X"
                elif field == 2:
                    letter = "O"
                else:
                    letter = " "
                res += " " + letter + " "
                if j != 2:
                    res += "|"
            res += "\n"
            if i != 2:
                res += "-----------\n"
        return res

    def getResult(self):
        """returns the current result: 1 or 2 if player 1 or 2 has won, 0 if no one has won (yet)"""
        b = self.fields
        def hasWon(player):
            for i in range(0,3):
               if b[i][0] == b[i][1] == b[i][2] == player:
                   return True
               if b[0][i] == b[1][i] == b[2][i] == player:
                   return True
            if b[0][0] == b[1][1] == b[2][2] == player:
                return True
            if b[2][0] == b[1][1] == b[0][2] == player:
                return True
            return False
        if hasWon(1):
            return 1
        elif hasWon(2):
            return 2
        else:
            return 0

    def isOver(self):
        """checks if the game is over: there is a winner, or the board is full"""
        if self.getResult() != 0:
            return True
        empty = 0
        for row in self.fields:
            for field in row:
                if (field == 0):
                    empty += 1
        if empty == 0:
            return True
        else:
            return False

#### an abstract class for players

class Player:
    """A Player makes moves into a Board.
       Subclasses must implement the abstract method getMove."""
    def __init__(self, n):
        """n is the name of the player"""
        self.name = n
    def getName(self):
        """returns the name"""
        return self.name
    def getMove(self,board,asPlayer):
        """board is an instance of Board; asPlayer is the current player (1 or 2)."""
        pass

#### playing a game between two players

class Game():
    """plays a game between two players, which amust be instances of Player"""
    def __init__(self, p1, p2):
        """p1 and p2 are the two players; p1 goes first"""
        self.player1 = p1
        self.player2 = p2

    def run(self):
        """plays the game and returns the result
           result is 0/1/2 for draw/first player wins/second player wins"""
        # create a new board
        board = Board()

        # loop until game is over
        while not board.isOver():
            print(board)

            # get the current player
            if board.getCurrentPlayer() == 1:
                currentPlayer = self.player1
            else:
                currentPlayer = self.player2

            # get the move from the player
            print("player " + currentPlayer.getName() + " to move")
            (row,column) = currentPlayer.getMove(board, board.getCurrentPlayer())

            # make the move
            board.makeMove(row,column)

        # return the result of the game
        print(board)
        return board.getResult()


#### some example players

import random

class RandomPlayer(Player):
    """A Player that plays into a random free field."""
    def getMove(self,board, asPlayer):
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if board.getField(row, col) == 0:
                break
        return (row,col)

class HumanPlayer(Player):
    """ A Player that asks interactively for moves."""
    def getMove(self,board):
        print("Enter your move as player " + str(asPlayer))
        row = int(input("row (0-2): "))
        col = int(input("column (0-2): "))
        return (row,col)

#### testing

def test():
    p1 = RandomPlayer("random 1")
    p2 = HumanPlayer("user")
    g = Game(p1,p2)
    result = g.run()
    if result == 0:
        print("draw")
    elif result == 1:
        print("player 1 wins")
    elif result == 2:
        print("player 2 wins")
