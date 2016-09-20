x = float(raw_input("Please type in a positive number: "))
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
#finds middle point and makes guess
ans = (high + low)/2.0

#checks whether the abs(ans**2-x) is bigger or equal to epsilon
while abs(ans**2-x) >= epsilon:
	print "low = " + str(low) + " high = " + str(high) + " ans = " + str(ans)
	numGuesses += 1
	#if ans**2 < x, the lower limit is raised to ans
	if ans**2 < x:
		low = ans
	#if ans**2 > x, the higher limit is decreased to ans
	else:
		high = ans
	#ans is redefined by dividing the sum of the new high and low by 2
	ans = (high + low)/2.0

print "numGuesses = " + str(numGuesses)
print str(ans) + " is close to square root of " + str(x)