char = raw_input("Enter character: ")
num = int(raw_input("Enter integer: "))

for i in range (0, num):
	char = chr(ord(char)+1)
	print char
