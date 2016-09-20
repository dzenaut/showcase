string = raw_input("Enter string: ")
string = string.lower()

alph_string = ""
long_alph = ""

for i in range(len(string)):
	if i == len(string)-1:
		alph_string += string[i]
		if len(alph_string) > len(long_alph):
			long_alph = alph_string
	elif ord(string[i]) <= ord(string[i+1]):
		alph_string += string[i]
	else:
		alph_string += string[i]
		if len(alph_string) > len(long_alph):
			long_alph = alph_string
		alph_string = ""

print "The longest string is", long_alph

		