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

print isWordGuessed('zepter', ['z', 'p', 'e','t', 'r','s'])