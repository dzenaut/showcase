epsilon = 0.01
y = float(raw_input("Please give me a positive number to find the square root of:\t"))
guess = y/2.0
attempts = 0

while abs(guess*guess - y) >= epsilon:
	guess = guess - (((guess**2)-y)/(2*guess))
	attempts += 1


print "Square root of " + str(y) + " is about " + str(guess)
print "Attempts: " + str(attempts)