import random

string = raw_input("Enter string that is made up of 'C', 'c', 'V' and 'v'! ")

small_cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't' 'v', 'w', 'x', 'y', 'z']
big_cons = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
small_vow = ['a', 'e', 'i', 'o', 'u']
big_vow = ['A', 'E', 'I', 'O', 'U']

newstr = ""

for letter in string:
	if letter == "c":
		newstr = newstr + small_cons[random.randrange(0, len(small_cons))]
	elif letter == "C":
		newstr = newstr + big_cons[random.randrange(0, len(big_cons))]
	elif letter == "v":
		newstr = newstr + small_vow[random.randrange(0, len(small_vow))]
	elif letter == "V":
		newstr = newstr + big_vow[random.randrange(0, len(big_vow))]

print newstr