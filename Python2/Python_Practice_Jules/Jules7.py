letter = raw_input("Enter letter: ")

#if letter in "qwertzuiopasdfghjklyxcvbnm":   alternatively:
if letter.isalpha():
	print ord(letter)
else:
	print "Error"
