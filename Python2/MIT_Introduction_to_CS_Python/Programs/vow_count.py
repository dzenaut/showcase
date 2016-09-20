str = raw_input("Enter string: ")
str = str.lower()

count = 0

for letter in str:
	if letter in 'aeiou':
		count += 1

print "There are", count, "vowels in your string."
