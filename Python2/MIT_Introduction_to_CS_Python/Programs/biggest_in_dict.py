animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def Biggest(aDict):
	dummy = []
	for e in aDict:
		if len(aDict[e]) > len(dummy):
			dummy = aDict[e]
			key = e
	return key

print Biggest(animals)
