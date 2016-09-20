x = int(raw_input("Give me an integer that is >= 1: "))
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0

'''
continue loop until the difference between ans**2 and x is less than epsilon and 
answer is smaller or equal to x
'''

while (abs(ans**2-x)) >= epsilon and ans <= x:
	#generate test
	ans += step
	numGuesses += 1
print "NumGuesses = " + str(numGuesses)
if abs(ans**2-x) >= epsilon:
	print "Failed on square root of " + str(x)
else:
	print str(ans) + " is close to the square root of " + str(x)