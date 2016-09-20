celsius = float(raw_input("Enter degree Celsius: "))

fahr = (9/5.0)* celsius + 32

if fahr > 104:
	print "The temperature is", fahr, ", F that is very hot!"
elif fahr < 32:
	print "The temperature is", fahr, ", Fthat is very cold!"
else:
	print "The temperature is", fahr, "F!"