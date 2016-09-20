#Assignment 1.3
#Dennis Ledwon

from p1_1 import board
from p1_2 import checkgame, makemove, haswon

def tictactoe():
    '''Plays an interactive game of tictactoe. Asks players to input coordinates that describe where the symbol is to be placed. x gives information about the row (1-3), y gives information about the column (1-3).'''

    # counter to keep track of whether it is player 1's or player 2's turn
    counter = 0

    #starting board, all tiles are empty
    boardlist = [[0,0,0],[0,0,0],[0,0,0]]

    #ask players for their names
    name1 = input('Player 1, please enter your name: ')
    name2 = input('Player 2, please enter your name: ')

    #repeat as long as there are still free tiles
    while not checkgame(boardlist) == 0:

        #player 1's turn
        if counter%2 == 0:

            #ask for coordinates to place the symbol on the board
            print(name1, end=", ")
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))

            #update boardlist based on user input of coordinates
            boardlist = makemove(x, y, boardlist, 1)

            #display board
            board(boardlist)

            #check whether player 1's move just won the game, if so, break out of the while loop and end the game
            if haswon(boardlist, 1):
                print('Congratulations', name1, ", you won!")
                break

            #update counter
            counter += 1

        #player 2's turn
        else:

            #analogous to comments for player 1
            print(name2, end=", ")
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            boardlist = makemove(x, y, boardlist, 2)
            board(boardlist)
            if haswon(boardlist, 2):
                print('Congratulations', name2, ", you won!")
                break


            counter += 1


#These questions will be on the exam, for sure 1.1 and 1.2


