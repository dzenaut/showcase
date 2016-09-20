char = raw_input("Enter a character: ")

if 48 <= ord(char) and ord(char) <= 57:
	print "Character is a digit."
elif 97 <= ord(char) and ord(char) <= 122:
	print "Character is a lowercase letter."
elif 65 <= ord(char) and ord(char) <= 90:
	print "Character is an uppercase letter"
else:
	print "The character is neither a letter nor a digit."