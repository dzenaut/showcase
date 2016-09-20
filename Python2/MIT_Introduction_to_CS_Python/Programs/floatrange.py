def frange(x, y, jump):
	while x < y:
    	yield x
    	x += jump

print frange(1, 5, 0.1)