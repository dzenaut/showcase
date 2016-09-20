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

print getGuessedWord("kaviar", ['k', 'a', 'i', 'r'])