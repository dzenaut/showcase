# This program works if you place it in the same directory as example_solution_week_1_and_2.py

# This is a partial solution to Problem 6.2 and 6.3.
# Missing parts are marked by '# ...'

# import Board (the Model class)
from example_solution_week_1_and_2 import *

# import tkinter so that we can create a graphical interface
from tkinter import *

# the View class
# the view handles all graphical display and user interaction
class View:
    def __init__(self, controller):
        # create a window
        self.window = Tk()
        # set window title
        self.window.title("TicTacToe - " + controller.player.getName())
        # store the controller in an attribute
        self.controller = controller
        # create 3x3 buttons for the fields of the board and store them in a list
        self.buttons = []
        for row in range(0,3):
            buttonRow = []
            for col in range(0,3):
               # create the button and add it to the window
               b = self.addButton(row,col)
               # store the button in buttonRow
               buttonRow.append(b)
            self.buttons.append(buttonRow)
        # self.buttons is now of the form [ [button, button, button], [button, button, button], [button, button, button] ]

        # 6.3: create label and position it
        self.label = Label(self.window)
        self.label["text"] = "State of the Game"
        self.label.place(relx = 0, rely = 3/5, relheight = 1/5, relwidth = 1)

        # create 2 buttons for a new game as player 1/2 and add it to the window
        b1 = Button(self.window)
        b2 = Button(self.window)
        # set the text of the buttons
        b1["text"] = "New Game as 1"
        b2["text"] = "New Game as 2"
        # position them at the bottom
        b1.place(relx = 0, rely=4/5, relheight=1/5)
        b2.place(relx = 1/2, rely=4/5, relheight=1/5)
        # set the statement to execute when the buttons are pressed
        b1["command"] = lambda:controller.notifyNewGamePressed(1)
        b2["command"] = lambda:controller.notifyNewGamePressed(2)

    def addButton(self, row, col):
        """creates the button for field (row, col)"""
        # create a new button and add it to the window
        b = Button(self.window)
        # no text initially
        b["text"] = ""
        # choose foreground and background color
        b["fg"]   = "black"
        b["bg"]   = "white"
        # set the statement to execute when the button is pressed
        # see above for note on lambda
        b["command"] = lambda:self.controller.notifyFieldPressed(row,col)
        # position the button in the window
        b.place(relx=col/3, rely=row/5, relheight=1/5, relwidth=1/3)
        # return the new button
        return b

    def redraw(self,board):
        """updates the view by redrawing according to the board"""
        # for every field
        for row in range(0,3):
            for col in range(0,3):
                # get the button
                button = self.buttons[row][col]
                # get the value of the field
                field = board.getField(row,col)
                # set the text of the button according to the value of the field
                # 6.2: set the backgroundtext of the button according to the value of the field
                if field == 1:
                    button["text"] = "X"
                    button["bg"] = "red"
                    # ...
                elif field == 2:
                    button["text"] = "O"
                    button["bg"] = "green"
                    # ...
                else:
                    button["text"] = ""
                    button["bg"] = "white"
                    # ...
        self.label["text"] = self.controller.stateofGame()

# the Controller class
# the controller handles the board and the game play
# The controller tells the view what to display by calling the redraw method.
# The view tells the controller what the user did by calling the notifyXXX methods.
class Controller:
    def __init__(self, player):
       self.player = player     # store the player in an attribute
       self.board = Board()     # create a new board
       self.view  = View(self)  # create a new view
       self.userPlaysAs = None  # 1 or 2 if the user is player 1 or player 2

    def start(self):
       self.view.window.mainloop() # start the tkinter main loop, which handles the window and user interaction

    def notifyFieldPressed(self,row,col):
       """the function that is called when the button (row, col) is pressed"""
       # if it is the user's turn and the game is not over
       if self.userPlaysAs == self.board.getCurrentPlayer() and not self.board.isOver():
            if self.board.getField(row,col) == 0:
               # make the user's move in the model
               self.board.makeMove(row,col)
               # update the view
               self.view.redraw(self.board)
               # if the game is not over, make a computer move
               if not self.board.isOver():
                   self.computerMoves()
            else:
                pass # ignore clicks on occupied fields
       else:
            pass # ignore clicks when not user's turn

    def notifyNewGamePressed(self, x):
        """the function that is called when a 'new game' button is pressed"""
        # reset the board
        self.board = Board()
        # set the position of the user (1 or 2)
        self.userPlaysAs = x
        # update the view
        self.view.redraw(self.board)
        # if the computer should start, make a computer move
        if x == 2:
           self.computerMoves()

    def computerMoves(self):
       """this function makes one move by the computer, i.e., self.player"""
       # get a move from self.player
       (row,column) = self.player.getMove(self.board)
       # make the move in the model
       self.board.makeMove(row,column)
       # update the view
       self.view.redraw(self.board)

    def stateofGame(self):
      '''returns a string about the state of the game that will be printed on the label'''
      if self.board.getResult() == 1:
        return "Player 1 won!"
      elif self.board.getResult() == 2:
        return "Player 2 won!"
      else:
        if self.board.isOver() == True:
          return "Draw!"
        else:
          return str("Player " + str(self.board.getCurrentPlayer()) + " plays!")




#############################################################
from p4_2 import SmartPlayer

# create a computer player so that we can test the program
# if you have one, change this to use your SmartPlayer
smart = SmartPlayer("Smart")

# create a Controller for playing against the computer
controller = Controller(smart)

# start the game
controller.start()
