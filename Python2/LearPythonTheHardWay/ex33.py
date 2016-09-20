'''
i = 0
limit = 6
numbers = []
stepsize = 2

def listnumbers(i, limit, numbers, stepsize):
	while i < limit:
	    print "At the top i is %d" % i
	    numbers.append(i)

	    i = i + stepsize
	    print "Numbers now: ", numbers
	    print "At the bottom i is %d" % i

#listnumbers(i, limit, numbers)
listnumbers(i, limit, numbers, stepsize)
'''

'''
print "The numbers: "

for num in numbers:
    print num
'''

check = range(1, 10)
numbers = []

for i in check:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i