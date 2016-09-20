
low = 0
high = 100
ans = (low + high)/2

print "Please think of a number between 0 and 100!"
print "Is your secret number " + str(ans) + "?"

response = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter c do indicate I guessed correctly. ")

while True:
	if response == 'c':
		print "Game over, your secret number was: " + str(ans)
		break
	elif response == 'h':
		high = ans
		ans = (low + high)/2
		print "Is your secret number " + str(ans) + "?"
		response = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter c do indicate I guessed correctly. ")
	elif response == 'l':
		low = ans
		ans = (low + high)/2
		print "Is your secret number " + str(ans) + "?"
		response = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter c do indicate I guessed correctly. ")
	else:
		print "Sorry, I did not understand your input."
		print "Is your secret number " + str(ans) + "?"
		response = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter c do indicate I guessed correctly. ")



#Better version -> Much shorter code

'''
print "Please think of a number between 0 and 100!"

hi = 100
lo = 0
guessed = False

while not guessed:
	guess = (hi + lo)/2
	print "Is your secret number " + str(guess)+ "?"
	user_inp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

	if user_inp == 'c':
		guessed = True
	elif user_inp == 'h':
		hi = guess
	elif user_inp == 'l':
		lo = guess
	else:
		print "Sorry, I did not understand your input."

print "Game over. Your secret number was: " + str(guess)
'''