string = raw_input("Enter string: ")
string = string.lower()

count = 0

for i in range(len(string)-2):
	if 'bob' == string[i:i+3]:
		count += 1

print count