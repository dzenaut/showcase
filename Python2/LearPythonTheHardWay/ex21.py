def add(a, b):
	#print "ADDING %.1f + %.1f" % (a, b)
	return a + b

def subtract(a, b):
	#print "SUBTRACTING %.1f - %.1f" % (a, b)
	return a - b

def multiply(a, b):
	#print "MULTIPLYING %.1f * %.1f" % (a, b)
	return a * b

def divide(a, b):
	#print "DIVIDING %.1f / %.1f" % (a, b)
	return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %.1f, Height: %.1f, Weight: %.1f, IQ: %.1f" % (age, height, weight, iq)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#add(35, subtract(74, multiply(180, divide(50 / 2))))
#add(35, subtract(74, multiply(180, 25)))
#add(35, subtract(74, 4500))
#add(35, -4426)
#-4391

print "That becomes: ", what, "Can you do it by hand?"

'''
return a + b (in add) does the following
	---> function is ready to return value to its caller
'''

def root(a):
	return a ** 0.5

def square(a):
	return a ** 2

number = int(raw_input("Please give me an integer! "))
if root(square(number)) == number:
	print "Dennis understood the return command!"
else:
	print "Dennis is an idiot!"

#24 + 34 / 100 - 1023

test = subtract(add(24, divide(34, float(100))), 1023)
print "That becomes: ", test








