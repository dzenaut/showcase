#Assignment 1.2
#Dennis Ledwon

def checkgame(list):
    '''Looks at a board of tictactoe and returns 0 if all fields are filled, 1 if there is an empty field and it is player 1\'s turn, 2 if there is an empty field and it is player 2\'s turn. Input is a nested list with three sublist of length three, elements are 1, 2, 0'''

    #set counters to keep track of how many O's, X's and how many occupied tiles there are on the board.
    ocounter = 0
    xcounter = 0
    totcounter = 0

    #iterate over every element in every sublist and check whether it is equal to 1 or 2. Update counters, otherwise pass because the field is empty
    for sublist in list:
        for element in sublist:
            if element == 2:
                ocounter += 1
            elif element == 1:
                xcounter += 1
            else:
                pass

    #if 9 tiles are occupied, the game is over. Occupied tiles is the sum of 1s and 2s on the board
    totcounter = ocounter + xcounter
    if totcounter == 9:
        return 0

    #if there are more 1s, player 2 has to play
    elif xcounter>ocounter:
        return 2

    #otherwise, it is player 1's turn
    else:
        return 1


def check(a, b, c):
    '''Returns True if three elements that are != 0 are the same, otherwise returns False'''

    if a == b == c and a!=0:
        return True
    else:
        return False

def makemove(x, y, boardlist, player):
    '''Changes boardlist depending on user input'''
    boardlist[(x-1)][(y-1)] = player
    return boardlist

def haswon(list, player):
    '''Looks for a winning combination on the board and returns True if the player 1\'s move won the game, returns False if it did not win the game.'''

    #goes though every winning combination and checks whether the according symbols are the same, using the check function
    boolean = False
    boolean = boolean or check(list[0][0], list[0][1], list[0][2])
    boolean = boolean or check(list[1][0], list[1][1], list[1][2])
    boolean = boolean or check(list[2][0], list[2][1], list[2][2])
    boolean = boolean or check(list[0][0], list[1][0], list[2][0])
    boolean = boolean or check(list[0][1], list[1][1], list[2][1])
    boolean = boolean or check(list[0][2], list[1][2], list[2][2])
    boolean = boolean or check(list[0][0], list[1][1], list[2][2])
    boolean = boolean or check(list[0][2], list[1][1], list[2][0])

    return boolean
