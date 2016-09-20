def isIn(char, aStr):
	'''
	string has to be alphabetical
	'''

	high = len(aStr)
	low = 0
	x = int((high+low)/2)

	#if the string is empty
	if len(aStr) == 0:
		return False
	#if the string only has one character
	elif len(aStr) == 1:
		return char == aStr
	#if the middle character is a lucky true guess
	elif char == aStr[x]:
		return True
	#if the middle character is not a lucky guess -> bisection search
	elif char < aStr[x]:
		return False or isIn(char, aStr[:x])
	elif char > aStr[x]:
		return False or isIn(char, aStr[x+1:])


print isIn("u", "abbbbbbbtu")
