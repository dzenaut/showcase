# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter in lettersGuessed:
            test = True
        else: 
            return False
            
    return test




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    newstring = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            newstring += letter
        else:
            newstring += "_"
    return newstring




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableletters = ""
    alphstring = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphstring:
        if letter in lettersGuessed:
            availableletters += ""
        else:
            availableletters += letter
    return availableletters


    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is", len(secretWord), "letters long."
    print "_________________________"

    guesses = 8
    lettersGuessed = []
    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        lguess = raw_input("Enter a letter! ")
        lguess = lguess.lower()
        if lguess in lettersGuessed:
            print "You have", guesses, "guesses left."
            print "Available letters:", getAvailableLetters(lettersGuessed)
            print "Oops, you have already guessed that letter:", getGuessedWord(secretWord, lettersGuessed)
            print "________________"
        else: 
            lettersGuessed.append(lguess)
        if lguess in secretWord:
            print "You have", guesses, "guesses left."
            print "Available letters:", getAvailableLetters(lettersGuessed)
            print "Good guess:", getGuessedWord(secretWord, lettersGuessed)
            print "________________"
        else:
            guesses -= 1
            print "You have", guesses, "guesses left."
            print "Available letters:", getAvailableLetters(lettersGuessed)
            print "Oops, that letter is not in my word:", getGuessedWord(secretWord, lettersGuessed)
            print "________________"

    if isWordGuessed(secretWord, lettersGuessed):
        print "Congratulations, you won!"
    elif guesses == 0:
        print "You lost!"
        print "The word was:", secretWord






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
