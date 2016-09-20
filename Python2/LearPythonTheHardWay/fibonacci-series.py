a, b = 0, 1
while b < 10000000000000000000000:
	print str(b) + " " + str(len(str(b)))
	a, b = b, a + b