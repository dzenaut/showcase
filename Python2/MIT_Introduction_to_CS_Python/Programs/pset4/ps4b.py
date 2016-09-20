from ps4a import *
import time

GLOBAL_SCORE_COMP = 0
GLOBAL_SCORE = 0

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    
    # Keep track of the total score
    global GLOBAL_SCORE
    score = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
    
        # Display the hand
        print "Your hand:",
        displayHand(hand)
        
        # Ask user for input
        word = raw_input("Enter word or a single dot ('.') to exit this hand: ")
        
        # If the input is a single period:
        if word == ".":
        
            # End the game (break out of the loop)
            break

            
        # Otherwise (the input is not a single period):
        else:
        
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
            
                # Reject invalid word (print a message followed by a blank line)
                print "Your word is not valid."
                print ""

            # Otherwise (the word is valid):
            else:

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                wordscore = getWordScore(word, n)
                score += wordscore
                print "The word has a score of", wordscore
                print "The updated score is", score
                print ""
                # Update the hand 
                hand = updateHand(hand, word)
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print "Your final score of the hand is", score
    GLOBAL_SCORE += score


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """

    # Create a new variable to store the maximum score seen so far (initially 0)
    bestscore = 0

    # Create a new variable to store the best word seen so far (initially None)
    bestword = None

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth
            score = getWordScore(word, HAND_SIZE)

            # If the score for that word is higher than your best score
            if score > bestscore:

                # Update your best score, and best word accordingly
                bestscore = score
                bestword = word
        else:
            continue


    # return the best word you found.
    return bestword


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    global GLOBAL_SCORE_COMP
    score = 0

    while calculateHandlen(hand) > 0:
        print "Your hand:",
        displayHand(hand)
        word = None
        word = compChooseWord(hand, wordList, HAND_SIZE)
        print "test"
        if word is None:
            print "No more options to continue the game."
            break
        else:
            wordscore = getWordScore(word, n)
            score += wordscore
            print "The best word is:", word, "with a score of", wordscore
            print "The updated score is", score
            print ""
            hand = updateHand(hand, word)

    print "Your final score of the hand is", score
    GLOBAL_SCORE_COMP += score
                


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand = {}
    while True:
        instruction = raw_input("Press 'n' for a new hand.\nPress 'r' to replay your old hand.\nPress 'e' to exit the game.\n\n")
        print ""

        if instruction == 'n':
            hand = dealHand(HAND_SIZE)
            while True:
                decision = raw_input("Enter 'u' if you want to play or 'c' if you want the computer to go:\n\n")
                print ""
                if decision == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                elif decision == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print "Invalid input. Please enter 'c' or 'u'!"
        elif instruction == 'r':
            if hand == {}:
                print "Sorry, this is your first hand. Please make a new hand by pressing 'n'."
            else:
                while True:
                    decision = raw_input("Enter 'u' if you want to play or 'c' if you want the computer to go:\n\n")
                    print ""
                    if decision == 'c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                    elif decision == 'u':
                        playHand(hand, wordList, HAND_SIZE)
                        break
                    else:
                        print "Invalid input. Please enter 'c' or 'u'!"
        elif instruction == 'e':
            break
        else:
            print "Your input is invalid."
            print ''
    print "Thanks for playing! Your total score is: " + str(GLOBAL_SCORE)
    print "The computer's score is: " + str(GLOBAL_SCORE_COMP)



if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


