#Assignment 5.1
#Dennis Ledwon

#Both of these exceptions are raised in the makemove method of the class Board2 in the file p.3_2.py. They are then handled in the run method of the Game class in p4_3.py

class OccupiedMove(Exception):
    '''If a player makes a move on a field that is already occupied, this OccupiedMove Exception is raised.'''
    def __str__(self):
        return '\nOccupied field, you lose.'



class InvalidMove(Exception):
    '''If a player makes a move that is outside of the range of the board, this InvalidMove Exception is raised.'''
    def __str__(self):
        return '\nInvalid move, you lose.'


