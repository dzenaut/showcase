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

print getAvailableLetters('a')