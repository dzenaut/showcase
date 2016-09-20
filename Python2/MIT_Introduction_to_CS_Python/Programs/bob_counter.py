string = raw_input("Enter string: ")
string = string.lower()

count = 0
x = 0
y = 3
test = True

while test:
	if 'bob' == string[x:y]:
		count += 1
		x += 1
		y += 1
	else: 
		x += 1
		y +=1
	if y > len(string):
		test = False
		


print "The substring 'bob' can be found", count, "times in your string."