word = input("Enter string: ")



def right(word):
	space = ""
	for letter in word:
		print(space + letter)
		space += " "


def left(word):
	space = "   "
	for letter in word:
		if len(space) > 0:
			print (space + letter)
			space = space[:-1]


tristep = 3
n = 1
check = True

while check:

	if tristep * n + 1 > len(word):
		trword = word[tristep*(n-1):]
		if n%2 != 0:
			right(trword)
		else:
			left(trword)
		check = False
	else:
		trword = word[tristep*(n-1):tristep*n]
		if n%2 != 0:
			right(trword)
		else:
			left(trword)
		n += 1

