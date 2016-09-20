loop = True 
while loop:
	num = int(raw_input("Enter Integer: "))
	if num == 0:
		loop = not True
	elif num % 7 == 0:
		print "Integer is divisible by 7."
	else:
		print "Integer is not divisible by 7."
