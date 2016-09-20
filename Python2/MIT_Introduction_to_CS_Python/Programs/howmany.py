def howmany(aDict):
	
    dummy = []
    for e in aDict:
    	dummy += aDict[e]
    print type(dummy)
    return len(dummy)

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print howmany(animals)

