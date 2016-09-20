# defines the variable x to "There are 10 types of people.", because %d is a spaceholder for 10 
x = "There are %d types of people." % 10
# defines the variable binary to the string "binary"
binary = "binary"
# defines the variable do_not to the string "don't"
do_not = "don't"
# defines the variable y as the string "Those who know binary and those who don't." %s, %s are spaceholders for the variables binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# prints variable "I said (variable x)", because %r is a spaceholder for x, %r used because there is the number 10
print "I said: %r." % x
# same thing
print "I also said: '%s'." % y

# sets the variable hilarious to False
hilarious = False
# sets the variable joke_evaluation to "Isn't that joke so funny?! %r"
joke_evaluation = "Isn't that joke so funny?! %r"

# prints joke_evaluation's string, then % hilarious just means that the %r in joke evaluation's string is a placeholder for hilarious' string
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e