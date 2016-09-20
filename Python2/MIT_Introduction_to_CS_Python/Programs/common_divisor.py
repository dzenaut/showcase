def gcdIter(a, b):
	'''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
	start = min(a, b)
	while not(a%start == 0 and b%start == 0):
		start -= 1
	return start

print gcdIter(50, 75)
