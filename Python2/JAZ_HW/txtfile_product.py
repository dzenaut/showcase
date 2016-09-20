product = 1

tf = "ab.txt"

txt = open(tf)

for char in txt.read():
	if char == " ":
		pass
	else:
		product *= ord(char)
		

print product

