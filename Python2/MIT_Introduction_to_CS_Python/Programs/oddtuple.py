def oddTuple(aTup):
	'''
	aTup: a oddTuple

	returns: tuple, every other element of aTup.
	'''
	newtup = ()
	for i in range(len(aTup)):
		if i%2 == 0:
			#element has to be a singleton, indicated by the comma
			newtup += (aTup[i],)
	return newtup

print oddTuple((1, 2, 3, 'car', 'Dennis'))

#also possible: return tuple[::2]