#Assignment 1.1
#Dennis Ledwon

def board(list):
    '''Takes as input a list of 3 lists with length 3. Elements are the numbers 1 (prints 'X' for player1), 2 (prints '0' for player 2), 0 (prints and empty field) that print according symbols on a tictactoe board.'''

    #counter to assure that a ____________ is printed after the first two rows of the tictactoe board, but not after the third one
    count = 0

    #go through every element in every sublist
    for sublist in list:
        for i in range(len(sublist)):

            #for the first two rows of the tictactoe game
            if count<2:

                #for the element in the 3rd column, i.e. the last element of the sublist, a new row is started. Two rows of the tictactoe game are separated by ___________. 1 is converted to X, 2 converted to O and 0 to an empty space here.
                if (i+1)%3 == 0:
                    if sublist[i] == 0:
                        print(' ', end='\n___________\n\n')
                    elif sublist[i] == 1:
                        print('X', end='\n___________\n\n')
                    elif sublist[i] == 2:
                        print('O', end='\n___________\n\n')

                #for the elements of the first, the converted symbol is printed and | is printed so that columns 1 and 2 are optically separated
                else:
                    if sublist[i] == 0:
                        print(' ', end=' | ')
                    elif sublist[i] == 1:
                        print('X', end=' | ')
                    elif sublist[i] == 2:
                        print('O', end=' | ')

            #for the last row of the tictactoe game
            else:

                #no printing of the ___________ after the last element of the last row is printed
                if (i+1)%3 == 0:
                    if sublist[i] == 0:
                        print(' ')
                    elif sublist[i] == 1:
                        print('X')
                    elif sublist[i] == 2:
                        print('O')

                #see previous comments
                else:
                    if sublist[i] == 0:
                        print(' ', end=' | ')
                    elif sublist[i] == 1:
                        print('X', end=' | ')
                    elif sublist[i] == 2:
                        print('O', end=' | ')

        #update counter
        count += 1

