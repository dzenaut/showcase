#Assignment 2.3
#Dennis Ledwon

from p1_1 import board
from p1_2 import makemove, haswon, checkgame
from p2_1 import randomMove
from p2_2 import modifyBoard

def vsComp():
    '''Play tictactoe against a Computer as Player 2'''

    #ask player 1 for name, player 2 is named Computer
    name1 = input('Player 1, please enter your name: ')
    name2 = 'Computer'

    #counter to keep track whether Player 1 or computer is playing
    counter = 0

    #set starting board
    boardlist = [[0,0,0],[0,0,0],[0,0,0]]

    #Announces whose turn it is and makes sure the game is not over yet
    while not checkgame(boardlist) == 0:

        #if it is Player 1's turn
        if counter % 2 == 0:

            #ask Player 1 for coordinates
            print(name1, end=", ")
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))

            #change list (map of game) according to player 1's moves
            boardlist = makemove(x,y,boardlist, 1)

            #display board after move
            board(boardlist)

            #break out of loop if last move won the game
            if haswon(boardlist, name1):
                print('Congratulations,', name1, ", you won!")
                break

            #increase counter and print an empty line
            counter += 1
            print('\n')

        #if it is the computer's turn
        elif counter % 2 != 0:

            #generate a random move from the computer
            gametuple = randomMove(boardlist, 2)

            #extract list from the tuple
            boardlist = modifyBoard(boardlist, gametuple, 2)

            #display board after computer's move
            board(boardlist)

            #break out of the loop if the last move won
            if haswon(boardlist, name2):
                print("The Computer won. Nobody's perfect.")
                break

            #increase counter and print an empty line
            counter += 1
            print('\n')









