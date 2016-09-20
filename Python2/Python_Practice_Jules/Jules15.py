def containsDigit(string):
	if "0" in string or "1" in string:
		print "Contains digits."
	else:
		print "Does not contain digits."

def getlow(string):
	string = string.lower()
	string = string.replace("o", "O")
	print string

string = raw_input("Enter string: ")
containsDigit(string)
getlow(string)