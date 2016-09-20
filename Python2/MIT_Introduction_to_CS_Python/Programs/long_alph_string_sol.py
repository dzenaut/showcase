def longABC(s):
	abc = s[0] #Initial Substring
	abcMax = "" #Longest Substring
	for i in range(1, len(s)):
		if ord(s[i]) >= ord(s[i-1]):
			abc += s[i]
			if len(abc) > len(abcMax):
				abcMax = abc
		else:
			abc = s[i]
	return abcMax

s = raw_input("Enter string: ")
if s == "":
	s = raw_input("Enter string: ")
else:
	z = longABC(s)
	print z