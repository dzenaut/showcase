string = raw_input("Enter string: ")

space = " "
nrspace = 0

for letter in string:
	newstr = space*nrspace + letter
	print newstr
	nrspace += 1

