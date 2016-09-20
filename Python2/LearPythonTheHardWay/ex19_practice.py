#define the function BMI_calc(), calculates BMI and then prints it in a string
def BMI_calc(name, mass_in_kg, height_in_m):
	BMI = mass_in_kg / height_in_m ** 2
	#The specifier %.1f means that the variable will be a float and that it will have 1 decimal
	print "%s BMI is equal to %.1f." % (nameII, BMI)

#define the function BMI_plusX(), calculates BMI if you were 10 kg heavier, using BMI_calc
def BMI_plusX(name, mass_in_kg, height_in_m):
	BMI_calc(name, mass_in_kg + 10, height_in_m)

name = raw_input("What is your name? ")

#if the last letter of the name is "s", nameII = name + "'", otherwise name = name + "'S"
if name[len(name)-1] == 's':
	nameII = name + "'"
else: 
	nameII = name + "'s"
#float in front of raw_input, so that the string is converted to a number	
mass_in_kg = float(raw_input("Please tell me your mass in kg: "))
height_in_m = float(raw_input("Please tell me your height in m: "))

BMI_calc(name, mass_in_kg, height_in_m)

print "If %s weight increased by 10 kg, his BMI would be: " % nameII
BMI_plusX(name, mass_in_kg, height_in_m)
