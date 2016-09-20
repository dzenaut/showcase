x = float(raw_input('Enter a decimal number between 0 and 1: '))


#Find a power of 2 that gives a whole number when multiplied with x

p = 0
while ((2**p)*x)%1 != 0:
	print "Remainder = " + str((2**p)*x - int((2**p)*x))
	p += 1

#multiply x with the found power of 2 to get an integer
num = int(x*(2**p))

result = ''
if num == 0:
	result = '0'
while num > 0:
	result = str(num%2) + result
	num = num/2

#put enough 0s in fron by comparing what the difference between p and the length of the result is
for i in range(p-len(result)): 
	result = '0' + result

#need right place to find the decimal point
result = result[0:-p] + '.' + result[-p:]
print "The binary representation of the decimal " + str(x) + ' is ' + str(result)

'''
If there is no integer p such that x*(2**p) is a whole number, then internal representation is always
an approximation
'''

